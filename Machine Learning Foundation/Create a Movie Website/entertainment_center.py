import fresh_tomatoes
import media
Harry_Potter = media.Movie("Harry Potter",
	                 "The Boy Who Lived.",
	                 "https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG/220px-Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
	                 "<embed src='http://player.youku.com/player.php/sid/XMzQ3OTE5NDU2/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>")
#creat the instance
Divergent = media.Movie("Divergent",
	                 "Beyond five factions.",
	                 "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Divergent.jpg/220px-Divergent.jpg",
	                 "<embed src='http://player.youku.com/player.php/sid/XNjY5ODE1MjE2/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>")

Lucy = media.Movie("Lucy",
	                 "Everything is connected and existence is only proven through time.",
	                 "https://upload.wikimedia.org/wikipedia/en/thumb/1/14/Lucy_%282014_film%29_poster.jpg/220px-Lucy_%282014_film%29_poster.jpg",
	                 "<embed src='http://player.youku.com/player.php/sid/XNjkzNzkyNjA0/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>")
Harry_Potter.show_trailer()
#movies = [Harry_Potter, Divergent, Lucy] #建立电影列表
#fresh_tomatoes.open_movies_page(movies) #调用fresh_tomatoes中函数创建网页

fresh_tomatoes.open_movies_page(movies)
