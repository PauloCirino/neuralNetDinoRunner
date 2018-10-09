import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from PIL import Image
import io

options = webdriver.ChromeOptions()
options.add_argument('headless')

#driver = webdriver.PhantomJS('phantomjs')
driver = webdriver.Chrome(executable_path="/Users/paulocirino/Downloads/chromedriver")
driver.get("file:///Users/paulocirino/Downloads/t-rex-runner-gh-pages/index.html")

score_element = driver.find_element_by_id('current-score-html')
print('Score = ', score_element.text, '\n')

driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_UP)

frame = driver.find_element_by_class_name("runner-container")
img_base = frame.screenshot_as_base64
img_png = frame.screenshot_as_png

img_pil = Image.open(io.BytesIO(img_png))
img_np = np.array(img_pil)
