import requests
from bs4 import BeautifulSoup
import sys

url = "https://www.oxfordlearnersdictionaries.com/us/definition/english/" + sys.argv[1]
urlverb = "https://www.oxfordlearnersdictionaries.com/us/definition/english/" + sys.argv[1] + "_2"
headag = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(url,headers = headag)
soup = BeautifulSoup(response.text,'html.parser')
definition_noun = soup.find('span', class_ = 'def').text

if definition_noun:
    print("Noun: " + definition_noun)
else:
    print("Definition not found")

response_verb = requests.get(urlverb,headers = headag)
soup_verb = BeautifulSoup(response_verb.text,'html.parser')

definition_verb = soup_verb.find('span', class_ = 'def').text

if definition_verb:
    print("Verb: " + definition_verb)


