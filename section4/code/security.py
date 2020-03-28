from werkzeug.security import safe_str_cmp
from user import User

# 範例使用 mapping 就不用一直遍歷列表來查找 user
users = [
    # {
    #     'id': 1,
    #     'username': 'bob',
    #     'password': 'asdf'
    # }
    # 改為 User class
    User(1, 'bob', 'asdf')
]

# 改為 User class
# username_mapping = { 'bob': {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
# }}
username_mapping = {u.username: u for u in users}

# 改為 User class
# userid_mapping = { 1: {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
# }}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)