from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

Builder.load_string("""
<MainScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'D:\FYP\pic\wall2.jpeg'
    BoxLayout:
        id: login_layout
        orientation: 'vertical'
        padding: [20,60,20,60]
        spacing: 10
        
        Label:
            text: 'HealthPro'
            font_size: 32
        
        BoxLayout:
            orientation: 'vertical'
            
            Label:
                text: 'Username'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20
        
            TextInput:
                id: username
                multiline:False
                
            
        BoxLayout:
            orientation: 'vertical'
            
            Label:
                text: 'Password'
                font_size: 18
                halign: 'left'
                text_size: root.width-20, 20
            
            TextInput:
                id: password
                password: True
                multiline:False
        
            Label:
                id: info
                text: ''
                markup: True
        
        BoxLayout:
            spacing: 30
            Button:
                text: 'Create Account'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                pos_hint: {'center_x':0.35,'center_y':0.6}
                on_press: root.manager.current = root.but_click()
            
            Button:
                text: 'login'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = root.but_cool()


<SettingsScreen>:
    BoxLayout:
        id: login_layout
        orientation: 'vertical'
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'main'
            
<FlatButton@ButtonBehavior+Label>:
    text: 'default'
<HomeScreen>:
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (1,1,1,1)
        Rectangle:
            size: self.size
            pos: self.pos
            
    BoxLayout:
        id: top_nav
        size_hint_y: None
        height: 30
        pos_hint: {'top': 1}
        canvas.before:
            Color:
                rgba: (.06, .45, .45, 1)
            Rectangle:
                size: self.size
                pos: self.pos
        FlatButton:
            id: file_trigger
            text: 'file'
            on_release: file_dropdown.open(self)
            size_hint: (.1,None)
            height: 30
            
            Widget:
                on_parent: file_dropdown.dismiss()    
                
                DropDown:
                    id: file_dropdown
                    Button:
                        id: close
                        text: 'quit'
                        size_hint_y: None
                        height: 30
        Label:
            text: 'HealthPro'
            #bold: True
            size_hint: (.9,None) 
            height: 30
    BoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x: .2
            orientation: 'vertical'
            spacing: 3
            canvas.before:
                Color:
                    rgba: (.06, .40, .40, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos
            
            ToggleButton:
                id: user_toggle
                text: 'Explore'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'home'
            ToggleButton:
                id: product_toggle
                text: 'Insert Ingredient'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'ingredient'
            ToggleButton:
                id: analysis_toggle
                text: 'Track Calories'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'hello'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            size_hint_x: .8
            
            BoxLayout:
                id: login_layout
                padding: [20,60,20,60]
                spacing: 5
                orientation: 'vertical'
                
            
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
        
                    Button:
                        text: 'Dinner'
                        font_size: 30
                        size: 280, 150
                        size_hint: None, None
                        pos_hint: {'center_x':0.5,'center_y':1}
                        background_normal: 'D:\FYP\pic\dinner2.jpg'
<BFScreen>:
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (1,1,1,1)
        Rectangle:
            size: self.size
            pos: self.pos
            
    BoxLayout:
        id: top_nav
        size_hint_y: None
        height: 30
        pos_hint: {'top': 1}
        canvas.before:
            Color:
                rgba: (.06, .45, .45, 1)
            Rectangle:
                size: self.size
                pos: self.pos
        FlatButton:
            id: file_trigger
            text: 'file'
            on_release: file_dropdown.open(self)
            size_hint: (.1,None)
            height: 30
            
            Widget:
                on_parent: file_dropdown.dismiss()    
                
                DropDown:
                    id: file_dropdown
                    Button:
                        id: close
                        text: 'quit'
                        size_hint_y: None
                        height: 30
        Label:
            text: 'HealthPro'
            #bold: True
            size_hint: (.9,None) 
            height: 30
    BoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x: .2
            orientation: 'vertical'
            spacing: 3
            canvas.before:
                Color:
                    rgba: (.06, .40, .40, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos
            
            ToggleButton:
                id: user_toggle
                text: 'Explore'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'home'
            ToggleButton:
                id: product_toggle
                text: 'Insert Ingredient'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'ingredient'
            ToggleButton:
                id: analysis_toggle
                text: 'Track Calories'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        ScrollView:
            size: self.size
            GridLayout:
                id: content
                #size_hint_x: .8
                size_hint_y: None
                rows:6
                cols:2
                spacing: 20
                padding: 50
                #row_default_height:40
                
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                    
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                    
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                Button:
                    text: 'Omellete'
                    font_size: 24
                    background_normal: "D:\FYP\pic\Breakfast\omelette.jpg"
                    size_hint_x:None
                    size_hint_y:None
                    width:200
                    height: 200
                        
<IngredientScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size 
            source: 'D:\FYP\pic\wall2.jpeg'
    BoxLayout:
        id: login_layout
        orientation: 'vertical'
        padding: [20,60,20,60]
        spacing: 10
        
        BoxLayout:
            orientation: 'vertical'
               
            Label:
                text: 'you can insert your ingredient to find recipes'
                font_size: 18
                color: (0,0,0,1)
                halign: 'left'
                text_size: root.width-50, 20

            TextInput:
                id: username
                multiline:False
                size_hint: (.7, None)
                height: 30
                
        BoxLayout:            
            Button:
                text: 'Go'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = 'home'
                
<CalScreen>:
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (1,1,1,1)
        Rectangle:
            size: self.size
            pos: self.pos
            
    BoxLayout:
        id: top_nav
        size_hint_y: None
        height: 30
        pos_hint: {'top': 1}
        canvas.before:
            Color:
                rgba: (.06, .45, .45, 1)
            Rectangle:
                size: self.size
                pos: self.pos
        FlatButton:
            id: file_trigger
            text: 'file'
            on_release: file_dropdown.open(self)
            size_hint: (.1,None)
            height: 30
            
            Widget:
                on_parent: file_dropdown.dismiss()    
                
                DropDown:
                    id: file_dropdown
                    Button:
                        id: close
                        text: 'quit'
                        size_hint_y: None
                        height: 30
        Label:
            text: 'HealthPro'
            #bold: True
            size_hint: (.9,None) 
            height: 30
    BoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x: .2
            orientation: 'vertical'
            spacing: 3
            canvas.before:
                Color:
                    rgba: (.06, .40, .40, 1)
                Rectangle:
                    size: self.size
                    pos: self.pos
            
            ToggleButton:
                id: user_toggle
                text: 'Explore'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'home'
            ToggleButton:
                id: product_toggle
                text: 'Insert Ingredient'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'ingredient'
            ToggleButton:
                id: analysis_toggle
                text: 'Track Calories'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        GridLayout:
            id: content
            #size_hint_x: .8
            rows:6
            cols:2
            spacing: 20
            padding: 50
            #row_default_height:40
            Label:
                text: 'Age'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30
                
            TextInput:
                id: age
                height: 30
                multiline: False
                size_hint_x:None
                size_hint_y:None
                width:400
                height: 30
            Label:
                text: 'Gender'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30
                
            TextInput:
                id: gender
                height: 30
                multiline: False
                size_hint_x:None
                size_hint_y:None
                width:400
                height: 30
            Label:
                text: 'weight'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30
            TextInput:
                id: weight
                height: 30
                multiline: False
                size_hint_x:None
                size_hint_y:None
                width:400
                height: 30
            Label:
                text: 'Height'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30
            TextInput:
                id: height
                height: 30
                multiline: False
                size_hint_x:None
                size_hint_y:None
                width:400
                height: 30
            Label:
                text: 'Exercise'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30
            Spinner:
                id: exercise
                size_hint: None, None
                size: 400, 44
                pos_hint: {'center': (.5, .5)}
                text: 'Home'
                values: 'Basal Metabolic Rate', 'Little/no exercise', '3 times/week', '4 times/week', '5 times/week', 'Daily'
                on_text:
                    print("The spinner {} has text {}".format(self, self.text))     
                   
            Button:
                text: 'Submit'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                #pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = root.but_sub()
            Label:
                id: info
                text: ''
                markup: True
              

<HelloScreen>:
    FloatLayout:
        Spinner:
            size_hint: None, None
            size: 100, 44
            pos_hint: {'center': (.5, .5)}
            text: 'Home'
            values: 'Home', 'Work', 'Other', 'Custom'
            on_text:
                print("The spinner {} has text {}".format(self, self.text))


""")

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "healthypro"
)

#global userLogId
# Declare both screens
class MainScreen(Screen):

    def but_click(self):

        un = self.ids.username.text
        pw = self.ids.password.text
        info = self.ids.info
        cursor = db.cursor()

        if un == "" and pw == "":
            info.text = '[color=#FF0000]Enter username and password[/color]'
            sm.current = "main"
        else:
            ## defining the Query
            query = "INSERT INTO users(username,password) VALUES (%s, %s)"

            ## storing values in a variable
            values = (un, pw)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.close()

            print(cursor.rowcount, "records inserted")

            sm.current = "home"

    def but_cool(self):
        global userLogId
        un = self.ids.username.text
        pw = self.ids.password.text
        info = self.ids.info

        cursor = db.cursor()
        loadname = "SELECT * FROM users WHERE username = '%s' AND password = '%s'"
        cursor.execute(loadname % (un, pw))
        #cursor.execute(query)
        logincheck = cursor.fetchall()
        if len(logincheck) > 0:
            print(logincheck)
            userLogId = logincheck[0][0]
            print(userLogId)
            sm.current = "home"
        else:
            info.text = '[color=#FF0000]Incorrect username/password[/color]'
            sm.current = "main"
    # exists

    def but_lol(self):
        un = self.ids.username.text
        pw = self.ids.password.text
        cursor = db.cursor()

        query = ("SELECT * FROM user WHERE uname=%s AND password=%s")

        values = (un, pw)

        logincheck = cursor.execute(query, values)

        if values == logincheck:
            print("pass")
            print("Successfully loaded ")

        else:
            print
            "nope"

    def breakfast(self):
        cursor = db.cursor()
        omellete = self.ids.omellete

        query = ("SELECT * FROM breakfast WHERE bf_name='omellete'")
        cursor.execute(query)


class SettingsScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class BFScreen(Screen):
    pass

class IngredientScreen(Screen):
    pass

class CalScreen(Screen):
    def but_sub(self):
        global userLogId
        ag = self.ids.age.text
        gen = self.ids.gender.text
        weig = self.ids.weight.text
        heig = self.ids.height.text
        info = self.ids.info
        cursor = db.cursor()

        if ag == "" and gen == "":
            #info.text = '[color=#FF0000]Enter username and password[/color]'
            print("nope")
            sm.current = "main"
        else:
            ## defining the Query
            query = "INSERT INTO users(age,gender,weight,height) VALUES (%s, %s, %s, %s)"

            query = ('''
                        UPDATE users

                        SET age = %s,
                            gender = %s,
                            weight = %s,
                            height = %s

                        WHERE user_id = '%s'        
                        ''')

            ## storing values in a variable
            values = (ag, gen, weig, heig, userLogId)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.close()
            info.text = '[color=#008000]you have entered your body information[/color]'
            print(cursor.rowcount, "records inserted")

            sm.current = "cal"


class HelloScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(BFScreen(name='bf'))
sm.add_widget(IngredientScreen(name='ingredient'))
sm.add_widget(CalScreen(name='cal'))
sm.add_widget(HelloScreen(name='hello'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()