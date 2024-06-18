from Model.base_model import BaseScreenModel


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    data = [
        {
            'pk': '1',
            'name': 'Fendi Watch',
            'price': '10,000.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya'
        },
        {
            'pk': '2',
            'name': 'Fendi1 Watch',
            'price': '20,000.00',
            'category': 'Printing',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya'
        },
        {
            'pk': '3',
            'name': 'Fendi2 Watch',
            'price': '11,000.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya'
        },
        {
            'pk': '4',
            'name': 'Fendi3 Watch',
            'price': '10,200.00',
            'category': 'Restaurant',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': "Ma'ata"
        },
        {
            'pk': '5',
            'name': 'Fendi4 Watch',
            'price': '30,000.00',
            'category': 'Bookshop',
            'description': 'Lorem has been around for a thousands of decades',
            'vendor': 'Amarya'
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

    items_data = []

    cart_items = []

    is_remove_item = False