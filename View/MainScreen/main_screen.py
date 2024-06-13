from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from View.base_screen import BaseScreenView
from kivy.clock import Clock


class MainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """


class BottomNav(MDBoxLayout):
    selected = ObjectProperty()
    screen_manager = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(BottomNav, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.init_selected, 1)

    def init_selected(self, *args, **kwargs):
        try:
            self.selected = self.ids.btn1
            self.selected.style = 'tonal'
        except AttributeError as e:
            print(e)

    def switch(self, btn, screen_name):
        # if btn.style == 'text':
        if self.selected:
            self.selected.style = 'text'
            self.selected = btn
        else:
            self.selected = btn
        btn.style = 'tonal'
        # else:
        #     btn.style = 'text'
        self.screen_manager.current = screen_name