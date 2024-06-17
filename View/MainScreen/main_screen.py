from kivy.uix.recycleview import RecycleViewBehavior, RecycleDataModel, RecycleDataAdapter, RecycleView, \
    RecycleLayoutManagerBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, AliasProperty
from View.base_screen import BaseScreenView
from kivy.clock import Clock


class MainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """


class BottomNav(MDBoxLayout):
    selected = ObjectProperty()
    screen_manager = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(BottomNav, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.init_selected, 1)

    def init_selected(self, *args, **kwargs):
        try:
            self.selected = self.ids.btn1
            self.selected.style = 'tonal'
        except AttributeError as e:
            print(e)

    def switch(self, btn, screen_name):
        # if btn.style == 'text':
        # if self.selected:
        try:
            self.selected.style = 'text'
        except Exception as e:
            print(e)
        # else:
        #     self.selected = btn
        self.selected = btn
        btn.style = 'tonal'
        # else:
        #     btn.style = 'text'
        self.screen_manager.current = screen_name

class Rv(RecycleViewBehavior, MDBoxLayout):
    def __init__(self, **kwargs):
        if self.data_model is None:
            kwargs.setdefault('data_model', RecycleDataModel())
        if self.view_adapter is None:
            kwargs.setdefault('view_adapter', RecycleDataAdapter())
        super(Rv, self).__init__(**kwargs)

        fbind = self.fbind
        # fbind('scroll_x', self.refresh_from_viewport)
        # fbind('scroll_y', self.refresh_from_viewport)
        fbind('size', self.refresh_from_viewport)
        self.refresh_from_data()

    def _convert_sv_to_lm(self, x, y):
        lm = self.layout_manager
        tree = [lm]
        parent = lm.parent
        while parent is not None and parent is not self:
            tree.append(parent)
            parent = parent.parent

        if parent is not self:
            raise Exception(
                'The layout manager must be a sub child of the recycleview. '
                'Could not find {} in the parent tree of {}'.format(self, lm))

        for widget in reversed(tree):
            x, y = widget.to_local(x, y)

        return x, y

    def get_viewport(self):
        lm = self.layout_manager
        lm_w, lm_h = lm.size
        w, h = self.size
        scroll_y = min(1, 0)
        scroll_x = min(1, 0)

        if lm_h <= h:
            bottom = 0
        else:
            above = (lm_h - h)
            bottom = max(0, lm_h - above - h)

        bottom = max(0, (lm_h - h))
        left = max(0, (lm_w - w))
        width = min(w, lm_w)
        height = min(h, lm_h)

        # now convert the sv coordinates into the coordinates of the lm. In
        # case there's a relative layout type widget in the parent tree
        # between the sv and the lm.
        left, bottom = self._convert_sv_to_lm(left, bottom)
        return left, bottom, width, height

    def save_viewport(self):
        pass

    def restore_viewport(self):
        pass

    def add_widget(self, widget, *args, **kwargs):
        super(Rv, self).add_widget(widget, *args, **kwargs)
        if (isinstance(widget, RecycleLayoutManagerBehavior) and
                not self.layout_manager):
            self.layout_manager = widget

    def remove_widget(self, widget, *args, **kwargs):
        super(Rv, self).remove_widget(widget, *args, **kwargs)
        if self.layout_manager == widget:
            self.layout_manager = None



    # or easier way to use
    def _get_data(self):
        d = self.data_model
        return d and d.data

    def _set_data(self, value):
        d = self.data_model
        if d is not None:
            d.data = value

    data = AliasProperty(_get_data, _set_data, bind=["data_model"])


    def _get_viewclass(self):
        a = self.layout_manager
        return a and a.viewclass

    def _set_viewclass(self, value):
        a = self.layout_manager
        if a:
            a.viewclass = value

    viewclass = AliasProperty(_get_viewclass, _set_viewclass,
                              bind=["layout_manager"])