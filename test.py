import unittest
import os
import shutil
import urllib2
from datetime import datetime, timedelta
from subprocess import check_output, call, CalledProcessError

class TestJoyParser(unittest.TestCase):

  def test_today_date(self):
    today = datetime.now().strftime('%d.%m.%Y')

    output = check_output(["python", "main.py",'{}{}'.format("--date=", today)])

    DIR = os.path.join('out','default','{} {}'.format(today,'new'))

    self.assertEqual(30, len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    self.assertEqual(output, '{} {} {}'.format("Posts saved: 30 on", today, "with tag new\n"))

  def test_last_year(self):
    last_year = (datetime.now() - timedelta(days=365)).strftime('%d.%m.%Y')

    output = check_output(["python", "main.py",'{}{}'.format("--date=", last_year)])

    DIR = os.path.join('out','default','{} {}'.format(last_year,'new'))

    self.assertEqual(0, len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    

    self.assertEqual(output, '{} {} {}'.format("Posts saved: 0 on", last_year, "with tag new\n"))
    self.assertEqual(output, 'Posts saved: 0 on {} with tag new\n'.format(last_year))



  def test_date_format(self):
    today = datetime.now().strftime('%Y.%m.%d')
    with self.assertRaises(CalledProcessError):
      check_output(["python", "main.py",'{}{}'.format("--date=", today)])
      

  def test_tag_format(self):
    today = datetime.now().strftime('%d.%m.%Y')
    tag = 'asd'
    with self.assertRaises(CalledProcessError):
      check_output(["python", "main.py",'{}{}'.format("--tag=", tag)])

  def tearDown(self):
    if os.path.exists('out'):
      shutil.rmtree(os.path.join('out'))



if __name__ == '__main__':
  unittest.main()