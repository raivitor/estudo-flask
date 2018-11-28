from werkzeug.security import safe_str_cmp
from user import User

users = [
	User(1, 'Rai Vitor', '123456')
	User(2, 'Monnaliza Medeiros', '1q2w3e')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
	user = username_table.get(username, None)
	if user and safe_str_cpm(user.password, password):
		return user