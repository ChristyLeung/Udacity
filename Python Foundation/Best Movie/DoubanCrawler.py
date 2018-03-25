import expanddouban
from bs4 import BeautifulSoup
import csv
import codecs

def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    resultUrl = url + "," + category + "," + location
    return resultUrl

class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link
    def print_data(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link, self.cover_link)

    def getMovies(category, location):
        movies = []
        for loc in location:
            html = expanddouban.getHtml(getMovieUrl(category, loc))
            soup = BeautifulSoup(html, "html.parser")
            content_a = soup.find(id="content").find(class_="list-wp").find_all("a",recursive=False)
            for element in content_a:
                movie_name = element.find(class_="title").string
                movie_rate = element.find(class_="rate").string
                movie_location = loc
                movie_category = category
                movie_info_link = element.get("href")
                movie_cover_link = element.find("img").get("src")
                movies.append(Movie(movie_name, movie_rate, movie_location,
                movie_category, movie_info_link, movie_cover_link).print_data())
        return movies

category_list = ["科幻", "青春", "音乐"]
location_list = ["大陆", "美国", "香港", "台湾", "日本", "韩国", "英国", "法国",
"德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗", "加拿大", "澳大利亚",
"爱尔兰", "瑞典", "巴西", "丹麦"]

yins_list1 = getMovies("科幻", location_list)
yins_list2 = getMovies("青春", location_list)
yins_list3 = getMovies("音乐", location_list)


f = codecs.open("movies.csv", "w", "utf_8_sig")
writer = csv.writer(f)
writer.writerow(yins_list1)
writer.writerow(yins_list2)
writer.writerow(yins_list3)
f.close()

def putMax(yinslist):
    input_dict = {"大陆":0, "美国":0, "香港":0, "台湾":0, "日本":0, "韩国":0,
    "英国":0, "法国":0, "德国":0, "意大利":0, "西班牙":0, "印度":0, "泰国":0,
    "俄罗斯":0, "伊朗":0, "加拿大":0, "澳大利亚":0, "爱尔兰":0, "瑞典":0, "巴西":0,
    "丹麦":0}
    total = 0
    for movie in yinslist:
        for loc in location_list:
            if loc in movies:
                input_dict[loc] += 1
    for idict in input_input:
        input_dict[idict] = round((input_dict[idict]/total)*100,2)
    return sorted(input_dict.items(), key=lambda x:x[1], reverse=True)[:3]

    def turnTostr(max_tuple):
        result_list = []
        i = 0
        while i < len(max_tuple):
            element = max_tuple[i]
            ele = str(element)
            e = "{}占百分之{},排名{}".format(ele[2:ele.index(",") - 1], ele[ele.index(",") + 2:-3], i + 1)
            i += 1
            result_list.append(e)
        return result_list

    max_list = [turnTostr(putMax(yins_list1)), turnTostr(putMax(yins_list2)), turnTostr(putMax(yins_list3))]

    f = open("output.txt", "w")
    f.write("科幻、青春、音乐")
    j = 0
    while j < len(category_list):
        f.write("{}类别电影数量排名前三的地区和百分比为: \n".format(category_list[j]))
        i = 0
        while i < len(max_list[j]):
            f.write(max_list[j][i])
            f.write("\n")
            i += 1
        j += 1

    f.close()

