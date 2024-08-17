from View.base_screen import BaseScreenView
from kivy.clock import Clock

class SignupScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    # def do_login_on_signup(self):
        self.app.add_screen('login screen')
        Clock.schedule_once(lambda _:self.model.pass_attribute('login screen', self.model.email, 'email'), 1)
        Clock.schedule_once(lambda _:self.model.notify_observers_methods('login screen', 'do_login_on_signup'), 1)
