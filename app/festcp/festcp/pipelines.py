# -*- coding: utf-8 -*-
import psycopg2
from django.core.mail import EmailMessage

from config.settings import DATABASES
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from festalist.models import FestaListKeyword


class FestcpPipeline(object):
    def open_spider(self, spider):
        hostname = DATABASES['default']['HOST']
        username = DATABASES['default']['USER']
        password = DATABASES['default']['PASSWORD']
        database = DATABASES['default']['NAME']
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.conn = self.connection.cursor()

    def close_spider(self, spider):
        self.conn.quit()
        self.connection.quit()

    def process_item(self, item, spider):
        try:
            email_list = []
            keywords = FestaListKeyword.objects.all()
            for keyword in keywords:
                if keyword.keyword in item['title']:
                    email_list += [a.email for a in keyword.user.iterator()]
            email_list = list(set(email_list))

            def Send_Email(users):
                email = EmailMessage(
                    f'festacrawling.xyz에서 보내드립니다.', # 메시지 타이틀
                    f'찜해놓으신 keyword 가 등록되어 메일 발송해드립니다.'
                    f'홈페이지에 들어오셔서 확인 부탁드립니다.',
                    to=users,  # 메시지수신인
                )
                email.send()

            Send_Email(email_list)

        except:
            pass

        try:
            self.conn.execute(
                "insert into festalist_festalist(title, image, host, date, content, apply, tickets, link) values(%s, %s, %s, %s, %s, %s, %s, %s)",
                (item['title'], item['image'], item['host'], item['date'], item['content'], item['apply'],
                 item['tickets'], item['link'],))
        except psycopg2.IntegrityError:
            self.conn.rollback()
        else:
            self.connection.commit()
        return item
