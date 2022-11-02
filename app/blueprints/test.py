from xml.sax.xmlreader import AttributesImpl
from flask import Blueprint
from datetime import datetime
import model as m
from flask import jsonify, flash, redirect, url_for, request


test = Blueprint("test", __name__, url_prefix="/test")


# @attrs.define
# class TestTable:
#     id: str


@test.route("/test-get-all", methods=["GET"])
def test_get_all():
    test_data = m.TestTable.query.order_by(m.TestTable.count.asc()).all()
    return jsonify([data.__repr__() for data in test_data])

    # test_list = []
    # for data in test_data:
    #     test.list.append(TestTable(id=data.id))
    # return jsonify(test_list)


@test.route("/test-get-one/<count>", methods=["GET"])
def test_get_one(count):
    row = m.TestTable.query.filter(m.TestTable.count == count).one_or_none()
    if row is None:
        flash(f"A table with row count {count} was not found!")
        return redirect(url_for("test_get_all"))
    return jsonify(row.__repr__())


@test.route("/test-add/<name>/<count>", methods=["GET", "POST"])
def add_row(name, count):
    row = m.TestTable(
        created=datetime.utcnow(),
        name=name if name else None,
        count=count if count else 0,
    )
    m.db.session.add(row)
    m.db.session.commit()
    flash(f"New row successfully added")
    return redirect(url_for("test.test_get_all"))


@test.route("/test-update/<id>/<name>/<count>", methods=["GET", "POST"])
def update_row(id, name, count):
    row = m.TestTable.query.filter(m.TestTable.id == id).one_or_none()

    if row is None:
        flash(f"A table with row id {id} was not found!")
        return redirect(url_for("test.test_get_all"))

    if name:
        row.name = name
    if count:
        row.count = count

    m.db.session.commit()

    flash(f"Test table with row id {id} was updated")
    return redirect(url_for(f"test.test_get_all"))


@test.route("/test-delete/<id>", methods=["GET", "POST"])
def delete_row(id):
    row = m.TestTable.query.filter(m.TestTable.id == id).one_or_none()
    if row is None:
        flash(f"A table row with id {id} does not exist!")
        return redirect(url_for("test.test_get_all"))
    m.db.session.delete(row)
    m.db.session.commit()
    flash(f"A table with row id {id} was deleted!")
    return redirect(url_for("test.test_get_all"))
