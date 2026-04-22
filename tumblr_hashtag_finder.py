from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ড্রাইভার সেটআপ
driver = webdriver.Chrome()  # ক্রোম ড্রাইভার ব্যবহার করছি

# Tumblr খুলুন
driver.get('https://www.tumblr.com')

# একটু ওয়েট করে নিন (যদি লগ ইন না করেই পোস্টগুলো দেখতে চান)
time.sleep(5)

# পোস্টগুলোর হ্যাশট্যাগ সংগ্রহ করুন
posts = driver.find_elements(By.CSS_SELECTOR, 'a')  # লিঙ্কগুলো ধরছি, তবে তুমি স্পেসিফিক হ্যাশট্যাগ এলিমেন্ট সিলেক্ট করতে পারো
for post in posts[:10]:  # প্রথম ১০টা পোস্ট ধরে নিই
    if '#' in post.text:
        print(post.text)

# শেষে ব্রাউজার বন্ধ করুন
driver.quit()
