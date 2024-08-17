from View.base_screen import BaseScreenView
from kivy.clock import Clock

class OtpVerificationScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        self.model.notify_observers_methods('login screen', 'do_populate_api_method')
        Clock.schedule_once(lambda _:self.app.add_screen('on boarding screen'), 1)
