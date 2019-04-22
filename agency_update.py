#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import pandas
import mysql.connector
import viewlist

# headers
print("content-type:text/html; charset=utf-8\n")
print()

# id값 가져오기
# - script traceback
cgitb.enable(display=1)
# - cgitb.enable(display=0, logdir="../logdir")

# 작성한 글의 페이지로 보내버린다
form = cgi.FieldStorage()
agencylist = form["agency"].value.split(',')

# # mysql 연결
# myconn = mysql.connector.connect(user='root', password='mk246900',
#                                host='127.0.0.1',
#                                database='rawtgalaxy')
# mycursor = conn.cursor()
#
# if 'D171' in agencylist:
#     sql = "INSERT INTO agency_r() values ()"
#     cursor.execute(sql, (""))
# else:
#     sql = "INSERT INTO agency_cr() values ()"
#


for i in agencylist:
    data = pandas.read_csv(agencylist[i])
    print(data)
