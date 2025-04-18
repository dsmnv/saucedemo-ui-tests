import time
import allure
from pages.inventory_page import InventoryPage


def test_catalog_items_displayed(page, login_as_standard_user, inventory_page):
    with allure.step('Открыта страница каталога'):
        assert page.url == 'https://www.saucedemo.com/inventory.html'
        assert inventory_page.get_page_title() == 'Products'

    with allure.step('На странице каталога отображается 6 товаров'):
        assert inventory_page.get_items_count() == 6

    with allure.step('Каждый товар содержит имя, цену и кнопку'):
        items_count = inventory_page.get_items_count()
        for i in range(items_count):
            name = inventory_page.item_names.nth(i)
            price = inventory_page.item_prices.nth(i)
            button = inventory_page.add_to_cart_buttons.nth(i)

            assert name.is_visible(), f'Имя товара {i+1} не отображается'
            assert price.is_visible(), f'Цена товара {i + 1} не отображается'
            assert button.is_visible(), f'Кнопка товара {i + 1} не отображается'
    allure.attach(page.screenshot(),
                  name='Страница каталога с товарами',
                  attachment_type=allure.attachment_type.JPG)


def test_low_to_high_sort(page, login_as_standard_user, inventory_page):
    with allure.step('Кнопка сортировки отображается'):
        assert inventory_page.sort.is_visible()

    with allure.step('Выбрана сортировка low to high'):
        inventory_page.sort.select_option('lohi')

    with allure.step('Товары отсортированы по увеличению цены'):
        # Создаем пустой список, циклом проходимся по всем ценам на странице и складываем их в список
        items_count = inventory_page.get_items_count()
        prices = []

        for i in range(items_count):
            price_text = inventory_page.item_prices.nth(i).inner_text()
            price_number = float(price_text.replace('$', ''))
            prices.append(price_number)
        assert prices == sorted(prices)
        allure.attach(str(prices), name='Цены на странице', attachment_type=allure.attachment_type.TEXT)
        allure.attach(page.screenshot(),
                      name='Отсортированная страница каталога',
                      attachment_type=allure.attachment_type.JPG)


def test_z_to_a_sort(page, login_as_standard_user, inventory_page):
    with allure.step('Кнопка сортировки отображается'):
        inventory_page.sort.is_visible()

    with allure.step('Выбрана сортировка Z to A'):
        inventory_page.sort.select_option('za')

    names = [
        inventory_page.item_names.nth(i).inner_text()
        for i in range(inventory_page.get_items_count())
    ]

    with allure.step('Товары отсортированы корректно'):
        assert names == sorted(names, reverse=True)
        allure.attach(str(names), name='Список товаров', attachment_type=allure.attachment_type.TEXT)
        allure.attach(page.screenshot(),
                      name='Отсортированная страница каталога',
                      attachment_type=allure.attachment_type.JPG)


def test_add_product_to_cart(page, add_product_to_cart, inventory_page):
    added_product = inventory_page.item_names.nth(0).inner_text()
    with allure.step('Состояние кнопки изменилось'):
        assert inventory_page.add_to_cart_buttons.nth(0).inner_text() == 'Remove'

    with allure.step('На значке корзины отобразился добавленный товар'):
        assert inventory_page.cart_badge.is_visible()
        assert inventory_page.cart_badge.inner_text() == '1'
    allure.attach(page.screenshot(),
                  name='Товар добавлен в корзину',
                  attachment_type=allure.attachment_type.JPG)

    with allure.step('Переходим в корзину для проверки добавленного товара'):
        inventory_page.open_cart.click()
        assert page.url == 'https://www.saucedemo.com/cart.html'
        assert page.locator('.inventory_item_name').inner_text() == added_product
    allure.attach(page.screenshot(),
                  name='Корзина',
                  attachment_type=allure.attachment_type.JPG)


def test_remove_product_from_cart(page, add_product_to_cart, inventory_page):
    with allure.step('Товар добавлен в корзину'):
        assert inventory_page.add_to_cart_buttons.nth(0).inner_text() == 'Remove'
        assert inventory_page.cart_badge.inner_text() == '1'

    with allure.step('Состояние кнопки вернулось к исходному'):
        inventory_page.add_to_cart_buttons.nth(0).click()
        assert inventory_page.add_to_cart_buttons.nth(0).inner_text() == 'Add to cart'

    with allure.step('Бейдж у корзины исчез после удаления товара'):
        assert inventory_page.cart_badge.is_hidden()
    allure.attach(page.screenshot(),
                  name='Страница после удаления товара',
                  attachment_type=allure.attachment_type.JPG)


