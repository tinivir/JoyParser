from web import WebContent
from file_manager import DirMethods


class JoyParser:
	out_dir = 'out'
	out_subdir = 'default'
	pages = 3
	url = None
	tag = None

	def __init__(self, out_dir, out_subdir, pages):
		self.out_dir = out_dir
		self.out_subdir = out_subdir
		self.pages = pages

	def parse_date(self, date, section):
		path = DirMethods.make_dir(self.out_dir, self.out_subdir, '{} {}'.format(date, section))
		web = WebContent(path, date=date, url='http://joyreactor.cc')
		web.get_pages(self.pages, section)
		return DirMethods.dir_len(path)
