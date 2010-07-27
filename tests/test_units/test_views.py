import unittest

class LegacyViewTests(unittest.TestCase):
    def _makeOne(self, app):
        from pylons.views import LegacyView
        return LegacyView(app)

    def test_it(self):
        request = DummyRequest()
        view = self._makeOne(dummyapp)
        response = view(request)
        self.assertEqual(response, dummyapp)

class Test_expose(unittest.TestCase):
    def _makeOne(self, **kw):
        from pylons.views import expose
        return expose(**kw)

    def test_call(self):
        inst = self._makeOne(a=1, b=2)
        def wrapped():
            """ """
        result = inst(wrapped)
        self.failUnless(result is wrapped)
        self.assertEqual(result.__exposed__, {'a':1, 'b':2})

def dummyapp(environ, start_response):
    """ """

class DummyRequest:
    def get_response(self, application):
        return application