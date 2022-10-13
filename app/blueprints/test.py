from flask import Blueprint
from datetime import datetime
import model as m
from flask import jsonify, flash, redirect, url_for, request


test = Blueprint("test", __name__, url_prefix='/test')


@test.route("/test-get-all", methods=["GET"])
def test_get_all():
	test_data = m.TestTable.query.all()
	return jsonify([data.__repr__() for data in test_data])


@test.route("/test-get-one/<number>", methods=["GET"])
def test_get_one(number):
	row = m.TestTable.query.filter(m.TestTable.count == number).one_or_none()
	if row is None:
		flash(f"A table with row count number {number} was not found!")
		return redirect(url_for('test_get_all')) 
	return jsonify(row.__repr__())


@test.route("/test-add", methods=["POST"])
def add_row():
	if not request.json:
		abort(400)
	row = m.TestTable(
		created=datetime.utcnow(),
		name=request.json.get('name'),
		count=request.json.get('count'),
	)
	m.db.session.add(row)
	m.db.session.commit()
	flash(f"New row successfully added")
	return redirect(url_for('test_get_all'))


@test.route("/test-update/<number>", methods=["GET", 'POST'])
def update_row(number):
	if not request.json:
		abort(400)

	row = m.TestTable.query.filter(m.TestTable.count == number).one_or_none()

	if row is None:
		flash(f"A table with row count number {number} was not found!")
		return redirect(url_for('test_get_all'))

	row.name = request.json.get('name', row.name)
	row.count = request.json.get('count', row.count)

	m.db.session.commit()

	return redirect(url_for(f'test_get_all'))


@test.route("/test-delete/<number>", methods=["GET", "POST"])
def delete_row(number):
	row = m.TestTable.query.filter(m.TestTable.count == number).one_or_none()
	if row is None:
		flash(f"A table row with count number {number} does not exist!")
		return redirect(url_for('test_get_all'))
	m.db.session.delete(row)
	m.db.session.commit()
	flash(f"A table with row count number {number} was deleted!")
	return redirect(url_for('test_get_all'))
