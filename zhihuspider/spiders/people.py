# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.shell import inspect_response
from zhihuspider.items import ZhihuspiderItem


class PeopleSpider(scrapy.Spider):
    name = 'people'

    following_url='http://www.zhihu.com/api/v4/members/{}/followees?limit=10&offset=0'
    profile_url='https://www.zhihu.com/api/v4/members/{}?include=allow_message%2Cis_o'\
                'rg%2Cemployments%2Canswer_count%2Cbusiness%2Cfollowing_question_count%'\
                '2Cfavorited_count%2Cfollowing_columns_count%2Cquestion_count%2C'\
                'voteup_count%2Cthanked_count%2Cfollowing_count%2Clocations%2C'\
                'participated_live_count%2Cdescription%2Cfollower_count%2Carticles_count'\
                '%2Cfollowing_topic_count%2Ceducations%2Cgender%5B%3F(type%3Dbest_answerer)%5D.topics'

    scrapied=set()

    def start_requests(self):
        start_url_token='excited-vczh'
        
        yield scrapy.Request(url=self.following_url.format(start_url_token),callback=self.parse_url_token)
    
    def parse_url_token(self,response):
        jsonresponse = json.loads(response.body_as_unicode())
        
        try:
            next=jsonresponse.get('paging',None).get('next',None)
        except:
            next=None
            
        data=jsonresponse.get('data',None)
        if len(data)!=0:
            if next:
                yield scrapy.Request(url=next,callback=self.parse_url_token)
            for dt in data:
                if dt["url_token"] not in self.scrapied:
                    self.scrapied.add(dt["url_token"])
                    yield scrapy.Request(url=self.profile_url.format(dt["url_token"]),callback=self.parse_item)
                    
        


    def parse_item(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        item = ZhihuspiderItem() 
        attributes=["url_token",
                    "name",
                    "headline",
                    "avatar_url",
                    "answer_count",
                    "articles_count",
                    "follower_count",
                    "is_org",
                    "following_count",
                    "gender",
                    "voteup_count",
                    "question_count",
                    "participated_live_count",
                    "thanked_count",
                    "favorited_count",
                    "following_topic_count",
                    "following_question_count",
                    "following_columns_count"]
        for attribute in attributes:
            item[attribute]=jsonresponse.get(attribute,None)

        
        buss=jsonresponse.get("business",None)
        if buss:
            item["business"]=buss.get("name",None)
        else:
            item["business"]=''

        #获取教育信息列表
        ed_list=[]
        educations_list=jsonresponse.get("educations",None)
        if len(educations_list)!=0:
            for education in educations_list:
                try:
                    major=education.get("major",None).get("name",None)
                except:
                    major=''
                try:    
                    school=education.get("school",None).get("name",None)
                except:
                    school=''
                ed_list.append({"school":school,"major":major})
        item["educations"]=ed_list

        #获取就业信息列表
        emp_list=[]
        employments_list=jsonresponse.get("employments",None)
        if len(employments_list)!=0:
            for employment in employments_list:
                try:
                    company=employment.get('company',None).get('name',None)
                except:
                    company=''
                try:
                    job=employment.get('job',None).get('name',None)
                except:
                    job=''
                emp_list.append({"company":company,"job":job})
        item["employments"]=emp_list

        #获取居住地点
        loca_list=[]        
        location_list=jsonresponse.get("locations",None)
        if len(location_list)!=0:
            for location in location_list:
                name=location.get('name',None)
                loca_list.append(name)
        item["locations"]=loca_list

        return item