from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
# from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.list import MDListItem
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp

Builder.load_string(
'''
#:import images_path kivymd.images_path
<IconItem>
    MDListItemLeadingIcon:
        icon: root.icon
    MDListItemSupportingText:
        id: item_text
        text: root.text

<PreviousMDIcons>
    md_bg_color: self.theme_cls.backgroundColor
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        MDBoxLayout:
            adaptive_height: True
            MDIconButton:
                icon: 'magnify'
                pos_hint: {'center_y': .5}
            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: 
                    root.set_list_md_icons(self.text, True)
        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            bar_width: dp(16)
            scroll_type: ['bars', 'content']
            RecycleBoxLayout:
                padding: dp(10), dp(10), 0, dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)

class IconItem(MDListItem):
    icon = StringProperty()
    text = StringProperty()
    def on_press(self):
        Clipboard.copy(self.ids.item_text.text)
        MDSnackbar(
            MDSnackbarText(
                text=f"'{self.ids.item_text.text}' Copied to clipboard",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
        ).open()

class PreviousMDIcons(MDScreen):
    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''
        print(text, search)
        def add_icon_item(name_icon):
            self.ids.rv.data.append(
            {
            "viewclass": "IconItem",
            "icon": name_icon,
            "text": name_icon,
            "callback": lambda x: x,
            }
            )
        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()
    def build(self):
        return self.screen
    def on_start(self):
        self.screen.set_list_md_icons()

MainApp().run()