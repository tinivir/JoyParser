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
@click.option('--section', default="new")
@click.option('--path', default="default")
def joy(date, section, path):
	joy_parser = JoyParser('out', path, 3)

	count = joy_parser.parse_date(date, section)

	print 'Posts saved: {} on {} with section {}'.format(count, date, section)

if __name__ == '__main__':
    joy()