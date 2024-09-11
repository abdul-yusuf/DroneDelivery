import importlib

from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import MDWidget
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogContentContainer, MDDialogSupportingText, \
    MDDialogButtonContainer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp
import View.TrackOrderScreen.track_order_screen
# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.TrackOrderScreen.track_order_screen)


class TrackOrderScreenController:
    """
    The `TrackOrderScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """


    txt_box1 = None
    txt_box2 = None
    txt_box3 = None
    txt_box4 = None

    def create_text_box(self):
        txt_box = MDTextField(
            mode='outlined',
            input_type='number',
            on_text=self.evaluate_txt_box
        )
        return txt_box

    def evaluate_txt_box(self, *args, **kwargs):
        txt1 = self.txt_box1.text
        txt2 = self.txt_box2.text
        txt3 = self.txt_box3.text
        txt4 = self.txt_box4.text

        if txt1 != '' and txt2 != '' and txt3 != '' and txt4 != '':
            print(txt1, txt2, txt3, txt4)

    def __init__(self, model):
        self.model = model  # Model.track_order_screen.TrackOrderScreenModel
        self.view = View.TrackOrderScreen.track_order_screen.TrackOrderScreenView(controller=self, model=self.model)

    def get_view(self) -> View.TrackOrderScreen.track_order_screen:
        return self.view

    def do_set_dialog(self):
        self.txt_box1 = self.create_text_box()
        self.txt_box2 = self.create_text_box()
        self.txt_box3 = self.create_text_box()
        self.txt_box4 = self.create_text_box()

        MDDialog(
            MDDialogHeadlineText(
                text="OTP Authentication",
                halign="left",
            ),
            MDDialogSupportingText(
                text="we have sent you an otp to your email kindly input the pin for your package to be droped.",
                halign="left",
            ),
            MDDialogButtonContainer(
                # MDWidget(),
                MDBoxLayout(
                    self.txt_box1,
                    self.txt_box2,
                    self.txt_box3,
                    self.txt_box4,
                    orientation='horizontal',
                    adaptive_height=True,
                    spacing=dp(10)
                ),
                MDButton(
                    MDButtonText(
                        text='Authenticate',
                        pos_hint={'center_x': .5, 'center_y': .5}
                    ),
                    # pos_hint={'center_x': .5, 'top': .5},
                    theme_width='Custom',
                    size_hint_x=.6,
                    radius=dp(4),
                    on_press=self.evaluate_txt_box,
                ),
                orientation='vertical',
                spacing=dp(10)
            ),
            size_hint=(.9, None),
        ).open()

