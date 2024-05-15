## FUNCTIONALITY
Program that tracks the price of a product in Amazon
sending an email when it reachs a target price

### Libraries needed
requests - Make the HTML request
bs4 - Web scrapping
lxml - Parser with BeautifulSoup method
smtplib - Send email

### Global variables
YOUR EMAIL & PASSWORD (generate it for Python)
TARGET PRICE to decide if the email must be sent
URL_WEBSITE - Product to track
headers - HTTP headers requested

### Step 1: Web Scrapping
Inspect the website to get the price and title
id=productTitle
class_=a-offscreen (sometimes is aok-offscreen)

### Step 2: Send email
smtplib.SMTP
encode("utf-8") - Otherwise it will pop up a fault