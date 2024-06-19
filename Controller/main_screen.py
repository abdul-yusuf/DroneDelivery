import asynckivy
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.chip.chip import LabelTextContainer
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp

from View.MainScreen.main_screen import MainScreenView
from kivy.clock import Clock

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

        asynckivy.start(self.add_screen_reference_to_data())

    def get_view(self) -> MainScreenView:
        return self.view

    async def add_screen_reference_to_data(self):
        await asynckivy.sleep(0)
        for item in self.model.data:
            item['on_press'] = lambda _=item: self.do_open_item_detail(_)
            item['root_x'] = self
            self.model.items_data.append(item)

        self.view.ids.rv.data = self.model.items_data

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

    def do_open_item_detail(self, item=None):
        self.view.app.add_screen('item detail screen', switch=False)
        self.model.pass_attribute('item detail screen', self.view.ids.rv2.data, attr='cart_items')
        self.model.pass_attribute('item detail screen', self, attr='main_screen_controller')
        self.view.app.dialog.open()
        Clock.schedule_once(lambda _:self.model.pass_attribute('item detail screen', item), 1)
        Clock.schedule_once(lambda _:self.model.notify_observers('item detail screen'), 1)
        Clock.schedule_once(lambda _:self.view.app.add_screen('item detail screen'),1)
        Clock.schedule_once(lambda _:self.view.app.dialog.dismiss(), 1)

    def do_add_item_to_cart(self, pk):
        self.model.pass_attribute('main screen', pk)
        self.model.notify_observers('main screen')

    def do_remove_item_from_cart(self, pk):
        self.model.pass_attribute('main screen', pk)
        self.model.pass_attribute('main screen', True, attr='is_remove_item')
        self.model.notify_observers('main screen')

    def add_item_to_cart(self):
        if isinstance(self.model.data, str):
            item_data = None
            for item in self.model.items_data:
                if item['pk'] == self.model.data:
                    item_data = item
                    break
            try:
                is_added = False
                # print(dir(self.view.ids.rv2.data))
                for item in self.view.ids.rv2.data:
                    if self.model.data == item['pk']:
                        index = self.view.ids.rv2.data.index(item)
                        item['qty'] += 1
                        self.view.ids.rv2.data[index] = item
                        print('Item Added')
                        is_added = True
                        MDSnackbar(
                            MDSnackbarText(
                                text="Item updated.",
                            ),
                            y=dp(24),
                            pos_hint={"center_x": 0.5, "top": .9},
                            size_hint_x=0.8,
                        ).open()
                        break
                if not is_added:
                    item = item_data
                    item['root_x'] = self
                    item['qty'] = 1
                    self.view.ids.rv2.data.append(item)
                    MDSnackbar(
                        MDSnackbarText(
                            text="Item added to cart.",
                        ),
                        y=dp(24),
                        pos_hint={"center_x": 0.5, "top": .9},
                        size_hint_x=0.8,
                    ).open()
                    print('Item Added2')
            except Exception as e:
                print(e)
                # item = item_data
                # item['qty'] = 1
            self.view.ids.cart_info.text = f"Item Qty: {len(self.view.ids.rv2.data)}\n\n[b]TOTAL: ₦ {sum(float(x['price'].split(',')[0] + x['price'].split(',')[1]) if x['qty'] == 1 else float(x['price'].split(',')[0] + x['price'].split(',')[1]) * int(x['qty']) for x in self.view.ids.rv2.data)}[/b]"
        else:
            print(self.model.data.__str__, 'not instance')

    def remove_item_from_cart(self):
        if isinstance(self.model.data, str):
            item_data = None
            for item in self.model.items_data:
                if item['pk'] == self.model.data:
                    item_data = item
                    break
            try:
                for item in self.view.ids.rv2.data:
                    if self.model.data == item['pk']:
                        if item['qty'] <= 1:
                            self.view.ids.rv2.data.remove(item)
                            MDSnackbar(
                                MDSnackbarText(
                                    text="Item removed from cart.",
                                ),
                                y=dp(24),
                                pos_hint={"center_x": 0.5, "top": .9},
                                size_hint_x=0.8,
                            ).open()
                        else:
                            index = self.view.ids.rv2.data.index(item)
                            item['qty'] -= 1
                            self.view.ids.rv2.data[index] = item
                            MDSnackbar(
                                MDSnackbarText(
                                    text="Item updated.",
                                ),
                                y=dp(24),
                                pos_hint={"center_x": 0.5, "top": .9},
                                size_hint_x=0.8,
                            ).open()
                        break
            except Exception as e:
                print(e)
            self.view.ids.cart_info.text = f"Item Qty: {len(self.view.ids.rv2.data)}\n\n[b]TOTAL: ₦ {sum(float(x['price'].split(',')[0] + x['price'].split(',')[1]) if x['qty'] == 1 else float(x['price'].split(',')[0] + x['price'].split(',')[1]) * int(x['qty']) for x in self.view.ids.rv2.data)}[/b]"
