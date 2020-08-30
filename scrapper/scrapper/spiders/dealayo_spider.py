import scrapy
import json
f = open("darazdump.txt", "w")

class DealAyoSpider(scrapy.Spider):
    name = "dealayo"
    def start_requests(self):
        urls = [
            "https://www.dealayo.com/electronics/mobile-tablet/mobile.html",
            "https://www.dealayo.com/electronics/mobile-tablet/tablets.html",
            "https://www.dealayo.com/electronics/mobile-tablet/wearables-gears.html",
            "https://www.dealayo.com/electronics/mobile-tablet/mobile-tablets-accessories.html",
            "https://www.dealayo.com/electronics/laptops-computers/laptops.html",
            "https://www.dealayo.com/electronics/laptops-computers/desktops.html",
            "https://www.dealayo.com/electronics/laptops-computers/monitors.html",
            "https://www.dealayo.com/electronics/laptops-computers/printers-scanners.html",
            "https://www.dealayo.com/electronics/laptops-computers/network-components.html",
            "https://www.dealayo.com/electronics/laptops-computers/external-hard-drives.html",
            "https://www.dealayo.com/electronics/tv-audio-video/televisions.html",
            "https://www.dealayo.com/electronics/tv-audio-video/home-theater-speakers.html",
            "https://www.dealayo.com/electronics/tv-audio-video/mp3-media-players.html",
            "https://www.dealayo.com/electronics/tv-audio-video/video-players.html",
            "https://www.dealayo.com/electronics/tv-audio-video/projectors.html",
            "https://www.dealayo.com/electronics/tv-audio-video/video-games-consoles.html",
            "https://www.dealayo.com/electronics/camera/digital-camera.html",
            "https://www.dealayo.com/electronics/camera/dslr-camera.html",
            "https://www.dealayo.com/electronics/camera/handy-cam.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/air-conditioner.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/washing-machine-dryer.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/water-geysers.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/inverter-batteries-stabilizers.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/solar-appliances.html"
            "https://www.dealayo.com/home-and-furniture/home-appliances/generators.html",
            "https://www.dealayo.com/electronics/personal-grooming-appliances.html",
            "https://www.dealayo.com/electronics/personal-grooming-appliances/trimmers-shavers.html",
            "https://www.dealayo.com/electronics/personal-grooming-appliances/hair-dryers.html",
            "https://www.dealayo.com/electronics/personal-grooming-appliances/hair-curlers.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/refrigerator-freezer.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/induction-cooker-cooktops.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/electric-kettles.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/water-purifiers.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/juicers-mixers-grinders.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/microwaves-ovens.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/air-fryers-deep-fryers.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/dish-washers.html",
            "https://www.dealayo.com/electronics/office-equipments.html",
            "https://www.dealayo.com/women-fashion/clothing.html",
            "https://www.dealayo.com/women-fashion/clothing/lingerie-sleep-wear.html",
            "https://www.dealayo.com/women-fashion/footwear.html",
            "https://www.dealayo.com/watches-26.html",
            "https://www.dealayo.com/women-fashion/beauty-grooming.html",
            "https://www.dealayo.com/women-fashion/beauty-grooming/make-up.html",
            "https://www.dealayo.com/women-fashion/personal-care-appliances.html",
            "https://www.dealayo.com/women-fashion/personal-care-appliances/hair-straighteners.html",
            "https://www.dealayo.com/women-fashion/personal-care-appliances/hair-dryers.html",
            "https://www.dealayo.com/women-fashion/personal-care-appliances/epilators.html",
            "https://www.dealayo.com/men-fashion.html",
            "https://www.dealayo.com/men-fashion/footwear.html",
            "https://www.dealayo.com/watches-30.html",
            "https://www.dealayo.com/backpacks-16.html",
            "https://www.dealayo.com/men-fashion/personal-care-appliances.html",
            "https://www.dealayo.com/men-fashion/personal-care-appliances/trimmers-shavers.html",
            "https://www.dealayo.com/men-fashion/personal-care-appliances/grooming-kits.html",
            "https://www.dealayo.com/men-fashion/personal-care-appliances/hair-care.html",
            "https://www.dealayo.com/baby-and-kids.html",
            "https://www.dealayo.com/baby-and-kids/toys-and-gaming.html",
            "https://www.dealayo.com/baby-and-kids/baby-care.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/diapers-potty-training.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/diapers-potty-training/baby-diapers.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/diapers-potty-training/potty-seats-chairs.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/feeding-nursing.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/feeding-nursing/bottle-feeding.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/feeding-nursing/mealtime-essentials.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/bath-skin-care.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/bath-skin-care/bathing.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/bath-skin-care/baby-grooming.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/baby-health-safety.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/baby-health-safety/baby-monitors.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/baby-health-safety/medical-care.html",
            "https://www.dealayo.com/baby-and-kids/baby-care/baby-gear-nursery.html",
            "https://www.dealayo.com/baby-and-kids/baby-gifting-sets.html",
            "https://www.dealayo.com/baby-and-kids/baby-maternity-care.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/air-coolers.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/fan.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/steam-dry-iron.html",
            "https://www.dealayo.com/home-and-furniture/home-appliances/vacuum-cleaner.html",
            "https://www.dealayo.com/home-and-furniture/kitchenware.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/chimney.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/coffee-maker.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/toasters-sandwich-maker.html",
            "https://www.dealayo.com/home-and-furniture/kitchen-appliances/rice-cooker-electric-cooker.html",
            "https://www.dealayo.com/health-outdoor/fitness-equipment.html",
            "https://www.dealayo.com/health-outdoor/fitness-equipment/treadmills.html",
            "https://www.dealayo.com/health-outdoor/fitness-equipment/single-multi-station-gym.html",
            "https://www.dealayo.com/health-outdoor/fitness-equipment/press-machine.html",
            "https://www.dealayo.com/health-outdoor/fitness-equipment/exercise-benches.html",
            "https://www.dealayo.com/health-outdoor/fitness-equipment/exercise-bikes.html",
            "https://www.dealayo.com/automobiles-and-accessories.html",
            "https://www.dealayo.com/more/groceries.html",
            "https://www.dealayo.com/more/office-supplies-stationery/office-accessories.html",
        ]
        yield scrapy.Request(url=urls[1], callback=self.productListParser)
        #for url in urls:
        #    yield scrapy.Request(url=url, callback=self.productListParser)

    def productListParser(self,response):
        products = response.css("div.products-grid ul li.product-item")
        if products:
            for product in products:
                url = product.css("h2.product-name a::attr(href)").get()
                name = product.css("h2.product-name a::attr(title)").get()
                price = product.css("span.price::text").get()
                tempImage = product.css("div.amda-product-top img::attr(src)").get()
                yield scrapy.Request(url=url, callback=self.productDescriptionParser,meta={"name":name,"tempImage":tempImage,"price":price,"url":url})
            mainPage = response.css("div.pages ol") 
            nextPage = mainPage.css("li a.next::attr(href)").get()
            if nextPage:
                yield scrapy.Request(url=nextPage, callback=self.productListParser)

    def productDescriptionParser(self,response):
        imageList =response.css("div#viewmore-slider img::attr(data-rsmainimg)").getall()
        descriptionHTML = response.css("div.box-description").get()
        f.write(str(response.meta["name"])+" \n")
        with open('./Datas/dealayo-2020-08-30.json', mode='a') as productsjson:
            data = {
                "name": str(response.meta["name"]),
                "price": response.meta["price"],
                "url": response.meta["url"],
                "CatagoryName": "",
                "image": response.meta["tempImage"],
                "description": descriptionHTML,
                "images": imageList
            }
            productsjson.write(json.dumps(data))
            productsjson.write("\n")
            productsjson.close()
