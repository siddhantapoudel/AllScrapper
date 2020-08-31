import scrapy
import json

class OlizStoreSpider(scrapy.Spider):
    name = "oliz_store"
    def start_requests(self):
        url = "https://www.olizstore.com/"
        yield scrapy.Request(url=url, callback=self.homePageParser)

    def homePageParser(self, response):
        cats = response.css("li.level2")
        for cat in cats:
            catUrl = cat.css("a::attr(href)").get()
            yield scrapy.Request(url=catUrl, callback=self.categoryListPageParser)

    def categoryListPageParser(self, response):
        productList = response.css("div.product-item-info")
        for product in productList:
            productURL = product.css("div.product-item-photo a::attr(href)").get()
            tempImage = product.css("div.product-item-photo a img::attr(src)").get()
            productName = product.css("div.details strong.product-item-name a::text").get()
            finalName = productName.strip()
            productPrice = product.css("div.price-final_price span.price-final_price span.price::text").get()
            data = {
                "name":finalName,
                "image":tempImage,
                "price":productPrice,
                "url":productURL
            }
            yield scrapy.Request(url=productURL, callback=self.productDescriptionParser,meta=data)
            

    def productDescriptionParser(self, response):
        description = response.css("div.description div")[0].get()
        with open('./Datas/oliz-store-2020-08-30.json', mode='a') as productsjson:
            data = {
                "name": str(response.meta["name"]),
                "price": response.meta["price"],
                "url": response.meta["url"],
                "CatagoryName": "",
                "image": response.meta["image"],
                "description": description,
                "images": [response.meta["image"]]
            }
            productsjson.write(json.dumps(data))
            productsjson.write("\n")
            productsjson.close()
