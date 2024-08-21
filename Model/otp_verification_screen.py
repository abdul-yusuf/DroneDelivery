from Model.base_model import BaseScreenModel, snackbar_notification


class OtpVerificationScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.otp_verification_screen.OtpVerificationScreen.OtpVerificationScreenView` class.
    """
    email = None
    otp = None

    def do_verify_otp(self):
        self.dialog.open()
        payload = {
            "email":self.email,
            "pin":self.otp
        }
        print(payload)
        self.api.post_request('https://yusufabdul.pythonanywhere.com/accounts/otp/verify/', self, payload=payload)

    def on_success(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        self.notify_observers('otp verification screen')
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('ERROR: ', args, kwargs)
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)

        if isinstance(args[1].values(), list):
            msg = args[1]
        else:
            msg = args[1][list(args[1])[0]]
        snackbar_notification(f"{msg}")
        self.dialog.dismiss()
