#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi, cgitb
import viewlist
print("content-type:text/html; charset=utf-8\n")  # headers
print()

# id값 가져오기
cgitb.enable(display=1)  # script traceback
# cgitb.enable(display=0, logdir="../logdir")

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('../data/' + pageId, 'r').read()
else:
    pageId = 'welcome'
    description = 'hello web'

# html코드 실행
print('''
<!doctype html>
<html>

<head>
  <title>WEB - python</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <p style="margin-top:45px;">
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
  </p>
</body>

</html>

'''.format(title=pageId, listStr=viewlist.getList()))
