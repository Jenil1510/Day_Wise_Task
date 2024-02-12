# a simple file writer object

from contextlib import contextmanager

# inputFile = open("myfile.txt", "a")
class MessageWriter(object):
	def __init__(self, filename):
		self.file_name = filename

	@contextmanager
	def open_file(self):
		try:
			file = open(self.file_name, 'w')
			yield file
		finally:
			file.close()


# usage
message_writer = MessageWriter('myfile.txt')
with message_writer.open_file() as myfile:
	myfile.write('hello world') 

