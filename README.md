# zhihu_scrapy
基于粉丝链，知乎用户信息爬虫，使用python3 开发
*****

## 准备

+ 一台主机需安装[Redis](https://redis.io/)和[MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

+ 将MongoDB和Redis的ip，密码等配置写入[zhihu_scrapy/zhihuspider/setting.py](https://github.com/xxiaocheng/zhihu_scrapy/blob/master/zhihuspider/settings.py) 中的 `MONGO_URI` ,`MONGO_DATABASE` ,`REDIS_URL`  参数中。

+ 安装依赖

    pip install -r requirements.txt

+ 关于设置随机请求头请[参考](https://github.com/alecxe/scrapy-fake-useragent)


+ 关于ip代理设置请[参考](https://github.com/aivarsk/scrapy-proxies)

## 运行

+ 确认Redis 和MongoDB可以被其他主机访问到
+ 执行爬虫 
    scrapy crawl people 
+ 第一个客户端执行需向Redis插入urls

    redis-cli lpush people:start_urls https://www.zhihu.com/api/v4/members/{url_token}/followees?limit=20&offset=0

+ 更多scrapy-redis 设置[参考](https://scrapy-redis.readthedocs.io/en/stable/)





