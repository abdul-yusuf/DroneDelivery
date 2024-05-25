import importlib

import View.TripSearchScreen.trip_search_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.TripSearchScreen.trip_search_screen)




class TripSearchScreenController:
    """
    The `TripSearchScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.trip_search_screen.TripSearchScreenModel
        self.view = View.TripSearchScreen.trip_search_screen.TripSearchScreenView(controller=self, model=self.model)

    def get_view(self) -> View.TripSearchScreen.trip_search_screen:
        return self.view
