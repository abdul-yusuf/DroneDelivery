import asynckivy
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.chip.chip import LabelTextContainer
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp
from kivy.graphics import Rectangle, Color, Line, Bezier, Ellipse, Triangle
from kivy_garden.mapview import MapView, MapMarkerPopup, MapMarker, MapSource

# from kivy.garden.mapview import MapView, MarkerMap
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogContentContainer, MDDialogSupportingText, \
    MDDialogButtonContainer

import geocoder
from kivy.utils import platform
from kivy.clock import mainthread
from plyer import gps
from View.MainScreen.main_screen import MainScreenView
from kivy.clock import Clock

from kivy.uix.widget import Widget
import re
import requests
from kivy.network.urlrequest import UrlRequest


class fscreen(Widget):
    my_avat = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.parent = None
        self.list_of_lines = []
        self.route_points = []
        self.placed = False
        self.exists = False
        self.ids.main_map.zoom = 15
        if 'lat' in kwargs.keys():
            print(kwargs)
        self.ids.main_map.center_on(self.ids.main_map_me.lat, self.ids.main_map_me.lon)
        self.my_avat = 'assets/images/me.png'

    def press(self):
        print(str(self.ids.main_map_me.lat) + ' | ' + str(self.ids.main_map_me.lon))

    def place_pin(self):
        self.placed = True

    def remove_pin(self):
        if self.exists == True:
            self.ids.main_map.remove_widget(self.dist)
            self.placed = False
            self.exists = False

    def on_touch_up(self, touch):
        if touch.y > self.height * 0.05:
            if self.placed == True and self.exists == False:
                self.dist = MapMarkerPopup(lat=self.ids.main_map.get_latlon_at(touch.x, touch.y)[0],
                                           lon=self.ids.main_map.get_latlon_at(touch.x, touch.y)[1],
                                           source='assets/images/location_icon.png'
                                           )
                self.dist.size = [self.width*0.3, self.height*0.05]
                # self.btn = MDButton(MDButtonText(text='print loc'), on_press=self.press_dist)
                # self.dist.add_widget(self.btn)
                self.ids.main_map.add_widget(self.dist)
                print(self.ids.main_map.parent)
                self.exists = True

    def press_dist(self, instance):
        print(self.dist.lat)
        print(self.dist.lon)

        self.start_lon = self.ids.main_map_me.lon
        self.start_lat = self.ids.main_map_me.lat

        self.end_lon = self.dist.lon
        self.end_lat = self.dist.lat
        self.body = {"coordinates": [[self.start_lon, self.start_lat], [self.end_lon, self.end_lat]]}


    def update_route_lines(self, *args):
        for j in range(1, len(self.route_points), 1):
            self.list_of_lines[j - 1].points = [self.route_points[j - 1].pos[0], self.route_points[j - 1].pos[1],
                                                self.route_points[j].pos[0], self.route_points[j].pos[1]]


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    gps_location = ''
    gps_status = ''
    map = None

    def do_create_map(self):
        # self.map = MapView(
        #             lat=11.15358,
        #             lon=7.651,
        #             zoom=18,
        #             size_hint=(1, 1),
        #             pos_hint={"center_x": .5, "center_y": .5},
        #         )

        self.map = fscreen()
        return self.map

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

        asynckivy.start(self.add_screen_reference_to_data())

    def get_view(self) -> MainScreenView:
        return self.view

    async def add_screen_reference_to_data(self):
        await asynckivy.sleep(0)
        self.model.items_data = []
        for item in self.model.data:
            item['on_press'] = lambda _=item: self.do_open_item_detail(_)
            item['root_x'] = self
            self.model.items_data.append(item)
        print('Async Data: ', self.model.data)
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
        self.view.app.dialog.open()
        self.view.app.add_screen('item detail screen', switch=False)
        Clock.schedule_once(
            lambda _: self.model.pass_attribute('item detail screen', self.view.ids.rv2.data, attr='cart_items'), 0)
        Clock.schedule_once(lambda _: self.model.pass_attribute('item detail screen', item))
        Clock.schedule_once(lambda _: self.model.notify_observers('item detail screen'), 0)
        print('item: ', item)
        Clock.schedule_once(
            lambda _: self.model.pass_attribute('item detail screen', self, attr='main_screen_controller'), 0)
        Clock.schedule_once(lambda _: self.view.app.add_screen('item detail screen'), 2)
        Clock.schedule_once(lambda _: self.view.app.dialog.dismiss(), 2)

    def do_add_item_to_cart(self, pk):
        self.model.pass_attribute('main screen', pk)
        self.model.notify_observers('main screen')

    def do_remove_item_from_cart(self, pk):
        self.model.pass_attribute('main screen', pk)
        self.model.pass_attribute('main screen', True, attr='is_remove_item')
        self.model.notify_observers('main screen')

    def add_item_to_cart(self):
        if isinstance(self.model.data, int):
            item_data = None
            print(self.view.ids.rv.data, self.model.data)
            for item in self.view.ids.rv.data:
                if item['pk'] == self.model.data:
                    item_data = item
                    print(item)
                    break
            try:
                is_added = False
                # print(dir(self.view.ids.rv2.data))
                for item in self.view.ids.rv2.data:
                    if self.model.data == item['pk']:
                        index = self.view.ids.rv2.data.index(item)
                        item['qty'] += 1
                        self.view.ids.rv2.data[index] = item
                        self.model.pass_attribute('item detail screen', self.view.ids.rv2.data, attr='cart_items')
                        print('Item Added')
                        is_added = True
                        MDSnackbar(
                            MDSnackbarText(
                                text="Item updated.",
                            ),
                            y=dp(24),
                            pos_hint={"center_x": 0.5, "top": .25},
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
                        pos_hint={"center_x": 0.5, "top": .25},
                        size_hint_x=0.8,
                    ).open()
                    print('Item Added2')
            except Exception as e:
                print('Add func error: ', e)
                # item = item_data
                # item['qty'] = 1
            self.view.ids.cart_info.text = f"Item Qty: {len(self.view.ids.rv2.data)}\n\n[b]TOTAL: ₦ {sum(float(x['price']) if x['qty'] == 1 else float(x['price']) * int(x['qty']) for x in self.view.ids.rv2.data)}[/b]"
        else:
            print(self.model.data.__str__, 'not instance')

    def remove_item_from_cart(self):
        if isinstance(self.model.data, int):
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
                                pos_hint={"center_x": 0.5, "top": .25},
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
                                pos_hint={"center_x": 0.5, "top": .25},
                                size_hint_x=0.8,
                            ).open()
                        break
            except Exception as e:
                print('Remove func error: ', e)
            self.view.ids.cart_info.text = f"Item Qty: {len(self.view.ids.rv2.data)}\n\n[b]TOTAL: ₦ {sum(float(x['price']) if x['qty'] == 1 else float(x['price']) * int(x['qty']) for x in self.view.ids.rv2.data)}[/b]"
        self.do_check_if_cart_item()

    def do_go_to_checkout(self):
        self.model.pass_attribute('checkout screen', self.view.ids.rv2.data)
        self.view.app.add_screen('checkout screen')

    def do_check_if_cart_item(self):
        if not self.view.ids.rv2.data == []:
            self.view.ids.checkout_btn.disabled = False
            self.view.ids.checkout_btn.style = 'filled'
        else:
            self.view.ids.checkout_btn.style = 'outlined'
            self.view.ids.checkout_btn.disabled = True

    def do_set_dialog(self):
        # btn=
        MDDialog(
            MDDialogHeadlineText(
                text="Change Address:",
                halign="center",
            ),
            # MDDialogSupportingText(
            #     text="we have sent you an otp to your email kindly input the pin for your package to be droped.",
            #     halign="left",
            # ),
            MDDialogContentContainer(
                # MDWidget(),
                MDRelativeLayout(
                    self.do_create_map(),
                    size_hint=(1, None),
                    # height='280dp'
                    height=self.view.app.root.height / 2
                    # adaptive_height=True,
                ),
                MDButton(
                    MDButtonIcon(
                        icon='target',
                        pos_hint={'center_x': .5, 'center_y': .5},
                    ),
                    on_press=self.do_get_location,
                    pos_hint={'center_x': .85, 'center_y': .45},
                ),
                orientation='vertical',
                # adaptive_height=True,
                size_hint=(1, None),
                # size_hint_y=.8,
                spacing="8dp",
                height=self.view.app.root.height / 2,
            ),
            size_hint=(.9, None),
            height=self.view.app.root.height / 2,
        ).open()

    def request_android_permissions(self):
        """
        Since API 23, Android requires permission to be requested at runtime.
        This function requests permission and handles the response via a
        callback.

        The request will produce a popup if permissions have not already been
        been granted, otherwise it will do nothing.
        """
        from android.permissions import request_permissions, Permission

        def callback(permissions, results):
            """
            Defines the callback to be fired when runtime permission
            has been granted or denied. This is not strictly required,
            but added for the sake of completeness.
            """
            if all([res for res in results]):
                print("callback. All permissions granted.")
            else:
                print("callback. Some permissions refused.")

        request_permissions([Permission.ACCESS_COARSE_LOCATION,
                             Permission.ACCESS_FINE_LOCATION], callback)

    def do_get_location(self, *args, **kwargs):
        print('Getting Location.....')
        if platform == "android":
            print("gps.py: Android detected. Requesting permissions")
            self.request_android_permissions()
            try:
                self.gps = gps.configure(on_location=self.on_location,
                                         on_status=self.on_status)
                self.gps.start(1000, 0)
            except NotImplementedError:
                # import traceback
                # traceback.print_exc()
                self.gps_status = 'GPS is not implemented for your platform'
                pass
        else:
            try:
                location = geocoder.ip('me')
                org = location.json['org']
                addr = location.json['address']
                if org == 'AS37686 Ahmadu Bello University Zaria Nigeria' and addr == 'Zaria, Kaduna State, NG':
                    print('You are within our area of service')
                    print('org: ', org, 'addr: ', addr)
                    print(dir(self.map))
                    self.map.ids.main_map.center_on(location.latlng[0], location.latlng[1])
                else:
                    print('You are not within our area of service')
                    print('org: ', org, 'addr: ', addr)
                print(self.map.ids.main_map.lat, self.map.ids.main_map.lon)
            except Exception as e:
                print('Location Error:', e)

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])
        print(self.gps_location)
        # self.model.lat = kwargs
        # self.model.lon =

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)
