import fresh_tomatoes
import media

Harry_Potter = media.Movie("Harry Potter",
	                   "The Boy Who Lived.",
	                   "http://i3.hexunimg.cn/2014-03-13/162998912.jpg",
	                   "https://v.youku.com/v_show/id_XMzQ3OTE5NDU2.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
#creat the instance
Divergent = media.Movie("Divergent",
	                   "Beyond five factions.",
	                   "http://www.nsmovie.com/data/2010/s/www.sz100722.com/db_pictures/201408/29/1409282076152163.jpg",
	                   "https://v.youku.com/v_show/id_XNjY5ODE1MjE2.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")

Lucy = media.Movie("Lucy",
	                   "Everything is connected and existence is only proven through time.",
	                   "http://www.suanning.com/uploadfile/2014/1102/20141102100428833.jpg",
	                   "https://v.youku.com/v_show/id_XNjkzNzkyNjA0.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")


"""
Harry_Potter.show_trailer()
Divergent.show_trailer()
Lucy.show_trailer()
"""

#movies = [Harry_Potter, Divergent, Lucy] #建立电影列表
#fresh_tomatoes.open_movies_page(movies) #调用fresh_tomatoes中函数创建网页

movies = [Harry_Potter, Divergent, Lucy]
fresh_tomatoes.open_movies_page(movies)
