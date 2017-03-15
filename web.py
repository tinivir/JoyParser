import os
import urllib2
import click
from bs4 import BeautifulSoup


class WebContent:

	url = None
	soup = None
	date = None
	path = None
	tag = None
	pages = None
	subdomain = None

	def __init__(self, path, date=None, url=None):
		self.date = date
		self.path = path
		self.url = url

	def download_post(self, name, post):
		if self.path:
			source_path = os.path.join(self.path, '{}%s.{}'.format(name,'html')) 
			i = 0
			while os.path.exists(source_path % i):
				i += 1
			with open(source_path % i, 'w') as f:
				f.write(str(post))
	
	def parse_page(self):
		post_array = self.soup.find_all(class_="postContainer")
		for post in post_array:
			date = post.find(class_="date").find(class_="date").text
			post_name = post.find(class_="date").text
			source_post = post.find(class_="post_content")			
			if date == self.date:
				self.download_post(post_name,source_post)


	def get_next_url(self):
		next_url = self.soup.find(class_="next").get('href')
		return next_url

	def get_pages(self, pages, section):
		url = '{}/{}'.format(self.url, section)
		for i in range(pages):
			try:
				response = urllib2.urlopen(url)
			except urllib2.HTTPError as e:
				raise click.BadParameter("Invalid tag")
			self.soup = BeautifulSoup(response.read(), 'html.parser')
			self.parse_page()
			url = '{}{}'.format(self.url, self.get_next_url())


