#https://pypi.org/project/tmdbv3api/

#успешные запросы
#http://api.themoviedb.org/3/discover/movie?api_key=b4ce63bd08fd5898313dd68dbd5dff18&certification_country=US&certification=R&sort_by=vote_average.desc


import inspect

from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Discover

KEY = 'b4ce63bd08fd5898313dd68dbd5dff18'
tmdb = TMDb()
movie = Movie()
#movie.api_key = KEY
#movie.query = 'Terminator'
prefix = 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'



def get_upcoming():

#
#	{
#  "adult": false,
#  "backdrop_path": null,
#  "belongs_to_collection": null,
#  "budget": 0,
#  "genres": [
#    {
#      "id": 99,
#      "name": "Documentary"
#    }
#  ],
#  "homepage": "",
# "id": 413323,
# "imdb_id": "tt5852644",
#  "original_language": "en",
#  "original_title": "Deadpool: From Comics to Screen... to Screen",
#  "overview": "This documentary divided into five segments examines the source and its path to the movies, backstory, special effects story/character areas, cast and performances. It includes notes from Reynolds, Liefeld, Miller, Wernick, Reese, executive producers Aditya Sood and Stan Lee, co-creator/comics writer Fabian Nicieza, producer Simon Kinberg, comics writer Joe Kelly, specialty costume designer Russell Shinkle, makeup designer Bill Corso, production designer Sean Haworth, director of photography Ken Seng, executive producer/unit production manager John J. Kelly, previs supervisor Franck Balson, stunt coordinator Philip J. Silvera, visual effects supervisors Pauline Duvall and Jonathan Rothbart, visual effects producer Annemarie Griggs, 2nd unit director/stunt coordinator Robert Alonzo, special effects coordinator Alex Burdett, utility stunts Regis Harrington, composer Tom Holkenberg, and actors Morena Baccarin, TJ Miller, Brianna Hildebrand, Leslie Uggams, Ed Skrein, and Gina Carano.",
#  "popularity": 0,
#  "poster_path": "/chV0avy5ogIB2PMTInT4KpHDzwj.jpg",
#  "production_companies": [],
#  "production_countries": [],
#  "release_date": "2016-05-10",
#  "revenue": 0,
#  "runtime": 80,
#  "spoken_languages": [],
#  "status": "Released",
#  "tagline": "",
#  "title": "Deadpool: From Comics to Screen... to Screen",
#  "video": false,
#  "vote_average": 0,
#  "vote_count": 0
#}

	movie.api_key = KEY
	print(movie.api_key)
	#movie.language = 'ru-RU'
	#print(movie.language)
	#movie.adult = True
	#print(movie.adult)

	print()
	film_list = []

	search = movie.upcoming()
	for res in search:
		if res.poster_path is None:
			print('Посмотреть заглушку постера ' + res.title)
			continue
		else:
			# бэкграунд
			# 'belongs_to_collection':{'backdrop_path': '/cpmbkwSxZnKO69V82A9a34tvk2E.jpg'}
			print(res.title, prefix + res.poster_path)
			#film_list.append([res.title, prefix + res.poster_path])

	return film_list




def Search(line):
	#https://api.themoviedb.org/3/search/movie?api_key=b4ce63bd08fd5898313dd68dbd5dff18&query=Robocop
	#api_key String required
	#language String optional
	#query String required
	#page Integer optional
	#include_adult Boolean optional
	#region String optional
	#year Integer optional
	#primary_release_year Integer optional

#Что будем парсить
#префикс для картинок 'poster_path': /t/p/w300_and_h450_bestv2
#полный путь https://www.themoviedb.org/t/p/w300_and_h450_bestv2/d2lVpxBRboVPL49n6fsUAWX8aUc.jpg

#{'adult': False, 
#'backdrop_path': '/xKb6mtdfI5Qsggc44Hr9CCUDvaj.jpg', 
#'belongs_to_collection': {
#    'id': 528, 
#    'name': 'Терминатор (Коллекция)', 
#    'poster_path': '/w6Ya0LPeW9flEqY6wcIUtBWQCD0.jpg', 
#    'backdrop_path': '/cpmbkwSxZnKO69V82A9a34tvk2E.jpg'}, 
#    'budget': 102000000, 
#    'genres': [{'id': 28, 'name': 'боевик'}, 
#        {'id': 53, 'name': 'триллер'}, 
#        {'id': 878, 'name': 'фантастика'}], 
#        'homepage': 'https://www.lionsgate.com/movies/terminator-2-judgment-day', 
#        'id': 280, 
#        'imdb_id': 'tt0103064', 
#        'original_language': 'en', 
#        'original_title': 'Terminator 2: Judgment Day', 
#        'overview': 'Война роботов и людей продолжается. Казалось, что человечество обречено на полное уничтожение. Но благодаря своему лидеру Джону Коннору у сопротивления появляется шанс победить. Не имея возможности убить Джона в реальном времени, роботы отправляют в прошлое свою самую совершенную разработку — терминатора-убийцу из жидкого металла, способного принимать любое обличье.', 
#        'popularity': 56.767, 
#        'poster_path': '/67MopMcqqke4sJmcOwY5zu3kmYz.jpg',  
#        'release_date': '1991-07-03', 
#        'status': 'Released', 
#        'tagline': 'То же железо, та же модель, новая миссия', 
#        'title': 'Терминатор 2: Судный день', 
#        'video': False, 
#        'vote_average': 8.0, 
#        'vote_count': 9138



#id

#backdrop_path
#genre_ids

#original_language
#original_title
#overview
#popularity
#poster_path
#release_date
#title
#video
#vote_average
#vote_count


	movie.api_key = KEY
	print(movie.api_key)
	
	movie.query = line
	print(movie.query)

	movie.language = 'ru-RU'
	print(movie.language)
	
	movie.adult = True
	print(movie.adult)

	print()
	film_list = []

	search = movie.search(movie.query)
	for res in search:
		if res.poster_path is None:
			print('Посмотреть заглушку постера ' + res.title)
			continue
		else:
			# бэкграунд
			# 'belongs_to_collection':{'backdrop_path': '/cpmbkwSxZnKO69V82A9a34tvk2E.jpg'}
			print(prefix + res.poster_path)
			film_list.append([res.title, prefix + res.poster_path])

	return film_list
		#print(res.id)
		#print(res.title)
		#print(res.overview)
		#print('Rating:', res.vote_average)
		
	#tmdb.page = 1
	#movie.include_adult = True #optional
	#tmdb.region String #optional
	#tmdb.year Integer #optional
	#tmdb.primary_release_year = Integer #optional



#search = movie.search('Mad Max')
#for res in search:
#    print(res.id)
#    print(res.title)
#    print(res.overview)
#    print(res.poster_path)
#    print(res.vote_average)




#for res in search:
#	print(res.id)
#	print(res.title)
#	print(res.overview)
#	print(res.poster_path)
#	print(res.vote_average)


#movie = Movie()
#print(inspect.getmembers(movie, predicate=inspect.ismethod))

# Получите список популярных фильмов в базе данных фильмов. Этот список обновляется каждый день.
#popular = movie.popular()
#for p in popular:
    #print(p.id)
    #print(p.title)
    #print(p.overview)
    #print(p.poster_path)
    #print()

#alternative_titles = movie.alternative_titles
#cache_clear = movie.cache_clear
#changes = movie.changes
#credits = movie.credits

#external = movie.external
#external_ids = movie.external_ids
#images = movie.images
#keywords = movie.keywords
#latest = movie.latest
#lists = movie.lists
#now_playing = movie.now_playing


#recommendations = movie.recommendations(movie_id=111)
#for recommendation in recommendations:
#    print(recommendation.title)
#    print(recommendation.overview)

#release_dates = movie.release_dates
#reviews = movie.reviews

#search = movie.search('Mad Max')
#for res in search:
#    print(res.id)
#    print(res.title)
#    print(res.overview)
#    print(res.poster_path)
#    print(res.vote_average)

#search = movie.search('Terminator')

#for res in search:
#	print(res.id)
#	print(res.title)
#	print(res.overview)
#	print(res.poster_path)
#	print(res.vote_average)





# Получите основную информацию о фильме.

#m = movie.details(id)

#print(m.title)
#print(m.overview)
#print(m.popularity)


#similar = movie.similar
#top_rated = movie.top_rated
#upcoming = movie.upcoming
#videos = movie.videos

# Какие фильмы идут в кинотеатрах?
#discover = Discover()
#movie = discover.discover_movies({
#    'primary_release_date.gte': '2021-01-01',
#    'primary_release_date.lte': '2021-03-22'
#})

# Какие фильмы самые популярные?
#movie = discover.discover_movies({
#    'sort_by': 'popularity.desc'
#})

# Какие детские фильмы самые популярные?
#movie = discover.discover_movies({
#    'certification_country': 'US',
#    'certification.lte': 'G',
#    'sort_by': 'popularity.desc'
#})


#get_upcoming()
if __name__ == '__main__':
    CarouselApp().run()