import json

class NewPipeline(object):
    def open_spider(self, spider):
        try: # 打开json文件
            self.file = open('new-house.json', "w", encoding="utf-8")
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item) # 生成字典对象
        json_str = json.dumps(dict_item, ensure_ascii=False) + "\n" # 生成json串
        self.file.write(json_str) # 将json串写入到文件中
        return item
    
    def close_spider(self, spider):
        self.file.close() # 关闭文件

class OldPipeline(object):
    def open_spider(self, spider):
        try: # 打开json文件
            self.file = open('old-house.json', "w", encoding="utf-8")
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item) # 生成字典对象
        json_str = json.dumps(dict_item, ensure_ascii=False) + "\n" # 生成json串
        self.file.write(json_str) # 将json串写入到文件中
        return item
    
    def close_spider(self, spider):
        self.file.close() # 关闭文件
