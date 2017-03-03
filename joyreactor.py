from web import WebContent
from file_manager import DirMethods

class JoyParser:
	out_dir = 'out'
	out_subdir = 'default'
	pages = 3
	subdomain = None
	tag = None
	section = None

	def parse(self):
		return 0

	@staticmethod
	def parse_date(date, section):
		JoyParser.section = section
		DirMethods.make_def_dir(JoyParser.out_dir,JoyParser.out_subdir)
		subdir = DirMethods.make_sub_dir('{} {}'.format(date, section))
		WebContent.get_pages(JoyParser.pages, JoyParser.section, date, subdir)
		return 0
