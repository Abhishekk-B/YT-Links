from selenium import webdriver
import os, time, csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from website.imagescrapper import imageFolder
import pandas as pd

from selenium.webdriver.chrome.service import Service
# path = "C:\Development\chromedriver"
# s = Service(path)


# chrome_options = webdriver.ChromeOptions()
# # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# channelName = "krish naik"
# url = "https://www.youtube.com/"
# driver = webdriver.Chrome(service=s, options=chrome_options)


def youTubeScrapper(channelName):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    url = "https://www.youtube.com/"
    # driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(url)
    input = driver.find_element(By.NAME, "search_query")
    input.send_keys(channelName)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    subscribersTag = driver.find_element(By.ID, 'subscribers')
    subscribers = subscribersTag.text
    print(subscribers)
    time.sleep(1)
    title = driver.find_element(By.ID, "channel-title").find_element(By.ID, "text")
    title.click()
    print("title clicked")
    time.sleep(2)
    try:
        videotab = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')
        print("videootab try")
    except:
        videotab = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]')
    print("checcc")
    time.sleep(1)
    videotab.click()
    print("videotab clicked")
    time.sleep(2)
    videoList10 = driver.find_elements(By.CSS_SELECTOR, "#dismissible #details h3 a")
    videoTitle = []
    videoLink = []
    subscriber = []
    time.sleep(2)
    views = driver.find_elements(By.CSS_SELECTOR, "#metadata-container #metadata-line span")
    viewList = [view.text for view in views]
    newview = [viewList[i] for i in range(len(viewList)) if i % 2 == 0]
    i = 0
    for video in videoList10:
        if video.text == "":
            pass
        else:
            link = video.get_attribute("href")
            videoLink.append(link)
            videoTitle.append(video.text)
            subscriber.append(subscribers)
        i = i+1
    imagesList = imageFolder(videoLink, channelName)
    zipped = [list(x) for x in zip(videoTitle, videoLink)]
    sr_no = []
    for i in range(len(zipped)):
        k = zipped[i]
        z = k.insert(0, str(i + 1))
        y = k.insert(3, imagesList[i])
        x = k.insert(4, newview[i])
        d = k.insert(5,subscribers)
        sr_no.append(k)
    with open(channelName.lower()+".csv", "w", encoding="utf-8") as dataFile:
        fieldnames = ["Sr_No", "Video Title", "Video Link", "Image Link", "Views", "Subscriber"]
        writer = csv.writer(dataFile)
        writer.writerow(fieldnames)
        for i in range(len(zipped)):
            writer.writerow(sr_no[i])
    driver.quit()
    return videoLink



def file(channel):
    name = channel.lower()
    abc = []
    df = pd.read_csv(name + ".csv")
    titles = df['Video Title'].tolist()
    images = df['Image Link'].tolist()
    links = df['Video Link'].tolist()
    numbers = df['Sr_No'].tolist()
    views = df['Views'].tolist()
    subscriber = df['Subscriber'].tolist()
    abc.append(numbers)
    abc.append(titles)
    abc.append(links)
    abc.append(images)
    abc.append(name)
    abc.append(views)
    abc.append(subscriber)
    return abc


