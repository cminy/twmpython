#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb

# id값 가져오기
cgitb.enable(display=1)  # script traceback
# cgitb.enable(display=0, logdir="./logdir")


# 작성한 글의 페이지로 보내버린다
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_file = open('data/' + title, 'w')
opened_file.write(description)
opened_file.close()

# redirection
print("Location: index.py?id=" + title)
print()
