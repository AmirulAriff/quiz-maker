from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemeManager

from kivy.core.window import Window



import mysql.connector as mysql

# Window.size = (300, 500)

KV = """
#:import os os

ScreenManager:


    id: screen_manager
    create: create
    

    Screen:
        id: create
        name: 'create'
        username: username
        password: password
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'D:\FYP\pic\wall2.jpeg'
        MDLabel:
            text: "HealthPro"
            pos_hint: {'center_x':0.8,'center_y':0.84}
            font_size: 30
        FloatLayout: 
            MDTextField:
                id: username
                hint_text: "Enter username"
                helper_text: "or click on forgot username"
                helper_text_mode: "on_focus"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                size_hint_x:None
                width:300



            MDTextField:
                id: password
                hint_text: "Enter password"
                helper_text: "or click on forgot username"
                helper_text_mode: "on_focus"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.4}
                size_hint_x:None
                width:300

            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.35,'center_y':0.1}
                #on_release: post(JSON.text)

            MDRectangleFlatButton:
                text: 'Create Account'
                pos_hint: {'center_x':0.55,'center_y':0.1}
                on_release: screen_manager.current = app.login()








"""

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="healthpro"
)


class ContentNavigationDrawer(BoxLayout):
    pass


class DemoApp(MDApp):
    screen_manager = ObjectProperty(None)

    def login(self):
        un = self.screen_manager.create.username.txt
        pw = self.screen_manager.create.password.txt
        cursor = db.cursor()
        ## defining the Query
        query = "INSERT INTO user(uname,password) VALUES (%s, %s)"

        ## storing values in a variable
        values = (un, pw)
        ## executing the query with values
        cursor.execute(query, values)

        ## to make final output we have to run
        ## the 'commit()' method of the database object
        db.commit()
        db.close()

        print(cursor.rowcount, "records inserted")

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "800"
        screen = Screen()

        username = Builder.load_string(KV)

        screen.add_widget(username)
        return screen


DemoApp().run()