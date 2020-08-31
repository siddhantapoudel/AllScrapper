import scrapy
import json

class SochekoSpider(scrapy.Spider):
    name = "socheko"
    def start_requests(self):
        url = "https://cdn.storehippo.com/origin/prd/ms/store/sochekonep/cacheEntities/EN/storedata-prd_ms17244_1581593611441.js"
        yield scrapy.Request(url=url, callback=self.homePageParser)

    def homePageParser(self, response):
        catagoriesURLList = []
        content = response.text
        itemjson = json.loads(content[16:-1])
        for headCatagory in itemjson["ms.categories"]:
            catagorylist = headCatagory["children"]
            for catagories in catagorylist:
                if len(catagories["children"]) > 1:
                    for subCatagories in catagories["children"]:
                        catagoriesURLList.append({"Name": subCatagories["name"], "URL": subCatagories["alias"]})
                else:
                    catagoriesURLList.append({"Name": catagories["name"], "URL": catagories["alias"]})

        for catagoriesURL in catagoriesURLList:
            start = 0
            catagoryPageAPI = "https://www.socheko.com/api/1/entity/ms.products?filters=%5B%7B%22field%22:%22categories%22,%22type%22:%22manual%22,%22value%22:%5B%22" + \
                              catagoriesURL["URL"] + "%22%5D,%22operator%22:%22in%22%7D,%7B%22field%22:%22publish%22,%22type%22:%22manual%22,%22value%22:%221%22%7D%5D&limit=40&sort=-created_on&start=" + str(start) + "&total=1"
            yield scrapy.Request(url=catagoryPageAPI, callback=self.noOfPagesParser,meta={"CategoryURL":catagoriesURL["URL"],"CategoryName":catagoriesURL["Name"]})

    def noOfPagesParser(self, response):
        catagoryPageJson = json.loads(response.text)
        totalProducts = catagoryPageJson["paging"]["total"]
        # print(totalProducts)
        if totalProducts > 40:
            noOfPages = int(totalProducts / 40) + 1
            print("No of Pages " + str(noOfPages))
            startPagination = 0
            for page in range(noOfPages):
                catagoryPaginationAPI = "https://www.socheko.com/api/1/entity/ms.products?filters=%5B%7B%22field%22:%22categories%22,%22type%22:%22manual%22,%22value%22:%5B%22" + \
                                        response.meta["CategoryURL"] + "%22%5D,%22operator%22:%22in%22%7D,%7B%22field%22:%22publish%22,%22type%22:%22manual%22,%22value%22:%221%22%7D%5D&limit=40&sort=-created_on&start=" + str(startPagination) + "&total=1"
                startPagination = startPagination + 40
                yield scrapy.Request(url=catagoryPaginationAPI,callback=self.productDetailsParser,meta={"CategoryURL":response.meta["CategoryURL"],"CategoryName":response.meta["CategoryName"]})
        else:
            for item in catagoryPageJson['data']:
                imagesList = []
                tempImage = ""
                descriptionDetails = ""
                itemURL = "https://www.socheko.com/product/" + item["alias"]
                print(item['name'] + " : " + str(item['price']))
                if 'images' in item:
                    for images in item['images']:
                        if 'tempSrc' in images:
                            imagesList.append(images['tempSrc'])
                        else:
                            pass
                    if 'tempSrc' in item['images'][0]:
                        tempImage = item['images'][0]['tempSrc']
                else:
                    tempImage = ""
                if 'description' in item:
                    descriptionDetails = ""
                    descriptionDetails = item['description']
                else:
                    descriptionDetails = "No Description"
                with open('./Datas/socheko-2020-08-31.json', mode='a') as productsjson:
                    data = {
                        "name": item['name'],
                        "price": str(item['price']),
                        "url": itemURL,
                        "CatagoryName": response.meta["CategoryName"],
                        "image": tempImage,
                        "description": descriptionDetails,
                        "images": imagesList
                    }
                    productsjson.write(json.dumps(data))
                    productsjson.write("\n")
                    productsjson.close()


    def productDetailsParser(self,response):
        catagoryPageJson = json.loads(response.text)
        for item in catagoryPageJson['data']:
            imagesList = []
            tempImage = ""
            descriptionDetails = ""
            itemURL = "https://www.socheko.com/product/" + item["alias"]
            print(item['name'] + " : " + str(item['price']))
            if 'images' in item:
                for images in item['images']:
                    if 'tempSrc' in images:
                        imagesList.append(images['tempSrc'])
                    else:
                        pass
                if 'tempSrc' in item['images'][0]:
                    tempImage = item['images'][0]['tempSrc']
            else:
                tempImage = ""
            if 'description' in item:
                descriptionDetails = item['description']
            else:
                descriptionDetails = "No Description"
            with open('./Datas/socheko-2020-08-31.json', mode='a') as productsjson:
                data = {
                    "name": item['name'],
                    "price": str(item['price']),
                    "url": itemURL,
                    "CatagoryName": response.meta["CategoryName"],
                    "image": tempImage,
                    "description": descriptionDetails,
                    "images": imagesList
                }
                productsjson.write(json.dumps(data))
                productsjson.write("\n")
                productsjson.close()