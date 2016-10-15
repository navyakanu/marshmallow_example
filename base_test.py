import unittest

from marshest_examples.user_apis import UsersAPIClient


class APIBaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_api_client = UsersAPIClient(url="http://reqres.in/api")