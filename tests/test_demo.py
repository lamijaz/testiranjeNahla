
from pickle import TRUE
from pages.home_page import HomePage
import time


def test_app(driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user","secret_sauce")
    assert home_page.get_text() == "PRODUCTS"
    home_page.confirm("add-to-cart-sauce-labs-backpack")
    home_page.confirm("add-to-cart-sauce-labs-onesie")
    home_page.confirm("shopping_cart_container")
    assert home_page.get_text() == "YOUR CART"
    assert home_page.get_text_items("item_4_title_link") == "Sauce Labs Backpack"
    assert home_page.get_text_items("item_2_title_link") == "Sauce Labs Onesie"
    home_page.confirm("checkout")
    assert home_page.get_text() == "CHECKOUT: YOUR INFORMATION"
    home_page.checkout("Lamija","Zuhric","71000")
    home_page.confirm("continue")
    assert home_page.get_text() == "CHECKOUT: OVERVIEW"
    assert home_page.get_text_items("item_4_title_link") == "Sauce Labs Backpack"
    assert home_page.get_text_items("item_2_title_link") == "Sauce Labs Onesie"
    home_page.confirm("finish")
    assert home_page.get_text() == "CHECKOUT: COMPLETE!"
    home_page.confirm("react-burger-menu-btn")
    home_page.confirm("logout_sidebar_link")
    home_page.logout()
    time.sleep(3)
    
   