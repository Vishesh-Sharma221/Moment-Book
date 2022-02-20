screen_helper = """
ScreenManager:
    LoginScreen
    MenuScreen

<LoginScreen>:
    name: 'login'
    MDLabel:
        text: "Moment Book"
        halign: "center"
        font_style: "H4"
        font_name: "GUI/assets/SecularOne-Regular.ttf"
        pos_hint: {'center_x':0.5, 'center_y':0.9}

    MDTextField:
        hint_text: "Enter your username" 
        helper_text: "Your MySQL username"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width: 300
        multiline: False
        font_name: "GUI/assets/SecularOne-Regular.ttf"
    MDTextField:
        hint_text: "Enter your password" 
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint_x: None
        size_hint_y: None
        width: 300
        height: 400
        font_name: "GUI/assets/SecularOne-Regular.ttf"
    MDRectangleFlatButton:
        text:"Log in"
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'
        

<MenuScreen>
    name: 'menu'
    MDLabel:
        text: "Main Menu"
        halign: "center"
        font_style: "H3"
        pos_hint: {'center_x':0.5, 'center_y':0.9}

"""
