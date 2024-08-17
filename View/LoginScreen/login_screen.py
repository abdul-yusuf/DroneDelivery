from View.base_screen import BaseScreenView
from kivy.clock import Clock
from libs.api import API


class LoginScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if self.model._called_func:
            if self.model._called_func[0] == 'do_login':
                headers = {"Authorization": "Token " + str(self.model.token), "Content-Type": "application/json"}
                # self.app.api = API(headers=headers)
                self.model.populated_api = API(headers=headers)
                self.model.do_check_user()
            elif self.model._called_func[0] == 'do_check_user':
                headers = {"Authorization": "Token " + str(self.model.token), "Content-Type": "application/json"}
                self.app.api = API(headers=headers)
                self.app.add_screen('main screen')

        # self.model.pass_attribute('')

    def do_login_on_signup(self):
        print(self.model.email)
        self.ids.email.text = self.model.email

    def do_send_otp(self):
        self.app.add_screen('mobile verification screen')
        Clock.schedule_once(
            lambda _: self.model.pass_attribute('mobile verification screen', self.model.email, 'email'), 1)
        self.model.notify_observers('mobile verification screen')

    def do_populate_api_method(self):
        headers = {"Authorization": "Token " + str(self.model.token), "Content-Type": "application/json"}
        self.app.api = API(headers=headers)
