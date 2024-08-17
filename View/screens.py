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
from Model.vendor_list_screen import VendorListScreenModel
from Controller.vendor_list_screen import VendorListScreenController
from Model.vendor_detail_screen import VendorDetailScreenModel
from Controller.vendor_detail_screen import VendorDetailScreenController
from Model.item_detail_screen import ItemDetailScreenModel
from Controller.item_detail_screen import ItemDetailScreenController
from Model.checkout_screen import CheckoutScreenModel
from Controller.checkout_screen import CheckoutScreenController
from Model.edit_profile_screen import EditProfileScreenModel
from Controller.edit_profile_screen import EditProfileScreenController
from Model.faq_screen import FaqScreenModel
from Controller.faq_screen import FaqScreenController
from Model.aboutus_screen import AboutusScreenModel
from Controller.aboutus_screen import AboutusScreenController
from Model.contactus_screen import ContactusScreenModel
from Controller.contactus_screen import ContactusScreenController
from Model.feedback_screen import FeedbackScreenModel
from Controller.feedback_screen import FeedbackScreenController
from Model.track_order_screen import TrackOrderScreenModel
from Controller.track_order_screen import TrackOrderScreenController

screens = {
    'track order screen': {
        'model': TrackOrderScreenModel,
        'controller': TrackOrderScreenController,
        'kv': 'View/TrackOrderScreen/track_order_screen.kv'
    },
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
        'kv': 'View/MainScreen/main_screen.kv'
    },
    'signup screen': {
        'model': SignupScreenModel,
        'controller': SignupScreenController,
        'kv': 'View/SignupScreen/signup_screen.kv'
    },
    'on boarding screen': {
        'model': OnBoardingScreenModel,
        'controller': OnBoardingScreenController,
        'kv': 'View/OnBoardingScreen/on_boarding_screen.kv'
    },
    'welcome screen': {
        'model': WelcomeScreenModel,
        'controller': WelcomeScreenController,
        'kv': 'View/WelcomeScreen/welcome_screen.kv'
    },
    'vendor detail screen': {
        'model': VendorDetailScreenModel,
        'controller': VendorDetailScreenController,
        'kv': 'View/VendorDetailScreen/vendor_detail_screen.kv'
    },
    'vendor list screen': {
        'model': VendorListScreenModel,
        'controller': VendorListScreenController,
        'kv': 'View/VendorListScreen/vendor_list_screen.kv'
    },
    'item detail screen': {
        'model': ItemDetailScreenModel,
        'controller': ItemDetailScreenController,
        'kv': 'View/ItemDetailScreen/item_detail_screen.kv'
    },
    'order history screen': {
        'model': OrderHistoryScreenModel,
        'controller': OrderHistoryScreenController,
        'kv': 'View/OrderHistoryScreen/order_history_screen.kv'
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
    'edit profile screen': {
        'model': EditProfileScreenModel,
        'controller': EditProfileScreenController,
        'kv': 'View/EditProfileScreen/edit_profile_screen.kv'
    },
    # 'aboutus screen': {
    #     'model': AboutusScreenModel,
    #     'controller': AboutusScreenController,
    # },
    # 'checkout screen': {
    #     'model': CheckoutScreenModel,
    #     'controller': CheckoutScreenController,
    # },
    # 'contactus screen': {
    #     'model': ContactusScreenModel,
    #     'controller': ContactusScreenController,
    # },
    # 'faq screen': {
    #     'model': FaqScreenModel,
    #     'controller': FaqScreenController,
    # },
    # 'feedback screen': {
    #     'model': FeedbackScreenModel,
    #     'controller': FeedbackScreenController,
    # },
}