import pytest

from base_test import APIBaseTest


class UsersAPITests(APIBaseTest):

    @classmethod
    def setUpClass(cls):
        super(UsersAPITests, cls).setUpClass()

    @pytest.mark.create_user
    def test_create_user(self):
        new_user = self.user_api_client.create_users("abcd", "QA")              # Create single user
        self.assertEquals(new_user.status_code, 201, msg="Status code does not match")
        new_user = new_user.object
        self.assertEquals(new_user.name, "abcd", msg="Name does not match")
        self.assertEquals(new_user.job, "QA", msg="Job does not match")

    @pytest.mark.single_user
    def test_get_single_user(self):
        new_user_details = self.user_api_client.get_single_users("1")               # Get Single user
        self.assertEquals(new_user_details.status_code,200,msg="Status code does not match for get users")
        new_user_details = new_user_details.object
        self.assertEquals(new_user_details.id, 1, msg="Name does not match")




