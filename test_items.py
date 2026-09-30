import time


def test_product_page_has_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    add_to_basket_button = browser.find_element(
        "css selector", "button.btn-add-to-basket"
    )

    assert add_to_basket_button.is_displayed(), \
        "Кнопка добавления в корзину не найдена на странице"