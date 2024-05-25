from View.base_screen import BaseScreenView
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem


class MainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def on_switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str,
        ):
        print(bar, item, item_icon, item_text)
        self.ids.screen_manager.current = item_text


class CustomNavigationBar(MDNavigationBar):

    def set_active_item(self, item: MDNavigationItem) -> None:
        """Sets the currently active element on the panel."""

        for widget in self.children:
            if item is widget:
                widget.active = True
                self.dispatch(
                    "on_switch_tabs",
                    widget,
                    # widget.ids.icon_container.children[0].icon
                    widget.icon
                    if len(widget.ids.icon_container.children)
                    else "",
                    # widget.ids.label_container.children[0].text
                    widget.text
                    # if len(widget.ids.label_container.children)
                    # else "",
                )
            else:
                widget.active = False