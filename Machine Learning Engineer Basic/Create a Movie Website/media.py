# -*- coding:utf-8 -*- 
import webbrowser


class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_url = trailer_youtube
	#instance method
	def show_trailer(self):
		webbrowser.open(self.trailer_url)
"""
函数调用，为电影网站的特定对象初始化这些属性值，声明它们的属性
"""
