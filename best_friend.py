import scrapy

class BestFriendSpider(scrapy.Spider):
    name = "bestfriend_spider"
    url = raw_input("inserisci l'url: ")
    start_urls = [url]
    def parse(self, response):
        css_class = ".correct"
        #clean_res = response.css(xp).xpath("@value").extract() answers as letters a, b, c, d
        clean_res = response.css(css_class).xpath("div/text()").extract() #answers as answer text
        counter = 0
        for unicod in clean_res:
            counter += 1
            #print correct answers
            print "Risposta numero " + str(counter) + ": " + unicod.encode("ascii", "replace")
