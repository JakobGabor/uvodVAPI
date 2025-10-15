"""
# slovar (dict), JSON
slovar = {"ključ" : "vrednost", "ključ2" : "vrednost2"}
print(slovar)

# klic ključa
print(slovar["ključ"])

imenik = {"Ažbe" : "031860377", "Bine" : "082346823", "Cene" : "0827345832"}
print(imenik["Cene"])
"""

import requests

baseUrl = "https://api.agify.io?name=Muhammad"
call = requests.get(baseUrl).json()
# print(call) response code
print(f"Muhammad je povprečno star ")
print(call["age"])
print(f"Muhammad je ")
print(call["count"])

