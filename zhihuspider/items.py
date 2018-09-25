# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_token=scrapy.Field()             #用户唯一识别id
    name=scrapy.Field()                     #姓名
    headline=scrapy.Field()                #一句话描述
    avatar_url=scrapy.Field()               #头像url
    answer_count=scrapy.Field()             #回答数 
    articles_count=scrapy.Field()           #文章数
    follower_count=scrapy.Field()           #粉丝数量
    is_org=scrapy.Field()                   #是否是机构账号
    following_count=scrapy.Field()          #关注数目
    gender=scrapy.Field()                   #性别  1男 -1女
    educations=scrapy.Field()               #教育经历     [school ,major]
    employments=scrapy.Field()              #工作经历     [job ,company]
    voteup_count=scrapy.Field()             #被赞同数
    question_count=scrapy.Field()           #提问数
    participated_live_count=scrapy.Field()  #参加的live数量
    locations=scrapy.Field()                #居住地
    thanked_count=scrapy.Field()            #被感谢数
    favorited_count=scrapy.Field()          #被收藏数
    following_topic_count=scrapy.Field()    #关注的话题数目
    following_question_count=scrapy.Field() #关注的问题数目
    following_columns_count=scrapy.Field()  #关注的专栏数目
    business=scrapy.Field()                 #所在行业