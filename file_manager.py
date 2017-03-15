import os

class DirMethods:

	#make recursive function with n parameters
	@staticmethod
	def make_dir(*args):
		path = 	""
		for k in args:
			path = os.path.join(path, k)
			if not os.path.exists(path):
				os.makedirs(path)
		return path

	@staticmethod
	def dir_len(path):
		if path:
			return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])


