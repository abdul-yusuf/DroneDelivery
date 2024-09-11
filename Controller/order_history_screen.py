import importlib

import View.OrderHistoryScreen.order_history_screen
from kivy.clock import Clock
# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.OrderHistoryScreen.order_history_screen)




class OrderHistoryScreenController:
    """
    The `OrderHistoryScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.order_history_screen.OrderHistoryScreenModel
        self.view = View.OrderHistoryScreen.order_history_screen.OrderHistoryScreenView(controller=self, model=self.model)

    def get_view(self) -> View.OrderHistoryScreen.order_history_screen:
        return self.view


    def do_open_track_progress(self, pk):
        self.view.app.add_screen('track order screen')
        Clock.schedule_once(lambda _=pk:self.model.pass_attribute('track order screen', _), 1)
        Clock.schedule_once(lambda _:self.model.notify_observers('track order screen'), 1)