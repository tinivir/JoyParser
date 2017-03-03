import os

class DirMethods:

	out_dir = None
	out_subdir = None

	@staticmethod
	def make_dir(out_dir):
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)

	@staticmethod
	def make_def_dir(out_dir,out_subdir):
		DirMethods.out_dir = out_dir
		DirMethods.make_dir(DirMethods.out_dir)
		DirMethods.out_subdir = os.path.join(DirMethods.out_dir,out_subdir)
		DirMethods.make_dir(DirMethods.out_subdir)
		return DirMethods.out_subdir

	@staticmethod
	def make_sub_dir(out_dir):
		subdir = os.path.join(DirMethods.out_subdir,out_dir) #huinya
		DirMethods.make_dir(subdir)
		return subdir


