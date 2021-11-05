from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<MyWidget>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (1,1,1,1)
        Rectangle:
            size: self.size
            pos: self.pos
    ActionBar:
        background_normal: ''
        background_down: ''
        background_color: 0, 1, 0, 1
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'Healthpro'
                with_previous: False
    BoxLayout:
        orientation: 'vertical'
        spacing: 20
        Button:
            text: 'breakfast'
            #color: (0,0,0,1)
            font_size: 30
            size: 280, 150
            size_hint: None, None
            pos_hint: {'center_x':0.5,'center_y':0.1}
            background_normal: 'D:\FYP\pic\Breakfast.jpg'
            on_press: root.manager.current = 'bf'

        Button:
            text: 'Lunch'
            font_size: 30
            size: 280, 150
            size_hint: None, None
            pos_hint: {'center_x':0.5,'center_y':0.1}
            background_normal: 'D:\FYP\pic\lunch2.jpg'
            on_press: root.manager.current = 'lu'

        Button:
            text: 'Dinner'
            font_size: 30
            size: 280, 150
            size_hint: None, None
            pos_hint: {'center_x':0.5,'center_y':1}
            background_normal: 'D:\FYP\pic\dinner2.jpg'
            on_press: root.manager.current = 'din'
    ActionBar:
        ActionView:
            ActionPrevious:
                with_previous: True
                ActionButton:
                    text: 'hello'
                ActionButton:
                    text: 'hello'
                ActionButton:
                    text: 'hello'
''')


class MyWidget(BoxLayout):
    pass


class TestApp(App):
    def build(self):
        return MyWidget()


TestApp().run()