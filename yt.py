from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, csv
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



def youTubeScrapper(channelName):
    opt = webdriver.ChromeOptions()
    opt.add_argument(
        '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"')

    opt.add_argument("--start-maximized")
    # opt.add_argument("--headless")
    opt.add_argument("--mute-audio")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--incognito")
    opt.add_argument("--disable-dev-shn-usage")
    opt.add_argument("--disable-gpu")
    opt.page_load_strategy = 'eager'
    driver = webdriver.Chrome(
    chrome_options=opt, executable_path=ChromeDriverManager().install())
    driver.delete_all_cookies()
    url = "https://www.youtube.com/"
    driver.get(url)
    input = driver.find_element(By.NAME, "search_query")
    input.send_keys(channelName)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    title = driver.find_element(By.ID, "channel-title").find_element(By.ID, "text")
    subscribersTag = driver.find_element(By.ID, 'subscribers')
    subscribers = subscribersTag.text
    print(subscribers)
    title.click()
    time.sleep(2)
    videotab = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')
    videotab.click()
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
    zipped = [list(x) for x in zip(videoTitle, videoLink)]
    sr_no = []
    for i in range(len(zipped)):
        k = zipped[i]
        z = k.insert(0, str(i + 1))
        x = k.insert(3, newview[i])
        d = k.insert(4,subscribers)
        sr_no.append(k)

    with open(channelName.lower()+".csv", "w", encoding="utf-8") as dataFile:
        fieldnames = ["Sr_No", "Video Title", "Video Link", "Views", "Subscriber"]
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
    links = df['Video Link'].tolist()
    numbers = df['Sr_No'].tolist()
    views = df['Views'].tolist()
    subscriber = df['Subscriber'].tolist()
    abc.append(numbers)
    abc.append(titles)
    abc.append(links)
    abc.append(name)
    abc.append(views)
    abc.append(subscriber)
    return abc