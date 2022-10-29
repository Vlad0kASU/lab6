import datetime
from werkzeug.security import generate_password_hash
import json
from FileIOConcreteStrategy import FileIOConcreteStrategy


class Note():
	def __init__(self, data, user_id):
		self.data = data
		self.date = datetime.datetime.now()
		self.user_id = user_id


class User():
	def __init__(self, id, email, password, first_name):
		self.id = id
		self.email = email
		self.password = generate_password_hash(password, method='sha256')
		self.first_name = first_name
		self.notes = []
		self.strategy = FileIOConcreteStrategy

	def add_note(self, data):
		self.notes.append(Note(data=data, user_id=id))

	def show_notes(self):
		for note in self.notes:
			print('-'*20, note.data, note.date, sep='\n')

	def save_notes(self):
		self.strategy.write(self, notes=self.notes)


	def load_notes(self):
		with open('json.json', 'w') as f:
			self.notes = json.load(f)['notes']

if __name__ == '__main__':
	user = User(1, 'test@test.ru', 'qwerasdf', 'Vlad')
	try:
		user.add_note('test_note')
		while True:
			pass
	except KeyboardInterrupt:
		print('пока')
	finally:
		user.save_notes()
