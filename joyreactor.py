from web import WebContent
from file_manager import DirMethods

class JoyParser:
	out_dir = 'out'
	out_subdir = 'default'
	pages = 3
	url = None
	tag = None
	section = None

	def parse(self):
		web = WebContent()
		web.url = self.url
		web.path = DirMethods.make_def_dir(self.out_dir, self.out_subdir)
		return web.get_pages(self.pages, self.tag)

	@staticmethod
	def parse_date(date, section):
		JoyParser.section = section
		DirMethods.make_def_dir(JoyParser.out_dir, JoyParser.out_subdir)
		subdir = DirMethods.make_sub_dir('{} {}'.format(date, section))
		web = WebContent()
		web.date = date
		web.path = subdir
		return web.get_pages(JoyParser.pages, JoyParser.section)
