from datetime import datetime, timedelta
from joyreactor import JoyParser


today = datetime.now().strftime('%d.%m.%Y')
last_year = (datetime.now() - timedelta(days=365)).strftime('%d.%m.%Y')

JoyParser.out_dir = 'out'
JoyParser.out_subdir = 'default'
JoyParser.pages = 3

count_new = JoyParser.parse_date(today, 'all')
count_best = JoyParser.parse_date(today, 'best')
assert count_new > count_best

assert not JoyParser.parse_date(last_year, 'best')

joy_parser = JoyParser()
joy_parser.subdomain = 'gf'
joy_parser.tag = 'Stanford Pines'
joy_parser.pages = 5
joy_parser.out_subdir = 'gf_subdir'
assert joy_parser.parse() == 50