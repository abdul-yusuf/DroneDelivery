from View.base_screen import BaseScreenView
from kivy.clock import Clock

class MobileVerificationScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.model.do_send_otp()

    def go_to_verification_screen(self):
        if self.model.is_first:
            self.model.is_first = False
            print(self.model.email)
            self.app.add_screen('otp verification screen', switch=False)
            # self.model.notify_observers('otp verification screen')
            Clock.schedule_once(lambda _:self.model.pass_attribute('otp verification screen', self.model.email, attr='email'), 1)
            Clock.schedule_once(lambda _:self.app.add_screen('otp verification screen'), 1)

    def on_pre_enter(self, *args):
            self.model.is_first = True
