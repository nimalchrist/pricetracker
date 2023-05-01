# import requests
# from bs4 import BeautifulSoup


# def getScrappedProducts(product_name):
#     product_dict = {'amazon': [], 'flipkart': []}

#     # Amazon scraping using ScrapingBee API
#     amazon_url = f"https://www.amazon.in/s?k={product_name}"
#     try:
#         # Send a GET request to the ScrapingBee API endpoint for Amazon
#         amazon_response = requests.get(amazon_url)
#         if (amazon_response.status_code == 200):
#             # Parse the HTML content using BeautifulSoup for Amazon
#             amazon_soup = BeautifulSoup(amazon_response.content, 'html.parser')

#             # Find all the Amazon product containers on the page
#             amazon_product_containers = amazon_soup.find_all(
#                 'div', {'class': 's-result-item'})

#             # Loop through each Amazon product container and extract the title and price
#             i = 0
#             for amazon_product in amazon_product_containers:
#                 amazon_title_element = amazon_product.find(
#                     'h2', {'class': 'a-size-mini'})
#                 amazon_price_element = amazon_product.find(
#                     'span', {'class': 'a-price'})
#                 amazon_image_element = amazon_product.find(
#                     'img', {'class': 's-image'})

#                 # If the Amazon title and price elements exist, extract the text
#                 if amazon_title_element and amazon_price_element:
#                     amazon_title = amazon_title_element.text.strip()
#                     amazon_currency_symbol = amazon_price_element.find(
#                         'span', {'class': 'a-price-symbol'}).text.strip()
#                     amazon_price_value = amazon_price_element.find(
#                         'span', {'class': 'a-price-whole'}).text.strip()
#                     amazon_price = amazon_currency_symbol+" "+amazon_price_value
#                     amazon_image_url = amazon_image_element['src']if amazon_image_element else 'https://rukminim1.flixcart.com/image/312/312/ktketu80/mobile/6/n/d/iphone-13-mlpg3hn-a-apple-original-imag6vpyghayhhrh.jpeg?q=70'

#                     # Add the Amazon product details to the dictionary
#                     current_product = {
#                         'name': amazon_title,
#                         'price': amazon_price,
#                         'image_url': amazon_image_url
#                     }
#                     product_dict['amazon'].append(current_product)
#                     i += 1

#         else:
#             return "No product found on Amazon"
#     except Exception as e:
#         print(e)

#     # Flipkart scraping using requests and BeautifulSoup
#     flipkart_url = f"https://www.flipkart.com/search?q={product_name}"

#     try:
#         # Send a GET request to the ScrapingBee API endpoint for Flipkart
#         flipkart_response = requests.get(flipkart_url)
#         if flipkart_response.status_code == 200:
#             # Parse the HTML content using BeautifulSoup for Flipkart
#             flipkart_soup = BeautifulSoup(
#                 flipkart_response.content, 'html.parser')

#             # Find all the Flipkart product containers on the page
#             flipkart_product_containers = flipkart_soup.find_all(
#                 'div', {'class': '_2kHMtA'})

#             # Loop through each Flipkart product container and extract the title and price
#             for flipkart_product in flipkart_product_containers:
#                 flipkart_title_element = flipkart_product.find(
#                     'div', {'class': '_4rR01T'})
#                 flipkart_price_element = flipkart_product.find(
#                     'div', {'class': '_30jeq3 _1_WHN1'})

#                 # If the Flipkart title and price elements exist, extract the text
#                 if flipkart_title_element and flipkart_price_element:
#                     flipkart_title = flipkart_title_element.text.strip()
#                     flipkart_price = flipkart_price_element.text.strip()
#                     flipkart_image_element = flipkart_product.find(
#                         'img', {'class': '_396cs4 _3exPp9'})
#                     flipkart_image_url = flipkart_image_element[
#                         'src'] if flipkart_image_element else 'https://t3.ftcdn.net/jpg/04/34/72/82/240_F_434728286_OWQQvAFoXZLdGHlObozsolNeuSxhpr84.jpg'

#                     # Append the Flipkart title, price, and image URL to the product list
#                     current_product = {
#                         'name': flipkart_title,
#                         'price': flipkart_price,
#                         'image_url': flipkart_image_url
#                     }
#                     product_dict['flipkart'].append(current_product)

#             return product_dict
#         else:
#             return "No products found"

#     except Exception as e:
#         print(e)

import random
import requests
from bs4 import BeautifulSoup




def getScrappedProducts(product_name):
    product_dict = {'amazon': [], 'flipkart': []}
    card_title = ""
    card_price = ""
    card_product_url = ""
    card_image_url = ""

    proxies_list = [
        '167.172.248.53:3128',
        '194.226.34.132:5555',
        '203.202.245.62:80',
        '141.0.70.211:8080',
        '118.69.50.155:80',
        '201.55.164.177:3128',
        '51.15.166.107:3128',
        '91.205.218.64:80',
        '128.199.237.57:8080',
    ]
    proxies = {
        'http': random.choice(proxies_list)
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', "Regerer": ''}

    # Amazon scraping using ScrapingBee API
    try:
        # Send a GET request to the ScrapingBee API endpoint for Amazon
        # amazon_url = f"https://app.scrapingbee.com/api/v1/?api_key=4WFKLJBI9ZHLPYJQ38QA4NCSMYYLFFACU3O9YBKKBZ6SU6ZV9CA9BSLKNGQ8I351XZLI1MM3FZ8SF88O&url=https://www.amazon.in/s?k={product_name}"

        amazon_url = f'https://www.amazon.in/s?k={product_name}'

        amazon_response = requests.get(
            amazon_url, headers=headers, proxies=proxies)
        if (amazon_response.status_code == 200):
            # Parse the HTML content using BeautifulSoup for Amazon
            amazon_soup = BeautifulSoup(amazon_response.content, 'html.parser')

            # Find all the Amazon product containers on the page
            amazon_product_containers = amazon_soup.find_all(
                'div', {'class': 's-result-item'})

            # Loop through each Amazon product container and extract the title and price
            i = 0
            for amazon_product in amazon_product_containers:
                # Skip the advertisement containers
                if 's-ad-slot' in amazon_product.get('class', []):
                    continue
                amazon_title_element = amazon_product.find(
                    'h2', {'class': 'a-size-mini'})
                amazon_price_element = amazon_product.find(
                    'span', {'class': 'a-price'})
                amazon_image_element = amazon_product.find(
                    'img', {'class': 's-image'})
                amazon_product_url_element = amazon_product.find(
                    'a',{'class': 'a-link-normal s-no-outline'}
                )    

                # If the Amazon title and price elements exist, extract the text
                if amazon_title_element and amazon_price_element:
                    amazon_title = amazon_title_element.text.strip()
                    amazon_currency_symbol = amazon_price_element.find(
                        'span', {'class': 'a-price-symbol'}).text.strip()
                    amazon_price_value = amazon_price_element.find(
                        'span', {'class': 'a-price-whole'}).text.strip()
                    amazon_price = amazon_currency_symbol+" "+amazon_price_value
                    amazon_image_url = amazon_image_element['src']if amazon_image_element else 'https://rukminim1.flixcart.com/image/312/312/ktketu80/mobile/6/n/d/iphone-13-mlpg3hn-a-apple-original-imag6vpyghayhhrh.jpeg?q=70'
                    amazon_product_url = amazon_product_url_element['href']
                    # Add the Amazon product details to the dictionary
                    current_product = {
                        'name': amazon_title,
                        'price': amazon_price,
                        'image_url': amazon_image_url,
                        #'product_url': f"https://www.amazon.in/s?k={product_name}"
                        'product_url': f"https://www.amazon.in{amazon_product_url}"
                    }
                    product_dict['amazon'].append(current_product)
                    i += 1
        else:
            return "No products found on Amazon"
    except Exception as e:
        print(e)

    # Flipkart scraping using requests and BeautifulSoup
    flipkart_url = f"https://www.flipkart.com/search?q={product_name}"

    try:
        # Send a GET request to the ScrapingBee API endpoint for Flipkart
        flipkart_response = requests.get(flipkart_url)
        if flipkart_response.status_code == 200:
            # Parse the HTML content using BeautifulSoup for Flipkart
            flipkart_soup = BeautifulSoup(
                flipkart_response.content, 'html.parser')

            # Find all the Flipkart product containers on the page
            flipkart_view1 = flipkart_soup.find_all(
                'div', {'class': '_2kHMtA'})[:-2]
            
            flipkart_view2 = flipkart_soup.find_all('div',{'class': '_1YokD2 _3Mn1Gg'})
            
            if flipkart_view1:
                flipkart_product_containers = flipkart_view1
            else:
                flipkart_product_containers = flipkart_view2


            # Loop through each Flipkart product container and extract the title and price
            if flipkart_product_containers == flipkart_view1:
                for flipkart_product in flipkart_product_containers:
                    flipkart_title_element = flipkart_product.find(
                        'div', {'class': '_4rR01T'})
                    flipkart_price_element = flipkart_product.find(
                        'div', {'class': '_30jeq3 _1_WHN1'})
                    
                    # If the Flipkart title and price elements exist, extract the text
                    if flipkart_title_element and flipkart_price_element:
                        flipkart_title = flipkart_title_element.text.strip()
                        flipkart_price = flipkart_price_element.text.strip()
                        flipkart_image_element = flipkart_product.find(
                            'img', {'class': '_396cs4'})
                        flipkart_image_url = flipkart_image_element[
                            'src'] if flipkart_image_element else 'https://t3.ftcdn.net/jpg/04/34/72/82/240_F_434728286_OWQQvAFoXZLdGHlObozsolNeuSxhpr84.jpg'
                        flipkart_product_element = flipkart_product.find(
                            'a',{'class': '_1fQZEK'}
                        )
                        flipkart_product_url = flipkart_product_element['href']
                        # Append the Flipkart title, price, and image URL to the product list
                        current_product = {
                            'name': flipkart_title,
                            'price': flipkart_price,
                            'image_url': flipkart_image_url,
                            #'product_url': f"https://www.flipkart.com/search?q={product_name}"
                            'product_url':f"https://www.flipkart.com{flipkart_product_url}"
                        }
                        product_dict['flipkart'].append(current_product)

                return product_dict
            else:

                    flipkart_row_elements = flipkart_soup.find_all("div", class_="_1AtVbE col-12-12")
                    for single_row in flipkart_row_elements:
                        inner_row = single_row.find(
                            "div", class_="_13oc-S _1t9ceu")
                        if inner_row:
                            simple_product_container = inner_row.find(
                                "div", class_="_1xHGtK _373qXS")
                            if simple_product_container:
                                price_container = simple_product_container.find(
                                    "div", class_="_2B099V")
                                title = price_container.find("a", class_="IRpwTa")
                                
                                card_title = title.text

                                if price_container:
                                    inner_price = price_container.find("div", class_="_25b18c")
                                    if inner_price:
                                        price = inner_price.find("div", class_="_30jeq3")
                                        
                                        card_price = price.text

                                product_ulr_container = simple_product_container.find(
                                    "a", class_="_2UzuFa")
                                
                                card_product_url = f"http://flipkart.com{product_ulr_container['href']}"
                                    

                                if product_ulr_container:
                                    image_container = product_ulr_container.find(
                                        "div", class_="_3ywSr_")
                                    if image_container:
                                        inner_image_container = image_container.find(
                                            "div", class_="_312yBx SFzpgZ")
                                        if inner_image_container:
                                            image_url = inner_image_container.find(
                                                "img", class_="_2r_T1I")
                                            
                                            card_image_url = image_url['src']

                        # Append the Flipkart title, price, and image URL to the product list
                        current_product = {
                            'name': card_title,
                            'price': card_price,
                            'image_url': card_image_url,
                            'product_url': card_product_url
                        }
                        product_dict['flipkart'].append(current_product)

                    return product_dict

        else:
            return "No products found on flipkart"

    except Exception as e:
        print(e)


# getting the cheapest product from the  dictionary of scrapped products..
def getCheapestProduct(product_dict):
    cheapest_product = None
    cheapest_price = float('inf')

    # Loop through all the products in the dictionary
    for store_products in product_dict.values():
        for product in store_products:
            # Extract the price value as a float
            price_value = float(
                product['price'].replace(',', '').replace('₹', ''))
            if price_value < cheapest_price:
                # If the current product is cheaper than the current cheapest, update the variables
                cheapest_product = product
                cheapest_price = price_value

    return cheapest_product
