from marshest.marshest.marshclients import MarshClient
from marshest_examples.user_models import CreatedUserResponse, CreateUsersRequest

class UsersAPIClient(MarshClient):

    def __init__(self, url):
        super(UsersAPIClient, self).__init__(format_for_serializing='json', format_for_deserializing='json')
        self.url = url
        self.default_headers = {"Accept": "application/json", "Content-Type": "application/json"}

    def create_users(self, name, job, requestslib_kwargs=None):
        url = '{0}/users'.format(self.url)
        request = CreateUsersRequest(name=name, job=job)
        return self.request('POST', url,
                            response_entity_type=CreatedUserResponse,
                            request_entity=request,
                            headers=self.default_headers,
                            kwargs=requestslib_kwargs)
