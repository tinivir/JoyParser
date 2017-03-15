import unittest
import os
import shutil
import urllib2
from file_manager import DirMethods
from datetime import datetime, timedelta
from subprocess import check_output, call, CalledProcessError

class TestJoyParser(unittest.TestCase):

  subdir = 'test'
  dir_ = 'out'
  path = None

  today = datetime.now()

  def run_cmd(self, **kwargs):
    # self.run_cmd(date=123, path='test', section='section1')
    if 'path' not in kwargs:
      kwargs['path'] = self.subdir
    params = ['--{}={}'.format(k, v) for k, v in kwargs.items()]
    cmd = ["python", "main.py"]
    cmd += params
    return check_output(cmd)

  def dir_path(self, date, section):
    return os.path.join(self.dir_, self.subdir,'{} {}'.format(date, section))

  def test_today_date(self):
    today = TestJoyParser.today.strftime('%d.%m.%Y')
    output = self.run_cmd(date=today)
    self.path = self.dir_path(today, 'new')
    self.assertEqual(30, DirMethods.dir_len(self.path))
    self.assertEqual(output, 'Posts saved: 30 on {} with section new\n'.format(today))

  def test_last_year(self):
    last_year = (TestJoyParser.today - timedelta(days=365)).strftime('%d.%m.%Y')
    output = self.run_cmd(date=last_year)
    self.path = self.dir_path(last_year, 'new')
    self.assertEqual(0, DirMethods.dir_len(self.path))
    self.assertEqual(output, 'Posts saved: 0 on {} with section new\n'.format(last_year))

  def test_date_format(self):
    wrong_date = TestJoyParser.today.strftime('%Y.%m.%d')
    with self.assertRaises(CalledProcessError):
      self.run_cmd(date=wrong_date)

  def test_section_format(self):
    today = TestJoyParser.today.strftime('%d.%m.%Y')
    section = 'asd'
    self.path = self.dir_path(today, section)
    with self.assertRaises(CalledProcessError):
      self.run_cmd(section=section)

  def tearDown(self):
    if self.path and os.path.exists(self.path):
      shutil.rmtree(self.path)

if __name__ == '__main__':
  unittest.main()