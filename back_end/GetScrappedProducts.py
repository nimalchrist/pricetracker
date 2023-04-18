# import requests
# from bs4 import BeautifulSoup


# def getScrappedProducts(product_name):
#     print("callled")
#     product_list = []
#     amazon_url = f"https://app.scrapingbee.com/api/v1/?api_key=J56Q9QBZBHOLMI4DX4I8SHCXJSQ0PON1ADLPE49H3OBR4GSCE0B3G4T2WZTDKJBJCOXF9M3M001V3L0S&url=https://www.amazon.in/s?k={product_name}"

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
#                     # Print the Amazon title and price of the product

#                     # print(
#                     # f"Amazon: {amazon_title} {amazon_price} {amazon_image_url}")

#                     current_product = {
#                         'name': amazon_title,
#                         'price': amazon_price,
#                         'image_url': amazon_image_url
#                     }
#                     product_list.append(current_product)
#                     i += 1

#             return product_list
#         else:
#             return "No product found"

#     except Exception as e:
#         print(e)

import requests
from bs4 import BeautifulSoup


def getScrappedProducts(product_name):
    product_dict = {'amazon': [], 'flipkart': []}

    # Amazon scraping using ScrapingBee API

    try:
        # Send a GET request to the ScrapingBee API endpoint for Amazon
        amazon_url = f"https://app.scrapingbee.com/api/v1/?api_key=4WFKLJBI9ZHLPYJQ38QA4NCSMYYLFFACU3O9YBKKBZ6SU6ZV9CA9BSLKNGQ8I351XZLI1MM3FZ8SF88O&url=https://www.amazon.in/s?k={product_name}"

        amazon_response = requests.get(amazon_url)
        if (amazon_response.status_code == 200):
            # Parse the HTML content using BeautifulSoup for Amazon
            amazon_soup = BeautifulSoup(amazon_response.content, 'html.parser')

            # Find all the Amazon product containers on the page
            amazon_product_containers = amazon_soup.find_all(
                'div', {'class': 's-result-item'})

            # Loop through each Amazon product container and extract the title and price
            i = 0
            for amazon_product in amazon_product_containers:
                amazon_title_element = amazon_product.find(
                    'h2', {'class': 'a-size-mini'})
                amazon_price_element = amazon_product.find(
                    'span', {'class': 'a-price'})
                amazon_image_element = amazon_product.find(
                    'img', {'class': 's-image'})

                # amazon_product.find('a', {'class': 'a-link-normal'})['href']

                # If the Amazon title and price elements exist, extract the text
                if amazon_title_element and amazon_price_element:
                    amazon_title = amazon_title_element.text.strip()
                    amazon_currency_symbol = amazon_price_element.find(
                        'span', {'class': 'a-price-symbol'}).text.strip()
                    amazon_price_value = amazon_price_element.find(
                        'span', {'class': 'a-price-whole'}).text.strip()
                    amazon_price = amazon_currency_symbol+" "+amazon_price_value
                    amazon_image_url = amazon_image_element['src']if amazon_image_element else 'https://rukminim1.flixcart.com/image/312/312/ktketu80/mobile/6/n/d/iphone-13-mlpg3hn-a-apple-original-imag6vpyghayhhrh.jpeg?q=70'

                    # Add the Amazon product details to the dictionary
                    current_product = {
                        'name': amazon_title,
                        'price': amazon_price,
                        'image_url': amazon_image_url,
                        # 'product_url': amazon_product_url
                    }
                    product_dict['amazon'].append(current_product)
                    i += 1

        else:
            return "No product found on Amazon"
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
            flipkart_product_containers = flipkart_soup.find_all(
                'div', {'class': '_2kHMtA'})

            # Loop through each Flipkart product container and extract the title and price
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
                        'img', {'class': '_396cs4 _3exPp9'})
                    flipkart_image_url = flipkart_image_element[
                        'src'] if flipkart_image_element else 'https://t3.ftcdn.net/jpg/04/34/72/82/240_F_434728286_OWQQvAFoXZLdGHlObozsolNeuSxhpr84.jpg'

                    flipkart_url_element = flipkart_product.find(
                        'a', {'class': '_1fQZEK'})['href']

                    # Append the Flipkart title, price, and image URL to the product list
                    current_product = {
                        'name': flipkart_title,
                        'price': flipkart_price,
                        'image_url': flipkart_image_url,
                        'product_url': flipkart_image_element
                    }
                    product_dict['flipkart'].append(current_product)

            return product_dict
        else:
            return "No products found"

    except Exception as e:
        print(e)
