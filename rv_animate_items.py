'''How to use Animation with RecycleView items?

In case you really want to use the Animation class with RecycleView, you'll
likely encounter an issue, as widgets are moved around, they are used to
represent different items, so an animation on a specific item is going to
affect others, and this will lead to really confusing results.

This example works around that by creating a "proxy" widget for the animation,
and, by putting it in the data, allowing the displayed widget to mimic the
animation. As the item always refers to its proxy, whichever widget is used to
display the item will keep in sync with the animation.

'''
from copy import copy

from kivy.app import App
from kivy.clock import triggered
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.properties import (
    ObjectProperty, ListProperty
)


KV = '''
<Item>:
    index: None
    animation_proxy: None


RecycleView:
    data: app.data
    viewclass: 'Item'
    RecycleBoxLayout:
        orientation: 'vertical'
        size_hint: 1, None
        height: self.minimum_height
        default_size_hint: 1, None
        default_size: 0, dp(40)
'''


class Item(Button):
    pass


class Application(App):
    data = ListProperty()

    def build(self):
        self.data = [
            {'index': i, 'text': 'hello {}'.format(i), 'animation_proxy': None}
            for i in range(10)
        ]
        return Builder.load_string(KV)

if __name__ == "__main__":
    Application().run()
