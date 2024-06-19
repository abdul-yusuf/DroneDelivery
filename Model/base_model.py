# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.


class BaseScreenModel:
    """Implements a base class for model modules."""

    _observers = []

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
