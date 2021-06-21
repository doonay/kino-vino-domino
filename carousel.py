import kino
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.utils.fitimage import FitImage
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.write()


class MainWindow(FloatLayout):
		def add_caro(s):
		#main_box = BoxLayout(orientation='horizontal')
		#carousel = Carousel(direction='right')
		
		#upcoming = kino.get_upcoming()
		
		#for film in upcoming:
		#	box_card = BoxLayout(orientation='vertical')
		#	label_name = Label(text=film[0], size_hint=(1, 0.1), font_size='20sp', halign='center', valign='middle')
		#	image_poster = AsyncImage(source=film[1], allow_stretch=False)
#
#			box_card.add_widget(label_name)
#			box_card.add_widget(image_poster)
#
#			carousel.add_widget(box_card)
			print(type(s), str(s), 'передано!')
	


class CarouselApp(App):
		#	standart img source: 'https://www.themoviedb.org/t/p/w1920_and_h600_multi_faces_filter(duotone,032541,01b4e4)/7VrRna8S3x6xbijooeBmxqvHXiu.jpg'


	def build(self):

		#------------слева панель
    
    


		#------------справа карусель


		#list_films = kino.Search('Terminator')

		
		#for film in list_films:
			#print(film)

#		for film in list_films:
			#bg = FitImage(source=self.BG_IMG)
#			box_card = BoxLayout(orientation='vertical')
#			label_name = Label(text=film[0], size_hint=(1, 0.1), font_size='20sp', halign='center', valign='middle')
			#image_poster = AsyncImage(source=film[1], allow_stretch=False)
#			image_poster = AsyncImage(source=film[1], allow_stretch=False)

#			box_card.add_widget(label_name)
#			box_card.add_widget(image_poster)
#
#			carousel.add_widget(box_card)
		#RightPanel.add_widget(Carousel)

		return MainWindow()

if __name__ == '__main__':
    CarouselApp().run()