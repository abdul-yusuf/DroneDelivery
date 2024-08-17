from Model.base_model import BaseScreenModel, snackbar_notification


class MobileVerificationScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.mobile_verification_screen.MobileVerificationScreen.MobileVerificationScreenView` class.
    """

    email = None
    is_first = True
    _called_func = []

    def do_send_otp(self):
        if self.is_first:
            self._called_func.insert(0, 'do_send_otp')
            self.dialog.open()
            self.api.post_request('http://127.0.0.1:8000/accounts/otp/generate/', self, payload={"email": self.email})
        else:
            self.do_resend_otp()

    def do_resend_otp(self):
        self._called_func.insert(0, 'do_resend_otp')
        self.dialog.open()
        self.api.post_request('http://127.0.0.1:8000/accounts/otp/generate/', self, payload={"email": self.email})

    def on_success(self, *args, **kwargs):
        if self._called_func:
            if self._called_func[0] == 'do_send_otp':
                print('Success: ', args, kwargs)
                # self.notify_observers('mobile verification screen')
                self.notify_observers_methods('mobile verification screen', 'go_to_verification_screen')
                snackbar_notification(f"OTP has been sent to {self.email}.")
                self.dialog.dismiss()

            if self._called_func[0] == 'do_resend_otp':
                print('Success: ', args, kwargs)
                snackbar_notification(f"Check your mail: {self.email} OTP has been sent.")
                self.notify_observers_methods('mobile verification screen', 'go_to_verification_screen')
                self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('ERROR: ', args, kwargs)
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)
        try:
            if isinstance(args[1].values(), list):
                msg = args[1]
            else:
                msg = args[1][list(args[1])[0]]
            snackbar_notification(f"{msg}")
        except Exception as e:
            snackbar_notification(f"{e}")
        self.dialog.dismiss()
