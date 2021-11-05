from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, StringProperty
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

            BoxLayout:
                id: login_layout
                padding: [20,60,20,60]
                spacing: 5
                orientation: 'vertical'


                BoxLayout:
                    orientation: 'horizontal'
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
            RV:
            
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
            Low:                   

<IngredientScreen>:
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
            rows:6
            cols:2
            spacing: 20
            padding: 50
            #row_default_height:40
            Label:
                text: 'Insert Your Ingredient'
                color: (0,0,0,1)
                size_hint_x:None
                size_hint_y:None
                width:30
                height: 30

            TextInput:
                id: ingredient
                height: 30
                multiline: False
                size_hint_x:None
                size_hint_y:None
                width:400
                height: 30
            

            Button:
                text: 'Submit'
                background_color: 1.000, 1.000, 0.330, 0.500
                size: 100, 60
                size_hint: None, None
                #pos_hint: {'center_x':0.8,'center_y':0.6}
                on_press: root.manager.current = root.but_search()

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
            RVV:

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
            size_hint_x: .8
            rows:17
            cols:2
            spacing: 20
            padding: 50
            #row_default_height:40
            
            BoxLayout:
                orientation: 'vertical'
                #size:200,200
                #size_hint: None, None
                Label:
                    text: "hello"
                    color: (0,0,0,1)
            Button:
                text: "lol"
                
            



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

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="healthypro"
)
cursor = db.cursor()

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

class LuScreen(Screen):
    pass

class RecommendationScreen(Screen):
    pass

class HIScreen(Screen):
    pass

class LOScreen(Screen):
    pass

class AnalysisScreen(Screen):
    pass

class IngredientScreen(Screen):
    def but_search(self):
        ingredient = self.ids.ingredient.text

        if ingredient == "":
            print("no no no boii")
        else:
            query_start = "SELECT bf_name FROM breakfast WHERE bf_ing LIKE '%"
            query_end = "%'"
            query = query_start + ingredient + query_end
            cursor.execute(query)
            logincheck = cursor.fetchall()
            print(logincheck)
            db.commit()
            db.close()


class MyLabel(Label):
    value = NumericProperty(0)
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
        #calorie = self.ids.calorie
        cursor = db.cursor()
        #str(int(self.a.text) * int(self.b.text))


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
            values = (ag, gen, weig, heig, calorie,  userLogId)
            ## executing the query with values
            cursor.execute(query, values)

            ## to make final output we have to run
            ## the 'commit()' method of the database object
            db.commit()
            db.close()

            info.text = '[color=#008000]you have entered your body information[/color]'
            print(cursor.rowcount, "records inserted")
            #print(calorie)

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
            #db.commit()
            #db.close()



            #print(userLogId)
            #display = cursor.fetchall()
            trydis = display[0][1]
            trydis2 = display[0][2]
            trydis3 = display[0][3]

            print(trydis)
            fname.text = trydis
            serve.text = trydis2
            calorie.value = trydis3
            db.commit()
            #db.close()



# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(RecommendationScreen(name='recom'))
sm.add_widget(HIScreen(name='HI'))
sm.add_widget(LOScreen(name='LO'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(BFScreen(name='bf'))
sm.add_widget(LuScreen(name='lu'))
sm.add_widget(IngredientScreen(name='ingredient'))
sm.add_widget(CalScreen(name='cal'))
sm.add_widget(DisCalScreen(name='discal'))
sm.add_widget(HelloScreen(name='hello'))
sm.add_widget(AnalysisScreen(name='analy'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()