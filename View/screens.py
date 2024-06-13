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
    'welcome screen': {
        'model': WelcomeScreenModel,
        'controller': WelcomeScreenController,
        'kv': 'View/WelcomeScreen/welcome_screen.kv'
    },
    # 'order history screen': {
    #     'model': OrderHistoryScreenModel,
    #     'controller': OrderHistoryScreenController,
    # },
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
        'kv': 'View/MainScreen/main_screen.kv'
    },
    'on boarding screen': {
        'model': OnBoardingScreenModel,
        'controller': OnBoardingScreenController,
        'kv': 'View/OnBoardingScreen/on_boarding_screen.kv'
    },
    'otp verification screen': {
        'model': OtpVerificationScreenModel,
        'controller': OtpVerificationScreenController,
        'kv': 'View/OtpVerificationScreen/otp_verification_screen.kv'
    },
    'mobile verification screen': {
        'model': MobileVerificationScreenModel,
        'controller': MobileVerificationScreenController,
        'kv': 'View/MobileVerificationScreen/mobile_verification_screen.kv'
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
        'kv': 'View/LoginScreen/login_screen.kv'
    },
    'signup screen': {
        'model': SignupScreenModel,
        'controller': SignupScreenController,
        'kv': 'View/SignupScreen/signup_screen.kv'
    },
}