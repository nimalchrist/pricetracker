# import requests
# from bs4 import BeautifulSoup

# product_name = str(input("Enter: "))
# product_dict = {'amazon': [], 'flipkart': []}
# flipkart_url = f'https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
# flipkart_response = requests.get(flipkart_url)
# if flipkart_response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup for Flipkart
#     flipkart_soup = BeautifulSoup(flipkart_response.content, 'html.parser')

#     # Find all the Flipkart product cards on the page
#     flipkart_product_cards = flipkart_soup.find_all(
#         'div', {'class': '_2kHMtA'})

#     # Loop through each Flipkart product card and extract the title and price for each card
#     for flipkart_product_card in flipkart_product_cards:
#         flipkart_title_element = flipkart_product_card.find(
#             'a', {'class': '_2mylT6'})
#         flipkart_price_element = flipkart_product_card.find(
#             'div', {'class': '_30jeq3 _1_WHN1'})

#         # If the Flipkart title and price elements exist, extract the text
#         if flipkart_title_element and flipkart_price_element:
#             flipkart_title = flipkart_title_element.text.strip()
#             flipkart_currency_symbol = flipkart_price_element.find(
#                 'div', {'class': '_30jeq3'}).text.strip()
#             flipkart_price = flipkart_price_element.find(
#                 'div', {'class': '_30jeq3'}).text.strip()
#             flipkart_image_element = flipkart_product_card.find(
#                 'img', {'class': '_396cs4 _3exPp9'})
#             flipkart_image_url = flipkart_image_element['src'] if flipkart_image_element else ''
#             flipkart_product_url_element = flipkart_product_card.find(
#                 'a', {'class': '_1fQZEK'})
#             flipkart_product_url = flipkart_product_url_element['href']

#             # Add the Flipkart product details to the dictionary
#             current_product = {
#                 'name': flipkart_title,
#                 'price': flipkart_currency_symbol + " " + flipkart_price,
#                 'image_url': flipkart_image_url,
#                 'product_url': "https://www.flipkart.com" + flipkart_product_url
#             }
#             product_dict['flipkart'].append(current_product)

#     print(product_dict)
# else:
#     print("No products found on Flipkart")


import requests
from bs4 import BeautifulSoup

product_name = "watches"
url = f'https://www.flipkart.com/search?q={product_name}'
response = requests.get(url)
flipkart_soup = BeautifulSoup(response.content, 'html.parser')

flipkart_row_elements = flipkart_soup.find_all("div",class_="_1AtVbE col-12-12")

for single_row in flipkart_row_elements:
    inner_row = single_row.find("div", class_="_13oc-S _1t9ceu")
    if inner_row:
        simple_product_container = inner_row.find(
            "div", class_="_1xHGtK _373qXS")
        if simple_product_container:
            price_container = simple_product_container.find("div", class_="_2B099V")
            title = price_container.find("a", class_="IRpwTa")
            print(title.text)
            
            if price_container:
                inner_price = price_container.find("div", class_="_25b18c")
                if inner_price:
                    price = inner_price.find("div", class_="_30jeq3")
                    print(price.text)


            product_ulr_container = simple_product_container.find("a", class_="_2UzuFa")
            print("http://flipkart.com"+product_ulr_container['href'])

            if product_ulr_container:
                image_container = product_ulr_container.find(
                    "div", class_="_3ywSr_")
                if image_container:
                    inner_image_container = image_container.find(
                        "div", class_="_312yBx SFzpgZ")
                    if inner_image_container:
                        image_url = inner_image_container.find(
                            "img", class_="_2r_T1I")
                        print(image_url['src'])

            
        
    




