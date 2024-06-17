import importlib

import View.VendorDetailScreen.vendor_detail_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.VendorDetailScreen.vendor_detail_screen)



class VendorDetailScreenController:
    """
    The `VendorDetailScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.vendor_detail_screen.VendorDetailScreenModel
        self.view = View.VendorDetailScreen.vendor_detail_screen.VendorDetailScreenView(controller=self, model=self.model)

    def get_view(self) -> View.VendorDetailScreen.vendor_detail_screen:
        return self.view
