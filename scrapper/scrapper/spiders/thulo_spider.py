import scrapy
import itertools
import re
f = open("darazdump.txt", "w")


class ThuloSpider(scrapy.Spider):
    name= "thulo"
    """
    def start_requests(self):
        url = "https://thulo.com/categories/"
        yield scrapy.Request(url=url, callback=self.categoryListParser)

    def categoryListParser(self,response):
        lists = response.css("div.ty-column--categories-catalog")
        for list in lists:
            url = list.css("a::attr(href)").get()
            yield scrapy.Request(url="https:"+url+'?ajax=true', callback=self.subCategoryParser)

    def subCategoryParser(self,response):
        sublists = response.css("div.BigOfferHead li")
        for list in links:
            suburl = list.css("a::attr(href)").get()
            categoryName = list.css("a::text").get()
            url = "https://thulo.com"+suburl
            yield scrapy.Request(url=url, callback=self.productListParser, meta={"CategoryName":categoryName,"MainUrl":url})
    """

    def start_requests(self):
        #for link in links:
        #    yield scrapy.Request(url=link, callback=self.categoryListParser)
        links = ["https://thulo.com/rice/"
            ,"https://thulo.com/beaten-rice/"
            ,"https://thulo.com/rice-flour/"
            ,"https://thulo.com/flour/"
            ,"https://thulo.com/bread-crumbs/"
            ,"https://thulo.com/pasta-macaroni/"
            ,"https://thulo.com/wheat/"
            ,"https://thulo.com/vermicelli/"
            ,"https://thulo.com/spaghetti/"
            ,"https://thulo.com/instant-mix/"
            ,"https://thulo.com/baking-powder-leaveners-and-yeasts/"
            ,"https://thulo.com/chips/"
            ,"https://thulo.com/baking-chocolates/"
            ,"https://thulo.com/pudding/"
            ,"https://thulo.com/daal-pulses-and-lentils/"
            ,"https://thulo.com/olive-oil/"
            ,"https://thulo.com/sunflower-oil/"
            ,"https://thulo.com/mustard-oil/"
            ,"https://thulo.com/soybean-oil/"
            ,"https://thulo.com/corn-oil/"
            ,"https://thulo.com/avocado-oil/"
            ,"https://thulo.com/salt/"
            ,"https://thulo.com/seasonings-and-flavors/"
            ,"https://thulo.com/vinegar/"
            ,"https://thulo.com/common-spices/"
            ,"https://thulo.com/sugar/"
            ,"https://thulo.com/sesame-fenugreek/"
            ,"https://thulo.com/fish-and-seafood/"
            ,"https://thulo.com/fresh-meat/"
            ,"https://thulo.com/eggs/"
            ,"https://thulo.com/dry-meat/"
            ,"https://thulo.com/lunch-meat/"
            ,"https://thulo.com/organic-masyaura/"
            ,"https://thulo.com/corn/"
            ,"https://thulo.com/flour-en/"
            ,"https://thulo.com/breakfast-items/"
            ,"https://thulo.com/cereal-porridge-and-muesli/"
            ,"https://thulo.com/jam-jelly-and-marmalade/"
            ,"https://thulo.com/mayonnaise-and-sandwich-spreads/"
            ,"https://thulo.com/tea/"
            ,"https://thulo.com/coffee/"
            ,"https://thulo.com/fruit-juices-and-drinks/"
            ,"https://thulo.com/energy-and-soft-drinks/"
            ,"https://thulo.com/concentrate-syrups/"
            ,"https://thulo.com/soft-drink-mixes/"
            ,"https://thulo.com/digestive-biscuits/"
            ,"https://thulo.com/biscuits-and-rusks/"
            ,"https://thulo.com/cookies/"
            ,"https://thulo.com/crackers/"
            ,"https://thulo.com/cream-biscuits-chocolate-biscuits/"
            ,"https://thulo.com/dry-fruits-nuts-and-seeds/"
            ,"https://thulo.com/chocolates-bars-and-gums/"
            ,"https://thulo.com/salty-snacks/"
            ,"https://thulo.com/chips-prawn-and-papad/"
            ,"https://thulo.com/sweets-mithai-and-rotis/"
            ,"https://thulo.com/health-drinks-and-supplements/"
            ,"https://thulo.com/chia-seeds/"
            ,"https://thulo.com/chyawanprash/"
            ,"https://thulo.com/honey/"
            ,"https://thulo.com/cakes-and-muffins/"
            ,"https://thulo.com/swiss-rolls/"
            ,"https://thulo.com/breads/"
            ,"https://thulo.com/donut/"
            ,"https://thulo.com/syrups/"
            ,"https://thulo.com/sauce-and-ketchup/"
            ,"https://thulo.com/pickles/"
            ,"https://thulo.com/olives/"
            ,"https://thulo.com/canned-fruits-beans-and-vegetables/"
            ,"https://thulo.com/noodles-and-ramen/"
            ,"https://thulo.com/instant-soups/"
            ,"https://thulo.com/popcorn/"
            ,"https://thulo.com/frozen-foods/"
            ,"https://thulo.com/titaura/"
            ,"https://thulo.com/cheese-and-butter/"
            ,"https://thulo.com/ice-cream-and-novelties/"
            ,"https://thulo.com/milk/"
            ,"https://thulo.com/fresh-cream/"
            ,"https://thulo.com/curd/"
            ,"https://thulo.com/chhurpi/"
            ,"https://thulo.com/fresh-vegetable/"
            ,"https://thulo.com/fresh-fruits/"
            ,"https://thulo.com/herbs-and-seasonings/"
            ,"https://thulo.com/organic-fruits-and-vegetables/"
            ,"https://thulo.com/exotic-fruits-and-veggies/"
            ,"https://thulo.com/cuts-and-sprouts/"
            ,"https://thulo.com/liquid-dishwash/"
            ,"https://thulo.com/dishwash-bar/"
            ,"https://thulo.com/dishwash-powder/"
            ,"https://thulo.com/dishwash-scrub-and-brush/"
            ,"https://thulo.com/dishwash-paste/"
            ,"https://thulo.com/detergent-cake/"
            ,"https://thulo.com/detergent-powder/"
            ,"https://thulo.com/fabric-softener/"
            ,"https://thulo.com/laundry-brush/"
            ,"https://thulo.com/brooms-mops-and-dusters/"
            ,"https://thulo.com/liquid-floor-cleaners/"
            ,"https://thulo.com/carpet-shampoo/"
            ,"https://thulo.com/mop-buckets/"
            ,"https://thulo.com/dustpans/"
            ,"https://thulo.com/floor-cleaning-scrub/"
            ,"https://thulo.com/metal-polish/"
            ,"https://thulo.com/liquid-kitchen-cleaner/"
            ,"https://thulo.com/cleaning-sponges/"
            ,"https://thulo.com/kitchen-towels/"
            ,"https://thulo.com/liquid-toilet-cleaners/"
            ,"https://thulo.com/toilet-brushes/"
            ,"https://thulo.com/toilet-cleaning-tablets/"
            ,"https://thulo.com/drain-openers/"
            ,"https://thulo.com/air-freshener-and-airwick/"
            ,"https://thulo.com/glass-cleaner/"
            ,"https://thulo.com/humidifier/"
            ,"https://thulo.com/bathroom-supplies/"
            ,"https://thulo.com/body-wash/"
            ,"https://thulo.com/soaps/"
            ,"https://thulo.com/hand-wash/"
            ,"https://thulo.com/shampoo-and-conditioners/"
            ,"https://thulo.com/shower-gel/"
            ,"https://thulo.com/tissue-paper/"
            ,"https://thulo.com/tooth-brush/"
            ,"https://thulo.com/tooth-paste/"
            ,"https://thulo.com/wet-wipes/"
            ,"https://thulo.com/baby-foods/"
            ,"https://thulo.com/diapers/"
            ,"https://thulo.com/pet-food/"
        ]
        yield scrapy.Request(url=links[0], callback=self.productListParser)

    def productListParser(self,response):
        categoryName = response.css("h1.ty-mainbox-title span::text").get()
        itemsList = response.css("div.ty-column4")
        for item in itemsList:
            imageSoup = item.css("div.ty-grid-list__image")
            tempImage = imageSoup.css("img::attr(src)").get()
            itemURL = imageSoup.css("a::attr(href)").get()
            itemTitle = item.css("a.product-title::text").get()
            priceList = item.css("span.ty-price-num")
            if priceList[1]:
                itemPrice = priceList[1].get()
            data = {
                "name":itemTitle,
                "url":itemURL,
                "price":itemPrice,
                "image":tempImage,
                "category":categoryName
            }
            yield scrapy.Request(url=itemURL, callback=self.productPageParser,meta=data)
        text = response.css("div.ty-pagination a.ty-pagination__next::attr(href)").get()
        if text:
            yield scrapy.Request(url=text, callback=self.productListParser)
        """
        text = response.css("div.ty-pagination a.ty-pagination__next::text").get()
        if text:
            yield scrapy.Request(url=mainUrl, callback=self.paginationListParser, meta={"MainUrl":mainUrl,"pageNo":page})
            tempTotal = re.findall(r'\d+', text)
            pages = tempTotal[1]
        else:
            pages = int(len(response.css("div.ty-pagination div.ty-pagination__items a"))/2)
        if response.url[-1] != '/':
            response.url = response.url+'/'
        else:
            pass
        for page in range(pages):
            page = page+1
            mainUrl = response.url+'page-'+str(page)
        """
        
    def productPageParser(self,response):
        imageList = []
        f.write(str(response.meta["name"])+" \n")
        descriptionsoup = response.css("div#content_description").get()
        imagesSoup = response.css("div.ty-product-bigpicture")
        imageMain = imagesSoup.css("div.ty-product-bigpicture__img")
        images = imageMain.css("a.cm-image-previewer img::attr(src)")
        for image in images:
            imageList.append(image.get())


