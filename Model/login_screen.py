from Model.base_model import BaseScreenModel, snackbar_notification


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
    """
    email = None
    password = None

    def do_login(self):
        print(self.email)
        print(self.password)
        if self.email not in ('', ' ') and self.password not in ('', ' '):
            self.dialog.open()
            self.api.post_request('http://127.0.0.1:8000/accounts/token/', self, payload={
                                                                                          "email": self.email,
                                                                                          "password": self.password
                                                                                     })
        else:
            snackbar_notification("Enter Email and Password")
            self.dialog.dismiss()

    def on_success(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        snackbar_notification("Login Successful")
        self.token = args[1]['token']
        self.notify_observers('login screen')
        # self.notify_observers('login screen')
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('ERROR: ', args, kwargs)
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)

        if isinstance(args[1].values(), list):
            msg= args[1]
        else:
            msg= args[1][list(args[1])[0]][0]
        snackbar_notification(f"{msg}")
        self.dialog.dismiss()
