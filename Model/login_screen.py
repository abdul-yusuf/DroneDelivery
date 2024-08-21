from Model.base_model import BaseScreenModel, snackbar_notification


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
    """
    def __init__(self, *args, **kwargs):
        super(LoginScreenModel, self).__init__(*args)
        self.email = None
        self.password = None
        self.is_new_user = False
        self._called_func = []
        self.populated_api = self.api

    def do_login(self):
        self._called_func.insert(0, 'do_login')
        if self.email not in ('', ' ') and self.password not in ('', ' '):
            self.dialog.open()
            self.api.post_request('https://yusufabdul.pythonanywhere.com/accounts/token/', self, payload={
                "email": self.email,
                "password": self.password
            })
        else:
            snackbar_notification("Enter Email and Password")
            self.dialog.dismiss()

    def do_check_user(self):
        self._called_func.insert(0, 'do_check_user')
        # self.dialog.open()
        self.populated_api.post_request('https://yusufabdul.pythonanywhere.com/accounts/user/', self, method='GET')
        self.dialog.dismiss()

    def on_success(self, *args, **kwargs):
        if self._called_func:
            if self._called_func[0] == 'do_login':
                snackbar_notification("Login Successful")
                self.token = args[1]['token']
                self.notify_observers('login screen')

            elif self._called_func[0] == 'do_check_user':
                print('Success', args, kwargs)
                snackbar_notification("Login Successful")
                self.notify_observers('login screen')
                self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('Error', args, kwargs)
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure', args, kwargs)
        if isinstance(args[1].values(), list):
            msg = args[1]
        else:
            if self._called_func:
                if self._called_func[0] == 'do_check_user':
                    msg = args[1][list(args[1])[0]]
                    if msg == "User inactive or deleted.":
                        self.is_new_user = True
                        self.notify_observers_methods('login screen', 'do_send_otp')
                else:
                    msg = args[1][list(args[1])[0]][0]
                    snackbar_notification(f"{msg}")
            else:
                msg = args[1][list(args[1])[0]][0]
                snackbar_notification(f"{msg}")
        self.dialog.dismiss()

    def do_populate_api_method(self):
        self.notify_observers_methods('login screen', 'do_populate_api_method')