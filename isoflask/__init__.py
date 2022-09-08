from datetime import datetime
from flask.json.provider import JSONProvider
import json
from flask import Flask
from pathlib import PosixPath

__name__ = 'isoflask'


class ISOJSONProvider(JSONProvider):
    def dumps(self, obj):
        if isinstance(obj, PosixPath):
            return json.dumps(obj.as_posix())
        elif isinstance(obj, datetime):
           return json.dumps(obj.isoformat())
        return json.dumps(obj)

    def loads(self, s, **kwargs):
        return json.loads(s)


class ISOFlask(Flask):

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.json = ISOJSONProvider(self)