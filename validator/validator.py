from pymongo import MongoClient
from money_parser import price_str
import json

def oliz_store_validator():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/oliz-store-2020-08-30.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        price = data["price"]
        strip_price = price_str(price)
        #sastodeal strip_name = data["name"].strip()
        #strip_price = data["price"].replace("\u0930\u0942 ","")
        insertData = {
            "name":data["name"],
            "price":int(float(strip_price)),
            "url":data["url"],
            "category":data["CatagoryName"],
            "image":data["image"],
            "description":data["description"],
            "images":data["images"]
        }
        found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
        if found is None:
           db.latestcol.insert_one(insertData)
        else:
            print("Found "+ insertData["name"])


def socheko():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/sochekonew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        price = data["price"]
        #sastodeal strip_name = data["name"].strip()
        #strip_price = data["price"].replace("\u0930\u0942 ","")
        insertData = {
            "name":data["name"],
            "price":int(float(price)),
            "url":data["url"],
            "category":data["CatagoryName"],
            "image":data["image"],
            "description":data["description"],
            "images":data["images"]
        }
        found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
        if found != {}:
            if insertData["price"]:
                db.latestcol.insert_one(insertData)
            else:
                print("No Price "+ insertData["name"])
        else:
            print("Found "+ insertData["name"])


def smartdoko():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/smartdokonew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        price = data["price"]
        strip_price = price_str(price)
        #sastodeal strip_name = data["name"].strip()
        #strip_price = data["price"].replace("\u0930\u0942 ","")
        insertData = {
            "name":data["name"],
            "price":int(strip_price),
            "url":data["url"],
            "category":data["CatagoryName"],
            "image":data["image"],
            "description":data["description"],
            "images":data["images"]
        }
        found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
        if found !={}:
            if insertData["price"]:
                db.latestcol.insert_one(insertData)
            else:
                print("No Price "+ insertData["name"])
        else:
            print("Found "+ insertData["name"])


def thulo():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/thulonew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        price = data["price"]
        #sastodeal strip_name = data["name"].strip()
        #strip_price = data["price"].replace("\u0930\u0942 ","")
        insertData = {
            "name":data["name"],
            "price":int(float(price)),
            "url":data["url"],
            "category":data["CatagoryName"],
            "image":data["image"],
            "description":data["description"],
            "images":data["images"]
        }
        found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
        if found !={}:
            if insertData["price"]:
                db.latestcol.insert_one(insertData)
            else:
                print("No Price "+ insertData["name"])
        else:
            print("Found "+ insertData["name"])


def sastodeal():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/sastodealnew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        if data['price'] is not None:
            price = data["price"]
            strip_price = price_str(price)
            print(int(float(strip_price)))
            strip_name = data["name"].strip()
            #strip_price = data["price"].replace("\u0930\u0942 ","")
            insertData = {
                "name":strip_name,
                "price":int(float(strip_price)),
                "url":data["url"],
                "category":data["CatagoryName"],
                "image":data["image"],
                "description":data["description"],
                "images":data["images"]
            }
            found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
            if found !={}:
                if insertData["price"]:
                    db.latestcol.insert_one(insertData)
                else:
                    print("No Price "+ insertData["name"])
            else:
                print("Found "+ insertData["name"])


def daraz():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/daraznew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        if data['price'] is not None:
            price = data["price"]
            strip_name = data["name"].strip()
            #strip_price = data["price"].replace("\u0930\u0942 ","")
            insertData = {
                "name":data["name"],
                "price":int(float(price)),
                "url":data["url"],
                "category":data["CatagoryName"],
                "image":data["image"],
                "description":data["description"],
                "images":data["images"]
            }
            found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
            if found !={}:
                if insertData["price"]:
                    db.latestcol.insert_one(insertData)
                else:
                    print("No Price "+ insertData["name"])
            else:
                print("Found "+ insertData["name"])

def okdam():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/okadamnew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        if data['price'] is not None:
            price = data["price"]
            #strip_price = data["price"].replace("\u0930\u0942 ","")
            insertData = {
                "name":data["name"],
                "price":int(float(price)),
                "url":data["url"],
                "category":data["CatagoryName"],
                "image":data["image"],
                "description":data["description"],
                "images":data["images"]
            }
            found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
            if found is None:
                if insertData["price"]:
                    db.latestcol.insert_one(insertData)
                else:
                    print("No Price "+ insertData["name"])
            else:
                print("Found "+ insertData["name"])

def dealayo():
    myclient = MongoClient("mongodb://localhost:27017/")
    db = myclient.scrapper
    file1 = open('../scrapper/Datas/dealayonew.json', 'r') 
    mycol = db.latestcol
    Lines = file1.readlines() 
    for line in Lines:
        data = json.loads(line)
        if data['price'] is not None:
            price = data["price"]
            strip_price = price_str(price)
            print(int(float(strip_price)))
            #strip_price = data["price"].replace("\u0930\u0942 ","")
            insertData = {
                "name":data["name"],
                "price":int(float(strip_price)),
                "url":data["url"],
                "category":data["CatagoryName"],
                "image":data["image"],
                "description":data["description"],
                "images":data["images"]
            }
            found = db.latestcol.find_one({"url":{"$eq":insertData["url"]}})
            if found is None:
                if insertData["price"]:
                    # print("Not Found "+ insertData["name"])
                    db.latestcol.insert_one(insertData)
                else:
                    print("No Price "+ insertData["name"])
            else:
                print("Found "+ insertData["name"])
        
if __name__ == "__main__":
   smartdoko()