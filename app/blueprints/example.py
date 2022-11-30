from datetime import datetime

from flask import Blueprint, flash, redirect, url_for

import model as m
from app.web.error_handler import make_error
from app.web.renderers import render_json

example = Blueprint("example", __name__, url_prefix="/example")


@example.route("/example-get-all", methods=["GET"])
@render_json()
def example_get_all():
    example_data = m.ExampleTable.query.order_by(m.ExampleTable.count.asc()).all()
    return dict(
        results=[
            dict(id=data.id, created=data.created, name=data.name, count=data.count)
            for data in example_data
        ]
    )


@example.route("/example-get-one/<count>", methods=["GET"])
@render_json()
def example_get_one(count):
    row = m.ExampleTable.query.filter(m.ExampleTable.count == count).one_or_none()

    if row is None:
        print(f"No row found: {row}")
        return make_error(
            message=f"A table with row count {count} was not found!", status=400
        )
    return dict(
        id=row.id, created=row.created, name=row.name, count=row.count
    )  # Don't need to return dict of results when only one result


@example.route("/example-add/<name>/<count>", methods=["GET", "POST"])
def add_row(name, count):
    row = m.ExampleTable(
        created=datetime.utcnow(),
        name=name if name else None,
        count=count if count else 0,
    )
    m.db.session.add(row)
    m.db.session.commit()
    flash(f"New row successfully added")
    return redirect(url_for("example.example_get_all"))


@example.route("/example-update/<id>/<name>/<count>", methods=["GET", "POST"])
def update_row(id, name, count):
    row = m.ExampleTable.query.filter(m.ExampleTable.id == id).one_or_none()

    if row is None:
        flash(f"A table with row id {id} was not found!")
        return redirect(url_for("example.example_get_all"))

    if name:
        row.name = name
    if count:
        row.count = count

    m.db.session.commit()

    flash(f"Test table with row id {id} was updated")
    return redirect(url_for(f"example.example_get_all"))


@example.route("/example-delete/<id>", methods=["GET", "POST"])
def delete_row(id):
    row = m.ExampleTable.query.filter(m.ExampleTable.id == id).one_or_none()
    if row is None:
        flash(f"A table row with id {id} does not exist!")
        return redirect(url_for("example.example_get_all"))
    m.db.session.delete(row)
    m.db.session.commit()
    flash(f"A table with row id {id} was deleted!")
    return redirect(url_for("example.example_get_all"))
