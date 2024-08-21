from Model.base_model import BaseScreenModel, snackbar_notification


class OrderHistoryScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.order_history_screen.OrderHistoryScreen.OrderHistoryScreenView` class.
    """
    data = None

    def do_get_order_list(self):
        self.dialog.open()
        self.api.post_request('https://yusufabdul.pythonanywhere.com/order/', self, method='GET')

    def on_success(self, *args, **kwargs):
        print('Success: ', args, kwargs)
        self.data = args[1]
        self.notify_observers('order history screen')
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        print('ERROR: ', args, kwargs)
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        print('Failure: ', args, kwargs)
        try:
            if isinstance(args[1].values(), list):
                msg = args[1]
            else:
                msg = args[1][list(args[1])[0]]
            snackbar_notification(f"{msg}")
        except AttributeError:
            snackbar_notification("An Error occurred")

        self.dialog.dismiss()
