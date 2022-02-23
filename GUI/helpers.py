screen_helper = """
WindowManager:
    LoginScreen
    MenuScreen

<LoginScreen>:
    name: 'login'
    Image:
        source: "GUI/assets/logo_transparent.png"
        pos_hint: {"center_x": .2,"center_y": .9}

    MDLabel:
        text: "Moment Book"
        halign: "center"
        font_style: "H4"
        font_name: "GUI/assets/Biscuit & Chocolat.ttf"
        pos_hint: {'center_x':0.5, 'center_y':0.9}

    MDTextField:
        id: usr
        hint_text: "Enter your username" 
        helper_text: "Your MySQL username"
        helper_text_mode: "on_focus"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width: 300
        multiline: False
        font_name: "GUI/assets/SecularOne-Regular.ttf"

    MDTextField:
        id: pwd
        hint_text: "Enter your password" 
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint_x: None
        size_hint_y: None
        width: 300
        height: 400
        icon_right: "eye-off"
        password: True
        font_name: "GUI/assets/SecularOne-Regular.ttf"
    MDRectangleFlatButton:
        id: btn
        text:"[color=#00ffcc]Log in[/color]"
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: app.connect_to_database()
        

<MenuScreen>
    name: 'menu'
    MDLabel:
        id: title
        text: "What's up?"
        halign: "center"
        font_style: "H6"
        pos_hint: {'center_x':0.7, 'center_y':0.9}
        font_name: "GUI/assets/SecularOne-Regular.ttf"

    # Image:
    #     source: "GUI/assets/logo_transparent.png"
    #     pos_hint: {"center_x": .1,"center_y": .9}

    MDFloatingActionButton:
        icon: "account"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.9, 'center_y':0.9}

    MDFloatingActionButton:
        icon: "book-multiple"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1, 'center_y':0.7}
    MDLabel:
        text: "My Memories"
        font_style: "H4"
        pos_hint: {'center_x':0.7, 'center_y':0.7}     
        font_name: "GUI/assets/SecularOne-Regular.ttf"

    MDFloatingActionButton:
        icon: "book-edit"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1, 'center_y':0.5}

    MDLabel:
        text: "Create!"
        font_style: "H4"
        pos_hint: {'center_x':0.7, 'center_y':0.5}  
        font_name: "GUI/assets/SecularOne-Regular.ttf"

    MDFloatingActionButton:
        icon: "file-document-edit"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1, 'center_y':0.3}

    MDLabel:
        text: "Edit"
        font_style: "H4"
        pos_hint: {'center_x':0.7, 'center_y':0.3}  
        font_name: "GUI/assets/SecularOne-Regular.ttf"

    MDFloatingActionButton:
        icon: "delete-forever"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1, 'center_y':0.1}

    MDLabel:
        text: "Delete"
        font_style: "H4"
        pos_hint: {'center_x':0.7, 'center_y':0.1}  
        font_name: "GUI/assets/SecularOne-Regular.ttf"

    MDRectangleFlatButton:
        text: "Go Back!"
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'login'

"""
