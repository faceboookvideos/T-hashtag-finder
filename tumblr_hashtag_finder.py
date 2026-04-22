from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ড্রাইভার সেট আপ
driver = webdriver.Chrome(ChromeDriverManager().install())

# Tumblr পেজ ওপেন করো (নির্দিষ্ট URL বসাও)
driver.get('https://www.tumblr.com')

# পেজ লোড হতে একটু সময় দাও
time.sleep(5)

# হ্যাশট্যাগ সংগ্রহের জন্য সব পোস্টের লিঙ্ক খুঁজে বের করো
posts = driver.find_elements(By.CSS_SELECTOR, 'a')  # উদাহরণ হিসেবে সব লিঙ্ক ধরছি

for post in posts:
    if '#' in post.text:
        print(post.text)

# সবশেষে ড্রাইভার বন্ধ করো
driver.quit()
