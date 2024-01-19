# Hobby project using the BKK GO APIs
Created by István Gy. Zsély, version 0.1

email: [zselyigy@gmail.com](email:zselyigy@gmail.com)

# Aim
This code was created to demonstrate how to build ETL pipelines in Python using
a free API and the AWS infrastucture.

# Project overview
The source of the data is the [BKK FUTÁR Utazástervező API](https://bkkfutar.docs.apiary.io/).



# Development environment
- Python 3.11.6
- Visual Studio Code 1.85.1
- Jupyter notebook extension v2023.11.1100101639
- AWS services: S3, Lambda

# Dependencies
The python code imports the following libraries:
- requests v2.31.0

# Format of the BKK bike rental API response
The structure of the data converted from JSON to Dict:

- "currentTime": time in Unix timestamp format (milliseconds since the Unix Epoch)
- "version": 3,
- "status": "OK",
- "code": 200,
- "text": "OK",
- "data": all the information embedded here

The "data" key contains the following subkeys:

- "list": the detailed information about the bikes and stations
- "outOfRange": false    ?
- "limitExceeded": false ?
- "class": "listWithReferences"  ?

"list" is a list of dictionaries about bikes or bike stations

An example:
```json
        {
            "id": "42711896",
            "lat": 47.51032,
            "lon": 19.028615,
            "name": "Millen\u00e1ris",
            "code": "0213",
            "type": "stele",
            "bikes": 1,
            "spaces": 999,
            "style": {
                "icon": {
                    "name": "vehicle-rental/mol-bubi"
                }
            }
        }
```

Based on the [API documentation](https://bkkfutar.docs.apiary.io/#reference/0/bicyclerental/bicyclerental):

- id (string):    MOL Bubi állomás azonosítója, e.g. 251962
- lat (number):   latitude, e.g. 47.511182000000005
- lon (number):   longitude, e.g. 19.080324700000002
- name(string):   elnevezés, e.g. 'Dózsa György út'
 - code (string):  kód, e.g. '0612' (I guess this is the unique identitier of the station/bike)
- type (enum):    kijelző típusa, e.g. '10inch' or 'character' (these denoted as strings)
- bikes(number):  elérhető kerékpárok száma, e.g. 5
- spaces (number): szabad kerékpár támaszok száma. Ha 0, akkor is elhelyezhető kerékpár az állomáson a "pót" támasznál. e.g. 10 (looks to be 999, not updated)
