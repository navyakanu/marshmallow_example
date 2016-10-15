import json
from marshest.marshest.marshmodels import MarshModel


class CreateUsersRequest(MarshModel):

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def _object_to_json(self):
        payload = {
            "name": self.name,
            "job": self.job
        }
        return json.dumps(payload)


class CreatedUserResponse(MarshModel):

    def __init__(self, name, job, id, createdAt):
        self.name = name
        self.job = job
        self.id = id
        self.createdAt = createdAt

    @classmethod
    def _json_to_object(cls, serialized_str):
        json_dict = json.loads(serialized_str.decode("utf-8"))
        return CreatedUserResponse(name=json_dict.get("name"),
                                   job=json_dict.get("job"),
                                   id=json_dict.get("id"),
                                   createdAt=json_dict.get("createdAt"))
