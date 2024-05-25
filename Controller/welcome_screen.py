import importlib

import View.WelcomeScreen.welcome_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.WelcomeScreen.welcome_screen)




class WelcomeScreenController:
    """
    The `WelcomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.welcome_screen.WelcomeScreenModel
        self.view = View.WelcomeScreen.welcome_screen.WelcomeScreenView(controller=self, model=self.model)

    def get_view(self) -> View.WelcomeScreen.welcome_screen:
        return self.view
