from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page):
        self.page: Page = page
        self.page_title: Locator = page.locator('.title')
        self.sort: Locator = page.locator('[data-test="product-sort-container"]')
        self.open_cart: Locator = page.locator('.shopping_cart_link')
        self.inventory_items: Locator = page.locator('.inventory_item')
        self.item_names: Locator = page.locator('.inventory_item_name')
        self.item_prices: Locator = page.locator('.inventory_item_price')
        self.add_to_cart_buttons: Locator = page.locator('button.btn_inventory')
        self.cart_badge: Locator = page.locator('.shopping_cart_badge')

    def get_items_count(self) -> int:
        return self.inventory_items.count()

    def get_page_title(self) -> str:
        return self.page_title.inner_text()




