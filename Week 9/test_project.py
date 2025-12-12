import project

def test_get_cart_total():
    project.store.cart = []
    assert project.get_cart_total() == 0, "Cart total should be 0 when cart is empty"

    product = project.search_product_by_name("Classic Watch")
    project.store.cart = [product]
    assert project.get_cart_total() == product.price, "Cart total should match the price of single item"

    product2 = project.search_product_by_name("Classic Shoes")
    project.store.cart.append(product2)
    expected_total = product.price + product2.price
    assert project.get_cart_total() == expected_total, "Cart total should sum all item prices"

def test_recommend_music_for_category():
    category = "Classic"
    song = project.recommend_music_for_category(category)
    assert isinstance(song, str), "Recommended song should be a string"
    another_song = project.recommend_music_for_category(category)
    assert isinstance(another_song, str), "Another recommendation should also be a string"

def test_search_product_by_name():
    product = project.search_product_by_name("Classic Watch")
    assert product is not None, "Product should exist"
    assert product.name == "Classic Watch", "Product name should match"
    assert product.price > 0, "Product price should be greater than 0"

    product_none = project.search_product_by_name("Nonexistent Product")
    assert product_none is None, "Should return None for non-existing product"
