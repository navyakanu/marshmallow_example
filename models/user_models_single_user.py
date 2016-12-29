import json
from marshest.marshmodels import MarshModel


class GetSingleUserResponse(MarshModel) :

    def __init__(self, id, first_name, last_name, avatar):
        self.id =id
        self.first_name=first_name
        self.last_name =last_name
        self.avatar =avatar



    @classmethod
    def _json_to_object(cls, serialized_str):
        json_dict_raw = json.loads(serialized_str.decode("utf-8"))
        json_dict = json_dict_raw.get("data")



        return GetSingleUserResponse(id=json_dict.get("id"),
                                     first_name=json_dict.get("first_name"),
                                     last_name=json_dict.get("last_name"),
                                     avatar=json_dict.get("avatar")
                                     )
