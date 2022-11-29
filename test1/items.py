import scrapy

class NewHouse(scrapy.Item):
    name = scrapy.Field()
    house_type = scrapy.Field()
    position = scrapy.Field()
    room_type = scrapy.Field()
    area = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()

class OldHouse(scrapy.Item):
    cell_name = scrapy.Field()
    position = scrapy.Field()
    room_type = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()