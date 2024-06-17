import asynckivy
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.chip.chip import LabelTextContainer

from View.MainScreen.main_screen import MainScreenView


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_view(self) -> MainScreenView:
        return self.view

    def do_search(self, keyword):
        items = []
        for item in self.model.items_data:
            if keyword in item['name']:
                items.append(item)

        if items:
            self.view.ids.rv.data = items
        else:
            self.view.ids.rv.data = self.model.items_data

    def do_populate_chip_box(self):
        self.view.ids.chip_box.clear_widgets()
        if self.model.categories_data:
            for item in self.model.categories_data:
                asynckivy.start(self.create_chips(item['name']))

    async def create_chips(self, name):
        '''Asynchronously creates and adds chips to the container.'''

        await asynckivy.sleep(-1)
        chip = MDChip(
            MDChipText(
                text=name,
            ),
            type="filter",
            md_bg_color="#303A29",

        )
        chip.bind(active=self.uncheck_chip)
        self.view.ids.chip_box.add_widget(chip)

    def uncheck_chip(self, current_chip: MDChip, active: bool) -> None:
        '''Removes a mark from an already marked chip.'''

        if active:
            for chip in self.view.ids.chip_box.children:
                if current_chip is not chip:
                    if chip.active:
                        chip.active = False

            for child in current_chip.children:
                if isinstance(child, LabelTextContainer):
                    for child in child.children:
                        if isinstance(child, MDChipText):
                            text = child.text

            items = []
            for item in self.model.items_data:
                if text in item['category']:
                    items.append(item)

            if items:
                self.view.ids.rv.data = items
            else:
                self.view.ids.rv.data = self.model.items_data