# # from kivy.lang import Builder
# #
# # from kivymd.app import MDApp
# # from kivymd.uix.tab import (
# #     MDTabsItem,
# #     MDTabsItemIcon,
# #     MDTabsItemText,
# #     MDTabsBadge,
# # )
# #
# # KV = '''
# # MDScreen:
# #     md_bg_color: self.theme_cls.backgroundColor
# #
# #     MDTabsPrimary:
# #         id: tabs
# #         pos_hint: {"center_x": .5, "center_y": .5}
# #
# #         MDDivider:
# # '''
# #
# #
# # class Example(MDApp):
# #     def on_start(self):
# #         for tab_icon, tab_name in {
# #             "airplane": "Flights",
# #             "treasure-chest": "Trips",
# #             "compass-outline": "Explore",
# #         }.items():
# #             if tab_icon == "treasure-chest":
# #                 self.root.ids.tabs.add_widget(
# #                     MDTabsItem(
# #                         MDTabsItemIcon(
# #                             MDTabsBadge(
# #                                 text="99",
# #                             ),
# #                             icon=tab_icon,
# #                         ),
# #                         MDTabsItemText(
# #                             text=tab_name,
# #                         ),
# #                     )
# #                 )
# #             else:
# #                 self.root.ids.tabs.add_widget(
# #                     MDTabsItem(
# #                         MDTabsItemIcon(
# #                             icon=tab_icon,
# #                         ),
# #                         MDTabsItemText(
# #                             text=tab_name,
# #                         ),
# #                     )
# #                 )
# #             self.root.ids.tabs.switch_tab(icon="airplane")
# #
# #     def build(self):
# #         self.theme_cls.primary_palette = "Olive"
# #         return Builder.load_string(KV)
# #
# #
# # Example().run()
#
#
# from kivy.lang import Builder
#
# from kivymd.app import MDApp
# from kivymd.uix.tab import (
#     MDTabsItemIcon,
#     MDTabsItemText,
#     MDTabsBadge, MDTabsItemSecondary,
# )
#
# KV = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDTabsSecondary:
#         id: tabs
#         pos_hint: {"center_x": .5, "center_y": .5}
#
#         MDDivider:
# '''
#
#
# # class Example(MDApp):
# #     def on_start(self):
# #         for tab_icon, tab_name in {
# #             "airplane": "Flights",
# #             "treasure-chest": "Trips",
# #             "compass-outline": "Explore",
# #         }.items():
# #             if tab_icon == "treasure-chest":
# #                 self.root.ids.tabs.add_widget(
# #                     MDTabsItemSecondary(
# #                         MDTabsItemIcon(
# #                             icon=tab_icon,
# #                         ),
# #                         MDTabsItemText(
# #                             text=tab_name,
# #                         ),
# #                         MDTabsBadge(
# #                             text="5",
# #                         ),
# #                     )
# #                 )
# #             else:
# #                 self.root.ids.tabs.add_widget(
# #                     MDTabsItemSecondary(
# #                         MDTabsItemIcon(
# #                             icon=tab_icon,
# #                         ),
# #                         MDTabsItemText(
# #                             text=tab_name,
# #                         ),
# #                     )
# #                 )
# #         self.root.ids.tabs.switch_tab(icon="airplane")
# #
# #     def build(self):
# #         self.theme_cls.primary_palette = "Olive"
# #         return Builder.load_string(KV)
# #
# #
# # Example().run()
#
#
# from kivy.lang import Builder
#
# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
# from kivymd.uix.tab import (
#     MDTabsItemIcon,
#     MDTabsItemText,
#     MDTabsItem,
# )
#
# KV = '''
# MDScreen:
#     md_bg_color: self.theme_cls.backgroundColor
#
#     MDTextField:
#         pos_hint: {"center_x": .5, "center_y": .5}
#         validator: "email"
#
#         MDTextFieldHelperText:
#             text: "user@gmail.com"
#             mode: "on_error"
#         MDTextFieldHintText:
#             id: pwd2
#             text: 'Confirm Password'
#         MDTextFieldTrailingIcon:
#             icon: "eye-off-outline"
#             on_press: self.icon = "eye-off-outline" if self.icon=="eye" else "eye"
# #                    on_: print('Hidden')
#     # MDTabsPrimary:
#     #     id: tabs
#     #     pos_hint: {"center_x": .5, "center_y": .5}
#     #     size_hint_x: 1
#     #
#     #     MDDivider:
#     #
#     #     MDTabsCarousel:
#     #         id: related_content_container
#     #         size_hint_y: None
#     #         height: dp(320)
# '''
#
#
# class Example(MDApp):
#     # def on_start(self):
#     #     for tab_icon, tab_name in {
#     #         "airplane": "Flights",
#     #         "treasure-chest": "Trips",
#     #         "compass-outline": "Explore",
#     #     }.items():
#     #         self.root.ids.tabs.add_widget(
#     #             MDTabsItem(
#     #                 MDTabsItemIcon(
#     #                     icon=tab_icon,
#     #                 ),
#     #                 MDTabsItemText(
#     #                     text=tab_name,
#     #                 ),
#     #             )
#     #         )
#     #         self.root.ids.related_content_container.add_widget(
#     #             MDLabel(
#     #                 text=tab_name,
#     #                 halign="center",
#     #             )
#     #         )
#     #         self.root.ids.tabs.switch_tab(icon="airplane")
#
#     def build(self):
#         self.theme_cls.primary_palette = "Olive"
#         return Builder.load_string(KV)
#
#
# Example().run

# import sys
# import os
# from kivy.base import runTouchApp
#
# from kivy_garden.mapview import MapMarker, MapView
# from kivy_garden.mapview.clustered_marker_layer import ClusteredMarkerLayer
# from kivy_garden.mapview.geojson import GeoJsonMapLayer
# from kivy_garden.mapview.utils import get_zoom_for_radius, haversine
#
# directory = ''
# filename = 'mapjson.json'
#
# source = os.path.join(directory, filename)
#
# options = {}
# layer = GeoJsonMapLayer(source=source)
#
# # try to auto center the map on the source
# lon, lat = layer.center
# options["lon"] = lon
# options["lat"] = lat
# min_lon, max_lon, min_lat, max_lat = layer.bounds
# radius = haversine(min_lon, min_lat, max_lon, max_lat)
# zoom = get_zoom_for_radius(radius, lat)
# options["zoom"] = zoom
#
# view = MapView(**options)
# view.add_layer(layer)
#
# marker_layer = ClusteredMarkerLayer(cluster_radius=200)
# view.add_layer(marker_layer)
#
# # create marker if they exists
# count = 0
#
#
# def create_marker(feature):
#     global count
#     geometry = feature["geometry"]
#     if geometry["type"] != "Point":
#         return
#     lon, lat = geometry["coordinates"]
#     marker_layer.add_marker(lon, lat)
#     count += 1
#
#
# layer.traverse_feature(create_marker)
# if count:
#     print("Loaded {} markers".format(count))
#
# runTouchApp(view)

# import sys
#
# from kivy.base import runTouchApp
# from kivy.lang import Builder
#
# if __name__ == '__main__' and __package__ is None:
#     from os import path
#
#     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#
#
# root = Builder.load_string(
#     """
# #:import sys sys
# #:import MapSource kivy_garden.mapview.MapSource
# MapView:
#     lat: 50.6394
#     lon: 3.057
#     zoom: 13
#     map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
#
#     MapMarkerPopup:
#         lat: 50.6394
#         lon: 3.057
#         popup_size: dp(230), dp(130)
#
#         Bubble:
#             BoxLayout:
#                 orientation: "horizontal"
#                 padding: "5dp"
#                 AsyncImage:
#                     source: "http://upload.wikimedia.org/wikipedia/commons/9/9d/France-Lille-VieilleBourse-FacadeGrandPlace.jpg"
#                     mipmap: True
#                 Label:
#                     text: "[b]Lille[/b]\\n1 154 861 hab\\n5 759 hab./km2"
#                     markup: True
#                     halign: "center"
#
# """
# )
#
# runTouchApp(root)

#
# from kivy.base import runTouchApp
# from kivy.lang import Builder
#
# if __name__ == '__main__' and __package__ is None:
#     from os import sys, path
#
#     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#
# root = Builder.load_string(
#     """
# #:import MapSource kivy_garden.mapview.MapSource
#
# <Toolbar@BoxLayout>:
#     size_hint_y: None
#     height: '48dp'
#     padding: '4dp'
#     spacing: '4dp'
#
#     canvas:
#         Color:
#             rgba: .2, .2, .2, .6
#         Rectangle:
#             pos: self.pos
#             size: self.size
#
# <ShadedLabel@Label>:
#     size: self.texture_size
#     canvas.before:
#         Color:
#             rgba: .2, .2, .2, .6
#         Rectangle:
#             pos: self.pos
#             size: self.size
#
# RelativeLayout:
#
#     MapView:
#         id: mapview
#         lat: 11.15358
#         lon: 7.651
#         zoom: 18
#         #size_hint: .5, .5
#         #pos_hint: {"x": .25, "y": .25}
#
#         #on_map_relocated: mapview2.sync_to(self)
#         #on_map_relocated: mapview3.sync_to(self)
#
#         MapMarker:
#             lat: 11.15358
#             lon: 7.651
#
#         MapMarker
#             lat: -33.867
#             lon: 151.206
#
#     Toolbar:
#         top: root.top
#         Button:
#             text: "Move to Lille, France"
#             on_release: mapview.center_on(50.6394, 3.057)
#         Button:
#             text: "Move to Sydney, Autralia"
#             on_release: mapview.center_on(-33.867, 151.206)
#         Spinner:
#             text: "mapnik"
#             values: MapSource.providers.keys()
#             on_text: mapview.map_source = self.text
#
#     Toolbar:
#         Label:
#             text: "Longitude: {}".format(mapview.lon)
#         Label:
#             text: "Latitude: {}".format(mapview.lat)
#     """
# )
#
# runTouchApp(root)



# coding=utf-8
"""
This example demonstrate how to use the MBTilesMapSource provider.
It supports v1.1 version of .mbtiles of Mapbox.
See more at http://mbtiles.org/

It currently require a Kivy version that can load data from a buffer. This
is not the case on every platform at 1.8.1, but we're going to fix it.
"""

import sys
import os

from kivy.base import runTouchApp

from kivy_garden.mapview import MapView
from kivy_garden.mapview.mbtsource import MBTilesMapSource
directory = ''
filename = 'mapjson.json'

# source = os.path.join(directory, filename)
source = MBTilesMapSource(os.path.join(directory, filename))
runTouchApp(
    MapView(
        map_source=source,
        lat=source.default_lat,
        lon=source.default_lon,
        zoom=source.default_zoom,
    )
)