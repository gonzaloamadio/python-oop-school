from unittest import TestCase

HAS_ATTR_MESSAGE = '\n {} \n should have attribute --> {}'


class BaseTestCase(TestCase):
    def assertHasAttr(self, obj, attrname, message=None):
        if not hasattr(obj, attrname):
            if message is not None:
                self.fail(message)
            else:
                self.fail(HAS_ATTR_MESSAGE.format(obj, attrname))
