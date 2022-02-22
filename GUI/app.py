import mysql.connector

from helpers import *
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager

from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.write()

class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

manager = ScreenManager()
manager.add_widget(LoginScreen(name='login'))
manager.add_widget(MenuScreen(name='menu'))

class Welcome(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)


    def build(self):
        Window.size = (630,630)
        self.theme_cls.theme_style = "Dark"

        return self.screen 

    def connect_to_database(self):
        username = self.root.get_screen('login').ids.usr.text
        password = self.root.get_screen('login').ids.pwd.text

        try:
            db = mysql.connector.connect(
                host="localhost",
                user=username,
                passwd=password,
                auth_plugin = "mysql_native_password"
            )		
            self.root.get_screen('login').ids.btn.text = "[color=#00ffcc]Log in[/color]"
            self.root.current = 'menu'
            self.root.get_screen('menu').ids.title.text = f"Welcome {username.capitalize()}!"
            return db
        except:
            self.root.get_screen('login').ids.btn.text = "[color=#ff0000]Log in[/color]"
            self.root.get_screen('login').ids.pwd.hint_text = "Incorrect Password!"
            return False


if __name__ == '__main__':
    Welcome().run()