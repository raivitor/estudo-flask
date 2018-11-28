from user import User

users = [
	User(1, 'Rai Vitor', '123456')
	User(2, 'Monnaliza Medeiros', '1q2w3e')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}