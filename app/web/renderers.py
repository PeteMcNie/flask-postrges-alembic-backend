import structlog
from flask import jsonify

import app

log = structlog.getLogger(__name__)


class render_json(object):
    def __call__(self, f):
        def wrapped(*args, **kwargs):
            try:
                data = f(*args, **kwargs)
            except Exception as e:
                log.exception(e)
                data = dict(message=e.message)

            if isinstance(data, list):
                raise TypeError(
                    "For reasons of good practice, you are not allowed to render_json a list. "
                    "Please use a dict instead."
                )
            if not isinstance(data, dict):
                return data

            response = app.response_class(jsonify(data), 200)
            response.content_type = "application/json; charset=utf-8"
            response.headers.set(
                "Cache-Control", "private, no-cache, no-store, must-revalidate"
            )
            response.headers.set("Expires", "Sat, 01 Jan 2000 00:00:00 GMT")
            response.headers.set("Pragma", "no-cache")

            return response

        wrapped.__name__ = f.__name__

        return wrapped
