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

manager = ScreenManager()
manager.add_widget(LoginScreen(name='login'))
manager.add_widget(MenuScreen(name='menu'))

class Welcome(MDApp):
    def build(self):
        Window.size = (630,630)
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(screen_helper)

        return screen 

if __name__ == '__main__':
    Welcome().run()