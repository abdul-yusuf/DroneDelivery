from View.base_screen import BaseScreenView


class OrderHistoryScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print('*'*20)
        print(self.model.data)
        data = []
        for item in self.model.data:
            item['rootx'] = self
            data.append(item)

        self.ids.rv3.data = data