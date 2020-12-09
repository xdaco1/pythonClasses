# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib.request    
# import json

binDict = {}
menu = '''
    ************************************************

         Messages crypt/decrypt utf-8 - binary

    ************************************************

    Please choose what you need:

    [e]ncrypt message
    [d]ecrypt message*
    [q]uit and exit

    *If you need to decrypt, please use 16 bit by every character
    
    '''


# def writeDict(jsonObject):
    
#     with open('binDictionary.csv','w') as f:
#         json.dump(jsonObject, f)

def getDictionary():
    print('::: Getting Dictionary ...')
    headers = {
        'User-Agent':'...' #This page doesn't like python User-Agent
    }
    url = 'https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=bin'
    
    table_rows = []
    attrs = []
    chars = []
    
    class TableData:
        vUnicode = ''
        vChar = ''
        vBin = ''
        vName = ''
    
    tabData = TableData()

    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content,'html.parser')
    
    table_container = soup.find_all('table',class_='codetable')

    for item in table_container:
        table_rows = item.find_all('tr')

    for tr in table_rows[1:]:
        row_data = tr.find_all('td')
        map_data = list(map(lambda data: data.text, row_data))

        if map_data[3] != '<control>':
            binDict[map_data[1]] = map_data[2].replace(' ','').zfill(16)

def encryptMessage(message):
    cWord=''
    for char in message:
        cWord += binDict[char]
    
    return cWord

def decryptMessage(message):

    # Revert binDict
    charDict = {}
    dWord = ''
    for key, value in binDict.items():
        charDict[value] = key

    # Decrypt message
    startPos = 0
    endPos = 16
    charItems=16

    while startPos < len(message):
        bin = message[startPos:endPos]
        dWord += charDict[bin]
        startPos += charItems
        endPos += charItems


    return dWord

def run(option):

    if option.lower() == 'e':
        encrypted = encryptMessage(str(input("Write the message to encrypt: ")))
        return encrypted
    elif option.lower() == 'd':
        decrypted = decryptMessage(str(input("Write the encrypted message (16 bit strigs): ")))
        return decrypted


if __name__ == "__main__":
    #getMessage
    getDictionary()

    while True:
        option = str(input(menu))
        if option.lower() == 'd' or option.lower() == 'e':
            print(run(option.lower()))
            break
        elif option.lower() == 'q':
            break
        else:
            print('Warning :: option {} not available. Please try again'.format(option))
            option = str(input(menu))