from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix import layout
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                on_press: root.manager.current = 'hello'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
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
                        on_press: root.manager.current = 'lu'

                    Button:
                        text: 'Dinner'
                        font_size: 30
                        size: 280, 150
                        size_hint: None, None
                        pos_hint: {'center_x':0.5,'center_y':1}
                        background_normal: 'D:\FYP\pic\dinner2.jpg'
                        on_press: root.manager.current = 'din'

<RecommendationScreen>:
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False    
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.44
                    pos_hint: {'center_x':30}
                    cols:1
                    spacing: 10
                    #row_default_height:40  
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 20
                        Button:
                            text: 'High Calorie'
                            #color: (0,0,0,1)
                            font_size: 30
                            size: 280, 150
                            size_hint: None, None
                            pos_hint: {'center_x':0.5,'center_y':0.5}
                            background_normal: 'D:\FYP\pic\highcalorie.jpg'
                            on_press: root.manager.current = 'HI'
        
                        Button:
                            text: 'Low Calorie'
                            font_size: 30
                            size: 280, 150
                            size_hint: None, None
                            pos_hint: {'center_x':0.5,'center_y':0.5}
                            background_normal: 'D:\FYP\pic\low.jpg'
                            on_press: root.manager.current = 'LO'
                            
                        Button:
                            text: 'Diabetic Appropriate'
                            font_size: 30
                            size: 280, 150
                            size_hint: None, None
                            pos_hint: {'center_x':0.5,'center_y':0.5}
                            background_normal: 'D:\FYP\pic\diabetic.jpg'
                            on_press: root.manager.current = 'diabe'
                            
                        Button:
                            text: 'Heart Healthy'
                            font_size: 30
                            size: 280, 150
                            size_hint: None, None
                            pos_hint: {'center_x':0.5,'center_y':0.5}
                            background_normal: 'D:\FYP\pic\heart.jpg'
                            on_press: root.manager.current = 'hear'
                                
                        Button:
                            text: 'Low Sodium'
                            font_size: 30
                            size: 280, 150
                            size_hint: None, None
                            pos_hint: {'center_x':0.5,'center_y':0.5}
                            background_normal: 'D:\FYP\pic\lowsodium.jpg'
                            on_press: root.manager.current = 'lowsod'


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
            rgba: (0, 0, 0, 1) if self.selected else (0, 181, 204, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    #color: (0, 181, 204, 1)
    on_press: root.on_enter(self)

<SelectableButton2>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0, 0, 0, 1) if self.selected else (0, 181, 204, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    #color: (0, 181, 204, 1)
    on_press: root.on_enter()

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

<BFScreen>:
    breakfast: breakfast

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.5
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: breakfast
                    
<DiabeticScreen>:
    diabetic: diabetic

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 2.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: diabetic
                    
<HeartScreen>:
    heart: heart

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 2.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: heart

<LowsodScreen>:
    lowsodium: lowsodium

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 2.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: lowsodium

<BFDetScreen>:
    #bfdet: bfdet

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    Label:
                        text : "Image"  
                        color: (0,0,0,1)
                    Label:
                        text: "Good: "
                        color: (0,0,0,1)
                    Label: 
                        text: "bad"
                        color: (0,0,0,1)
                    Button:
                        text: 'ingredient'
                        background_color: 1.000, 1.000, 0.330, 0.500
                        size: 100, 60
                        size_hint: None, None
                        #pos_hint: {'center_x':0.8,'center_y':0.6}
                        #on_press: root.manager.current = root.but_clr()



<RVVV>:
    BoxLayout:
        orientation: "vertical"
        #BoxLayout:
        #orientation: "vertical"
        #padding: 20

        GridLayout:
            size_hint: 1, None
            size_hint_y: None
            #spacing: 70
            height: 25
            cols: 3

            Label:
                text: "Name"
                color: (0, 181, 204, 1)

            Label:
                text: "Time(min)"
                color: (0, 181, 204, 1)

            Label:
                text: "Calorie"
                color: (0, 181, 204, 1)

        BoxLayout:
            RecycleView:
                viewclass: 'SelectableButton2'
                data: [{'text': str(x)} for x in root.data_items]

                SelectableRecycleGridLayout:
                    #padding: [20,60,20,60]
                    cols: 3
                    spacing: 10
                    default_size: None, dp(56)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    multiselect: True
                    touch_multiselect: True
                    multiline: True

<Low>:
    BoxLayout:
        orientation: "vertical"
        #BoxLayout:
        #orientation: "vertical"
        #padding: 20

        GridLayout:
            size_hint: 1, None
            size_hint_y: None
            #spacing: 70
            height: 25
            cols: 3

            Label:
                text: "Name"
                color: (0, 181, 204, 1)

            Label:
                text: "Time(min)"
                color: (0, 181, 204, 1)

            Label:
                text: "Calorie"
                color: (0, 181, 204, 1)

        BoxLayout:
            RecycleView:
                viewclass: 'SelectableButton'
                data: [{'text': str(x)} for x in root.data_items]

                SelectableRecycleGridLayout:
                    #padding: [20,60,20,60]
                    cols: 3
                    spacing: 10
                    default_size: None, dp(56)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    multiselect: True
                    touch_multiselect: True
                    multiline: True


<HIScreen>:
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            orientation: "vertical"
            size_hint: 1, 0.9
            RVVV:    

<LOScreen>:
    lowfood: lowfood

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: lowfood                

<IngredientScreen>:
    ingre: ingre
    input: input
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size 
            source: 'D:\FYP\pic\wall2.jpeg'
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7

        ScrollView:
            #size: 900,30
            size: self.size
            #do_scroll_x: False  
            GridLayout:
                id: content
                size_hint_x: 1
                size_hint_y: 1
                pos_hint: {'center_x':.9}
                rows:9
                cols:1
                spacing: 10
                padding: 39
                #row_default_height:40

                BoxLayout:
                    orientation: 'vertical'
                    #size:200,200
                    #size_hint: None, None
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: 'Insert Your Ingredient'
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.5,'center_y':0.6}
                    TextInput:
                        id: ingredient1
                        multiline: False
                        size_hint_x:None
                        size_hint_y:None
                        width:300
                        height: 30
                        pos_hint: {'center_x':0.5,'center_y':0.6}
                    Label:
                        text: "Result : "
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    Button:
                        text: 'Submit'
                        background_color: 1.000, 1.000, 0.330, 0.500
                        size: 100, 60
                        size_hint: None, None
                        #pos_hint: {'center_x':0.8,'center_y':0.6}
                        on_press: root.manager.current = root.but_search()
                    Button:
                        text: 'Clear'
                        background_color: 1.000, 1.000, 0.330, 0.500
                        size: 100, 60
                        size_hint: None, None
                        #pos_hint: {'center_x':0.8,'center_y':0.6}
                        on_press: root.manager.current = root.but_clr()
                    
                ScrollView:
                    #size: 900,30
                    size: self.size
                    #do_scroll_x: False   
                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 1.5
                        pos_hint: {'center_x':.9}
                        cols:1
                        spacing: 10
                        #row_default_height:40
                        id: ingre


<IngredientlistScreen>:
    BoxLayout:
        orientation: "vertical"
        #BoxLayout:
        #orientation: "vertical"
        #padding: 20

        GridLayout:
            size_hint: 1, None
            size_hint_y: None
            #spacing: 70
            height: 25
            cols: 3

            Label:
                text: "Name"
                color: (0, 181, 204, 1)

            Label:
                text: "Time(min)"
                color: (0, 181, 204, 1)

            Label:
                text: "Calorie"
                color: (0, 181, 204, 1)

        BoxLayout:
            RecycleView:
                viewclass: 'SelectableButton'
                data: [{'text': str(x)} for x in root.data_items]

                SelectableRecycleGridLayout:
                    #padding: [20,60,20,60]
                    cols: 3
                    spacing: 10
                    default_size: None, dp(56)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    multiselect: True
                    touch_multiselect: True
                    multiline: True

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        GridLayout:
            id: content
            #size_hint_x: .8
            rows:19
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

            Button:
                text: 'display'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                #pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = "discal"

            Button:
                text: 'Analysis'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                #pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = "analy"

            Label:
                id: info
                text: ''
                markup: True

            #MyLabel:
             #   id: calorie
              #  color: (0, 181, 204, 1)
               # text: "my calorie: {}".format(self.value)
                #markup: True



<RVV>:
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

<LuScreen>:
    lunch: lunch

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 2.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: lunch

<DinnerScreen>:
    dinner: dinner

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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 2.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: dinner

<DisCalScreen>:
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7

        #BoxLayout:
            #orientation: "vertical"
            #size_hint: 1, 0.9
            #RVV:
        GridLayout:
            id: content
            #size_hint_x: .8
            rows:17
            cols:2
            spacing: 20
            padding: 50
            #row_default_height:40

            MyLabel:
                id: age
                text: "my age: {}".format(self.value)
                markup: True
                color: (0, 181, 204, 1)

            MyLabel:
                id: gender
                text: "my gender: {}".format(self.value2)
                markup: True
                color: (0, 181, 204, 1)

            MyLabel:
                id: weight
                text: "my weight: {}".format(self.value)
                markup: True
                color: (0, 181, 204, 1)

            MyLabel:
                id: height
                text: "my height: {}".format(self.value)
                markup: True
                color: (0, 181, 204, 1)

            MyLabel:
                id: calorie
                text: "my calorie: {}".format(self.value)
                markup: True
                color: (0, 181, 204, 1)

            Button:
                text: 'Edit'
                on_press: root.manager.current = 'cal'

            Button:
                text: 'display'
                on_press: root.manager.current = root.but_try()

<HelloScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size 
            source: 'D:\FYP\pic\wall2.jpeg'
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        GridLayout:
            id: content
            #size_hint_x: .8
            rows:17
            cols:2
            spacing: 20
            padding: 50
            #row_default_height:40
            Label:
                text: 'Enter Food'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30

            TextInput:
                id: foodcalorie
                height: 30
                multiline: False
                size_hint_x:None
                size_hint_y:None
                width:400
                height: 30

            MyLabel:
                id: fname
                text: "food : {}".format(self.value2)
                markup: True
                color: (0, 181, 204, 1)

            MyLabel:
                id: serve
                text: "serving size : {}".format(self.value2)
                markup: True
                color: (0, 181, 204, 1)

            MyLabel:
                id: calorie
                text: "calorie : {}".format(self.value)
                markup: True
                color: (0, 181, 204, 1)


            Button:
                text: 'search'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                #pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = root.but_search()

<AnalysisScreen>
    box: box
    totcal: totcal
    bflist: bflist
    bfcal: bfcal
    dinlist: dinlist
    dincal: dincal

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size 
            source: 'D:\FYP\pic\wall2.jpeg'
    id: foodname
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        ScrollView:
            #size: 900,30
            size: self.size
            #do_scroll_x: False   
            GridLayout:
                id: content
                size_hint_x: 1
                size_hint_y: 1.8
                pos_hint: {'center_x':.9}
                rows:9
                cols:1
                spacing: 10
                padding: 39
                #row_default_height:40

                Spinner:
                    id: day
                    size_hint: None, None
                    size: 595, 40
                    #pos_hint: {'center': (.5, .5)}
                    text: 'Pick Your Day'
                    values: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
                    on_text:
                        print("The spinner {} has text {}".format(self, self.text))  

                GridLayout:
                    rows:7
                    cols:2
                    #size:200,200
                    #size_hint: None, None
                    #pos_hint: {'center_x':.9}
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "MealType: "
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Breakfast"
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Your Food: "
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    ScrollView:
                        #size: 900,30
                        size: self.size
                        #do_scroll_x: False   
                        GridLayout:
                            size_hint_x: 1
                            size_hint_y: 1.6
                            pos_hint: {'center_x':.9}
                            cols:1
                            spacing: 15
                            #padding: 39
                            #row_default_height:40
                            id: bflist
                    Label:
                        text: "Total Calorie: "
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 1.6
                        pos_hint: {'center_x':.9}
                        cols:1
                        spacing: 15
                        #padding: 39
                        #row_default_height:40
                        id: bfcal
                    Button:
                        text: "Add Food"
                        size: 100, 40
                        size_hint: None, None
                        on_press: root.manager.current = 'bfanalysis'


                GridLayout:
                    rows:7
                    cols:2
                    #size:200,200
                    #size_hint: None, None
                    #pos_hint: {'center_x':.9}
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "MealType: "
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Lunch"
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Your Food: "
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    ScrollView:
                        #size: 900,30
                        size: self.size
                        #do_scroll_x: False   
                        GridLayout:
                            size_hint_x: 1
                            size_hint_y: 1.6
                            pos_hint: {'center_x':.9}
                            cols:1
                            spacing: 15
                            #padding: 39
                            #row_default_height:40
                            id: box
                    Label:
                        text: "Total Calorie: "
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 1.6
                        pos_hint: {'center_x':.9}
                        cols:1
                        spacing: 15
                        #padding: 39
                        #row_default_height:40
                        id: totcal
                    Button:
                        text: "Add Food"
                        size: 100, 40
                        size_hint: None, None
                        on_press: root.manager.current = 'luanalysis'

                GridLayout:
                    rows:7
                    cols:2
                    #size:200,200
                    #size_hint: None, None
                    #pos_hint: {'center_x':.9}
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "MealType:"
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Dinner"
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Your Food: "
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    ScrollView:
                        #size: 900,30
                        size: self.size
                        #do_scroll_x: False   
                        GridLayout:
                            size_hint_x: 1
                            size_hint_y: 1.6
                            pos_hint: {'center_x':.9}
                            cols:1
                            spacing: 15
                            #padding: 39
                            #row_default_height:40
                            id: dinlist
                    Label:
                        text: "Total Calorie: "
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 1.6
                        pos_hint: {'center_x':.9}
                        cols:1
                        spacing: 15
                        #padding: 39
                        #row_default_height:40
                        id: dincal
                    Button:
                        text: "Add Food"
                        size: 100, 40
                        size_hint: None, None
                        on_press: root.manager.current = 'dianalysis'

                BoxLayout:
                    orientation: 'vertical'
                    #size:200,200
                    #size_hint: None, None
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "MealType: Snacks"
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Your Food: "
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Label:
                        text: "Total Calorie: "
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    Button:
                        text: "Add Food"
                        size: 100, 40
                        size_hint: None, None
                Button:
                    text: "Analysis Result"
                    size: 120, 40
                    size_hint: None, None
                    #pos_hint: {'center_x':3}
                    on_press: root.manager.current = 'result'

<AddFoodScreen>
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size 
            source: 'D:\FYP\pic\wall2.jpeg'
    id: addfood
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                #on_press: root.manager.current = 'cal'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        ScrollView:
            #size: 900,30
            size: self.size
            #do_scroll_x: False   
            GridLayout:
                id: content
                size_hint_x: 1
                size_hint_y: 0.7
                pos_hint: {'center_x':.9}
                rows:3
                cols:1
                spacing: 20
                padding: 39
                #row_default_height:40

                GridLayout:
                    #size_hint_x: .8
                    rows:9
                    cols:2
                    #spacing: 20
                    #padding: 50
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "Search my food"
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    TextInput:
                        hint: "Your Food: "
                        id: searchfood
                        height: 30
                        multiline: False
                        size_hint_x:None
                        size_hint_y:None
                        width:400
                        height: 30
                    MyLabel:
                        id: fname
                        text: "food : {}".format(self.value2)
                        markup: True
                        color: (0, 181, 204, 1)
                    MyLabel:
                        id: calorie
                        text: "calorie : {}".format(self.value)
                        markup: True
                        color: (0, 181, 204, 1)
                    MyLabel:
                        id: fname2
                        text: "food : {}".format(self.value2)
                        markup: True
                        color: (0, 181, 204, 1)
                    MyLabel:
                        id: fname3
                        text: "food : {}".format(self.value2)
                        markup: True
                        color: (0, 181, 204, 1)
                    Button:
                        #id: search
                        text: "search"
                        size: 100, 40
                        size_hint: None, None
                        on_press: root.manager.current = root.but_search()

                GridLayout:
                    id: manual
                    size_hint_y: 2
                    rows:11
                    cols:2
                    #spacing: 20
                    #padding: 50
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "Enter Food Manually"
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}
                    TextInput:
                        hint_text: "Your Food: "
                        id: food
                        height: 30
                        multiline: False
                        size_hint_x:None
                        size_hint_y:None
                        width:400
                        height: 30
                    Label:
                        text: "calorie"
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}

                    TextInput:
                        hint_text: "calorie: "
                        id: calcal
                        height: 30
                        multiline: False
                        size_hint_x:None
                        size_hint_y:None
                        width:400
                        height: 30

                    Label:
                        text: "Fat (g)"
                        color: (0,0,0,1)
                        #pos_hint: {'center_x':0.2,'center_y':0.6}

                    TextInput:
                        hint_text: "food type: "
                        id: type
                        height: 30
                        multiline: False
                        size_hint_x:None
                        size_hint_y:None
                        width:400
                        height: 30

                    Button:
                        text: "Add"
                        size: 100, 40
                        size_hint: None, None
                        on_press: root.manager.current = root.but_add()

<BFAnalysisScreen>:
    box: box
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                on_press: root.manager.current = 'hello'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: box

<LuAnalysisScreen>:
    box: box
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                on_press: root.manager.current = 'hello'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'

            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: box

<DiAnalysisScreen>:
    box: box
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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                on_press: root.manager.current = 'hello'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7
        BoxLayout:
            id: content
            #size_hint_x: .8

            ScrollView:
                #size: 900,30
                size: self.size
                #do_scroll_x: False   
                GridLayout:
                    size_hint_x: 1
                    size_hint_y: 1.6
                    pos_hint: {'center_x':.9}
                    cols:2
                    spacing: 10
                    padding: 39
                    #row_default_height:40
                    id: box

<FoodList>:
    BoxLayout:
        orientation: "vertical"
        #BoxLayout:
        #orientation: "vertical"
        #padding: 20

        GridLayout:
            size_hint: 1, None
            size_hint_y: None
            #spacing: 70
            height: 25
            cols: 3

            Label:
                text: "Name"
                color: (0, 181, 204, 1)

            Label:
                text: "Time(min)"
                color: (0, 181, 204, 1)

            Label:
                text: "Calorie"
                color: (0, 181, 204, 1)

        BoxLayout:
            RecycleView:
                viewclass: 'SelectableButton'
                data: [{'text': str(x)} for x in root.data_items]

                SelectableRecycleGridLayout:
                    id: grid
                    #padding: [20,60,20,60]
                    cols: 3
                    spacing: 10
                    default_size: None, dp(56)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'
                    multiselect: True
                    touch_multiselect: True
                    multiline: True

        Button:
            text: "Add"
            size: 100, 40
            size_hint: None, None
            on_press: root.manager.current = root.but_add()
    Button:
        text : 'Hello world'
        on_press : root.print_list()

<ResultScreen>:
    totalcal: totalcal
    moncal: moncal
    tuecal: tuecal
    wedcal: wedcal
    thucal: thucal
    frical: frical
    satcal: satcal
    suncal: suncal
    highday: highday
    highmealtype: highmealtype
    recommendation: recommendation
    suggestion: suggestion


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
                id: user_toggle
                text: 'Recommendation'
                size_hint_y: .1
                state: 'down'
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'recom'
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
                on_press: root.manager.current = 'hello'
            ToggleButton:
                id: analysis_toggle
                text: 'Analysis'
                size_hint_y: .1
                background_color: (.06, .47, .47, 1)
                background_normal: ''
                on_press: root.manager.current = 'cal'
            Label:
                id: sp
                text: ''
                size_hint_y: .7

        ScrollView:
            #size: 900,30
            size: self.size
            #do_scroll_x: False   
            GridLayout:
                id: content
                size_hint_x: 1
                size_hint_y: 1.5
                pos_hint: {'center_x':.9}
                rows:12
                cols:1
                spacing: 10
                padding: 39
                #row_default_height:40

                GridLayout:
                    rows:1
                    cols:3
                    size_hint_y: 0.3
                    spacing: 10
                    padding: 39
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height


                    Label:
                        text: "Monday"
                        size: 160, 80
                        size_hint: None, None
                        #color:(0,0,0,1)
                        #pos_hint: {'center_x':.8}
                        #on_press: root.manager.current = 'bfanalysis'
                    Label:
                        text: "Analysis Result"
                        size: 160, 80
                        size_hint: None, None
                        color:(0,0,0,1)
                        #pos_hint: {'center_x':.8}
                        #on_press: root.manager.current = 'bfanalysis'
                    Label:
                        text: "Monday"
                        size: 160, 80
                        size_hint: None, None
                        #pos_hint: {'center_x':.8}
                        #on_press: root.manager.current = 'bfanalysis'
                GridLayout:
                    rows:20
                    cols:2
                    size_hint_y: self.size_hint_y
                    
                    #size:200,200
                    #size_hint: None, None
                    #pos_hint: {'center_x':.9}
                    canvas.before:
                        Color:
                            rgba: .5, .5, .5, 1
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height

                    Label:
                        text: "This Week Total Calorie:"
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 1.6
                        pos_hint: {'center_x':.9}
                        cols:1
                        spacing: 20
                        #padding: 39
                        #row_default_height:40
                        id: totalcal
                    Label:
                        text: "Daily Total Calorie: "
                        color: (0,0,0,1)
                        pos_hint: {'center_x':0.2,'center_y':0.6}
                    ScrollView:
                        #size: 900,30
                        size_hint_x: 0.2
                        size_hint_y: 7.5
                        size: self.size
                        #do_scroll_x: False 
                        canvas.before:
                            Color:
                                rgba: .5, .5, .5, 1
                            Line:
                                width: 2
                                rectangle: self.x, self.y, self.width, self.height 
                        GridLayout:
                            size_hint_x: 0.8
                            size_hint_y: 1.7
                            pos_hint: {'center_x':.9}
                            rows: 14
                            cols:2
                            spacing: 30
                            padding: 10
                            #row_default_height:40

                            Label:
                                text: "Monday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: moncal
                            Label:
                                text: "Tuesday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: tuecal
                            Label:
                                text: "Wednesday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: wedcal
                            Label:
                                text: "Thursday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: thucal
                            Label:
                                text: "Friday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: frical
                            Label:
                                text: "Saturday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: satcal
                            Label:
                                text: "Sunday: "
                                color: (0,0,0,1)
                                pos_hint: {'center_x':0.2,'center_y':0.6}
                            GridLayout:
                                size_hint_x: 1
                                size_hint_y: 1.6
                                pos_hint: {'center_x':.9}
                                cols:1
                                spacing: 15
                                #padding: 39
                                #row_default_height:40
                                id: suncal

                    Label:
                        text: 'The highest calorie intake (Day) : '
                        color: (0,0,0,1)

                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 3
                        pos_hint: {'center_x':.9}
                        cols:1
                        #spacing: 15
                        #padding: 39
                        #row_default_height:40
                        id: highday

                    Label:
                        text: 'Meal Type : '
                        color: (0,0,0,1)

                    ScrollView:
                        #size: 900,30
                        size_hint_x: 0.2
                        size_hint_y: 5.2
                        size: self.size
                        #do_scroll_x: False 
                        canvas.before:
                            Color:
                                rgba: .5, .5, .5, 1
                            Line:
                                width: 2
                                rectangle: self.x, self.y, self.width, self.height

                        GridLayout:
                            size_hint_x: 1
                            size_hint_y: 3
                            pos_hint: {'center_x':.9}
                            cols:1
                            spacing: 15
                            #padding: 39
                            #row_default_height:40
                            id: highmealtype

                    Label:
                        text: 'Recommendation : '
                        color: (0,0,0,1)

                    ScrollView:
                        #size: 900,30
                        size_hint_x: 0.2
                        size_hint_y: 4.8
                        size: self.size
                        #do_scroll_x: False 
                        canvas.before:
                            Color:
                                rgba: .5, .5, .5, 1
                            Line:
                                width: 2
                                rectangle: self.x, self.y, self.width, self.height

                        GridLayout:
                            size_hint_x: 1
                            size_hint_y: 3
                            pos_hint: {'center_x':.9}
                            cols:1
                            spacing: 15
                            padding: 30
                            #row_default_height:40
                            id: recommendation


                    GridLayout:
                        size_hint_x: 1
                        size_hint_y: 1.2
                        pos_hint: {'center_x':.9}
                        cols:1
                        #spacing: 15
                        #padding: 39
                        #row_default_height:40
                        id: suggestion






""")

import mysql.connector as mysql
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.button import Button
import datetime

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="healthypro"
)
cursor = db.cursor()

global fooddetail


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

    def on_enter(self, instance):
        # self.selected = is_selected
        print(instance.text)

    def Pressbtn(self, instance):
        instance.parent.ids.lid.text = self.get_id(instance)


class SelectableButton2(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton2, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton2, self).on_touch_down(touch):
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

    def on_enter(self):
        sm.current = "home"


class RV(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_user()

    def get_user(self):
        loadname = "SELECT bf_name FROM breakfast Where food_type = 'Breakfast' ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class RVV(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(RVV, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_data()

    def get_data(self):
        loadname = "SELECT bf_name FROM breakfast Where food_type = 'Lunch' ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class RVVV(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(RVVV, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_data()

    def get_data(self):
        loadname = "SELECT bf_name, bf_time, bf_calorie FROM breakfast Where bf_calorie > 200 ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class Low(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(Low, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_data()

    def get_data(self):
        loadname = "SELECT bf_name, bf_time, bf_calorie FROM breakfast Where bf_calorie <= 200 ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class IngredientlistScreen(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(IngredientlistScreen, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_data()

    def get_data(self):
        loadname = "SELECT bf_name, bf_time, bf_calorie FROM breakfast Where bf_calorie <= 200 ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class FoodList(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(FoodList, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_data()

    def print_list(self):
        # here I expect textinputs id but got empty dict
        for child in self.ids.grid.children:
            print(child, child.text, child.id)

    def get_data(self):
        loadname = "SELECT foo_name, foo_calorie FROM foodcal Where foo_name = 200 ORDER BY bf_id ASC"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


class BFAnalysis(RecycleView):
    data_items = ListProperty([])
    image = Image(source='image.gif')

    def __init__(self, **kwargs):
        super(BFAnalysis, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        self.get_data()

    def get_data(self):
        loadname = "SELECT bf_name, bf_time, bf_calorie FROM breakfast Where food_type = 'breakfast'"

        cursor.execute(loadname)
        logincheck = cursor.fetchall()

        for row in logincheck:
            for col in row:
                self.data_items.append(col)


# global userLogId
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
        # cursor.execute(query)
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


class SettingsScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class BFScreen(Screen):
    breakfast = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        #fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_breakfast(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))

        query2 = "SELECT bf_name, bf_id FROM breakfast where food_type = 'breakfast'"

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.breakfast.add_widget(label1)
            label1.bind(on_press=self.press)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()


class BFDetScreen(Screen):
    pass


class LuScreen(Screen):
    lunch = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_lunch(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))

        query2 = "SELECT bf_name, bf_id FROM breakfast where food_type = 'lunch'"

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.lunch.add_widget(label1)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()

class DinnerScreen(Screen):
    dinner = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_dinner(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))

        query2 = "SELECT bf_name, bf_id FROM breakfast where food_type = 'dinner'"

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.dinner.add_widget(label1)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()


class RecommendationScreen(Screen):
    pass

class DiabeticScreen(Screen):
    diabetic = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        # fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_diabetic(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))


        type = "diabetic appropriate"
        query_start = "SELECT bf_name, bf_id FROM breakfast WHERE good LIKE '%"
        query_end = "%'"
        query2 = query_start + type + query_end

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.diabetic.add_widget(label1)
            label1.bind(on_press=self.press)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()

class HeartScreen(Screen):
    heart = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        # fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_heart(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))


        type = "heart healthy"
        query_start = "SELECT bf_name, bf_id FROM breakfast WHERE good LIKE '%"
        query_end = "%'"
        query2 = query_start + type + query_end

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.heart.add_widget(label1)
            label1.bind(on_press=self.press)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()

class LowsodScreen(Screen):
    lowsodium = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        # fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_lowsodium(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))


        type = "low sodium"
        query_start = "SELECT bf_name, bf_id FROM breakfast WHERE good LIKE '%"
        query_end = "%'"
        query2 = query_start + type + query_end

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.lowsodium.add_widget(label1)
            label1.bind(on_press=self.press)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()

class HIScreen(Screen):
    pass


class LOScreen(Screen):
    lowfood = ObjectProperty(None)

    def press(self, button):
        print("o yeah")
        fooddetail = button.bf_id
        sm.current = "bf_detail"

    def on_lowfood(self, *args):
        ID = 1
        query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

        cursor.execute(query.format(str(ID)))
        result = cursor.fetchone()[0]
        StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))

        query2 = "SELECT bf_name, bf_id FROM breakfast where food_type = 'breakfast' AND bf_calorie <= 200 "

        cursor.execute(query2)
        querycheck = cursor.fetchall()
        for i in querycheck:
            print(querycheck)
            label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20,
                            background_normal="D:\FYP\pic\Breakfast\{0}.jpg".format(str(i[1])))
            self.lowfood.add_widget(label1)

        # img = PIL.Image.open(StoredFilePath)
        # ImageFile.LOAD_TRUNCATED_IMAGES = True
        # img.show()
        # print(result)

        with open(StoredFilePath, "wb") as File:
            File.write(result)
            File.close()


class BFAnalysisScreen(Screen):
    box = ObjectProperty(None)

    def press(self, button):
        global userLogId
        print("kau press:  ", button.foo_id)

        global userLogId
        weekno = datetime.datetime.today().weekday()
        if weekno == 0:
            print("monday")
            query = "insert into monday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"
        elif weekno == 1:
            print("tuesday")
            query = "insert into tuesday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"
        elif weekno == 2:
            print("wednesday")
            query = "insert into wednesday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"
        elif weekno == 3:
            print("thursday")
            query = "insert into thursday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"
        elif weekno == 4:
            print("Friday")
            query = "insert into friday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"
        elif weekno == 5:
            print("Saturday")
            query = "insert into saturday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"
        elif weekno == 6:
            print("Sunday")
            query = "insert into sunday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Breakfast')"

        # query = "insert into monday (user_id, foo_id, mealtype) values ("+str(userLogId)+", "+str(button.foo_id)+", 'Breakfast')"
        # print(cursor.execute(query))
        db.commit()
        sm.current = "analy"
        # print(query)

        cursor.execute(query)
        db.commit()

    def on_box(self, *args):
        query = "SELECT foo_id, foo_name FROM foodcal ORDER BY foo_id ASC"

        cursor.execute(query)
        querycheck = cursor.fetchall()

        for i in querycheck:
            button = Button(text=str(i[1]), color=(1, 0, 1, 1), background_color=(0, 0, 0, 1),
                            outline_color=(1, 0, 1, 1))
            button.foo_id = i[0]
            self.box.add_widget(button)
            button.bind(on_press=self.press)


Factory.register('MyWidget', cls=BFAnalysisScreen)


class LuAnalysisScreen(Screen):
    box = ObjectProperty(None)

    def press(self, button):
        global userLogId
        print("kau press:  ", button.foo_id)

        weekno = datetime.datetime.today().weekday()
        if weekno == 0:
            print("monday")
            query = "insert into monday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"
        elif weekno == 1:
            print("tuesday")
            query = "insert into tuesday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"
        elif weekno == 2:
            print("wednesday")
            query = "insert into wednesday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"
        elif weekno == 3:
            print("thursday")
            query = "insert into thursday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"
        elif weekno == 4:
            print("Friday")
            query = "insert into friday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"
        elif weekno == 5:
            print("Saturday")
            query = "insert into saturday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"
        elif weekno == 6:
            print("Sunday")
            query = "insert into sunday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'Lunch')"

        # query = "insert into monday (user_id, foo_id, mealtype) values ("+str(userLogId)+", "+str(button.foo_id)+", 'Breakfast')"
        # print(cursor.execute(query))
        db.commit()
        sm.current = "analy"
        # print(query)

        cursor.execute(query)
        db.commit()

    def on_box(self, *args):
        query = "SELECT foo_id, foo_name FROM foodcal ORDER BY foo_id ASC"

        cursor.execute(query)
        querycheck = cursor.fetchall()

        for i in querycheck:
            button = Button(text=str(i[1]), color=(1, 0, 1, 1), background_color=(0, 0, 0, 1),
                            outline_color=(1, 0, 1, 1))
            button.foo_id = i[0]
            self.box.add_widget(button)
            button.bind(on_press=self.press)


Factory.register('MyWidget', cls=LuAnalysisScreen)


class DiAnalysisScreen(Screen):
    global weekno
    box = ObjectProperty(None)

    def press(self, button):
        global userLogId
        weekno = datetime.datetime.today().weekday()
        if weekno == 0:
            print("monday")
            query = "insert into monday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"
        elif weekno == 1:
            print("tuesday")
            query = "insert into tuesday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"
        elif weekno == 2:
            print("wednesday")
            query = "insert into wednesday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"
        elif weekno == 3:
            print("thursday")
            query = "insert into thursday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"
        elif weekno == 4:
            print("Friday")
            query = "insert into friday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"
        elif weekno == 5:
            print("Saturday")
            query = "insert into saturday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"
        elif weekno == 6:
            print("Sunday")
            query = "insert into sunday (user_id, foo_id, mealtype) values (" + str(userLogId) + ", " + str(
                button.foo_id) + ", 'dinner')"

        # print(cursor.execute(query))
        cursor.execute(query)
        db.commit()
        sm.current = "analy"
        # print(query)

    def on_box(self, *args):
        query = "SELECT foo_id, foo_name FROM foodcal ORDER BY foo_id ASC"

        cursor.execute(query)
        querycheck = cursor.fetchall()
        # print(querycheck)
        # lmao = querycheck[0][0]
        # print(lmao)
        for i in querycheck:
            button = Button(text=str(i[1]), color=(1, 0, 1, 1), background_color=(0, 0, 0, 1),
                            outline_color=(1, 0, 1, 1))
            button.foo_id = i[0]
            self.box.add_widget(button)
            button.bind(on_press=self.press)


Factory.register('MyWidget', cls=DiAnalysisScreen)


class AnalysisScreen(Screen):
    global weekno
    global userLogId
    weekno = datetime.datetime.today().weekday()
    data_items = ListProperty([])
    box = ObjectProperty(None)
    totcal = ObjectProperty(None)
    bflist = ObjectProperty(None)
    bfcal = ObjectProperty(None)
    dinlist = ObjectProperty(None)
    dincal = ObjectProperty(None)

    def on_bflist(self, *args):
        if weekno == 0:
            print("monday")
            query = "SELECT foodcal.foo_name FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 1:
            print("tuesday")
            query = "SELECT foodcal.foo_name FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 2:
            print("wednesday")
            query = "SELECT foodcal.foo_name FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 3:
            print("thursday")
            query = "SELECT foodcal.foo_name FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 4:
            print("Friday")
            query = "SELECT foodcal.foo_name FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 5:
            print("Saturday")
            query = "SELECT foodcal.foo_name FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 6:
            print("Sunday")
            query = "SELECT foodcal.foo_name FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        cursor.execute(query)

        querycheck = cursor.fetchall()
        print(querycheck)

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(i)
                self.bflist.add_widget(labell)

        else:
            labell = Label(text="No Food", color=(0, 181, 204, 1))
            self.bflist.add_widget(labell)
            print("tidakkkk")

    def on_bfcal(self, *args):
        if weekno == 0:
            print("monday")
            query = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 1:
            print("tuesday")
            query = "SELECT foodcal.foo_name FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 2:
            print("wednesday")
            query = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 3:
            print("thursday")
            query = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 4:
            print("Friday")
            query = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 5:
            print("Saturday")
            query = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        elif weekno == 6:
            print("Sunday")
            query = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND date = CURDATE()"
        cursor.execute(query)

        querycheck = cursor.fetchall()
        print(querycheck)

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                print(str(i))
                self.bfcal.add_widget(labell)

        else:
            labell = Label(text="No Food", color=(0, 181, 204, 1))
            self.bfcal.add_widget(labell)
            print("tidakkkk")

    def on_box(self, *args):
        if weekno == 0:
            print("monday")
            query = "SELECT foodcal.foo_name FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        elif weekno == 1:
            print("tuesday")
            query = "SELECT foodcal.foo_name FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        elif weekno == 2:
            print("wednesday")
            query = "SELECT foodcal.foo_name FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        elif weekno == 3:
            print("thursday")
            query = "SELECT foodcal.foo_name FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        elif weekno == 4:
            print("Friday")
            query = "SELECT foodcal.foo_name FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        elif weekno == 5:
            print("Saturday")
            query = "SELECT foodcal.foo_name FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        elif weekno == 6:
            print("Sunday")
            query = "SELECT foodcal.foo_name FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND date = CURDATE()"
        cursor.execute(query)

        querycheck = cursor.fetchall()
        print(querycheck)

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(i)
                self.box.add_widget(labell)

        else:
            labell = Label(text="No Food", color=(0, 181, 204, 1))
            self.box.add_widget(labell)
            print("tidakkkk")

    def on_totcal(self, *args):
        if weekno == 0:
            print("monday")
            query = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"
        elif weekno == 1:
            print("tuesday")
            query = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"
        elif weekno == 2:
            print("wednesday")
            query = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"
        elif weekno == 3:
            print("thursday")
            query = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"
        elif weekno == 4:
            print("Friday")
            query = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"
        elif weekno == 5:
            print("Saturday")
            query = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"
        elif weekno == 6:
            print("Sunday")
            query = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'Lunch' AND date = CURDATE()"

        cursor.execute(query)

        querycheck = cursor.fetchall()
        print(querycheck)

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                print(str(i))
                self.totcal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.totcal.add_widget(labell)
            print("tidakkkk")

    def on_dinlist(self, *args):
        if weekno == 0:
            print("monday")
            query = "SELECT foodcal.foo_name FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 1:
            print("tuesday")
            query = "SELECT foodcal.foo_name FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 2:
            print("wednesday")
            query = "SELECT foodcal.foo_name FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 3:
            print("thursday")
            query = "SELECT foodcal.foo_name FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 4:
            print("Friday")
            query = "SELECT foodcal.foo_name FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 5:
            print("Saturday")
            query = "SELECT foodcal.foo_name FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 6:
            print("Sunday")
            query = "SELECT foodcal.foo_name FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"

        cursor.execute(query)

        querycheck = cursor.fetchall()
        print(querycheck)

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(i)
                self.dinlist.add_widget(labell)

        else:
            labell = Label(text="No Food", color=(0, 181, 204, 1))
            self.dinlist.add_widget(labell)
            print("tidakkkk")

    def on_dincal(self, *args):
        if weekno == 0:
            print("monday")
            query = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 1:
            print("tuesday")
            query = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 2:
            print("wednesday")
            query = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 3:
            print("thursday")
            query = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 4:
            print("Friday")
            query = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 5:
            print("Saturday")
            query = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"
        elif weekno == 6:
            print("Sunday")
            query = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND date = CURDATE()"

        cursor.execute(query)

        querycheck = cursor.fetchall()
        print(querycheck)

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                print(str(i))
                self.dincal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.dincal.add_widget(labell)
            print("tidakkkk")


Factory.register('MyWidget', cls=AnalysisScreen)


class ResultScreen(Screen):
    global weekno

    weekno = datetime.datetime.today().weekday()
    data_items = ListProperty([])
    box = ObjectProperty(None)
    totalcal = ObjectProperty(None)
    moncal = ObjectProperty(None)
    tuecal = ObjectProperty(None)
    wedcal = ObjectProperty(None)
    thucal = ObjectProperty(None)
    frical = ObjectProperty(None)
    satcal = ObjectProperty(None)
    suncal = ObjectProperty(None)
    highday = ObjectProperty(None)
    highmealtype = ObjectProperty(None)
    recommendation = ObjectProperty(None)
    suggestion = ObjectProperty(None)

    def on_highday(self, *args):

        querymon = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymon)
        querymoncheck = cursor.fetchall()

        querytue = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytue)
        querytuecheck = cursor.fetchall()

        querywed = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywed)
        querywedcheck = cursor.fetchall()

        querythu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythu)
        querythucheck = cursor.fetchall()

        queryfri = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfri)
        queryfricheck = cursor.fetchall()

        querysat = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysat)
        querysatcheck = cursor.fetchall()

        querysun = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysun)
        querysuncheck = cursor.fetchall()

        query2 = "SELECT calorie FROM users WHERE user_id = 1"
        cursor.execute(query2)
        querycheck2 = cursor.fetchall()
        usercal = int(querycheck2[0][0])

        text = ""
        mon = (int(querymoncheck[0][0]) if querymoncheck[0][0] != None else 0)
        tue = (int(querytuecheck[0][0]) if querytuecheck[0][0] != None else 0)
        wed = (int(querywedcheck[0][0]) if querywedcheck[0][0] != None else 0)
        thu = (int(querythucheck[0][0]) if querythucheck[0][0] != None else 0)
        fri = (int(queryfricheck[0][0]) if queryfricheck[0][0] != None else 0)
        sat = (int(querysatcheck[0][0]) if querysatcheck[0][0] != None else 0)
        sun = (int(querysuncheck[0][0]) if querysuncheck[0][0] != None else 0)

        highest_calorie = max([mon, tue, wed, thu, fri, sat, sun])

        # breakfast = ..
        # lunch = ..
        # dinner = ..
        # highest_calorie_for_that_day = max([breakfast, lunch, dinner])

        if mon > usercal:
            text += "Monday,"
            # btn1 = Button(text="Recommendation", color=(0, 181, 204, 1))
            # self.highmealtype.add_widget(btn1)
        if tue > usercal:
            text += "Tuesday,"
        if wed > usercal:
            text += "Wednesday,"
        if thu > usercal:
            text += "Thursday,"
        if fri > usercal:
            text += "Friday,"
        if sat > usercal:
            text += "Saturday,"
        if sun > usercal:
            text += "Sunday,"

        text = text[:-1]

        labell = Label(text=str(text), color=(0, 181, 204, 1))
        self.highday.add_widget(labell)

    def on_highmealtype(self, *args):
        #global userLogId
        querymon = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymon)
        querymoncheck = cursor.fetchall()

        querytue = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytue)
        querytuecheck = cursor.fetchall()

        querywed = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywed)
        querywedcheck = cursor.fetchall()

        querythu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythu)
        querythucheck = cursor.fetchall()

        queryfri = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfri)
        queryfricheck = cursor.fetchall()

        querysat = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysat)
        querysatcheck = cursor.fetchall()

        querysun = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysun)
        querysuncheck = cursor.fetchall()

        query2 = "SELECT calorie FROM users WHERE user_id = 1"
        print("tidak!!!")
        #print(userLogId)
        print("tidak!!!!")
        cursor.execute(query2)
        querycheck2 = cursor.fetchall()
        usercal = int(querycheck2[0][0])

        # --------------------------------------------------------------------------------------------------------------
        # CHECK HIGHEST MEALTYPE
        querymonbf = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querymonlu = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querymondi = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymonbf)
        querymonbfcheck = cursor.fetchall()
        cursor.execute(querymonlu)
        querymonlucheck = cursor.fetchall()
        cursor.execute(querymondi)
        querymondicheck = cursor.fetchall()

        querytuebf = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querytuelu = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querytuedi = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytuebf)
        querytuebfcheck = cursor.fetchall()
        cursor.execute(querytuelu)
        querytuelucheck = cursor.fetchall()
        cursor.execute(querytuedi)
        querytuedicheck = cursor.fetchall()

        querywedbf = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querywedlu = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryweddi = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywedbf)
        querywedbfcheck = cursor.fetchall()
        cursor.execute(querywedlu)
        querywedlucheck = cursor.fetchall()
        cursor.execute(queryweddi)
        queryweddicheck = cursor.fetchall()

        querythubf = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querythulu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querythudi = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythubf)
        querythubfcheck = cursor.fetchall()
        cursor.execute(querythulu)
        querythulucheck = cursor.fetchall()
        cursor.execute(querythudi)
        querythudicheck = cursor.fetchall()

        queryfribf = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryfrilu = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryfridi = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfribf)
        queryfribfcheck = cursor.fetchall()
        cursor.execute(queryfrilu)
        queryfrilucheck = cursor.fetchall()
        cursor.execute(queryfridi)
        queryfridicheck = cursor.fetchall()

        querysatbf = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysatlu = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysatdi = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysatbf)
        querysatbfcheck = cursor.fetchall()
        cursor.execute(querysatlu)
        querysatlucheck = cursor.fetchall()
        cursor.execute(querysatdi)
        querysatdicheck = cursor.fetchall()

        querysunbf = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysunlu = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysundi = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysunbf)
        querysunbfcheck = cursor.fetchall()
        cursor.execute(querysunlu)
        querysunlucheck = cursor.fetchall()
        cursor.execute(querysundi)
        querysundicheck = cursor.fetchall()

        text2 = ""
        monbf = (int(querymonbfcheck[0][0]) if querymonbfcheck[0][0] != None else 0)
        monlu = (int(querymonlucheck[0][0]) if querymonlucheck[0][0] != None else 0)
        mondi = (int(querymondicheck[0][0]) if querymondicheck[0][0] != None else 0)

        tuebf = (int(querytuebfcheck[0][0]) if querytuebfcheck[0][0] != None else 0)
        tuelu = (int(querytuelucheck[0][0]) if querytuelucheck[0][0] != None else 0)
        tuedi = (int(querytuedicheck[0][0]) if querytuedicheck[0][0] != None else 0)

        wedbf = (int(querywedbfcheck[0][0]) if querywedbfcheck[0][0] != None else 0)
        wedlu = (int(querywedlucheck[0][0]) if querywedlucheck[0][0] != None else 0)
        weddi = (int(queryweddicheck[0][0]) if queryweddicheck[0][0] != None else 0)

        thubf = (int(querythubfcheck[0][0]) if querythubfcheck[0][0] != None else 0)
        thulu = (int(querythulucheck[0][0]) if querythulucheck[0][0] != None else 0)
        thudi = (int(querythudicheck[0][0]) if querythudicheck[0][0] != None else 0)

        fribf = (int(queryfribfcheck[0][0]) if queryfribfcheck[0][0] != None else 0)
        frilu = (int(queryfrilucheck[0][0]) if queryfrilucheck[0][0] != None else 0)
        fridi = (int(queryfridicheck[0][0]) if queryfridicheck[0][0] != None else 0)

        satbf = (int(querysatbfcheck[0][0]) if querysatbfcheck[0][0] != None else 0)
        satlu = (int(querysatlucheck[0][0]) if querysatlucheck[0][0] != None else 0)
        satdi = (int(querysatdicheck[0][0]) if querysatdicheck[0][0] != None else 0)

        sunbf = (int(querysunbfcheck[0][0]) if querysunbfcheck[0][0] != None else 0)
        sunlu = (int(querysunlucheck[0][0]) if querysunlucheck[0][0] != None else 0)
        sundi = (int(querysundicheck[0][0]) if querysundicheck[0][0] != None else 0)
        # ------------------------------------------------------------------------------------------------------------------------------

        text = ""
        mon = (int(querymoncheck[0][0]) if querymoncheck[0][0] != None else 0)
        tue = (int(querytuecheck[0][0]) if querytuecheck[0][0] != None else 0)
        wed = (int(querywedcheck[0][0]) if querywedcheck[0][0] != None else 0)
        thu = (int(querythucheck[0][0]) if querythucheck[0][0] != None else 0)
        fri = (int(queryfricheck[0][0]) if queryfricheck[0][0] != None else 0)
        sat = (int(querysatcheck[0][0]) if querysatcheck[0][0] != None else 0)
        sun = (int(querysuncheck[0][0]) if querysuncheck[0][0] != None else 0)

        highest_calorie = max([mon, tue, wed, thu, fri, sat, sun])

        # breakfast = ..
        # lunch = ..
        # dinner = ..
        # highest_calorie_for_that_day = max([breakfast, lunch, dinner])

        if mon > usercal:
            text += "Monday,"
            if monbf > 400:
                text2 += "breakfast,\n"
            if monlu > 700:
                text2 += "lunch,\n"
            if mondi > 500:
                text2 += "dinner,\n"
        if tue > usercal:
            text += "Tuesday,"
            if monbf > 400:
                text2 += "breakfast,"
            if monlu > 700:
                text2 += "lunch,"
            if mondi > 500:
                text2 += "dinner,"
        if wed > usercal:
            text += "Wednesday,"
            if monbf > 400:
                text2 += "breakfast,"
            if monlu > 700:
                text2 += "lunch,"
            if mondi > 500:
                text2 += "dinner,"
        if thu > usercal:
            text += "Thursday,"
            if monbf > 400:
                text2 += "breakfast,"
            if monlu > 700:
                text2 += "lunch,"
            if mondi > 500:
                text2 += "dinner,"
        if fri > usercal:
            text += "Friday,"
            if monbf > 400:
                text2 += "breakfast,\n"
            if monlu > 700:
                text2 += "lunch,\n"
            if mondi > 500:
                text2 += "dinner,\n"
        if sat > usercal:
            text += "Saturday,"
            if monbf > 400:
                text2 += "breakfast,"
            if monlu > 700:
                text2 += "lunch,"
            if mondi > 500:
                text2 += "dinner,"
        if sun > usercal:
            text += "Sunday,"
            if monbf > 400:
                text2 += "breakfast,"
            if monlu > 700:
                text2 += "lunch,"
            if mondi > 500:
                text2 += "dinner,"

        text = text[:-1]
        text2 = text2[:-1]

        labell = Label(text=str(text2), color=(0, 181, 204, 1))
        self.highmealtype.add_widget(labell)

    def press(self, labell):
        print("o yeah")
        sm.current = "LO"
        # fooddetail = button.bf_id

    def on_recommendation(self, *args):

        querymon = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymon)
        querymoncheck = cursor.fetchall()

        querytue = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytue)
        querytuecheck = cursor.fetchall()

        querywed = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywed)
        querywedcheck = cursor.fetchall()

        querythu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythu)
        querythucheck = cursor.fetchall()

        queryfri = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfri)
        queryfricheck = cursor.fetchall()

        querysat = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysat)
        querysatcheck = cursor.fetchall()

        querysun = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysun)
        querysuncheck = cursor.fetchall()

        query2 = "SELECT calorie FROM users WHERE user_id = 1"
        cursor.execute(query2)
        querycheck2 = cursor.fetchall()
        usercal = int(querycheck2[0][0])

        # --------------------------------------------------------------------------------------------------------------
        # CHECK HIGHEST MEALTYPE
        querymonbf = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querymonlu = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querymondi = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymonbf)
        querymonbfcheck = cursor.fetchall()
        cursor.execute(querymonlu)
        querymonlucheck = cursor.fetchall()
        cursor.execute(querymondi)
        querymondicheck = cursor.fetchall()

        querytuebf = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querytuelu = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querytuedi = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytuebf)
        querytuebfcheck = cursor.fetchall()
        cursor.execute(querytuelu)
        querytuelucheck = cursor.fetchall()
        cursor.execute(querytuedi)
        querytuedicheck = cursor.fetchall()

        querywedbf = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querywedlu = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryweddi = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywedbf)
        querywedbfcheck = cursor.fetchall()
        cursor.execute(querywedlu)
        querywedlucheck = cursor.fetchall()
        cursor.execute(queryweddi)
        queryweddicheck = cursor.fetchall()

        querythubf = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querythulu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querythudi = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythubf)
        querythubfcheck = cursor.fetchall()
        cursor.execute(querythulu)
        querythulucheck = cursor.fetchall()
        cursor.execute(querythudi)
        querythudicheck = cursor.fetchall()

        queryfribf = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryfrilu = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryfridi = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfribf)
        queryfribfcheck = cursor.fetchall()
        cursor.execute(queryfrilu)
        queryfrilucheck = cursor.fetchall()
        cursor.execute(queryfridi)
        queryfridicheck = cursor.fetchall()

        querysatbf = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysatlu = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysatdi = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysatbf)
        querysatbfcheck = cursor.fetchall()
        cursor.execute(querysatlu)
        querysatlucheck = cursor.fetchall()
        cursor.execute(querysatdi)
        querysatdicheck = cursor.fetchall()

        querysunbf = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysunlu = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysundi = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysunbf)
        querysunbfcheck = cursor.fetchall()
        cursor.execute(querysunlu)
        querysunlucheck = cursor.fetchall()
        cursor.execute(querysundi)
        querysundicheck = cursor.fetchall()

        text2 = ""
        monbf = (int(querymonbfcheck[0][0]) if querymonbfcheck[0][0] != None else 0)
        monlu = (int(querymonlucheck[0][0]) if querymonlucheck[0][0] != None else 0)
        mondi = (int(querymondicheck[0][0]) if querymondicheck[0][0] != None else 0)

        tuebf = (int(querytuebfcheck[0][0]) if querytuebfcheck[0][0] != None else 0)
        tuelu = (int(querytuelucheck[0][0]) if querytuelucheck[0][0] != None else 0)
        tuedi = (int(querytuedicheck[0][0]) if querytuedicheck[0][0] != None else 0)

        wedbf = (int(querywedbfcheck[0][0]) if querywedbfcheck[0][0] != None else 0)
        wedlu = (int(querywedlucheck[0][0]) if querywedlucheck[0][0] != None else 0)
        weddi = (int(queryweddicheck[0][0]) if queryweddicheck[0][0] != None else 0)

        thubf = (int(querythubfcheck[0][0]) if querythubfcheck[0][0] != None else 0)
        thulu = (int(querythulucheck[0][0]) if querythulucheck[0][0] != None else 0)
        thudi = (int(querythudicheck[0][0]) if querythudicheck[0][0] != None else 0)

        fribf = (int(queryfribfcheck[0][0]) if queryfribfcheck[0][0] != None else 0)
        frilu = (int(queryfrilucheck[0][0]) if queryfrilucheck[0][0] != None else 0)
        fridi = (int(queryfridicheck[0][0]) if queryfridicheck[0][0] != None else 0)

        satbf = (int(querysatbfcheck[0][0]) if querysatbfcheck[0][0] != None else 0)
        satlu = (int(querysatlucheck[0][0]) if querysatlucheck[0][0] != None else 0)
        satdi = (int(querysatdicheck[0][0]) if querysatdicheck[0][0] != None else 0)

        sunbf = (int(querysunbfcheck[0][0]) if querysunbfcheck[0][0] != None else 0)
        sunlu = (int(querysunlucheck[0][0]) if querysunlucheck[0][0] != None else 0)
        sundi = (int(querysundicheck[0][0]) if querysundicheck[0][0] != None else 0)
        # ------------------------------------------------------------------------------------------------------------------------------

        text = ""
        mon = (int(querymoncheck[0][0]) if querymoncheck[0][0] != None else 0)
        tue = (int(querytuecheck[0][0]) if querytuecheck[0][0] != None else 0)
        wed = (int(querywedcheck[0][0]) if querywedcheck[0][0] != None else 0)
        thu = (int(querythucheck[0][0]) if querythucheck[0][0] != None else 0)
        fri = (int(queryfricheck[0][0]) if queryfricheck[0][0] != None else 0)
        sat = (int(querysatcheck[0][0]) if querysatcheck[0][0] != None else 0)
        sun = (int(querysuncheck[0][0]) if querysuncheck[0][0] != None else 0)

        highest_calorie = max([mon, tue, wed, thu, fri, sat, sun])

        # breakfast = ..
        # lunch = ..
        # dinner = ..
        # highest_calorie_for_that_day = max([breakfast, lunch, dinner])

        if mon > usercal:
            text += "Monday,"
            if monbf > 400:
                text2 += "Eat low calorie food for breakfast(monday),\n"

            if monlu > 700:
                text2 += "Eat low calorie food for lunch(monday),\n"

            if mondi > 550:
                text2 += "Eat low calorie food for dinner(monday),\n"
        if tue > usercal:
            text += "Tuesday,"
            if tuebf > 400:
                text2 += "Eat low calorie food for \nbreakfast(tuesaday),\n"
            if tuelu > 700:
                text2 += "Eat low calorie food for \nlunch(tuesaday),\n"
            if tuedi > 550:
                text2 += "Eat low calorie food for \ndinner(tuesaday),\n"
        if wed > usercal:
            text += "Wednesday,"
            if wedbf > 400:
                text2 += "Eat low calorie food for \nbreakfast(wednesday),\n"
            if wedlu > 700:
                text2 += "Eat low calorie food for \nlunch(wednesday),\n"
            if weddi > 550:
                text2 += "Eat low calorie food for \ndinner(wednesday),\n"
        if thu > usercal:
            text += "Thursday,"
            if thubf > 400:
                text2 += "Eat low calorie food for \nbreakfast(thursday),\n"

            if thulu > 700:
                text2 += "Eat low calorie food for \nlunch(thursday),\n"

            if thudi > 550:
                text2 += "Eat low calorie food for \ndinner(thursday),\n"
        if fri > usercal:
            text += "Friday,"
            if fribf > 400:
                text2 += "Eat low calorie food for breakfast(friday),\n"

            if frilu > 700:
                text2 += "Eat low calorie food for lunch(friday),\n"

            if fridi > 550:
                text2 += "Eat low calorie food for dinner(friday),\n"
        if sat > usercal:
            text += "Saturday,"
            if satbf > 400:
                text2 += "You should eat low calorie food for \nbreakfast,"

            if satlu > 700:
                text2 += "You should eat low calorie food for \nlunch,"

            if satdi > 550:
                text2 += "You should eat low calorie food for \nlunch,"
        if sun > usercal:
            text += "Sunday,"
            if sunbf > 400:
                text2 += "You should eat low calorie food for breakfast,"

            if sunlu > 700:
                text2 += "You should eat low calorie food for lunch,"

            if sundi > 550:
                text2 += "You should eat low calorie food for lunch,"

        text = text[:-1]
        text2 = text2[:-1]

        labell = Label(text=str(text2), color=(0, 181, 204, 1))
        self.recommendation.add_widget(labell)
        # labell.bind(on_press=self.press)

    def recom(self, button):
        print("o yeah")
        sm.current = "LO"
        # fooddetail = button.bf_id

    def on_suggestion(self, *args):

        querymon = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymon)
        querymoncheck = cursor.fetchall()

        querytue = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytue)
        querytuecheck = cursor.fetchall()

        querywed = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywed)
        querywedcheck = cursor.fetchall()

        querythu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythu)
        querythucheck = cursor.fetchall()

        queryfri = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfri)
        queryfricheck = cursor.fetchall()

        querysat = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysat)
        querysatcheck = cursor.fetchall()

        querysun = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysun)
        querysuncheck = cursor.fetchall()

        query2 = "SELECT calorie FROM users WHERE user_id = 1"
        cursor.execute(query2)
        querycheck2 = cursor.fetchall()
        usercal = int(querycheck2[0][0])

        # --------------------------------------------------------------------------------------------------------------
        # CHECK HIGHEST MEALTYPE
        querymonbf = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querymonlu = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querymondi = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querymonbf)
        querymonbfcheck = cursor.fetchall()
        cursor.execute(querymonlu)
        querymonlucheck = cursor.fetchall()
        cursor.execute(querymondi)
        querymondicheck = cursor.fetchall()

        querytuebf = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querytuelu = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querytuedi = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querytuebf)
        querytuebfcheck = cursor.fetchall()
        cursor.execute(querytuelu)
        querytuelucheck = cursor.fetchall()
        cursor.execute(querytuedi)
        querytuedicheck = cursor.fetchall()

        querywedbf = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querywedlu = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryweddi = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querywedbf)
        querywedbfcheck = cursor.fetchall()
        cursor.execute(querywedlu)
        querywedlucheck = cursor.fetchall()
        cursor.execute(queryweddi)
        queryweddicheck = cursor.fetchall()

        querythubf = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querythulu = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querythudi = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querythubf)
        querythubfcheck = cursor.fetchall()
        cursor.execute(querythulu)
        querythulucheck = cursor.fetchall()
        cursor.execute(querythudi)
        querythudicheck = cursor.fetchall()

        queryfribf = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryfrilu = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        queryfridi = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(queryfribf)
        queryfribfcheck = cursor.fetchall()
        cursor.execute(queryfrilu)
        queryfrilucheck = cursor.fetchall()
        cursor.execute(queryfridi)
        queryfridicheck = cursor.fetchall()

        querysatbf = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysatlu = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysatdi = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysatbf)
        querysatbfcheck = cursor.fetchall()
        cursor.execute(querysatlu)
        querysatlucheck = cursor.fetchall()
        cursor.execute(querysatdi)
        querysatdicheck = cursor.fetchall()

        querysunbf = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'breakfast' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysunlu = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'lunch' AND YEARWEEK(date) = YEARWEEK(NOW())"
        querysundi = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND mealtype = 'dinner' AND YEARWEEK(date) = YEARWEEK(NOW())"
        cursor.execute(querysunbf)
        querysunbfcheck = cursor.fetchall()
        cursor.execute(querysunlu)
        querysunlucheck = cursor.fetchall()
        cursor.execute(querysundi)
        querysundicheck = cursor.fetchall()

        text2 = ""
        monbf = (int(querymonbfcheck[0][0]) if querymonbfcheck[0][0] != None else 0)
        monlu = (int(querymonlucheck[0][0]) if querymonlucheck[0][0] != None else 0)
        mondi = (int(querymondicheck[0][0]) if querymondicheck[0][0] != None else 0)

        tuebf = (int(querytuebfcheck[0][0]) if querytuebfcheck[0][0] != None else 0)
        tuelu = (int(querytuelucheck[0][0]) if querytuelucheck[0][0] != None else 0)
        tuedi = (int(querytuedicheck[0][0]) if querytuedicheck[0][0] != None else 0)

        wedbf = (int(querywedbfcheck[0][0]) if querywedbfcheck[0][0] != None else 0)
        wedlu = (int(querywedlucheck[0][0]) if querywedlucheck[0][0] != None else 0)
        weddi = (int(queryweddicheck[0][0]) if queryweddicheck[0][0] != None else 0)

        thubf = (int(querythubfcheck[0][0]) if querythubfcheck[0][0] != None else 0)
        thulu = (int(querythulucheck[0][0]) if querythulucheck[0][0] != None else 0)
        thudi = (int(querythudicheck[0][0]) if querythudicheck[0][0] != None else 0)

        fribf = (int(queryfribfcheck[0][0]) if queryfribfcheck[0][0] != None else 0)
        frilu = (int(queryfrilucheck[0][0]) if queryfrilucheck[0][0] != None else 0)
        fridi = (int(queryfridicheck[0][0]) if queryfridicheck[0][0] != None else 0)

        satbf = (int(querysatbfcheck[0][0]) if querysatbfcheck[0][0] != None else 0)
        satlu = (int(querysatlucheck[0][0]) if querysatlucheck[0][0] != None else 0)
        satdi = (int(querysatdicheck[0][0]) if querysatdicheck[0][0] != None else 0)

        sunbf = (int(querysunbfcheck[0][0]) if querysunbfcheck[0][0] != None else 0)
        sunlu = (int(querysunlucheck[0][0]) if querysunlucheck[0][0] != None else 0)
        sundi = (int(querysundicheck[0][0]) if querysundicheck[0][0] != None else 0)
        # ------------------------------------------------------------------------------------------------------------------------------

        text = ""
        mon = (int(querymoncheck[0][0]) if querymoncheck[0][0] != None else 0)
        tue = (int(querytuecheck[0][0]) if querytuecheck[0][0] != None else 0)
        wed = (int(querywedcheck[0][0]) if querywedcheck[0][0] != None else 0)
        thu = (int(querythucheck[0][0]) if querythucheck[0][0] != None else 0)
        fri = (int(queryfricheck[0][0]) if queryfricheck[0][0] != None else 0)
        sat = (int(querysatcheck[0][0]) if querysatcheck[0][0] != None else 0)
        sun = (int(querysuncheck[0][0]) if querysuncheck[0][0] != None else 0)

        highest_calorie = max([mon, tue, wed, thu, fri, sat, sun])

        # breakfast = ..
        # lunch = ..
        # dinner = ..
        # highest_calorie_for_that_day = max([breakfast, lunch, dinner])

        if mon > usercal:
            text += "Monday,"
            if monbf > 400:
                text2 += "Eat low calorie food for \nbreakfast(monday)\n,"
                button = Button(text="See Meal Suggestion for monday", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if monlu > 700:
                    text2 += "Eat low calorie food for \nlunch(monday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if mondi > 550:
                        text2 += "Eat low calorie food for \ndinner(monday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)
        if tue > usercal:
            text += "Tuesday,"
            if tuebf > 400:
                text2 += "Eat low calorie food for \nbreakfast(tuesday)\n,"
                button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if tuelu > 700:
                    text2 += "Eat low calorie food for \nlunch(tuesday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if tuedi > 550:
                        text2 += "Eat low calorie food for \ndinner(tuesday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)
        if wed > usercal:
            text += "Wednesday,"
            if wedbf > 400:
                text2 += "Eat low calorie food for \nbreakfast(wednesday)\n,"
                button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if wedlu > 700:
                    text2 += "Eat low calorie food for \nlunch(wednesday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if weddi > 550:
                        text2 += "Eat low calorie food for \ndinner(wednesday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)
        if thu > usercal:
            text += "Thursday,"
            if thubf > 400:
                text2 += "Eat low calorie food for \nbreakfast(thursday)\n,"
                button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if thulu > 700:
                    text2 += "Eat low calorie food for \nlunch(thursday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if thudi > 550:
                        text2 += "Eat low calorie food for \ndinner(thursday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)
        if fri > usercal:
            text += "Friday,"
            if fribf > 400:
                text2 += "Eat low calorie food for \nbreakfast(friday)\n,"
                button = Button(text="See Meal Suggestion for friday", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if frilu > 700:
                    text2 += "Eat low calorie food for \nlunch(friday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if fridi > 550:
                        text2 += "Eat low calorie food for \ndinner(friday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)
        if sat > usercal:
            text += "Saturday,"
            if satbf > 400:
                text2 += "Eat low calorie food for \nbreakfast(saturday)\n,"
                button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if satlu > 700:
                    text2 += "Eat low calorie food for \nlunch(saturday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if satdi > 550:
                        text2 += "Eat low calorie food for \ndinner(saturday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)
        if sun > usercal:
            text += "Sunday,"
            if sunbf > 400:
                text2 += "Eat low calorie food for \nbreakfast(sunday)\n,"
                button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                self.suggestion.add_widget(button)
                button.bind(on_press=self.recom)
            else:
                if sunlu > 700:
                    text2 += "Eat low calorie food for \nlunch(sunday)\n,"
                    button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                    self.suggestion.add_widget(button)
                    button.bind(on_press=self.recom)
                else:
                    if sundi > 550:
                        text2 += "Eat low calorie food for \ndinner(sunday)\n,"
                        button = Button(text="See Meal Suggestion", color=(1, 1, 1, 1))
                        self.suggestion.add_widget(button)
                        button.bind(on_press=self.recom)

        text = text[:-1]
        text2 = text2[:-1]

        # labell = Label(text=str(text2), color=(0, 181, 204, 1))
        # self.recommendation.add_widget(labell)
        # labell.bind(on_press=self.press)

    def on_totalcal(self, *args):

        query = "SELECT SUM(tbl.foo_calorie) AS TotalPrice FROM (SELECT foodcal.foo_calorie FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW()) UNION ALL SELECT foodcal.foo_calorie FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW()) UNION ALL SELECT foodcal.foo_calorie FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW()) UNION ALL SELECT foodcal.foo_calorie FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW()) UNION ALL SELECT foodcal.foo_calorie FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW()) UNION ALL SELECT foodcal.foo_calorie FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW()) UNION ALL SELECT foodcal.foo_calorie FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())) tbl"

        cursor.execute(query)

        querycheck = cursor.fetchall()
        # print("pishang")

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.totalcal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.totalcal.add_widget(labell)
            print("tidakkkk")

    def on_moncal(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM monday INNER JOIN foodcal ON monday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.moncal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.moncal.add_widget(labell)
            print("tidakkkk")

    def on_tuecal(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM tuesday INNER JOIN foodcal ON tuesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.tuecal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.tuecal.add_widget(labell)
            print("tidakkkk")

    def on_wedcal(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM wednesday INNER JOIN foodcal ON wednesday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.wedcal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.wedcal.add_widget(labell)
            print("tidakkkk")

    def on_thucal(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM thursday INNER JOIN foodcal ON thursday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.thucal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.thucal.add_widget(labell)
            print("tidakkkk")

    def on_frical(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM friday INNER JOIN foodcal ON friday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.frical.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.frical.add_widget(labell)
            print("tidakkkk")

    def on_satcal(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM saturday INNER JOIN foodcal ON saturday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.satcal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.satcal.add_widget(labell)
            print("tidakkkk")

    def on_suncal(self, *args):

        query = "SELECT sum(foodcal.foo_calorie) FROM sunday INNER JOIN foodcal ON sunday.foo_id=foodcal.foo_id WHERE user_id = 1 AND YEARWEEK(date) = YEARWEEK(NOW())"

        cursor.execute(query)

        querycheck = cursor.fetchall()

        if len(querycheck) > 0:
            for i in querycheck:
                labell = Label(text=str(i[0]), color=(0, 181, 204, 1))
                labell.foo_id = i[0]
                # print(str(i))
                self.suncal.add_widget(labell)
        else:
            labell = Label(text="No cal", color=(0, 181, 204, 1))
            self.suncal.add_widget(labell)
            print("tidakkkk")


class AddFoodScreen(Screen):
    data_items = ListProperty([])

    def but_search(self):
        searchfood = self.ids.searchfood.text
        fname = self.ids.fname
        fname2 = self.ids.fname2
        fname3 = self.ids.fname3
        calorie = self.ids.calorie

        if searchfood == "":
            print("no no no boii")
        else:
            query_start = "SELECT foo_name, foo_calorie FROM foodcal WHERE foo_name LIKE '%"
            query_end = "%'"
            query = query_start + searchfood + query_end
            cursor.execute(query)
            display = cursor.fetchall()
            # print(display)

            for x in display:
                print(x)

            trydis = display[0][0]
            trythat = display
            # trydis2 = display[0][2]
            trydis3 = display[0][1]

            print(trydis)
            fname.text = trydis

            if searchfood in display:
                # fname2.text = trythat
                print("yes")
            else:
                print("takde")

            # fname2.text = trythat
            fname3.text = trydis
            # serve.text = trydis2
            calorie.value = trydis3
            db.commit()

    def but_add(self):
        global userLogId
        food = self.ids.food.text
        calcal = self.ids.calcal.text
        type = self.ids.type.text
        # calorie = self.ids.calorie
        cursor = db.cursor()
        # str(int(self.a.text) * int(self.b.text))

        if food == "" and calcal == "":
            # info.text = '[color=#FF0000]Enter username and password[/color]'
            print("nope")
            sm.current = "addfood"
        else:
            ## defining the Query
            query = "insert into monday (foo_id, user_id) values ((select foo_id from foodcal where user_id = %s), %s, %s, %s)"

            ## storing values in a variable
            values = (userLogId, food, type, calcal)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.close()

            # info.text = '[color=#008000]you have entered your body information[/color]'
            print(cursor.rowcount, "records inserted")
            # print(calorie)

            sm.current = "addfood"


class IngredientScreen(Screen):
    ingre = ObjectProperty(None)

    def but_search(self):
        ingredient = self.ids.ingredient1.text

        if ingredient == "":
            print("no no no boii")
        else:
            ID = 1
            query = "SELECT bf_image FROM breakfast where bf_id = '{0}'"

            cursor.execute(query.format(str(ID)))
            result = cursor.fetchone()[0]
            StoredFilePath = "D:\FYP\pic\Breakfast\img{0}.jpg".format(str(ID))

            query_start = "SELECT bf_name FROM breakfast WHERE bf_ing LIKE '%"
            query_end = "%'"
            query2 = query_start + ingredient + query_end
            cursor.execute(query2)
            querycheck = cursor.fetchall()

            if len(querycheck) > 0:
                for i in querycheck:
                    label1 = Button(text=str(i[0]), color=(1, 1, 1, 1), font_size=20)
                    self.ingre.add_widget(label1)
                    #label1.bind(on_press=self.press)

            with open(StoredFilePath, "wb") as File:
                File.write(result)
                File.close()

    def but_clr(self):
        self.ids.ingredient1.text = ''
        labell = Label(text="BODOH", color=(0, 181, 204, 1))
        self.ingre.add_widget(labell)
        #layout.clear_widgets(labell)
        #self.ids.ingre.text = ''



class MyLabel(Label):
    value = NumericProperty(1.0)
    value2 = StringProperty(0)


class DisCalScreen(Screen):
    def but_try(self):
        global userLogId
        query = ("SELECT * FROM users WHERE user_id = '%s' ")
        value = (userLogId)
        cursor.execute(query % value)
        age = self.ids.age
        gender = self.ids.gender
        weight = self.ids.weight
        height = self.ids.height
        calorie = self.ids.calorie

        print(userLogId)
        display = cursor.fetchall()
        trydis = display[0][3]
        trydis2 = display[0][4]
        trydis3 = display[0][5]
        trydis4 = display[0][6]
        trydis5 = display[0][7]
        print(trydis)
        age.value = trydis
        gender.text = trydis2
        weight.value = trydis3
        height.value = trydis4
        calorie.value = trydis5
        db.commit()


class CalScreen(Screen):
    def but_sub(self):
        global userLogId
        ag = self.ids.age.text
        gen = self.ids.gender.text
        weig = self.ids.weight.text
        heig = self.ids.height.text
        info = self.ids.info
        # calorie = self.ids.calorie
        cursor = db.cursor()
        # str(int(self.a.text) * int(self.b.text))

        if ag == "" and gen == "":
            # info.text = '[color=#FF0000]Enter username and password[/color]'
            print("nope")
            sm.current = "cal"
        else:
            calorie = ((10 * (int(weig))) + (6.25 * (int(heig))) - (5 * (int(ag))) + 5) * 1.4
            ## defining the Query
            query = "INSERT INTO users(age,gender,weight,height) VALUES (%s, %s, %s, %s)"

            query = ('''
                        UPDATE users

                        SET age = %s,
                            gender = %s,
                            weight = %s,
                            height = %s,
                            calorie = %s


                        WHERE user_id = '%s'        
                        ''')

            ## storing values in a variable
            values = (ag, gen, weig, heig, calorie, userLogId)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.close()

            info.text = '[color=#008000]you have entered your body information[/color]'
            print(cursor.rowcount, "records inserted")
            # print(calorie)

            sm.current = "cal"

    def but_try(self):
        pass

    def but_kita(self):
        global userLogId
        data_items = ListProperty([])
        query = ("SELECT * FROM users WHERE user_id = '%s' ")
        value = (userLogId)
        cursor.execute(query % value)
        info = self.ids.info
        print(userLogId)
        display = cursor.fetchall()
        trydis = display
        print(trydis)
        info.value = trydis

        for row in display:
            for col in row:
                info.value = trydis


class HelloScreen(Screen):
    def but_search(self):
        foodcalorie = self.ids.foodcalorie.text
        fname = self.ids.fname
        serve = self.ids.serve
        calorie = self.ids.calorie

        if foodcalorie == "":
            print("no no no boii")
        else:
            query_start = "SELECT * FROM foodcal WHERE foo_name LIKE '%"
            query_end = "%'"
            query = query_start + foodcalorie + query_end
            cursor.execute(query)
            display = cursor.fetchall()
            print(display)
            # db.commit()
            # db.close()

            # print(userLogId)
            # display = cursor.fetchall()
            trydis = display[0][1]
            trydis2 = display[0][2]
            trydis3 = display[0][3]

            print(trydis)
            fname.text = trydis
            serve.text = trydis2
            calorie.value = trydis3
            db.commit()
            # db.close()


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(RecommendationScreen(name='recom'))
sm.add_widget(DiabeticScreen(name='diabe'))
sm.add_widget(HeartScreen(name='hear'))
sm.add_widget(LowsodScreen(name='lowsod'))
sm.add_widget(HIScreen(name='HI'))
sm.add_widget(LOScreen(name='LO'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(BFScreen(name='bf'))
sm.add_widget(BFDetScreen(name='bf_detail'))
sm.add_widget(LuScreen(name='lu'))
sm.add_widget(DinnerScreen(name='din'))
sm.add_widget(IngredientScreen(name='ingredient'))
sm.add_widget(CalScreen(name='cal'))
sm.add_widget(DisCalScreen(name='discal'))
sm.add_widget(HelloScreen(name='hello'))
sm.add_widget(AnalysisScreen(name='analy'))
sm.add_widget(ResultScreen(name='result'))
sm.add_widget(AddFoodScreen(name='addfood'))
sm.add_widget(BFAnalysisScreen(name='bfanalysis'))
sm.add_widget(LuAnalysisScreen(name='luanalysis'))
sm.add_widget(DiAnalysisScreen(name='dianalysis'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()