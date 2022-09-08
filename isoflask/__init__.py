from datetime import datetime
from flask.json.provider import JSONProvider
import json
from flask import Flask
from pathlib import Path

__name__ = 'isoflask'


class ISOJSONProvider(JSONProvider):
    def dumps(self, obj):
        if isinstance(obj, Path):
            obj = obj.as_posix()
        elif isinstance(obj, datetime):
            obj = obj.isoformat()
        return json.JSONEncoder.default(self, obj)

    def loads(self, s, **kwargs):
        return json.loads(s)


class ISOFlask(Flask):

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.json = ISOJSONProvider(self)