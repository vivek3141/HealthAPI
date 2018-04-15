from bs4 import BeautifulSoup
import urllib.request, urllib.error
import sqlite3


class Barcode():
    def __init__(self):
        pass

    def barcode(self, barcode):
        try:
            response = urllib.request.urlopen("https://world.openfoodfacts.org/product/" + barcode)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            ing = soup.find(id="ingredients_list").get_text()
        except urllib.error.HTTPError:
            return False
        x = ["PALM OIL","HIGH FRUCTOSE CORN SYRUP","MILK","GINGER","HYDROGENATED","ASPERTAME","SODIUM NITRATE","MSG"]
        li = ""
        for i in x:
            if i in str(ing).upper():
                li = li + " " + i
        st = ""
        if li is "":
            "This item contains " + ing + ", and is a safe product to eat."
        else:
            st = "This item contains " + ing + ", out of which " + str(li) + "is harmful for you."
        return st

