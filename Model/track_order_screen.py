from Model.base_model import BaseScreenModel, snackbar_notification


class TrackOrderScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.track_order_screen.TrackOrderScreen.TrackOrderScreenView` class.
    """

    data = {
        'pk': 60,
        'name': 'White Rice',
        'lat': '11.2340000000000000',
        'lon': '6.2075000000000000',
        'eta': '10 mins',
        'date': '02 August, 2024',
        'price': 10000,
        'payment_method': 'card',
        'item': [
            {
                'quantity': 1,
                'product': 1
            }
        ],
        'weight': '10 gram',
        'status': ''
    }
    pk = 1

    def do_get_detail_order(self):
        # self._called_func.insert(0, 'do_get_product_list')
        print(self.pk)
        self.dialog.open()
        self.api.post_request(f'http:'
                              f'//127.0.0.1:8000/order/{self.pk}/', self, method='GET')

    def on_success(self, *args, **kwargs):

        self.data = args[1]
        self.dialog.dismiss()

    def on_error(self, *args, **kwargs):
        snackbar_notification(f"{args[1].strerror}")
        self.dialog.dismiss()

    def on_failure(self, *args, **kwargs):
        if isinstance(args[1].values(), list):
            msg = args[1]
        else:
            msg = args[1][list(args[1])[0]]
        snackbar_notification(f"{msg}")
        self.dialog.dismiss()
