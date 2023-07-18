import json
class Response:
    def __init__(self, status:str = None, message:str = None, data:str = None):
        self.status = status
        self.message = message
        self.data = data
    def __json__(self):
        return json.dumps(self.__dict__, indent=2)