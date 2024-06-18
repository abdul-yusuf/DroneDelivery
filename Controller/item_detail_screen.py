import importlib

import View.ItemDetailScreen.item_detail_screen
from kivy.animation import Animation
from kivy.clock import Clock
# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.ItemDetailScreen.item_detail_screen)




class ItemDetailScreenController:
    """
    The `ItemDetailScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """
    def __init__(self, model):
        self.model = model  # Model.item_detail_screen.ItemDetailScreenModel
        self.view = View.ItemDetailScreen.item_detail_screen.ItemDetailScreenView(controller=self, model=self.model)

    def get_view(self) -> View.ItemDetailScreen.item_detail_screen:
        return self.view

    def do_add_item_to_cart(self):
        try:
            self.model.main_screen_controller.do_add_item_to_cart(self.model.data['pk'])
            self.do_check_if_item_in_cart()
            Clock.schedule_once(self.update_qty, 0)
        except Exception as e:
            print(e)

    def do_remove_item_from_cart(self):
        try:
            self.model.main_screen_controller.do_remove_item_from_cart(self.model.data['pk'])
            Clock.schedule_once(self.do_check_if_item_in_cart, 1)
            Clock.schedule_once(self.update_qty, 1)
        except Exception as e:
            print(e)

    def update_qty(self, *args, **kwargs):
        for item in self.model.cart_items:
            # if item['qty'] <= 1:
            #     self.view.ids.minus_btn.disabled = True
            # else:
            #     self.view.ids.minus_btn.disabled = False
            if self.model.data['pk'] == item['pk']:
                self.view.qty = item['qty']
                break

    def do_check_if_item_in_cart(self, *args, **kwargs):
        in_cart = False
        for item in self.model.cart_items:
            if self.model.data['pk'] == item['pk']:
                Animation(
                    pos_hint={'center_x': .5, 'top': -.57},
                    d=0.6/1
                ).start(self.view.ids.add_to_cart_btn)
                in_cart = True
                break
        if not in_cart:
            Animation(
                pos_hint={'center_x': .5, 'top': .07},
                d=0.6 / 1
            ).start(self.view.ids.add_to_cart_btn)