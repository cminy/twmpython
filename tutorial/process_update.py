#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os, cgi, cgitb

# id값 가져오기
cgitb.enable(display=1)  # script traceback
# cgitb.enable(display=0, logdir="../logdir")


# 작성한 글의 페이지로 보내버린다
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open('../data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('../data/' + pageId, '../data/' + title)

# redirection
print("Location: index.py?id=" + title)
print()
