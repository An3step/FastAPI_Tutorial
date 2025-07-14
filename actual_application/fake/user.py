from model.user import User
from error.Web_Exceptions import Missing, Duplicate

fakes = [
    User(name='user1', hashed_password='abc'),
    User(name='user2', hashed_password='a12')
]

def find(name: str)-> User | None:
    for user in fakes:
        if user.name == name:
            return user
    return None

def check_missing(name: str):
    if not find(name):
        raise Missing(name, "User in tests")
    
def check_duplicate(name: str):
    if not find(name):
        raise Duplicate(name, "User in tests")

def get_all() -> list[User]:
    return fakes

def get_one(name: str)->User:
    check_missing(name)
    return find(name)

def create(user: User)->User:
    check_duplicate(user)
    fakes.append(user)
    return user

def modify(name: str, user: User) -> User:
    check_missing(name)
    modified_user = find(name)
    modified_user.name = user.name
    modified_user.hashed_password = user.hashed_password
    return user

def delete(name: str) -> None:
    check_missing(name)
    for user in fakes:
        if user.name == name:
            fakes.remove(user)
            return user

