import urllib
import urllib2
import os
from lxml import html

class WebContent:

	url = 'http://joyreactor.cc'
	webContent = None
	tree = None
	date = None
	path = None

	@staticmethod
	def download_page():
		page = open('1.html', 'w')
		WebContent.page.write(WebContent.webContent)
		WebContent.page.close
	
	@staticmethod
	def parse_page():
		post_array = WebContent.tree.xpath('//div[@class="postContainer"]')
		for post in post_array:
			date = post.xpath('div/div[@class="ufoot"]/div[@class="ufoot_first"]/span[@class="date"]/span/span[@class="date"]/text()')[0]
			if date == WebContent.date:
				source_urls = post.xpath('div/div[@class="post_top"]/div[@class="post_content"]/div[@class="image"]')
				for url in source_urls:
					if url.xpath('a/@href'):
						source_url = url.xpath('a/@href')[0]
					elif url.xpath('img/@src'):
						source_url = url.xpath('img/@src')[0]
					elif url.xpath('span/a/@href'):
						source_url = url.xpath('span/a/@href')[0]
					else:
						print "error"
						continue
					print source_url
					source_name = source_url.split('/')[-1][-63:]
					source_path = os.path.join(WebContent.path, source_name) 
					urllib.urlretrieve(source_url, source_path)

	@staticmethod
	def get_next_url():
		next_url = WebContent.tree.xpath('//a[@class="next"]/@href')
		return next_url[0]


	@staticmethod
	def get_pages(pages, section, date, path):
		url = '{}/{}'.format(WebContent.url, section)
		WebContent.date = date
		WebContent.path = path
		for i in range(pages):
			print url
			response = urllib2.urlopen(url)
			WebContent.webContent = response.read()
			WebContent.tree = html.fromstring(WebContent.webContent)
			WebContent.parse_page()
			url = '{}{}'.format(WebContent.url, WebContent.get_next_url())


