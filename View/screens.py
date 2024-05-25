# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.
from Controller.signup_screen import SignupScreenController
from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.signup_screen import SignupScreenModel
from Model.on_boarding_screen import OnBoardingScreenModel
from Controller.on_boarding_screen import OnBoardingScreenController
from Model.welcome_screen import WelcomeScreenModel
from Controller.welcome_screen import WelcomeScreenController
from Model.mobile_verification_screen import MobileVerificationScreenModel
from Controller.mobile_verification_screen import MobileVerificationScreenController
from Model.otp_verification_screen import  OtpVerificationScreenModel
from Controller.otp_verification_screen import OtpVerificationScreenController
from Model.order_history_screen import OrderHistoryScreenModel
from Controller.order_history_screen import OrderHistoryScreenController

screens = {
    # 'order history screen': {
    #     'model': OrderHistoryScreenModel,
    #     'controller': OrderHistoryScreenController,
    # },
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
    'on boarding screen': {
        'model': OnBoardingScreenModel,
        'controller': OnBoardingScreenController,
    },
    'otp verification screen': {
        'model': OtpVerificationScreenModel,
        'controller': OtpVerificationScreenController,
    },
    'welcome screen': {
        'model': WelcomeScreenModel,
        'controller': WelcomeScreenController,
    },
    'mobile verification screen': {
        'model': MobileVerificationScreenModel,
        'controller': MobileVerificationScreenController,
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
    },
    'signup screen': {
        'model': SignupScreenModel,
        'controller': SignupScreenController,
    },
    'welcome screen': {
        'model': WelcomeScreenModel,
        'controller': WelcomeScreenController,
    },
}