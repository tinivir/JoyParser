from datetime import datetime
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
@click.option('--tag', default="new")

def joy(date, tag):
	
	JoyParser.out_dir = 'out'
	JoyParser.out_subdir = 'default'
	JoyParser.pages = 3

	count_new = JoyParser.parse_date(date, tag)

	print '{}: {} {} {} {} {}'.format("Posts saved", count_new, "on", date, "with tag", tag)

if __name__ == '__main__':
    joy()