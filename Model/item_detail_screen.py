from kivy.properties import ObjectProperty

from Model.base_model import BaseScreenModel


class ItemDetailScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.item_detail_screen.ItemDetailScreen.ItemDetailScreenView` class.
    """

    item_detail = {
        'pk': '1',
        'image': 'assets/images/product1.jpg',
        'name': 'item1',
        'price': '8,000.00',
        'category': 'category1',
        'description': 'Lorem Ipsum has been around for a thousand years',
        'vendor': 'Amarya',
        'weight': '1',
        'unit': 'kg'
    }

    data = {
        'pk': '1',
        'image': 'assets/images/product1.jpg',
        'name': 'item1',
        'price': '8,000.00',
        'category': 'category1',
        'description': 'Lorem Ipsum has been around for a thousand years',
        'vendor': 'Amarya',
        'weight': '1',
        'unit': 'kg'
    }

    cart_items = []

    main_screen_controller = None