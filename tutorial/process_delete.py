#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os, cgi, cgitb

# id값 가져오기
cgitb.enable(display=1)  # script traceback
# cgitb.enable(display=0, logdir="../logdir")


# 작성한 글의 페이지로 보내버린다
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('../data/' + pageId)

# redirection
print("Location: index.py")
print()
