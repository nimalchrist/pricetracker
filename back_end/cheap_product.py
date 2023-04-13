def getCheapestProduct(product_dict):
    cheapest_product = None
    cheapest_price = float('inf')

    # Loop through all the products in the dictionary
    for store_products in product_dict.values():
        for product in store_products:
            # Extract the price value as a float
            price_value = float(product['price'].replace(',', '').replace('₹', ''))
            if price_value < cheapest_price:
                # If the current product is cheaper than the current cheapest, update the variables
                cheapest_product = product
                cheapest_price = price_value

    return cheapest_product
