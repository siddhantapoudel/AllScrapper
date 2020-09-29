import scrapy
import itertools
import json
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from money_parser import price_str
import requests
driver = webdriver.Firefox()

class DarazSpider(scrapy.Spider):
    name = "daraz"
    def start_requests(self):
        driver.get("https://www.daraz.com.np")
        links = driver.find_elements_by_css_selector('ul.lzd-site-menu-sub li.lzd-site-menu-sub-item')
        for link in links:
            url = link.find_element_by_css_selector("a").get_attribute("href")
            catName = link.find_element_by_css_selector("a span").get_attribute("innerHTML")
            page = requests.get(url+"?ajax=true","html.parser")
            result = json.loads(page.content)
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
                            "category": str(catName),
                            "image": str(tempImage),
                            "description": "",
                            "images": []
                        }
                    yield scrapy.Request(url=str(itemURL), callback=self.productPageParser, meta=data)
            else:
                print("Error:"+ url)
            totalItems = int(result['mainInfo']['totalResults'])
            if totalItems>40:
                totalPage = 0
                if (totalItems % 40)>0:
                    totalPage = int(totalItems/40) + 1
                else:
                    totalPage = int(totalItems/40)
                for page in range(totalPage):
                    actPage = page+1
                    try:
                        driver.get(url+"?page="+str(actPage))
                        datas = driver.find_elements_by_css_selector("div[data-qa-locator='product-item']")
                        for data in datas:
                            tags = data.find_elements_by_tag_name("a")
                            name = tags[1].get_attribute("title")
                            pricetags = data.find_elements_by_tag_name("span")
                            price = price_str(pricetags[0].get_attribute("innerHTML"))
                            produrl = tags[0].get_attribute("href")
                            data = {
                                "name": str(name),
                                "price": int(price),
                                "url": str(produrl),
                                "category": str(catName),
                                "image": "",
                                "description": "",
                                "images": []
                            }
                            yield scrapy.Request(url=str(produrl), callback=self.productPageParser, meta=data)
                    except:
                        print("Error")

    def categoryListParser(self,response):
        links = response.css("ul.lzd-site-menu-sub li.lzd-site-menu-sub-item")
        num = 0
        for link in links:
            if num != 0:
                break
            num = num + 1
            url = link.css("a::attr(href)").get()
            categoryName = link.css("a span::text").get()
            test = link.css("a span::attr(data-spm-anchor-id)").get()
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
                        "category": str(response.meta["catName"]),
                        "image": str(tempImage),
                        "description": "",
                        "images": []
                    }
                yield scrapy.Request(url=str(itemURL), callback=self.productPageParser, meta=data)
        else:
            print("Error:"+ response.meta["mainURL"])
        totalItems = int(result['mainInfo']['totalResults'])
        if totalItems>40:
            totalPage = 0
            if (totalItems % 40)>0:
                totalPage = int(totalItems/40) + 1
            else:
                totalPage = int(totalItems/40)
            for page in range(totalPage):
                actPage = page+1
                try:
                    driver.get(response.meta["mainURL"]+"?page="+str(actPage))
                    datas = driver.find_elements_by_css_selector("div[data-qa-locator='product-item']")
                    for data in datas:
                        tags = data.find_elements_by_tag_name("a")
                        name = tags[1].get_attribute("title")
                        pricetags = data.find_elements_by_tag_name("span")
                        price = price_str(tags[0].get_attribute("innerHTML"))
                        url = tags[0].get_attribute("href")
                        data = {
                            "name": str(name),
                            "price": int(price),
                            "url": str(url),
                            "category": str(response.meta["catName"]),
                            "image": "",
                            "description": "",
                            "images": []
                        }
                        yield scrapy.Request(url=str(url), callback=self.productPageParser, meta=data)
                except:
                    print("Error")
        """
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
                yield scrapy.Request(url=response.url+"?page="+str(actPage)+"&spm=a2a0e.11779170.cate_1.1.287d2d2boKxfpT", callback=self.paginationListParser, meta={"CategoryName":response.meta["CategoryName"],"MainUrl":response.url})
        
        
        """
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
        image = ""
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
                    image = itemjson["data"]["root"]["fields"]["htmlRender"]["msiteShare"]["image"]
                except:
                    pass
                try:
                    descriptionText = itemjson["data"]["root"]["fields"]["product"]["highlights"]
                except:
                    descriptionText = ""
                response.meta["Description"] = descriptionText
        with open('./Datas/daraznew.json', mode='a') as productsjson:
            data = {
                "name": str(response.meta["name"]),
                "price": response.meta["price"],
                "url": response.meta["url"],
                "CatagoryName": response.meta["category"],
                "image": image,
                "description": descriptionText,
                "images": images
            }
            productsjson.write(json.dumps(data))
            productsjson.write("\n")
            productsjson.close()
        