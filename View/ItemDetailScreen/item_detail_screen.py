from View.base_screen import BaseScreenView
from kivy.properties import NumericProperty

class ItemDetailScreenView(BaseScreenView):
    qty = NumericProperty(defaultvalue=1)
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        self.controller.model.item_detail = self.controller.model.data
