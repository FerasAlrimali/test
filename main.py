from kivy.app import App
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.core.window import Window
Window.clearcolor = (243/255, 161/255, 32/255, 1)
class PriceChecker(BoxLayout):
    arText=StringProperty(get_display(arabic_reshaper.reshape(u'السعر')))
    aruom=StringProperty(get_display(arabic_reshaper.reshape(u'قطعة')))
    itemDescriptionar=StringProperty(get_display(arabic_reshaper.reshape(u'بلادي دقيق فاخر 1 ك')))
    itemDescriptionen="Beladi premium flour 1 KG"
    enuom=StringProperty("Piece")


class ThePriceCheckerApp(App):
    pass


ThePriceCheckerApp().run()