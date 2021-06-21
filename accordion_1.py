from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

import kino

Builder.load_string('''
<CenteredAsyncImage>:
    size_hint: 0.8, 0.8
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    mipmap: True
''')

class CenteredAsyncImage(AsyncImage):
    pass

class AccordionApp(App):
    def build(self):
        root = Accordion(orientation = 'vertical')
        list_films = kino.Search('Terminator')
        for film in list_films:
            print(type(film))
            item = AccordionItem(title='Title')
            #print(kino.Search('Terminator')[0])
            #item.add_widget(Label(text='Very big content\n' * 10))
            #item.add_widget(CenteredAsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/STS-116_spacewalk_1.jpg/1024px-STS-116_spacewalk_1.jpg'))
            item.add_widget(CenteredAsyncImage(source=film))
            root.add_widget(item)
        return root


if __name__ == '__main__':
    AccordionApp().run()
