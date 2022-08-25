from flask.json.provider import JSONProvider
import orjson
from flask import Flask

__name__ = 'isoflask'


class ISOJSONProvider(JSONProvider):

    def dumps(self, obj, *, option=None, **kwargs):
        if option is None:
            option = orjson.OPT_UTC_Z

        return orjson.dumps(obj, option=option).decode()

    def loads(self, s, **kwargs):
        return orjson.loads(s)



class ISOFlask(Flask):

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.json = ISOJSONProvider(self)