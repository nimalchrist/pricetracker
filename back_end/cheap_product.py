def getCheapestProduct(product_dict):
    cheapest_product = None
    cheapest_price = float('inf')
    cheap_prdtimage_url = ""
    cheap_prdt_url = ""


    # Loop through all the products in the dictionary
    for store_products in product_dict.values():
        for product in store_products:
            # Extract the price value as a float
            price_value = float(product['price'].replace(',', '').replace('₹', ''))
            img_url = product['image_url']
            prdt_url = product['product_url']
            if price_value < cheapest_price:
                # If the current product is cheaper than the current cheapest, update the variables
                cheapest_product = product
                cheapest_price = price_value
                cheapest_prdt_url = prdt_url
                cheapest_img_url = img_url
  
    return cheapest_product
