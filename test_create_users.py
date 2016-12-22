import pytest

from base_test import APIBaseTest


class UsersAPITests(APIBaseTest):

    @classmethod
    def setUpClass(cls):
        super(UsersAPITests, cls).setUpClass()

    @pytest.mark.create_user
    def test_create_user(self):
        new_user = self.user_api_client.create_users("jaydeep", "QA")
        self.assertEquals(new_user.status_code, 201, msg="Status code does not match")
        new_user = new_user.object
        print(new_user)
        self.assertEquals(new_user.name, "jaydeep", msg="Name does not match")
        self.assertEquals(new_user.job, "QA", msg="Job does not match")
            # print(vars(new_user_details))
            # self.assertEquals(new_user.status_code,200,msg="Status code does not match for get users")
            #
            # print(new_user_details.get("data"))
            # self.assertEquals(new_user.id, new_user_details.get("data").get("id"), msg="Name does not match")




