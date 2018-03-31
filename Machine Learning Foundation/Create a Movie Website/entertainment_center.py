"""
调用fresh_tomatoes中函数设计网页框架
"""

import fresh_tomatoes
import media

Harry_Potter = media.Movie("Harry Potter",
	                   "The Boy Who Lived.",
	                   "http://i3.hexunimg.cn/2014-03-13/162998912.jpg",
	                   "https://v.youku.com/v_show/id_XMzQ3OTE5NDU2.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
#creat the instance
Divergent = media.Movie("Divergent",
	                   "Beyond five factions.",
	                   "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=166130579,2736602097&fm=27&gp=0.jpg",
	                   "https://v.youku.com/v_show/id_XNjY5ODE1MjE2.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")

Lucy = media.Movie("Lucy",
	                   "Everything is connected and existence is only proven through time.",
	                   "http://www.suanning.com/uploadfile/2014/1102/20141102100428833.jpg",
	                   "https://v.youku.com/v_show/id_XNjkzNzkyNjA0.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")

Operation_Red_Sea = media.Movie("Operation Red Sea",
	                   "A gift for the 90th Anniversary of the Founding of the Chinese People's Liberation Army, as well as the party's 19th National Congress.",
	                   "http://img4.imgtn.bdimg.com/it/u=3747850136,3760372308&fm=11&gp=0.jpg",
	                   "https://v.youku.com/v_show/id_XMzQyMzMyNTYxMg==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
The_Avengers = media.Movie("The Avengers",
	                   "An union of six Marvel superheroes.",
	                   "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2896762636,3209917190&fm=27&gp=0.jpg",
	                   "https://v.youku.com/v_show/id_XMzExODk2ODA0.html?spm=a2h0j.11185381.Dramalist_wrap.5!2~5~5!51~A&s=cc13662e962411de83b1")

Coco = media.Movie("Coco",
	                   "Always remember our loved ones before the memory faded.",
	                   "http://img0.imgtn.bdimg.com/it/u=3964096485,3725473345&fm=27&gp=0.jpg",
	                   "https://v.youku.com/v_show/id_XMzEwNDQ3MTc3Mg==.html?spm=a2h0j.11185381.Dramalist_wrap.5!2~5~5!19~A&s=25efbfbdefbfbd17efbf")


"""
Harry_Potter.show_trailer()
Divergent.show_trailer()
Lucy.show_trailer()
Operation_Red_Sea.show_trailer()
The_Avengers.show_trailer()
Coco.show_trailer()
"""

#movies = [Harry_Potter, Divergent, Lucy, Operation_Red_Sea, The_Avengers, Coco] #建立电影列表
#fresh_tomatoes.open_movies_page(movies) #调用fresh_tomatoes中函数创建网页

movies = [Harry_Potter, Divergent, Lucy, Operation_Red_Sea, The_Avengers, Coco]
fresh_tomatoes.open_movies_page(movies)
