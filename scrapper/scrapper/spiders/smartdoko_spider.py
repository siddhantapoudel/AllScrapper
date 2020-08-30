import scrapy
f = open("darazdump.txt", "w")

class SmartDokoSpider(scrapy.Spider):
    name = "smartdoko"
    def start_requests(self):
        url = "https://smartdoko.com/"
        yield scrapy.Request(url=url, callback=self.homePageParser)

    def homePageParser(self, response):
        categories = response.css("div.ac-sub label a::attr(href)").getall()
        for category in categories:
            yield scrapy.Request(url=category, callback=self.categoryListParser)

    def categoryListParser(self, response):
        items = response.css("div.features_items div.productinfo")
        for item in items:
            name = item.css("p.title a::text").get()
            url = item.css("p.title a::attr(href)").get()
            tempurl = item.css("a")[0]
            tempImg = tempurl.css("img::attr(src)").get()
            price = item.css("h2::text").get()
            data={
                "name":name,
                "url":url,
                "tempImg":tempImg,
                "price":price
            }
            f.write(url+" \n")
            yield scrapy.Request(url = url, callback=self.productDescriptionParser,meta=data)
        paginations = response.css("ul.pagination li")
        for pagination in paginations:
            text = pagination.css("a::text").get()
            if text == "Next":
                pagiUrl = pagination.css("a::attr(href)").get()
                f.write(pagiUrl+" \n")
                yield scrapy.Request(url=pagiUrl, callback=self.categoryListParser)

    def productDescriptionParser(self,response):
        images = response.css("ul.thumbelina li")
        description = response.css("div.tabcontent").get()
        imageList = []
        f.write(str(response.meta["name"])+" \n")
        for image in images:
            tempImgURL = image.css("img::attr(src)").get().replace('/thumb','')
            imageList.append(tempImgURL)

