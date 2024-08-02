from View.base_screen import BaseScreenView
from libs.api import API

class LoginScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print(self.model.token)
        headers = {"Authorization": "Token " + str(self.model.token), "Content-Type": "application/json"}
        print(self.app.api._HEADERS)
        self.app.api = API(headers=headers)
        print(self.app.api._HEADERS)
        self.app.add_screen('main screen')

        # self.model.pass_attribute('')