from bs4 import BeautifulSoup
import requests
import csv
import time
import pandas as pd

def cleantext(text):
    return text.get_text().strip("\n").replace("\xa0", "").split("\n")

url = "https://w2.brreg.no/kunngjoring/kombisok.jsp?datoFra=01.01.2019&datoTil=02.01.2019&id_region=0&id_niva1=51&id_niva2=56&id_bransje1=0"

body = requests.get(url).content

soup = BeautifulSoup(body, 'html.parser')

myTable = soup.find_all("table", style="border-color: #999999;")
trs = myTable[0].find_all("tr")

# for entry in trs:
#     split = cleantext(entry)
#     print(split)

cleanlist = [cleantext(x) for x in trs]

# print(cleanlist)

strippedlist = [item for item in cleanlist if len(item) == 12]

# print(strippedlist)
relevantFields = [1, 4, 6, 8]
finishedlist = [[row[i] for i in relevantFields] for row in strippedlist]

finishedliststripped = [[element.strip() for element in row] for row in finishedlist]

print(finishedliststripped)
# cleaned = [x.strip("\n").replace("\xa0", "").split("\n") for x in trs]

# print(cleaned)
