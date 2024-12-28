import csv
import json
import jsonlines

data = []

with open('test.csv', mode ='r')as file:
    csvFile = list(csv.reader(file))

    mainList = csvFile[1:]

    for i in mainList:
        Usluga = {
            "imeUstanove": i[0],
            "lat": i[7],
            "lng": i[8],
            "adresa": i[6],
            "telefon": i[9], 
            "web": i[10],
            "preduvjeti": i[5], 
            "radnoVrijeme": i[11],
            "trosak": i[4],
            "namjenjeno": i[3],
            "opis": i[2], 
            "pruzatelj":  i[1],
            "kategorija": i[12] 
            }
        
        data.append(Usluga)


with jsonlines.open('data.jsonl', mode='w') as writer:
    for item in data:
        writer.write(item)


  