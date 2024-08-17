import importlib

import View.OtpVerificationScreen.otp_verification_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.OtpVerificationScreen.otp_verification_screen)
from kivy.clock import Clock


class OtpVerificationScreenController:
    """
    The `OtpVerificationScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.otp_verification_screen.OtpVerificationScreenModel
        self.view = View.OtpVerificationScreen.otp_verification_screen.OtpVerificationScreenView(controller=self, model=self.model)

    def get_view(self) -> View.OtpVerificationScreen.otp_verification_screen:
        return self.view

    def do_verify(self, *args, **kwargs):
        inst = self.view.ids
        if inst.txt1.text in ('', ' ') or inst.txt2.text in ('', ' ') or inst.txt3.text in ('', ' ') or inst.txt4.text in ('', ' '):
            inst.verify_btn.disabled = True
        else:
            inst.verify_btn.disabled = False
            self.model.otp = inst.txt1.text + inst.txt2.text + inst.txt3.text + inst.txt4.text
            self.model.do_verify_otp()
