from Model.base_model import BaseScreenModel, snackbar_notification
from json import dumps


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    data = [
        {
            'pk': '1',
            'image': 'assets/images/product1.jpg',
            'name': 'Fendi Watch',
            'price': '10000.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya',
            'weight': '1',
            'unit': 'kg'
        },
        {
            'pk': '2',
            'image': 'assets/images/product2.jpg',
            'name': 'Fendi1 Watch',
            'price': '20000.00',
            'category': 'Printing',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya',
            'weight': '1',
            'unit': 'kg'
        },
        {
            'pk': '3',
            'image': 'assets/images/product3.jpg',
            'name': 'Fendi2 Watch',
            'price': '11000.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya'
        },
        {
            'pk': '4',
            'image': 'assets/images/product4.jpg',
            'name': 'Fendi3 Watch',
            'price': '10200.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': "Ma'ata",
            'weight': '100',
            'unit': 'grams'
        },
        {
            'pk': '5',
            'image': 'assets/images/product5.jpg',
            'name': 'Fendi4 Watch',
            'price': '30000.00',
            'category': 'Bookshop',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya',
            'weight': '100',
            'unit': 'grams'
        },
    ]

    categories_data = [
        {
            'name': 'Restaurant'
        },
        {
            'name': 'Printing'
        },
        {
            'name': 'Bookshop'
        },
        {
            'name': 'Mon'
        },
        {
            'name': 'Fast Foood'
        },
    ]

    items_data: list = []

    cart_items: list = []

    is_remove_item: bool = False

    order_data: dict = {}

    _called_func = []

    def do_get_product_list(self):
        self._called_func.insert(0, 'do_get_product_list')
        self.dialog.open()
        self.api.post_request('https://yusufabdul.pythonanywhere.com/store/products/', self, method='GET')

    def do_set_order(self, data):
        """
        func to send order to the backend.

        """
        print('Order Details: ', data)
        self._called_func.insert(0, 'do_set_order')
        self.dialog.open()
        self.api.post_request('https://yusufabdul.pythonanywhere.com/order/create/', self, payload=data)

    def on_success(self, *args, **kwargs):

        if self._called_func:
            if self._called_func[0] == 'do_get_product_list':
                self.data = args[1]
                print(type(self.data))
                print(self.data)
                self.notify_observers_methods('main screen', "refresh_products_data")
            if self._called_func[0] == 'do_set_order':
                self.notify_observers_methods('main screen', "refresh_cart_data")

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
