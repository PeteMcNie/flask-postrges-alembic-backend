import structlog
from flask import jsonify

log = structlog.getLogger(__name__)


class render_json(object):
    def __call__(self, f):
        def wrapped(*args, **kwargs):
            try:
                data = f(*args, **kwargs)
                status = 200
            except Exception as e:
                log.exception(e)
                data = dict(message=e.message)
                status = 500

            if isinstance(data, list):
                raise TypeError(
                    "For reasons of good practice, you are not allowed to render_json a list. "
                    "Please use a dict instead."
                )
            if not isinstance(data, dict):
                return data

            response = jsonify(data)
            response.status_code = status
            response.content_type = "application/json; charset=utf-8"
            response.headers.set(
                "Cache-Control", "private, no-cache, no-store, must-revalidate"
            )
            response.headers.set("Expires", "Sat, 01 Jan 2000 00:00:00 GMT")
            response.headers.set("Pragma", "no-cache")

            return response

        wrapped.__name__ = f.__name__

        return wrapped
