import requests
import bs4


'''
This function will save a single image from given url.
'''


def save_single_image(link, filename):
    img = requests.get(url=link)
    if img.status_code != 200:
        raise Exception("Error loading a single image.")
    bytes = img.content
    with open(filename, "wb") as file:
        file.write(bytes)


'''
This function will parse all the car images from given url.
'''


def parse_all_images(root_page_url, folder):
    # 1. Go to the root_page_url
    root_page_url: str = "https://car.autohome.com.cn/pic/series-s32040/3170.html"
    page = requests.get(url=root_page_url)
    # 请求头，模拟浏览器操作
    if page.status_code != 200:
        raise Exception("Error while getting the root page.")

    # 2. Get all the links from "2018" section.
    # TODO: need to extract those links by myself.
    links = []
    soup = bs4.BeautifulSoup(page.text)
    car_model_selector = "div > div.uibox-con-search.js-context > div:nth-child(1) > div.search-pic-right > dl > dd:nth-child(8) > ul > li > a"
    for link in soup.select(car_model_selector):
        # Form each link after getting a result
        link = f'{"/".join(root_page_url.split("/")[:3])}{link.attrs["href"]}'
        links.append(link)
    # Make a directory for the images.
    import os
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 3. Process each car link
    car_model_index = 0
    for link in links:
        car_page = requests.get(url=link)
        if car_page.status_code != 200:
            raise Exception("Error while parsing this car link.")
        soup = bs4.BeautifulSoup(car_page.text)

        # 3.2. Select all the elements by selector "div.column.contentright.fn-visible > div:nth-child(7) > div > div > div.uibox-con > ul > li > a > img"
        car_img_selector = "div.column.contentright.fn-visible > div:nth-child(7) > div > div > div.uibox-con > ul > li > a"
        car_img_list = soup.select(car_img_selector)[:-1]

        # 3.3. Process each of selected images
        car_model_img_index = 0
        for car_img in car_img_list:
            # TODO:find out how to get "src" from <img src="...">
            car_page_link = f'{"/".join(root_page_url.split("/")[:3])}:{car_img.attrs["href"]}'
            car_picture_page = requests.get(car_page_link)
            car_picture_page_soup = bs4.BeautifulSoup(car_picture_page.text)
            car_picture_page_selector = "#img"
            car_img_link = f'https:{car_picture_page_soup.select_one(car_picture_page_selector).attrs["src"]}'
            save_single_image(
                car_img_link, f"{folder}/{car_model_index}-{car_model_img_index}.{car_img_link.split('.')[-1]}")
            car_model_img_index += 1
        car_model_index += 1
