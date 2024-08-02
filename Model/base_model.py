# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp

def snackbar_notification(msg):

    MDSnackbar(
        MDSnackbarText(
            text=f"{msg}",
        ),
        y=dp(24),
        adaptive_size=True,
        pos_hint={"center_x": 0.5, "top": .15},
        size_hint_x=0.8,
    ).open()


class BaseScreenModel:
    """Implements a base class for model modules."""

    _observers = []
    api = None
    token = None

    def __init__(self, api):
        from kivy.clock import Clock
        from kivy.factory import Factory
        from kivy.uix.modalview import ModalView
        from kivy.metrics import dp

        self.api = api
        spinner = Factory.MDCircularProgressIndicator(line_width=dp(1.5))
        self.dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            on_pre_open=lambda _: setattr(spinner, "active", True),
            on_dismiss=lambda _: setattr(spinner, "active", False)
        )
        Clock.schedule_once(lambda _: self.dialog.add_widget(spinner), 0)

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str) -> None:
        """
        Method that will be called by the observer when the model data changes.

        :param name_screen:
            name of the view for which the method should be called
            :meth:`model_is_changed`.
        """

        for observer in self._observers:
            if observer.name == name_screen:
                observer.model_is_changed()
                break

    def notify_observers_methods(self, name_screen: str, method) -> None:

        for observer in self._observers:
            if observer.name == name_screen:
                try:
                    exec(f"observer.{method}()")
                except Exception as e:
                    print(e)
                break

    def pass_attribute(self, name_screen: str, data, attr=None):
        """
        args:
            name_screen: str
            data: (list, dict)
        """
        for observer in self._observers:
            if observer.name == name_screen:
                if attr:
                    try:
                        exec(f'observer.model.{attr} = data')
                    except TypeError as e:
                        print(e)
                        eval(f'observer.model.{attr} = data')
                else:
                    observer.model.data = data
                break

    def append_attribute(self, name_screen: str, data):
        """
        args:
            name_screen: str
            data: (str, list, dict)
        """
        for observer in self._observers:
            if observer.name == name_screen:
                observer.model.data = data.append(data)
                break
