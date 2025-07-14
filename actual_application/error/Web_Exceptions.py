class Missing(Exception):
    def __init__(self, name: str, missing_object_name: str):
        super().__init__(f"{missing_object_name} with name - {name} not found")
        self.msg = f"{missing_object_name} with name - {name} not found"

class Duplicate(Exception):
    def __init__(self, name: str, missing_object_name: str):
        super().__init__(f"{missing_object_name} with name - {name} already exists")
        self.msg = f"{missing_object_name} with name - {name} already exists"