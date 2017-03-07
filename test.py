from datetime import datetime, timedelta
from joyreactor import JoyParser
import click


today = datetime.now().strftime('%d.%m.%Y')

def validate_date(ctx, param, value):
	try:
		datetime.strptime(value, '%d.%m.%Y')
		return (value)
	except ValueError:
		raise click.BadParameter('date need to be in format dd.mm.YYYY')

@click.command()
@click.option('--date', default=today,callback=validate_date, help='Date format dd.mm.YYYY')
@click.option('--tag', prompt='Tag')

def joy(date, tag):
	last_year = (datetime.now() - timedelta(days=365)).strftime('%d.%m.%Y')

	JoyParser.out_dir = 'out'
	JoyParser.out_subdir = 'default'
	JoyParser.pages = 3

	count_new = JoyParser.parse_date(date, tag)
	print "Posts saved: ", count_new, " on ", date, " with tag ", tag 

if __name__ == '__main__':
    joy()