import scrapy
import json
f = open("darazdump.txt", "w")

class OkDamSpider(scrapy.Spider):
    name = "okdam"

    def start_requests(self):
        url = "https://www.okdam.com/"
        yield scrapy.Request(url=url, callback=self.homePageParser)

    def homePageParser(self, response):
        # response.css('ul.menu a::attr(href)').getall() To get all the urls
        categoryUrls = response.css('div.megadrop div.grid-col ul li a::attr(href)').getall()
        for urls in categoryUrls:
            yield scrapy.Request(url=urls, callback=self.categoryListPageParser)
        #yield scrapy.Request(url=categoryUrls[1], callback=self.categoryListPageParser)


    def categoryListPageParser(self, response):
        # response.css("div.product-box img::attr(data-src)")[0].getall() for tempimage url
        mainCards = response.css("div.category-list a")
        for mainCard in mainCards:
            prodUrl = mainCard.css("::attr(href)").get()
            tempImage = mainCard.css("div.product-box img::attr(data-src)").get()
            prodName = mainCard.css("div.product_name::text").get().strip()
            priceTemp = mainCard.css("span.og-price::text").get()
            prodPrice = ''.join(filter(str.isdigit, priceTemp))
            data = {
                "name":prodName,
                "image":tempImage,
                "price":prodPrice,
                "url":prodUrl
            }
            yield scrapy.Request(url=prodUrl, callback=self.productPageParser, meta=data)
        paginations = response.css("ul.pagination li")
        for pagination in paginations:
            if pagination.css("a::text").get() == '›':
                url = pagination.css("a::attr(href)").get() # go to that page
                yield scrapy.Request(url=url, callback=self.categoryListPageParser)

    def productPageParser(self,response):
        description = response.css("div#speci01 div ul").get()
        images = response.css("ul#glasscase li")
        brandName = ""
        rating = response.css("div.product-main-rating a span::text").get()[1:-1]
        if response.css("a.brand-display::text").get():
            brandName = response.css("a.brand-display::text").get()
        imageList = []
        for image in images:
            imageUrl = image.css("img::attr(src)").get()
            imageList.append(imageUrl)
        with open('./Datas/okadam-2020-08-30.json', mode='a') as productsjson:
            data = {
                "name": str(response.meta["name"]),
                "price": response.meta["price"],
                "url": response.meta["url"],
                "CatagoryName": "",
                "image": response.meta["image"],
                "description": description,
                "images": imageList
            }
            productsjson.write(json.dumps(data))
            productsjson.write("\n")
            productsjson.close()