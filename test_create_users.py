import pytest

from marshest_examples.base_test import APIBaseTest


class UsersAPITests(APIBaseTest):

    @classmethod
    def setUpClass(cls):
        super(UsersAPITests, cls).setUpClass()

    @pytest.mark.create_user
    def test_create_user(self):
        new_user = self.user_api_client.create_users("jaydeep", "QA")
        self.assertEquals(new_user.status_code, 201, msg="Status code does not match")
        new_user = new_user.object
        self.assertEquals(new_user.name, "jaydeep", msg="Name does not match")
        self.assertEquals(new_user.job, "QA", msg="Job does not match")