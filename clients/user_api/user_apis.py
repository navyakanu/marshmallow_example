from marshest.marshclients import MarshClient

from clients.user_api.models.user_models import CreatedUserResponse, CreateUsersRequest
from clients.user_api.models.user_models_single_user import GetUserResponse


class UsersAPIClient(MarshClient):

    def __init__(self, url):
        super(UsersAPIClient, self).__init__(format_for_serializing='json', format_for_deserializing='json')
        self.url = url
        self.default_headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def create_users(self, name, job):                                  #create_users_api
        url = ('{0}/users').format(self.url)
        request = CreateUsersRequest(name=name, job=job)
        return self.request('POST', url,
                            response_entity_type=CreatedUserResponse,
                            request_entity=request,
                            headers=self.default_headers)

    def get_single_users(self,id):                                      #get_single_users GET request

        url =('{0}/users/{1}').format(self.url, id)
        print(url)
        return self.request('GET',url,
                            headers=self.default_headers,
                            response_entity_type=GetUserResponse)