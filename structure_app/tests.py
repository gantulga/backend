from django.test import TestCase
from django.contrib.auth.models import Group, User

from financial_app.models import Currency
from product_app.models import Product_category, Product, Basic_asset, Basic_asset_count, Item_transfer_type
from .models import Division, Client
from structure_app.models import Configuration_value
# Create your tests here.
#!/usr/bin/python
import MySQLdb
import json
import sqlalchemy as db

data = (
	[ 
		{ 
	      "model":"auth.group",
	      "pk":1,
	      "fields":{ 
	         "name":"Захирал",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":2,
	      "fields":{ 
	         "name":"Удирдлага",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":3,
	      "fields":{ 
	         "name":"Менежер",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":4,
	      "fields":{ 
	         "name":"Нярав",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":5,
	      "fields":{ 
	         "name":"Нягтлан",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":6,
	      "fields":{ 
	         "name":"Туслах",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":7,
	      "fields":{ 
	         "name":"Ахлах тогооч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":8,
	      "fields":{ 
	         "name":"Тогооч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":9,
	      "fields":{ 
	         "name":"Туслах тогооч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":10,
	      "fields":{ 
	         "name":"Бэлтгэгч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":11,
	      "fields":{ 
	         "name":"Угаагч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":12,
	      "fields":{ 
	         "name":"Бармен",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":13,
	      "fields":{ 
	         "name":"Зөөгч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":14,
	      "fields":{ 
	         "name":"Ресефшин",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":15,
	      "fields":{ 
	         "name":"Буудлын ресефшин туслах",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":16,
	      "fields":{ 
	         "name":"Үйлчлэгч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":17,
	      "fields":{ 
	         "name":"Үрэгч",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":18,
	      "fields":{ 
	         "name":"Массажист",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":19,
	      "fields":{ 
	         "name":"Угаалгын газрын ажилтан",
	      }
	   },
	   { 
	      "model":"auth.group",
	      "pk":20,
	      "fields":{ 
	         "name":"Аж ахуйн алба",
	      }
	   },
	   { 
	      "model":"auth.user",
	      "pk":1,
	      "fields":{ 
	         "password":"pbkdf2_sha256$180000$mYa91RoOjltY$5wE9z3y3ptuPnhywVsHxqn1Nddi29ha7sMfPftpCFEM=",
	         "last_login":"2020-01-25T09:41:13.302Z",
	         "is_superuser":1,
	         "username":"admin",
	         "first_name":"",
	         "last_name":"",
	         "email":"admin@admin.com",
	         "is_staff":1,
	         "is_active":1,
	         "date_joined":"2020-01-09T09:29:31.293Z",
	         "groups":[ 
	         	1, 2, 3, 4
	         ],
	         "user_permissions":[ 

	         ]
	      }
	   },
	   { 
	      "model":"auth.user",
	      "pk":2,
	      "fields":{ 
	         "password":"pbkdf2_sha256$180000$tPl3pr6gkXlB$HaForOBm4NfikPOi4u3bV2i8ss8tYUUYc9tQNourdn8=",
	         "last_login":"2020-01-05T08:39:38.760Z",
	         "is_superuser":0,
	         "username":"tsaska",
	         "first_name":"Tsaschikher",
	         "last_name":"Erdenebileg",
	         "email":"tsaskac@yahoo.com",
	         "is_staff":1,
	         "is_active":1,
	         "date_joined":"2020-01-05T04:31:35Z",
	         "groups":[ 
	         	2, 3, 4
	         ],
	         "user_permissions":[ 

	         ]
	      }
	   },
	   { 
	      "model":"auth.user",
	      "pk":3,
	      "fields":{ 
	         "password":"pbkdf2_sha256$180000$B2KYpVSCrhRP$fHFI26ameU47LiKZk/OjYXRAQOWNHdwGRcSzUcde1Fo=",
	         "last_login":"2020-01-05T07:34:51.148Z",
	         "is_superuser":0,
	         "username":"hashka",
	         "first_name":"Khas-Erdene",
	         "last_name":"Erdenebileg",
	         "email":"haku_10000@yahoo.com",
	         "is_staff":1,
	         "is_active":1,
	         "date_joined":"2020-01-05T07:02:11Z",
	         "groups":[ 
	         	2, 3, 4
	         ],
	         "user_permissions":[ 

	         ]
	      }
	   },
	   { 
	      "model":"auth.user",
	      "pk":4,
	      "fields":{ 
	         "password":"pbkdf2_sha256$180000$MqYnLtQ2Vkoa$58vbYZP7/KCpf9+lIXlkUstXglqQ2a0/HcnDjL2HOAU=",
	         "last_login":"2020-01-05T07:34:51.148Z",
	         "is_superuser":0,
	         "username":"erdenesoyol",
	         "first_name":"Erdenesoyol",
	         "last_name":"Bal",
	         "email":"erdenesoyol.b@yahoo.com",
	         "is_staff":0,
	         "is_active":1,
	         "date_joined":"2020-01-25T09:58:53Z",
	         "groups":[ 
	         	1
	         ],
	         "user_permissions":[ 

	         ]
	      }
	   },
	   { 
	      "model":"financial_app.currency",
	      "pk":1,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "name":"Төгрөг",
	         "ratio":1,
	         "country":"Mongolia",
	         "created_by":1,
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":1,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Оффис",
	         "description":"Оффис",
	         "users":[ 
	         	1, 2, 3, 4
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":2,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Гал тогоо",
	         "description":"Гал тогоо",
	         "users":[

	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":3,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Зочид буудал",
	         "description":"Зочид буудал",
	         "users":[
	         	
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":4,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Ресторан",
	         "description":"Ресторан",
	         "users":[
	         	
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":5,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Лоунж",
	         "description":"Лоунж",
	         "users":[
	         	
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":6,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Караоке & VIP өрөө",
	         "description":"Караоке & VIP өрөө",
	         "users":[
	         	
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":7,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Саун",
	         "description":"Саун",
	         "users":[
	         	
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.division",
	      "pk":8,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name":"Агуулах",
	         "description":"Агуулах",
	         "users":[
	         	
	         ],
	      }
	   },
	   { 
	      "model":"structure_app.client",
	      "pk":1,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":201,
	         "description":"2 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":2,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":202,
	         "description":"2 ортой хагас LUX өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":3,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":203,
	         "description":"1 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":4,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":204,
	         "description":"1 ортой LUX өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":5,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":205,
	         "description":"2 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":6,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":207,
	         "description":"1 ортой хагас LUX өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":7,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":301,
	         "description":"2 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":8,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":302,
	         "description":"2 ортой хагас LUX өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":9,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":303,
	         "description":"1 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":10,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":304,
	         "description":"1 ортой LUX өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":11,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":305,
	         "description":"2 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":12,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":306,
	         "description":"2 ортой энгийн өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":13,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":307,
	         "description":"1 ортой VIP өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":14,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":308,
	         "description":"1 ортой хагас LUX өрөө",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":15,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":100,
	         "description":"Зочид буудлын ресефшин",
	         "division":3,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":16,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":1,
	         "description":"Лоунж агуулах",
	         "division":8,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":17,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":2,
	         "description":"Зочид буудал агуулах",
	         "division":8,
	      }
	   },
	   {
	      "model":"structure_app.client",
	      "pk":18,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "number":3,
	         "description":"Угаалгын газар агуулах",
	         "division":8,
	      }
	   },
	   {
	      "model":"product_app.product_category",
	      "pk":1,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "parent": 0,
	         "name":"Зочид буудлын өрөө",
	         "description":"Зочид буудлын өрөөг түрээслэх үйлчилгээ.",
	      }
	   },
	   {
	      "model":"product_app.product_category",
	      "pk":2,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "parent": 1,
	         "name":"Зочид буудлын өрөөг хоногоор түрээслэх",
	         "description":"Зочид буудлын өрөөг хоногоор түрээслэх үйлчилгээ.",
	      }
	   },
	   {
	      "model":"product_app.product_category",
	      "pk":3,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "parent": 1,
	         "name":"Зочид буудлын өрөөг цагаар түрээслэх",
	         "description":"Зочид буудлын өрөөг цагаар түрээслэх үйлчилгээ.",
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":1,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "201 өрөө ХОНОГ",
	         "description":"Зочид буудлын 201 тоот өрөөг хоногоор түрээслэх",
	         "cost":105000.00,
	         "client":1,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":2,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "202 өрөө ХОНОГ",
	         "description":"Зочид буудлын 202 тоот өрөөг хоногоор түрээслэх",
	         "cost":130000.00,
	         "client":2,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":3,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "203 өрөө ХОНОГ",
	         "description":"Зочид буудлын 203 тоот өрөөг хоногоор түрээслэх",
	         "cost":89000.00,
	         "client":3,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":4,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "204 өрөө ХОНОГ",
	         "description":"Зочид буудлын 204 тоот өрөөг хоногоор түрээслэх",
	         "cost":150000.00,
	         "client":4,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":5,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "205 өрөө ХОНОГ",
	         "description":"Зочид буудлын 205 тоот өрөөг хоногоор түрээслэх",
	         "cost":105000.00,
	         "client":5,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":6,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "207 өрөө ХОНОГ",
	         "description":"Зочид буудлын 207 тоот өрөөг хоногоор түрээслэх",
	         "cost":120000.00,
	         "client":6,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":7,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "301 өрөө ХОНОГ",
	         "description":"Зочид буудлын 301 тоот өрөөг хоногоор түрээслэх",
	         "cost":105000.00,
	         "client":7,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":8,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "302 өрөө ХОНОГ",
	         "description":"Зочид буудлын 302 тоот өрөөг хоногоор түрээслэх",
	         "cost":130000.00,
	         "client":8,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":9,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "303 өрөө ХОНОГ",
	         "description":"Зочид буудлын 303 тоот өрөөг хоногоор түрээслэх",
	         "cost":89000.00,
	         "client":9,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":10,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "304 өрөө ХОНОГ",
	         "description":"Зочид буудлын 304 тоот өрөөг хоногоор түрээслэх",
	         "cost":150000.00,
	         "client":10,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":11,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "305 өрөө ХОНОГ",
	         "description":"Зочид буудлын 305 тоот өрөөг хоногоор түрээслэх",
	         "cost":105000.00,
	         "client":11,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":12,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "306 өрөө ХОНОГ",
	         "description":"Зочид буудлын 306 тоот өрөөг хоногоор түрээслэх",
	         "cost":105000.00,
	         "client":12,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":13,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "307 өрөө ХОНОГ",
	         "description":"Зочид буудлын 307 тоот өрөөг хоногоор түрээслэх",
	         "cost":250000.00,
	         "client":13,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":14,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "308 өрөө ХОНОГ",
	         "description":"Зочид буудлын 308 тоот өрөөг хоногоор түрээслэх",
	         "cost":120000.00,
	         "client":14,
	         "division":3,
	         "categories": [1, 2],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":15,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "201 өрөө ЦАГ",
	         "description":"Зочид буудлын 201 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":1,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":16,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "202 өрөө ЦАГ",
	         "description":"Зочид буудлын 202 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":2,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":17,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "203 өрөө ЦАГ",
	         "description":"Зочид буудлын 203 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":3,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":18,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "204 өрөө ЦАГ",
	         "description":"Зочид буудлын 204 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":4,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":19,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "205 өрөө ЦАГ",
	         "description":"Зочид буудлын 205 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":5,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":20,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "207 өрөө ЦАГ",
	         "description":"Зочид буудлын 207 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":6,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":21,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "301 өрөө ЦАГ",
	         "description":"Зочид буудлын 301 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":7,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":22,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "302 өрөө ЦАГ",
	         "description":"Зочид буудлын 302 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":8,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":23,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "303 өрөө ЦАГ",
	         "description":"Зочид буудлын 303 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":9,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":24,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "304 өрөө ЦАГ",
	         "description":"Зочид буудлын 304 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":10,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":25,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "305 өрөө ЦАГ",
	         "description":"Зочид буудлын 305 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":11,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":26,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "306 өрөө ЦАГ",
	         "description":"Зочид буудлын 306 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":12,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":27,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "307 өрөө ЦАГ",
	         "description":"Зочид буудлын 307 тоот өрөөг цагаар түрээслэх",
	         "cost":100000.00,
	         "client":13,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   {
	      "model":"product_app.product",
	      "pk":28,
	      "fields":{ 
	         "created_at":"2020-01-05T07:34:51.148Z",
	         "created_by":1,
	         "name": "308 өрөө ЦАГ",
	         "description":"Зочид буудлын 308 тоот өрөөг цагаар түрээслэх",
	         "cost":30000.00,
	         "client":14,
	         "division":3,
	         "categories": [1, 3],
	         "commodities": []
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"3",
	         "created_at":"2020-01-05 08:00:30.239995",
	         "name":"Толин грилл",
	         "description":"Газан грил",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"1",
	         "photo":"asset_images\/image_ybFsVV5.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"4",
	         "created_at":"2020-01-05 08:01:56.105342",
	         "name":"Газан плитка 8 ширэмтэй",
	         "description":"Жижиг 6 том 2",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"2",
	         "photo":"asset_images\/image_BpyPKfL.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"5",
	         "created_at":"2020-01-05 08:04:07.531608",
	         "name":"Хөлдөөгч 53кг",
	         "description":"Цагаан 1.2х0.8",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"3",
	         "photo":"asset_images\/image_GtrVGB8.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"6",
	         "created_at":"2020-01-05 08:05:47.565191",
	         "name":"4 ширэмтэй цахилгаан плитка",
	         "description":"Доороо дуковктой",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"4",
	         "photo":"asset_images\/image_tbQiKBl.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"7",
	         "created_at":"2020-01-05 08:06:59.772582",
	         "name":"Шилэн хаалгатай хөргөгч",
	         "description":"Дээжний хөргөгч",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"5",
	         "photo":"asset_images\/image_V26CztV.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"8",
	         "created_at":"2020-01-05 08:08:30.704694",
	         "name":"Хөргүүртэй бандан ширээ",
	         "description":"Доороо хөргүүртэй ширээ",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"6",
	         "photo":"asset_images\/image_Re1SE0R.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"9",
	         "created_at":"2020-01-05 08:09:46.455592",
	         "name":"Бэлтгэлийн ширээ",
	         "description":"Гүүдэг хаалгатай бэлтгэлийн ширээ",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"7",
	         "photo":"asset_images\/image_HEnAdJU.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"10",
	         "created_at":"2020-01-05 08:10:58.137319",
	         "name":"Ус буцалгагч",
	         "description":"40л",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"8",
	         "photo":"asset_images\/image_MiDY6pH.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"11",
	         "created_at":"2020-01-05 08:12:20.899064",
	         "name":"Гурил будааны сав",
	         "description":"Цагаан 30 кг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"9",
	         "photo":"asset_images\/image_xWoJGrL.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"12",
	         "created_at":"2020-01-05 08:13:26.922632",
	         "name":"Угаалтуур 1 тэй",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"10",
	         "photo":"asset_images\/image_RflTk9e.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"13",
	         "created_at":"2020-01-05 08:14:26.813908",
	         "name":"Богино долгионы зуух",
	         "description":"Цагаан жижиг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"11",
	         "photo":"asset_images\/image_qVKxtEA.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"14",
	         "created_at":"2020-01-05 08:15:20.631605",
	         "name":"Угаалтуур 3 тай",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"12",
	         "photo":"Default"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"15",
	         "created_at":"2020-01-05 08:16:40.491298",
	         "name":"Аяга таваг ариутгагч 2 хаалгатай",
	         "description":"Том 2 хаалгатай",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"13",
	         "photo":"asset_images\/image_t0EGsBt.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"16",
	         "created_at":"2020-01-05 08:17:50.267922",
	         "name":"Аяга таваг ариутгагч жижиг",
	         "description":"Жижиг дээр доороо хаалгатай",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"14",
	         "photo":"asset_images\/image_mFzYwQu.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"17",
	         "created_at":"2020-01-05 08:18:41.503190",
	         "name":"Жигнүүр 12 давхар",
	         "description":"Никель 12 давхар",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"15",
	         "photo":"asset_images\/image_5D3pN2h.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"18",
	         "created_at":"2020-01-05 08:19:34.131339",
	         "name":"Шарх шүүгээ 3 давхартай чулуутай",
	         "description":"Чулуутай шарх шүүгээ",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"16",
	         "photo":"asset_images\/image_fRlXZxy.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"19",
	         "created_at":"2020-01-05 08:20:13.808855",
	         "name":"Махны хөрөө",
	         "description":"Том",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"17",
	         "photo":"asset_images\/image_5rGnVZl.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"20",
	         "created_at":"2020-01-05 08:21:20.409718",
	         "name":"Махны машин",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"18",
	         "photo":"asset_images\/image_3VPan6g.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"21",
	         "created_at":"2020-01-05 08:22:56.141012",
	         "name":"Холигч",
	         "description":"Саарал жижиг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"19",
	         "photo":"asset_images\/image_Lbfmd6d.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"22",
	         "created_at":"2020-01-05 08:23:58.635222",
	         "name":"Угаалтуур 2 той",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"20",
	         "photo":"asset_images\/image_IFwJuef.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"23",
	         "created_at":"2020-01-05 08:24:59.730965",
	         "name":"Модон бандан ширээ",
	         "description":"Модон бандан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"21",
	         "photo":"asset_images\/image_gfAxNPm.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"24",
	         "created_at":"2020-01-05 08:25:43.430602",
	         "name":"Халуун тогоо",
	         "description":"5 л",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"22",
	         "photo":"asset_images\/image_oPxfdoB.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"25",
	         "created_at":"2020-01-05 08:27:04.906803",
	         "name":"Костроль 48см",
	         "description":"Хөнгөн цагаан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"23",
	         "photo":"asset_images\/image_TkQ7VlO.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"26",
	         "created_at":"2020-01-05 08:30:12.021767",
	         "name":"Костроль 5 төрөл",
	         "description":"Хөнгөн цагаан 48см, 42см, 33см, 30см, 24см",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"24",
	         "photo":"asset_images\/image_DbFUlQG.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"27",
	         "created_at":"2020-01-05 08:32:15.010449",
	         "name":"Битүү чанагч 3ш",
	         "description":"Никель 3 ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"25",
	         "photo":"asset_images\/image_l7S4maR.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"28",
	         "created_at":"2020-01-05 08:37:21.002615",
	         "name":"Хар лист",
	         "description":"Овенд",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"26",
	         "photo":"asset_images\/image_CNzbSkc.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"29",
	         "created_at":"2020-01-05 08:41:31.630736",
	         "name":"Хөнгөн цагаан лист",
	         "description":"Өндөр 6ш , нам 6ш нийт 12 ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"12",
	         "created_by_id":"2",
	         "code":"27",
	         "photo":"asset_images\/image_QQdRd20.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"30",
	         "created_at":"2020-01-05 08:42:35.649510",
	         "name":"Жижиг лист овен",
	         "description":"Овенгийн лист",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"28",
	         "photo":"asset_images\/image_VKjO5c9.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"31",
	         "created_at":"2020-01-05 08:44:29.997726",
	         "name":"Жигнүүрийн лист битүү",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"22",
	         "created_by_id":"2",
	         "code":"29",
	         "photo":"asset_images\/image_OD7Sl4d.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"32",
	         "created_at":"2020-01-05 08:46:01.311766",
	         "name":"Жигнүүрийн нүхтэй лист",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"10",
	         "created_by_id":"2",
	         "code":"30",
	         "photo":"asset_images\/image_9tM7r8j.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"33",
	         "created_at":"2020-01-05 08:49:11.883131",
	         "name":"Босоо том лист",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"31",
	         "photo":"asset_images\/image_DNrRkeD.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"34",
	         "created_at":"2020-01-05 08:50:33.140721",
	         "name":"Жүүсний сав",
	         "description":"Буфет",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"32",
	         "photo":"asset_images\/image_LxKXTMK.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"35",
	         "created_at":"2020-01-05 08:51:36.105245",
	         "name":"Шөлний тогоо",
	         "description":"Буфет",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"33",
	         "photo":"asset_images\/image_v3e7gIm.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"36",
	         "created_at":"2020-01-05 08:52:31.257425",
	         "name":"Цайны сав",
	         "description":"Буфет хоолонд гарна",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"34",
	         "photo":"asset_images\/image_BhQX3L2.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"37",
	         "created_at":"2020-01-05 08:53:16.745560",
	         "name":"Халуун сав",
	         "description":"Цайны халуун сав том",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"35",
	         "photo":"asset_images\/image_kUy4CDy.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"38",
	         "created_at":"2020-01-05 08:57:26.269991",
	         "name":"Гоёлын лист",
	         "description":"Шармал бариултай никель лиет",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"36",
	         "photo":"asset_images\/image_SavE6Gw.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"39",
	         "created_at":"2020-01-05 08:59:33.736448",
	         "name":"2-р хоолны буфет",
	         "description":"Буфет хоолонд гарна",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"37",
	         "photo":"asset_images\/image_FmMGAtM.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"40",
	         "created_at":"2020-01-05 09:01:15.701679",
	         "name":"Обши хоолны никель тогоо  24см",
	         "description":"Никель Жижиг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"38",
	         "photo":"asset_images\/image_hqOQrNe.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"41",
	         "created_at":"2020-01-05 09:02:51.588188",
	         "name":"Жин",
	         "description":"Электрон жин",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"39",
	         "photo":"asset_images\/image_MifeNrd.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"42",
	         "created_at":"2020-01-05 09:04:33.771838",
	         "name":"Ганбанз",
	         "description":"2 төрөл",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"12",
	         "created_by_id":"2",
	         "code":"40",
	         "photo":"asset_images\/image_NI1xM8Z.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"43",
	         "created_at":"2020-01-05 09:05:43.886084",
	         "name":"Ганбанзны суурь",
	         "description":"Никель суурь",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"41",
	         "photo":"asset_images\/image_NwZSFVl.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"44",
	         "created_at":"2020-01-05 09:07:24.118655",
	         "name":"Будаа агшаагч",
	         "description":"10л",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"3",
	         "code":"42",
	         "photo":"asset_images\/image_OCJvg5b.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"45",
	         "created_at":"2020-01-05 09:10:22.045806",
	         "name":"Шарсан төмсний сагс",
	         "description":"Төмөр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"12",
	         "created_by_id":"2",
	         "code":"43",
	         "photo":"asset_images\/image_d4l7C0k.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"46",
	         "created_at":"2020-01-05 09:13:14.244960",
	         "name":"Модон хусуур",
	         "description":"Мод",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"44",
	         "photo":"asset_images\/image_jRRoDEw.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"47",
	         "created_at":"2020-01-05 09:17:24.148013",
	         "name":"Шүүрэн шанага",
	         "description":"Их тосны шүүрэн шанага том жижиг дунд",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"45",
	         "photo":"asset_images\/image_NnnrrhO.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"48",
	         "created_at":"2020-01-05 09:18:13.699019",
	         "name":"Цайны шүүр",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"46",
	         "photo":"asset_images\/image_5Skpbdn.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"49",
	         "created_at":"2020-01-05 09:19:09.609156",
	         "name":"Махны алх",
	         "description":"Хөнгөн цагаан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"47",
	         "photo":"asset_images\/image_uHbwZrS.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"50",
	         "created_at":"2020-01-05 09:20:48.495214",
	         "name":"Будааны хусуур",
	         "description":"Цагаан пиавор",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"48",
	         "photo":"asset_images\/image_kYDH4qr.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"51",
	         "created_at":"2020-01-05 09:23:01.299939",
	         "name":"Гриллны хусуур",
	         "description":"Никель том 2ш, дунд 1ш,  битүү жижиг 1ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"4",
	         "created_by_id":"2",
	         "code":"49",
	         "photo":"asset_images\/image_7jNDx5w.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"52",
	         "created_at":"2020-01-05 09:36:20.388673",
	         "name":"Хоолны халбага",
	         "description":"Нүхтэй халбага 2ш, порцны халбага 4 ш, соусны халбага 4, хусуур 2",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"11",
	         "created_by_id":"2",
	         "code":"50",
	         "photo":"asset_images\/image_2K0FPhw.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"53",
	         "created_at":"2020-01-05 09:37:39.411613",
	         "name":"Пиццаны хусуур",
	         "description":"Жижиг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"51",
	         "photo":"asset_images\/image_eW34V0I.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"54",
	         "created_at":"2020-01-05 09:38:20.039602",
	         "name":"Зайрмагны халбага",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"52",
	         "photo":"asset_images\/image_CbmwVv1.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"55",
	         "created_at":"2020-01-05 09:39:17.565977",
	         "name":"Гар миксер",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"53",
	         "photo":"Default"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"56",
	         "created_at":"2020-01-05 09:41:37.308524",
	         "name":"Төмс арилгагч",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"54",
	         "photo":"asset_images\/image_7UgxfB8.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"57",
	         "created_at":"2020-01-05 09:45:15.582391",
	         "name":"Шанага",
	         "description":"3 төрөл том 1.2, дунд 0.8, жижиг 0.6",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"55",
	         "photo":"asset_images\/image_WyRdXwN.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"58",
	         "created_at":"2020-01-05 09:47:20.747870",
	         "name":"Тиорк",
	         "description":"3 төрөл никель, модон, пиавор",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"56",
	         "photo":"asset_images\/image_xdtQnmW.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"59",
	         "created_at":"2020-01-05 09:55:44.784318",
	         "name":"Өндөг хирчэгч",
	         "description":"Төмөр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"57",
	         "photo":"asset_images\/image_PMPh3me.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"60",
	         "created_at":"2020-01-05 09:58:31.956867",
	         "name":"Нүхтэй хавчаар",
	         "description":"Төмөр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"58",
	         "photo":"asset_images\/image_dBDzlDl.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"61",
	         "created_at":"2020-01-05 10:00:13.208757",
	         "name":"Резинтэй хавчаар",
	         "description":"Улаан өнгөтэй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"59",
	         "photo":"asset_images\/image_vKTY0uf.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"62",
	         "created_at":"2020-01-05 10:02:41.641922",
	         "name":"Том төмөр хавчаар",
	         "description":"Төмөр хавчаар хайчин хэлбэртэй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"4",
	         "created_by_id":"2",
	         "code":"60",
	         "photo":"asset_images\/image_bBktMXB.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"63",
	         "created_at":"2020-01-05 10:03:49.125073",
	         "name":"Сармис бяцлагч",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"61",
	         "photo":"asset_images\/image_cbzAZnS.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"64",
	         "created_at":"2020-01-05 10:04:58.251387",
	         "name":"Никель хүнд хоолны халбага",
	         "description":"Том",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"62",
	         "photo":"asset_images\/image_TMC2rPB.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"65",
	         "created_at":"2020-01-05 10:06:55.272565",
	         "name":"Төмөр бөөрөнхий хэв",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"63",
	         "photo":"asset_images\/image_IqYveD2.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"66",
	         "created_at":"2020-01-05 10:09:46.110396",
	         "name":"Модон ганбанз",
	         "description":"Мах нүддэг ганбанз",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"64",
	         "photo":"asset_images\/image_BRLgYua.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"67",
	         "created_at":"2020-01-05 10:11:12.739453",
	         "name":"Никель таг",
	         "description":"Гоелын таг том 1ш, жижиг 1ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"65",
	         "photo":"asset_images\/image_Mo2eHwW.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"68",
	         "created_at":"2020-01-05 10:13:39.295609",
	         "name":"Мензурк",
	         "description":"Пиавор",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"66",
	         "photo":"asset_images\/image_MWz6sM9.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"69",
	         "created_at":"2020-01-05 10:26:06.285134",
	         "name":"Газны гал",
	         "description":"Урт",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"67",
	         "photo":"asset_images\/image_uRHGwyL.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"70",
	         "created_at":"2020-01-05 10:30:00.998397",
	         "name":"Хөнгөн цагаан шанага",
	         "description":"4 төрөл",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"4",
	         "created_by_id":"2",
	         "code":"68",
	         "photo":"asset_images\/image_qhUf4Ee.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"71",
	         "created_at":"2020-01-05 10:43:24.565013",
	         "name":"Хайруулын таваг нам D34",
	         "description":"Намхан диаметр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"69",
	         "photo":"asset_images\/image_qaBnFfN.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"72",
	         "created_at":"2020-01-05 10:45:29.047896",
	         "name":"Хайруулын таваг нам D32",
	         "description":"Намхан хайруулын таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"70",
	         "photo":"asset_images\/image_D24e4Ye.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"73",
	         "created_at":"2020-01-05 10:47:23.476103",
	         "name":"Хайруулын таваг өндөр D28",
	         "description":"Undur tomor",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"71",
	         "photo":"asset_images\/image_yZnD9fT.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"74",
	         "created_at":"2020-01-05 10:48:17.981337",
	         "name":"Хайруулын таваг өндөр D32",
	         "description":"Өндөр хайруулын таваг төмөр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"72",
	         "photo":"asset_images\/image_ydu9mib.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"75",
	         "created_at":"2020-01-05 10:50:26.279204",
	         "name":"Хайруулын таваг хар d32",
	         "description":"Өндөр хар хайруулын таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"73",
	         "photo":"asset_images\/image_iikoN7m.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"76",
	         "created_at":"2020-01-05 10:51:38.863313",
	         "name":"Хайруулын таваг нам D20",
	         "description":"Хайруулын таваг жижиг төмөр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"74",
	         "photo":"asset_images\/image_iPgphXc.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"77",
	         "created_at":"2020-01-05 10:53:06.255814",
	         "name":"Шүүрэн шанага богино иштэй",
	         "description":"Их тосны шүүрэн шанага жижиг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"75",
	         "photo":"asset_images\/image_7Tj8OKW.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"78",
	         "created_at":"2020-01-05 10:54:54.071596",
	         "name":"Хогийн сав",
	         "description":"Пиавор саарал том",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"76",
	         "photo":"asset_images\/image_KgLRMzt.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"79",
	         "created_at":"2020-01-05 11:08:59.896881",
	         "name":"Зуушны хөргүүртэй ширээ",
	         "description":"Хөргүүртэй ширээ",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"77",
	         "photo":"asset_images\/image_xubg6N3.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"80",
	         "created_at":"2020-01-05 11:10:48.287209",
	         "name":"Пиавор төмпөн",
	         "description":"Дунд 4, жижиг 1ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"78",
	         "photo":"asset_images\/image_bCwfUW9.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"81",
	         "created_at":"2020-01-05 11:12:03.401155",
	         "name":"Нүхтэй төмөр төмпөн",
	         "description":"Том 1ш, жижиг 1ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"79",
	         "photo":"asset_images\/image_C6lK14c.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"82",
	         "created_at":"2020-01-05 11:13:39.335209",
	         "name":"Төмөр төмпөн ком",
	         "description":"Жижгээс томруулсан 11 ш",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"11",
	         "created_by_id":"2",
	         "code":"80",
	         "photo":"asset_images\/image_ZMMpHeu.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"83",
	         "created_at":"2020-01-05 11:18:40.059700",
	         "name":"Пиццаны мод",
	         "description":"Бариултай пиццаны мод 28, 22, 20",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"3",
	         "created_by_id":"2",
	         "code":"81",
	         "photo":"asset_images\/image_XF39pAU.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"84",
	         "created_at":"2020-01-05 11:20:43.338729",
	         "name":"Пиццаны дугуй төмөр лист",
	         "description":"Хар пиццаны бөөөний төөр лист",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"82",
	         "photo":"asset_images\/image_Euzc2A2.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"85",
	         "created_at":"2020-01-05 11:22:05.806954",
	         "name":"Пиццаны бариултай лист",
	         "description":"Хар өнгөтэй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"83",
	         "photo":"asset_images\/image_TbhlBCb.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"86",
	         "created_at":"2020-01-05 11:23:37.543233",
	         "name":"Будаа угаадаг шүүрэн шанага",
	         "description":"Никель нүхтэй том шанага",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"84",
	         "photo":"asset_images\/image_hojRq29.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"87",
	         "created_at":"2020-01-05 11:25:01.775455",
	         "name":"Хутганы ком",
	         "description":"Хар иштэй 9 ш хутга",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"9",
	         "created_by_id":"2",
	         "code":"85",
	         "photo":"asset_images\/image_NYcA5zn.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"88",
	         "created_at":"2020-01-05 11:25:49.699363",
	         "name":"Заазуур",
	         "description":"Том бор иштэй заазуур",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"86",
	         "photo":"asset_images\/image_4IInieL.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"89",
	         "created_at":"2020-01-05 11:27:26.411128",
	         "name":"Амтлагчны сав 5 тай",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"87",
	         "photo":"asset_images\/image_c2u9Ulb.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"90",
	         "created_at":"2020-01-05 11:28:52.305244",
	         "name":"Амтлагчны сав том 6 тай",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"88",
	         "photo":"asset_images\/image_oI7zEna.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"91",
	         "created_at":"2020-01-05 11:29:47.708682",
	         "name":"Тосны багс",
	         "description":"",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"89",
	         "photo":"asset_images\/image_Vzs94y3.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"92",
	         "created_at":"2020-01-05 11:30:41.485848",
	         "name":"Хананы цаг",
	         "description":"Дугуй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"90",
	         "photo":"asset_images\/image_haVoALA.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"93",
	         "created_at":"2020-01-05 11:31:50.533812",
	         "name":"Хогийн шүүр",
	         "description":"Усан цэнхэр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"91",
	         "photo":"asset_images\/image_dkxZQVA.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"94",
	         "created_at":"2020-01-05 11:32:29.055873",
	         "name":"Илдүүр",
	         "description":"Модон",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"92",
	         "photo":"asset_images\/image_Z55ZqBf.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"95",
	         "created_at":"2020-01-05 11:39:13.212133",
	         "name":"Обши хоолны хар тогоо",
	         "description":"Хар цуйвангийн тогоо",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"93",
	         "photo":"asset_images\/image_ZTRKWVz.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"96",
	         "created_at":"2020-01-05 11:41:09.673290",
	         "name":"Цайны данх",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"94",
	         "photo":"asset_images\/image_ezkb20r.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"97",
	         "created_at":"2020-01-05 11:42:43.103269",
	         "name":"Пицца зүсэгч",
	         "description":"Хар бариултай",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"3",
	         "code":"95",
	         "photo":"asset_images\/image_0PAINp7.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"98",
	         "created_at":"2020-01-05 11:44:36.310169",
	         "name":"Өлгүүр",
	         "description":"Төмөр өлгүүр",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"8",
	         "created_by_id":"2",
	         "code":"96",
	         "photo":"asset_images\/image_DhG1jgo.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"99",
	         "created_at":"2020-01-05 11:45:59.831577",
	         "name":"Агааржуулагч",
	         "description":"Никель том",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"97",
	         "photo":"asset_images\/image_WpKqTmv.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"100",
	         "created_at":"2020-01-05 11:48:56.865999",
	         "name":"Мензурк том",
	         "description":"Том жижиг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"3",
	         "code":"98",
	         "photo":"asset_images\/image_FKTAGAG.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"101",
	         "created_at":"2020-01-05 12:47:57.529129",
	         "name":"Суурь таваг",
	         "description":"Том шаазан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"9",
	         "created_by_id":"2",
	         "code":"99",
	         "photo":"asset_images\/image_t7T21m5.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"102",
	         "created_at":"2020-01-05 12:50:19.130842",
	         "name":"Ембүүн таваг",
	         "description":"Шаазан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"9",
	         "created_by_id":"2",
	         "code":"100",
	         "photo":"asset_images\/image_RdMI798.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"103",
	         "created_at":"2020-01-05 12:56:29.422229",
	         "name":"Хуурганы иржгэр таваг",
	         "description":"Шаазан иржгэр ирмэгтэй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"47",
	         "created_by_id":"2",
	         "code":"101",
	         "photo":"asset_images\/image_2ZIWuUe.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"104",
	         "created_at":"2020-01-05 12:58:45.797795",
	         "name":"Шөлний аяга жижиг",
	         "description":"Хуургатай тавганд дагалдах шөлний аяга",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"18",
	         "created_by_id":"2",
	         "code":"102",
	         "photo":"asset_images\/image_dXjIhVa.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"105",
	         "created_at":"2020-01-05 13:04:40.222573",
	         "name":"Обши хоолны таваг d12",
	         "description":"Тасалгаатай обши хоолны пиавор таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"10",
	         "created_by_id":"2",
	         "code":"103",
	         "photo":"asset_images\/image_WorHEdc.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"106",
	         "created_at":"2020-01-05 13:06:46.037572",
	         "name":"Обши хоолны таваг D14",
	         "description":"Обши хоолны тасалгаатай пиавор таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"10",
	         "created_by_id":"2",
	         "code":"104",
	         "photo":"asset_images\/image_Oknl970.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"107",
	         "created_at":"2020-01-05 13:08:17.139092",
	         "name":"Обши хоолны таваг d16",
	         "description":"Обши хоолны тасалгаатай пиавор таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"10",
	         "created_by_id":"2",
	         "code":"105",
	         "photo":"asset_images\/image_bMp6uXL.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"108",
	         "created_at":"2020-01-05 13:09:28.802061",
	         "name":"Махны цуглуулганы зуйван таваг",
	         "description":"Цагаан пиавор таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"106",
	         "photo":"asset_images\/image_Cwy6owA.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"109",
	         "created_at":"2020-01-05 13:10:29.519936",
	         "name":"Нүхтэй дугуй хуурганы таваг",
	         "description":"Пиавор дугуй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"107",
	         "photo":"asset_images\/image_4X8YCee.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"110",
	         "created_at":"2020-01-05 13:15:48.799068",
	         "name":"Сэт хоолны ширмэн таваг",
	         "description":"3 цагаан жижиг тавагтай дөрвөлжин ширэмтэй",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"21",
	         "created_by_id":"2",
	         "code":"108",
	         "photo":"asset_images\/image_lNDmc0k.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"111",
	         "created_at":"2020-01-05 13:17:29.058104",
	         "name":"Жижиг хачирны таваг",
	         "description":"Цагаан таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"30",
	         "created_by_id":"2",
	         "code":"109",
	         "photo":"asset_images\/image_u6x6NxS.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"112",
	         "created_at":"2020-01-05 13:20:29.463304",
	         "name":"Зуйван ширэм суурьтай",
	         "description":"Доороо модон суурьтай ширмэн таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"110",
	         "photo":"asset_images\/image_XeLQz4e.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"113",
	         "created_at":"2020-01-05 13:21:12.942589",
	         "name":"Обши шөлтэй хоолны халбага",
	         "description":"Никель",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"10",
	         "created_by_id":"2",
	         "code":"111",
	         "photo":"asset_images\/image_37cLCjg.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"114",
	         "created_at":"2020-01-05 13:22:33.353385",
	         "name":"Бариултай зууван том ширэм суурьтай",
	         "description":"Бариултай зууван том ширэм суурьтай",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"112",
	         "photo":"asset_images\/image_Hr6elJN.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"115",
	         "created_at":"2020-01-05 13:23:35.604585",
	         "name":"Бариултай зууван дундаж ширэм суурьтай",
	         "description":"Бариултай зууван дундаж  ширэм суурьтай",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"113",
	         "photo":"asset_images\/image_N4R8yE6.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"116",
	         "created_at":"2020-01-05 13:25:44.078337",
	         "name":"Хайруулын таваг хэлбэртэй ширэм суурьтай",
	         "description":"Хайруулын таваг хэлбэртэй ширэм",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"114",
	         "photo":"asset_images\/image_A13kFwG.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"117",
	         "created_at":"2020-01-05 13:28:00.435714",
	         "name":"Обши хоолны модон таваг 20 см",
	         "description":"",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"4",
	         "created_by_id":"2",
	         "code":"115",
	         "photo":"asset_images\/image_SqwAmqk.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"118",
	         "created_at":"2020-01-05 13:29:00.111544",
	         "name":"Обши хоолны модон таваг 30см",
	         "description":"",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"116",
	         "photo":"asset_images\/image_j5sQObx.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"119",
	         "created_at":"2020-01-05 13:29:52.973317",
	         "name":"Обши хоолны модон таваг 50 см",
	         "description":"",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"117",
	         "photo":"asset_images\/image_i3mLcuN.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"120",
	         "created_at":"2020-01-05 13:30:45.341623",
	         "name":"Зураастай модон таваг 70",
	         "description":"",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"6",
	         "created_by_id":"2",
	         "code":"118",
	         "photo":"asset_images\/image_kuIVDVK.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"121",
	         "created_at":"2020-01-05 13:32:45.183974",
	         "name":"Хясаан таваг хачирных жижиг",
	         "description":"Шаазан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"50",
	         "created_by_id":"2",
	         "code":"119",
	         "photo":"asset_images\/image_IgVPa6x.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"122",
	         "created_at":"2020-01-05 13:34:52.032051",
	         "name":"Зутан шөлний чихтэй аяга",
	         "description":"Шаазан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"21",
	         "created_by_id":"2",
	         "code":"120",
	         "photo":"asset_images\/image_e9CzMor.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"123",
	         "created_at":"2020-01-05 13:36:58.693141",
	         "name":"Цайны сэнжтэй аяга",
	         "description":"Шаазан сэнжтэй аяга",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"80",
	         "created_by_id":"2",
	         "code":"121",
	         "photo":"asset_images\/image_L9qsbpG.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"124",
	         "created_at":"2020-01-05 13:39:03.189057",
	         "name":"Удвал цэцгэн таваг жижиг d10",
	         "description":"Шаазан иржгэр хээтэй зууш салатны таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"45",
	         "created_by_id":"2",
	         "code":"122",
	         "photo":"asset_images\/image_BceMrBy.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"125",
	         "created_at":"2020-01-05 13:41:05.891394",
	         "name":"Удвал цэцгэн таваг d14",
	         "description":"Цагаан шаазан иржгэр хээтэй хоолны таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"43",
	         "created_by_id":"2",
	         "code":"123",
	         "photo":"asset_images\/image_JsnZzN8.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"126",
	         "created_at":"2020-01-05 13:41:48.768629",
	         "name":"Хясаан таваг том хоолны",
	         "description":"Шаазан зузаан хясаан таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"124",
	         "photo":"asset_images\/image_JA5MxHx.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"127",
	         "created_at":"2020-01-05 13:49:59.859463",
	         "name":"Обши хоолны никель тогоо 26см",
	         "description":"Никель тогоо",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"125",
	         "photo":"asset_images\/image_eddx31F.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"128",
	         "created_at":"2020-01-05 13:50:48.589326",
	         "name":"Обши хоолны никель тогоо 28см",
	         "description":"Никель тогоо",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"5",
	         "created_by_id":"2",
	         "code":"126",
	         "photo":"asset_images\/image_i5XC8RF.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"129",
	         "created_at":"2020-01-05 13:56:27.378127",
	         "name":"Пиавор сандал",
	         "description":"Угсардаг сандал",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"2",
	         "created_by_id":"2",
	         "code":"127",
	         "photo":"asset_images\/image_Oa7aUA3.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"130",
	         "created_at":"2020-01-05 13:57:29.337340",
	         "name":"Хутга ирлэгч",
	         "description":"Улаан",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"1",
	         "created_by_id":"2",
	         "code":"128",
	         "photo":"asset_images\/image_IpiY8B8.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"131",
	         "created_at":"2020-01-05 13:57:29.337340",
	         "name":"Дөрвөлжин пял таваг 30х30",
	         "description":"Дөрвөлжин пял таваг 30х30",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"50",
	         "created_by_id":"2",
	         "code":"130",
	         "photo":"asset_images\/image_IpiY8B8.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"132",
	         "created_at":"2020-01-05 13:57:29.337340",
	         "name":"Шөлний аяга",
	         "description":"Шөлний аяга",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"100",
	         "created_by_id":"2",
	         "code":"131",
	         "photo":"asset_images\/image_IpiY8B8.jpg"
	      }
	   },
	   { 
	      "model":"product_app.basic_asset",
	      "fields":{ 
	         "id":"1",
	         "created_at":"2020-01-06 06:24:08.166266",
	         "name":"Дөрвөлжин пял таваг 30х30",
	         "description":"Цагаан шаазан иржгэртэй таваг",
	         "realprice":"0",
	         "risedprice":"0",
	         "count":"24",
	         "created_by_id":"2",
	         "code":"129",
	         "photo":"asset_images\/image_fyAS3Xd.jpg"
	      }
	   },
	   { 
	      "model":"structure_app.configuration_value",
	      "fields":{ 
	         "id":"1",
	         "program_name":"Tesoro Center PRO",
	         "program_description":"Гүн Арвижих Эрдэнэс ХХК-ий Тэсоро төвийн үйл ажиллагаанд ашиглагдах үйлчилгээний болон санхүүгийн програм. Энэхүү програм нь тухайн компаний өмч бөгөөд хуулбарлан ашиглахыг хориглоно!",
	         "program_favicon_url":"dist/default/favicon.ico",
	         "program_logo_url":"dist/default/logo.png",
	         "noat_tax":"10",
	         "capital_city_tax":"0",
	      }
	   },
	   { 
	      "model":"product_app.item_transfer_type",
	      "fields":{ 
	         "id":"1",
	         "name":"Худалдан авалт",
	         "description":"Дэлгүүрээс шинээр худалдан авсан түүхий эд.",
	      }
	   },
	   { 
	      "model":"product_app.item_transfer_type",
	      "fields":{ 
	         "id":"2",
	         "name":"Шилжүүлэх",
	         "description":"Түүхий эд газар хооронд шилжүүлэх, хувиарлаж олгосон.",
	      }
	   },
	   { 
	      "model":"product_app.item_transfer_type",
	      "fields":{ 
	         "id":"3",
	         "name":"Борлуулалт",
	         "description":"Үйлчлүүлэгчдэд зарж борлуулсан",
	      }
	   },
	   { 
	      "model":"product_app.item_transfer_type",
	      "fields":{ 
	         "id":"4",
	         "name":"Бүтээгдэхүүнд зарцуулсан",
	         "description":"Үйлчлүүлэгчдэд зарж борлуулсан",
	      }
	   },
	   { 
	      "model":"product_app.item_transfer_type",
	      "fields":{ 
	         "id":"5",
	         "name":"Хэрэгцээнд",
	         "description":"Үйлчлэгчдийн хэрэгцээнд гэх мэт ажилчдын хэрэгцээнд олгосон",
	      }
	   }
	])

engine = db.create_engine('mysql+mysqldb://root:@localhost:3306/tesoro_mn?charset=utf8&use_unicode=0')
connection = engine.connect()
metadata = db.MetaData()

data = json.dumps(data)
python_list = json.loads(data)

for python_obj in python_list:

	if str(python_obj['model']) == "auth.user":
		tableName = "auth_user"
		modelName = "User"
	elif str(python_obj['model']) == "auth.group":
		tableName = "auth_user_groups"
		modelName = "Group"
	elif str(python_obj['model']) == "financial_app.currency":
		tableName = "financial_app_currency"
		modelName = "Currency"
	elif str(python_obj['model']) == "structure_app.division":
		tableName = "structure_app_division"
		modelName = "Division"
	elif str(python_obj['model']) == "structure_app.client":
		tableName = "structure_app_client"
		modelName = "Client"
	elif str(python_obj['model']) == "product_app.product_category":
		tableName = "product_app_product_category"
		modelName = "Product_category"
	elif str(python_obj['model']) == "product_app.product":
		tableName = "product_app_product"
		modelName = "Product"
	elif str(python_obj['model']) == "product_app.basic_asset":
		tableName = "product_app_basic_asset"
		modelName = "Basic_asset"
		python_obj['pk'] = python_obj['fields']['id']
	elif str(python_obj['model']) == "structure_app.configuration_value":
		tableName = "structure_app_configuration_value"
		modelName = "Configuration_value"
		python_obj['pk'] = python_obj['fields']['id']
	elif str(python_obj['model']) == "product_app.item_transfer_type":
		tableName = "product_app_item_transfer_type"
		modelName = "Item_transfer_type"
		python_obj['pk'] = python_obj['fields']['id']

	query = """SELECT * FROM """ + tableName + """ WHERE ID=""" + str(python_obj['pk'])
	checkrow = connection.execute(query).fetchone()
	if checkrow:
		print("Data baina.")
	else:
		if modelName == "User":
			dbitem = User()
			for k, v in python_obj['fields'].items():
				if str(v.__class__) == "<class 'list'>":
					pass
				else:
					setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved user")

		elif modelName == "Group":
			dbitem = Group()
			for k, v in python_obj['fields'].items():
				setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved group")

		elif modelName == "Currency":
			dbitem = Currency()
			for k, v in python_obj['fields'].items():
				if str(k) == "created_by":
					getObject = User.objects.get(pk=int(v))
					setattr(dbitem, k, getObject)
				else:
					setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved currency")

		elif modelName == "Client":
			dbitem = Client()
			for k, v in python_obj['fields'].items():
				if str(k) == "created_by":
					getObject = User.objects.get(pk=int(v))
					setattr(dbitem, k, getObject)
				elif str(k) == "division":
					getObject1 = Division.objects.get(pk=int(v))
					setattr(dbitem, k, getObject1)
				else:
					setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved client")

		elif modelName == "Division":
			dbitem = Division()
			for k, v in python_obj['fields'].items():
				if str(v.__class__) == "<class 'list'>":
					pass
				else:
					if str(k) == "created_by":
						getObject = User.objects.get(pk=int(v))
						setattr(dbitem, k, getObject)
					else:
						setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved division")

		elif modelName == "Product_category":
			dbitem = Product_category()
			for k, v in python_obj['fields'].items():
				if str(k) == "created_by":
					getObject = User.objects.get(pk=int(v))
					setattr(dbitem, k, getObject)
				elif str(k) == "parent":
					if v != 0:
						getObject1 = Product_category.objects.get(pk=int(v))
						setattr(dbitem, k, getObject1)
					else:
						pass
				else:
					setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved product category.")

		elif modelName == "Product":
			dbitem = Product()
			for k, v in python_obj['fields'].items():
				if str(v.__class__) == "<class 'list'>":
					pass
				else:
					if str(k) == "created_by":
						getObject = User.objects.get(pk=int(v))
						setattr(dbitem, k, getObject)
					elif str(k) == "client":
						getObject1 = Client.objects.get(pk=int(v))
						setattr(dbitem, k, getObject1)
					else:
						setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved product.")

		elif modelName == "Basic_asset":
			dbitem = Basic_asset()
			for k, v in python_obj['fields'].items():
				if str(v.__class__) == "<class 'list'>":
					pass
				else:
					if str(k) == "created_by":
						getObject = User.objects.get(pk=int(v))
						setattr(dbitem, k, getObject)
					elif str(k) == "count":
						quantity_balance = v
						pass
					else:
						setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.real_price = 0
			dbitem.rised_price = 0
			divisionObj = Division.objects.get(pk=2)
			dbitem.division = divisionObj
			tsaska = User.objects.get(pk=2)
			dbitem.updated_by = tsaska
			dbitem.save()
			print("Saved product.")
			dbitemo2m = Basic_asset_count.objects.create(created_at="2020-01-06 07:40:06.799933",
														updated_at="2020-01-06 07:40:06.799933",
														counted_day="2020-01-06",
														prev_quantity=0,
														quantity_balance=quantity_balance,
														quantity_increased=quantity_balance,
														quantity_deducted=0,
														controll_confirmed=False,
														basic_asset=dbitem,
														counted_by=tsaska,
														created_by=tsaska,
														updated_by=tsaska)
			print("Saved count of product.")

		elif modelName == "Configuration_value":
			dbitem = Configuration_value()
			for k, v in python_obj['fields'].items():
				setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			dbitem.save()
			print("Saved Configuration_value.")
		elif modelName == "Item_transfer_type":
			dbitem = Item_transfer_type()
			for k, v in python_obj['fields'].items():
				setattr(dbitem, k, v)
			dbitem.id = python_obj['pk']
			admin = User.objects.get(pk=1)
			dbitem.created_by = admin
			dbitem.save()
			print("Saved Item_transfer_type.")
		else:
			break


		for k, v in python_obj['fields'].items():
			if str(v.__class__) == "<class 'list'>":
				if str(k) == "groups":
					for a in v:
						dbitem.groups.add(a)
						print("Added user into group.")
				elif str(k) == "user_permissions":
					for a in v:
						dbitem.permissions.add(a)
						print("Added permission into user.")
				elif str(k) == "users":
					for a in v:
						dbitem.users.add(a)
						print("Added user into division.")
				elif str(k) == "categories":
					for a in v:
						dbitem.categories.add(a)
						print("Added product into category.")
				elif str(k) == "commodities":
					for a in v:
						dbitem.commodities.add(a)
						print("Added commodities into product.")
				else:
					break
			else:
				pass