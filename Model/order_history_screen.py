from Model.base_model import BaseScreenModel, snackbar_notification


class OrderHistoryScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.order_history_screen.OrderHistoryScreen.OrderHistoryScreenView` class.
    """

    def do_get_product_list(self):
        self._called_func.insert(0, 'do_get_product_list')
        self.dialog.open()
        self.api.post_request('http://127.0.0.1:8000/store/products/', self, method='GET')

    def on_success(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        self.notify_observers('main screen')
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('ERROR: ', args, kwargs)
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)

        if isinstance(args[1].values(), list):
            msg = args[1]
        else:
            msg = args[1][list(args[1])[0]]
        snackbar_notification(f"{msg}")
        self.dialog.dismiss()
