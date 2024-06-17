# from kivy.lang import Builder
#
# from kivymd.app import MDApp
# from kivymd.uix.tab import (
#     MDTabsItem,
#     MDTabsItemIcon,
#     MDTabsItemText,
#     MDTabsBadge,
# )
#
# KV = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDTabsPrimary:
#         id: tabs
#         pos_hint: {"center_x": .5, "center_y": .5}
#
#         MDDivider:
# '''
#
#
# class Example(MDApp):
#     def on_start(self):
#         for tab_icon, tab_name in {
#             "airplane": "Flights",
#             "treasure-chest": "Trips",
#             "compass-outline": "Explore",
#         }.items():
#             if tab_icon == "treasure-chest":
#                 self.root.ids.tabs.add_widget(
#                     MDTabsItem(
#                         MDTabsItemIcon(
#                             MDTabsBadge(
#                                 text="99",
#                             ),
#                             icon=tab_icon,
#                         ),
#                         MDTabsItemText(
#                             text=tab_name,
#                         ),
#                     )
#                 )
#             else:
#                 self.root.ids.tabs.add_widget(
#                     MDTabsItem(
#                         MDTabsItemIcon(
#                             icon=tab_icon,
#                         ),
#                         MDTabsItemText(
#                             text=tab_name,
#                         ),
#                     )
#                 )
#             self.root.ids.tabs.switch_tab(icon="airplane")
#
#     def build(self):
#         self.theme_cls.primary_palette = "Olive"
#         return Builder.load_string(KV)
#
#
# Example().run()


from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import (
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsBadge, MDTabsItemSecondary,
)

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTabsSecondary:
        id: tabs
        pos_hint: {"center_x": .5, "center_y": .5}

        MDDivider:
'''


# class Example(MDApp):
#     def on_start(self):
#         for tab_icon, tab_name in {
#             "airplane": "Flights",
#             "treasure-chest": "Trips",
#             "compass-outline": "Explore",
#         }.items():
#             if tab_icon == "treasure-chest":
#                 self.root.ids.tabs.add_widget(
#                     MDTabsItemSecondary(
#                         MDTabsItemIcon(
#                             icon=tab_icon,
#                         ),
#                         MDTabsItemText(
#                             text=tab_name,
#                         ),
#                         MDTabsBadge(
#                             text="5",
#                         ),
#                     )
#                 )
#             else:
#                 self.root.ids.tabs.add_widget(
#                     MDTabsItemSecondary(
#                         MDTabsItemIcon(
#                             icon=tab_icon,
#                         ),
#                         MDTabsItemText(
#                             text=tab_name,
#                         ),
#                     )
#                 )
#         self.root.ids.tabs.switch_tab(icon="airplane")
#
#     def build(self):
#         self.theme_cls.primary_palette = "Olive"
#         return Builder.load_string(KV)
#
#
# Example().run()


from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (
    MDTabsItemIcon,
    MDTabsItemText,
    MDTabsItem,
)

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDTextField:
        pos_hint: {"center_x": .5, "center_y": .5}
        validator: "email"

        MDTextFieldHelperText:
            text: "user@gmail.com"
            mode: "on_error"
        MDTextFieldHintText:
            id: pwd2
            text: 'Confirm Password'
        MDTextFieldTrailingIcon:
            icon: "eye-off-outline"
            on_press: self.icon = "eye-off-outline" if self.icon=="eye" else "eye"
#                    on_: print('Hidden')
    # MDTabsPrimary:
    #     id: tabs
    #     pos_hint: {"center_x": .5, "center_y": .5}
    #     size_hint_x: 1
    # 
    #     MDDivider:
    # 
    #     MDTabsCarousel:
    #         id: related_content_container
    #         size_hint_y: None
    #         height: dp(320)
'''


class Example(MDApp):
    # def on_start(self):
    #     for tab_icon, tab_name in {
    #         "airplane": "Flights",
    #         "treasure-chest": "Trips",
    #         "compass-outline": "Explore",
    #     }.items():
    #         self.root.ids.tabs.add_widget(
    #             MDTabsItem(
    #                 MDTabsItemIcon(
    #                     icon=tab_icon,
    #                 ),
    #                 MDTabsItemText(
    #                     text=tab_name,
    #                 ),
    #             )
    #         )
    #         self.root.ids.related_content_container.add_widget(
    #             MDLabel(
    #                 text=tab_name,
    #                 halign="center",
    #             )
    #         )
    #         self.root.ids.tabs.switch_tab(icon="airplane")

    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)


Example().run()