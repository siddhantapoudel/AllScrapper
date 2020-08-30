import scrapy
import itertools
f = open("darazdump.txt", "w")

class SastoDealSpider(scrapy.Spider):
    name = "sastodeal"
    def start_requests(self):
        url = "https://www.sastodeal.com/"
        yield scrapy.Request(url=url, callback=self.categoryListParser)

    def categoryListParser(self,response):
        links = response.css("li.level2 a::attr(href)").getall()
        for link in links:
            yield scrapy.Request(url=link, callback=self.productListParser, meta={"pageNo":1,"totalData":[],"mainURL":link})

    def productListParser(self,response):
        url = response.url
        totalList = []
        mainURL = response.meta["mainURL"]
        pageNo = response.meta["pageNo"]
        pageNo = pageNo + 1
        items = response.css("div.product-item-info")
        for item in items:
            url = item.css("a::attr(href)").get()
            name = item.css("a.product-item-link::text").get()
            price = item.css("span.price-final_price span.price::text").get()
            tempImg = items[0].css("img::attr(src)").get()
            if url == '#':
                break
            data = {
                "url":url,
                "name":name,
                "price":price,
                "tempImg":tempImg
            }
            totalList.append(data)
        if response.meta["totalData"] == totalList:
            pass
        else:
            for list in totalList:
                f.write(str(list["url"])+" \n")
                yield scrapy.Request(url=list["url"], callback=self.productDescriptionParser, meta=list)
            f.write(response.meta["mainURL"]+"?p="+str(pageNo)+" \n")
            yield scrapy.Request(url=response.meta["mainURL"]+"?p="+str(pageNo), callback=self.productPaginationParser, meta={"pageNo":pageNo,"totalData":totalList,"mainURL":response.meta["mainURL"]})

    def productPaginationParser(self,response):
        url = response.url
        paginationTotalList = []
        mainURL = response.meta["mainURL"]
        pagiPageNo = response.meta["pageNo"]
        pagiPageNo = pagiPageNo + 1
        items = response.css("div.product-item-info")
        for item in items:
            url = item.css("a::attr(href)").get()
            name = item.css("a.product-item-link::text").get()
            price = item.css("span.price-final_price span.price::text").get()
            tempImg = items[0].css("img::attr(src)").get()
            if url == '#':
                break
            data = {
                "url":url,
                "name":name,
                "price":price,
                "tempImg":tempImg
            }
            paginationTotalList.append(data)
        if response.meta["totalData"] == paginationTotalList:
            pass
        else:
            for list in paginationTotalList:
                f.write(str(list["url"])+" \n")
                yield scrapy.Request(url=list["url"], callback=self.productDescriptionParser, meta=list)
            f.write(mainURL+"?p="+str(pagiPageNo)+" \n")
            yield scrapy.Request(url=response.meta["mainURL"]+"?p="+str(pagiPageNo), callback=self.productListParser, meta={"pageNo":pagiPageNo,"totalData":paginationTotalList,"mainURL":response.meta["mainURL"]})

    def productDescriptionParser(self,response):
        desc = response.css("div#description").get()
        overview =  response.css("div.value").get()
        description = overview +"<br/><br/>" + desc
        f.write(str(response.meta["name"])+" \n")