
class StaticFactory(object):
    static_factory = None

    @staticmethod
    def initialise_factory():
        StaticFactory.static_factory = StaticFactory()
        return StaticFactory.static_factory

    def __init__(self):
        self.widgets = {}

    @staticmethod
    def register(name, obj):
        StaticFactory.static_factory._register(name, obj)

    def _register(self, name, obj):
        self.widgets[name] = obj

    @staticmethod
    def fetch(name):
        return StaticFactory.static_factory._fetch(name)

    def _fetch(self, name):
        try:
            return self.widgets[name]
        except KeyError as exc:
            raise RuntimeError("Factory object %s not found" % (name)) from exc
