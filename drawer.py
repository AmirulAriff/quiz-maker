from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.properties import BooleanProperty, ListProperty

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "healthypro"
)

cursor = db.cursor()

Builder.load_string('''
#:import random random.random

<CustomScreen>:
    hue: random()
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size

    Label:
        font_size: 42
        text: root.name

    Button:
        text: 'Next screen'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_release: root.manager.current = root.manager.next()

<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size

<SelectableButton>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0, 181, 204, 1) if self.selected else (0, 181, 204, 1)
        Rectangle:
            pos: self.pos
            size: self.size
            
    color: (0, 181, 204, 1)
        
<RV>:
    BoxLayout:
        orientation: "vertical"

        BoxLayout:
            RecycleView:
                viewclass: 'SelectableButton'
                data: [{'text': str(x)} for x in root.data_items]
                
                SelectableRecycleGridLayout:
                    #padding: [20,60,20,60]
                    cols: 1
                    spacing: 20
                    default_size: None, dp(56)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    multiselect: True
                    touch_multiselect: True
                    multiline: True
        

<RVScreen>:
    BoxLayout:
        orientation: "vertical"
        size_hint: 1, 0.9
        RV:
        

''')


class CustomScreen(Screen):
    hue = NumericProperty(0)


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)



    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)


    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        '''if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))'''


class RV(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_user()

    def get_user(self):
        loadname = "SELECT bf_name FROM breakfast ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class RVScreen(Screen):
    pass


class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()
        root.add_widget(CustomScreen(name='CustomScreen'))
        root.add_widget(RVScreen(name='RVScreen'))
        return root


if __name__ == '__main__':
    ScreenManagerApp().run()