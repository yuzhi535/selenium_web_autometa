from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from PIL import Image
from io import BytesIO

def take_webdata(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    try:
        wd = webdriver.Chrome(options=options)
        wd.set_window_size(1080, 720)  # Adjust the window size here
        wd.get(url)
        wd.implicitly_wait(5)
        # Get the page title
        page_title = wd.title
        screenshot = wd.get_screenshot_as_png()

    except WebDriverException as e:
        return Image.new('RGB', (1, 1)), page_title
    finally:
        if wd:
            wd.quit()

    return Image.open(BytesIO(screenshot)) , page_title