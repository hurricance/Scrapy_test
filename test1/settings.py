BOT_NAME = 'test1'
SPIDER_MODULES = ['test1.spiders']
NEWSPIDER_MODULE = 'test1.spiders'
ITEM_PIPELINES = {'test1.pipelines.NewPipeline': 300, 'test1.pipelines.OldPipeline': 300} #激活管道
COOKIES_ENBALE=False