from . import parse_all_images
import os

ROOT_PAGE_URL = 'https://car.autohome.com.cn/pic/series-s32040/3170.html'
SAVE_DIR = 'downloads'

if __name__ == '__main__':

    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), SAVE_DIR)

    parse_all_images(ROOT_PAGE_URL, folder)
