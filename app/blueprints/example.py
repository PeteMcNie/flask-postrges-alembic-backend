from flask import Blueprint

import model as m
# from app.actions import example_actions

example = Blueprint("example", __name__, url_prefix=None)


@example.route("/")
def index() -> str:
    """Homepage."""
    from sqlalchemy import select, text

    result = m.db.session.execute(
        select(text("1 + 1 AS result")).where(
            text("1 = :thing").bindparams(thing=m.test.VALUE)
        )
    ).scalar()
    print(result)

    # widget = m.Widget()
    # m.db.session.add(widget)
    # m.db.session.commit()

    from flask_sqlalchemy import get_debug_queries
    print(get_debug_queries())

    m.db.session.rollback()

    with m.db.engine.begin() as conn:
        conn.execute(text("select 1"))

    return f"example index {m.test.VALUE} {result}"