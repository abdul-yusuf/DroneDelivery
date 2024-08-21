from Model.base_model import BaseScreenModel, snackbar_notification


class SignupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.signup_screen.SignupScreen.SignupScreenView` class.
    """

    email = None
    first_name = None
    last_name = None
    password = None

    def do_signup(self):
        self.dialog.open()
        self.api.post_request('https://yusufabdul.pythonanywhere.com/accounts/signup/', self, payload={
                                                                                          "email": self.email,
                                                                                          "first_name": self.first_name,
                                                                                          "last_name": self.last_name,
                                                                                          "password": self.password
                                                                                     })
        self.dialog.dismiss()

    def on_success(self, *args, **kwargs):
        snackbar_notification("Signup Successful")
        self.notify_observers('signup screen')
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        if isinstance(args[1].values(), list):
            msg= args[1]
        else:
            msg= args[1][list(args[1])[0]][0]
        snackbar_notification(f"{msg}")
        self.dialog.dismiss()
