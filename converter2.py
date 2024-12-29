import csv
import json
import jsonlines

data = []

with open('test2.csv', mode ='r')as file:
    csvFile = list(csv.reader(file))

    mainList = csvFile[5:]

    for i in mainList:
        Usluga = {
            "imeUstanove": i[4],
            "pruzatelj":  i[8],
            # specificna usluga?
            "opis": i[16], 
            "namjenjeno": i[20],
            "trosak": i[24],
            "preduvjeti": i[28], 
            "adresa": i[32],
            "lat": i[34],
            "lng": i[36],
            "telefon": i[38], 
            "web": i[40],
            "radnoVrijeme": i[42],

            # ???
            # druga kategorija?
            "kategorija": i[2] 
            }
        
        data.append(Usluga)


with jsonlines.open('data2.jsonl', mode='w') as writer:
    for item in data:
        writer.write(item)


  
