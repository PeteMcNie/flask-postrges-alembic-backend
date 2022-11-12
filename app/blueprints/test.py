from datetime import datetime

from flask import Blueprint, flash, jsonify, redirect, request, url_for

import model as m

# from app.web.renderers import render_json

test = Blueprint("test", __name__, url_prefix="/test")


@test.route("/test-get-all", methods=["GET"])
# @render_json()
def test_get_all():
    test_data = m.TestTable.query.order_by(m.TestTable.count.asc()).all()
    return jsonify(
        [
            dict(id=data.id, created=data.created, name=data.name, count=data.count)
            for data in test_data
        ]
    )


@test.route("/test-get-one/<count>", methods=["GET"])
def test_get_one(count):
    row = m.TestTable.query.filter(m.TestTable.count == count).one_or_none()

    if row is None:
        print(f"No row found: {row}")
        # flash(f"A table with row count {count} was not found!")
        return jsonify(dict(message=f"A table with row count {count} was not found!"))
    return jsonify(dict(id=row.id, created=row.created, name=row.name, count=row.count))


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
