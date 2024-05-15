from bs4 import BeautifulSoup
import lxml
import smtplib
import requests

URL_website = "https://www.amazon.com/PlayStation%C2%AE5-console-slim-PlayStation-5/dp/B0CL61F39H/ref=sr_1_1?crid=19XIMTFB6RQ6K&dib=eyJ2IjoiMSJ9.AHjTd7ZFe8s8RHzX7QExwDesCneAdSrHHQ5Jj2D66rsaQO5rZeuKtyo8T4A2rvHeQWlsHxm1MKPIVXWfwgMhHouf27P3W94BhXvtSxin0RkrKmTENXKMMTmJh5hs4Emg7_-YeLDuaFHexNiYTlvxZhKr-d5E8fgW-2bqIVfzPV8A0ExVWFzvqPjPFlDd4red-F5L4Dk46tqHm-vU7oiazBDNVPZppCDaIrBUChhXRG4.WjJY7bBFCPBnOgJsq4_MkwtHB6o7CItVpZXmK2DddP0&dib_tag=se&keywords=playstation%2B5&qid=1715785046&sprefix=Plays%2Caps%2C190&sr=8-1&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8,gl;q=0.7"
}
TARGET_PRICE = 500.0
my_email = "EMAIL"
password = "PASSWORD"

response = requests.get(url=URL_website, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").getText().strip()
# Quitamos espaciones iniciales, separamos en espacios y cogemos el primero de los elementos
# Eliminando de la cadena el primer elemento que corresponde al simbolo de moneda [1:]
price = float(price.split(' ')[0][1:])

title = soup.find(class_="a-size-large product-title-word-break").getText().strip()

if price < TARGET_PRICE:
    print(title, price)
    message = f"{title}: {price}$"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{my_email}",
                            msg=f"Amazon Price Tracker\n\n"
                                f"{message}\n"
                                f"{URL_website}".encode("utf-8")
        )

else:
    print(f"Precio del producto ({price}) superior al objetivo de {TARGET_PRICE}")



