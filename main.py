"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

# import importlib
# import os
#
# from kivy import Config
#
# from PIL import ImageGrab
#
# # TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size
#
# # Change the values of the application window size as you need.
# Config.set("graphics", "height", resolution[1])
# Config.set("graphics", "width", "400")
#
# from kivy.core.window import Window
#
# # Place the application window on the right side of the computer screen.
# # Window.top = 0
# # Window.left = resolution[0] - Window.width
#
# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager
# import View.screens
#
class Navigation:
    def __init__(self, master):
        self.screens = []
        self.master = master
        self.manager = master.manager_screens
        self.count = 0

    def prev(self):
        print(self.screens)
        try:
            if len(self.screens) > 1:
                self.screens.pop()
                self.count = 0
            else:
                self.count += 1
                if self.count == 2:
                    self.master.stop()
            self.manager.current = self.screens[-1]
        except IndexError:
            self.count += 1
            if self.count == 2:
                self.master.stop()

    def add_screen(self, screen_name):
        self.screens.append(screen_name)
        return True

    def back(self):
        print(self.screens)
        try:
            self.screens.pop()
            print(self.screens)
            return self.screens[-1]
        except IndexError:
            return 'welcome screen'

#
# class MKT(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]
#
#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """
#
#         self.manager_screens = MDScreenManager()
#         self.nav = Navigation(self)
#         Window.bind(on_key_down=self.on_keyboard_down)
#         importlib.reload(View.screens)
#         screens = View.screens.screens
#
#         for i, name_screen in enumerate(screens.keys()):
#             model = screens[name_screen]["model"]()
#             controller = screens[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screens = self.manager_screens
#             view.name = name_screen
#             self.manager_screens.add_widget(view)
#             self.nav.add_screen(name_screen)
#         return self.manager_screens
#
#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.
#
#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """
#
#         if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#             self.rebuild()
#
#         print(keyboard, keycode, text, modifiers)
#         # Esc keyboard == 27 keycode == 41
#         if keyboard == 98:
#             self.nav.prev()
#             # self.manager_screens.current = self.nav.back()
#
#     def change_screen(self, name: str):
#         # print(name, View.screens.screens.keys())
#         print(name)
#         if name in View.screens.screens.keys():
#             self.manager_screens.current = name
#             self.nav.add_screen(name)
#
# MKT().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

# """
# The entry point to the application.
#
# The application uses the MVC template. Adhering to the principles of clean
# architecture means ensuring that your application is easy to test, maintain,
# and modernize.
#
# You can read more about this template at the links below:
#
# https://github.com/HeaTTheatR/LoginAppMVC
# https://en.wikipedia.org/wiki/Model–view–controller
# """
#

"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from View.screens import screens
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window

class MKT(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.root = MDScreenManager()
        self.manager_screens = self.root
        self.nav = Navigation(self)
        spinner = Factory.MDCircularProgressIndicator(line_width=dp(1.5))
        self.dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            on_pre_open=lambda _: setattr(spinner, "active", True),
            on_dismiss=lambda _: setattr(spinner, "active", False)
        )
        self.dialog.add_widget(spinner)
        self.add_screen('welcome screen')
        Window.bind(on_key_down=self.on_keyboard_down)

    def add_screen(self, name_screen, switch=True, first=False):
        print(self.nav.screens)
        if first:
            self.load_screen(name_screen, switch, first)
            return
        if not name_screen in self.nav.screens:
            self.dialog.open()
            Clock.schedule_once(lambda _: self.load_screen(name_screen, switch, first=True), 1)
        elif switch:
            self.change_screen(name_screen)

    def load_screen(self, name_screen, switch, first):
        try:
            # Builder.load_file(screens[name_screen]["kv"])
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)

            view = controller.get_view()
            view.name = name_screen
            self.manager_screens.add_widget(view)
            if switch:
                self.change_screen(name_screen)
            if first:
                self.dialog.dismiss()
        except KeyError as e:
            print(e)

    def change_screen(self, name: str):
        # print(name, View.screens.screens.keys())
        print(name)
        # if name in enumerate(screens.keys()):
        self.manager_screens.current = name
        self.nav.add_screen(name)
        print(self.nav.screens)

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
        """
        The method handles keyboard events.

        By default, a forced restart of an application is tied to the
        `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
        """

        # if "meta" in modifiers or "ctrl" in modifiers and text == "r":
        #     self.rebuild()

        print(keyboard, keycode, text, modifiers)
        # Esc keyboard == 27 keycode == 41
        if keyboard == 98:
            self.nav.prev()
            # self.manager_screens.current = self.nav.back()
MKT().run()
