import scrapy
import itertools
import json
import time


class DarazSpider(scrapy.Spider):
    name = "daraz"
    def start_requests(self):
        url = "https://www.daraz.com.np"
        yield scrapy.Request(url=url, callback=self.categoryListParser)

    def categoryListParser(self,response):
        links = response.css("ul.lzd-site-menu-sub li.lzd-site-menu-sub-item")
        for link in links:
            url = link.css("a::attr(href)").get()
            categoryName = link.css("a span::text").get()
            yield scrapy.Request(url="https:"+url+"?ajax=true", callback=self.productListParser, meta={"CategoryName":categoryName,"MainUrl":url})

    def productListParser(self,response):
        result = response.json()
        #parse for result once then move on to pagination if there is any
        if 'mods' in result:
            for items in result['mods']['listItems']:
                itemImages = []
                for thumbs in items['thumbs']:
                    itemImages.append(thumbs['image'])
                # print(itemImages)
                itemURL = "https:"+items['productUrl']
                tempImage = ""
                Price = float(items['price'])
                if 'image' in items:
                    tempImage = items["image"]
                data = {
                        "name": str(items['name']),
                        "price": int(Price),
                        "url": str(itemURL),
                        "category": str(response.meta["CategoryName"]),
                        "image": str(tempImage),
                        "description": "",
                        "images": []
                    }
                yield scrapy.Request(url=str(itemURL), callback=self.productPageParser, meta=data)
        else:
            print("Error:"+ response.url)
        totalItems = int(result['mainInfo']['totalResults'])
        if totalItems>40:
            totalPage = 0
            if (totalItems % 40)>0:
                totalPage = int(totalItems/40) + 1
            else:
                totalPage = int(totalItems/40)
            for page in range(totalPage):
                actPage = page+1
                yield scrapy.Request(url=response.url+"&page="+str(actPage), callback=self.paginationListParser, meta={"CategoryName":response.meta["CategoryName"],"MainUrl":response.url})

    def paginationListParser(self,response):
        result = response.json()
        if 'mods' in result:
            for items in result['mods']['listItems']:
                itemImages = []
                for thumbs in items['thumbs']:
                    itemImages.append(thumbs['image'])
                # print(itemImages)
                itemURL = "https:"+items['productUrl']
                tempImage = ""
                Price = float(items['price'])
                if 'image' in items:
                    tempImage = items["image"]
                data = {
                        "name": str(items['name']),
                        "price": int(Price),
                        "url": str(itemURL),
                        "category": str(response.meta["CategoryName"]),
                        "image": str(tempImage),
                        "description": "",
                        "images": []
                    }
                yield scrapy.Request(url=str(itemURL), callback=self.productPageParser, meta=data)
        else:
            print("Error:"+ response.url)

    def productPageParser(self,response):
        imgjson = response.css("script")
        images = []
        descriptionText = ""
        for itemj in imgjson:
            itemj = itemj.get()
            str2 = int(itemj.find("window.LZD_RETCODE_PAGENAME = 'pdp-pc'"))
            if str2 > 1:
                startStr = int(itemj.find("app.run(")) + 8
                endStr = int(itemj.find("catch(e)")) - 14
                itemjson = json.loads(itemj[startStr:endStr])
                try:
                    if itemjson["data"]["root"]["fields"]["skuGalleries"]["0"]:
                        for imgs in itemjson["data"]["root"]["fields"]["skuGalleries"]["0"]:
                            images.append(imgs["src"])
                        response.meta["Images"] = images
                except:
                    pass
                try:
                    descriptionText = itemjson["data"]["root"]["fields"]["product"]["highlights"]
                except:
                    descriptionText = ""
                response.meta["Description"] = descriptionText
        with open('./Datas/daraz-2020-08-31.json', mode='a') as productsjson:
            data = {
                "name": str(response.meta["name"]),
                "price": response.meta["price"],
                "url": response.meta["url"],
                "CatagoryName": response.meta["category"],
                "image": response.meta["image"],
                "description": descriptionText,
                "images": images
            }
            productsjson.write(json.dumps(data))
            productsjson.write("\n")
            productsjson.close()
        