from datetime import datetime
from flask.json.provider import JSONProvider
import json
from pathlib import Path
from flask import Flask

__name__ = "isoflask"


class ISOJSONProvider(JSONProvider):
    def default(self, obj):
        if isinstance(obj, Path):
            return obj.as_posix()
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class ISOFlask(Flask):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.json = ISOJSONProvider(self)
