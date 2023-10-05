# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Top250Pipeline:
    def process_item(self, item, spider):
        download_path = os.getcwd() + '/download/'
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        with open(download_path + 'top.csv','a',newline='') as f:
            f_csv = csv.DictWriter(f,['name','score','people','desc'])
            f_csv.writerows([item])
            print('csv成功')
        # print('----------->管道',item)
        return item
