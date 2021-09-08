# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from application.models import Stock, db

import sys
sys.path.insert(0, 'fav-stocks/application')
import models


class ScrappersPipeline:
    def __init__(self):
        engine = db.connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        stock = Stock()
        stock.symbol = item['symbol']
        stock.price = item['price']

        try:
            session.add()
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
