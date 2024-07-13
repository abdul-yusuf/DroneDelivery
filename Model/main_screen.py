from Model.base_model import BaseScreenModel


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
            'price': '10,000.00',
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
            'price': '20,000.00',
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
            'price': '11,000.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya'
        },
        {
            'pk': '4',
            'image': 'assets/images/product4.jpg',
            'name': 'Fendi3 Watch',
            'price': '10,200.00',
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
            'price': '30,000.00',
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