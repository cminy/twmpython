#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import viewlist

# headers
print("content-type:text/html; charset=utf-8\n")
print()

# id값 가져오기
# - script traceback
cgitb.enable(display=1)
# - cgitb.enable(display=0, logdir="../logdir")


form = cgi.FieldStorage()

if 'id' in form:
    title = pageId = form["id"].value
else:
    pageId = 'welcome'

# html코드 실행
print('''
<!doctype html>
<html>

<head>
  <title>TestData List</title>
  <meta charset="utf-8">
</head>

<body>
  <h3><a href="index.py">datasets</a></h3>
  <ol>
    {listStr}
  </ol>
</body>

</html>

'''.format(pageid=pageId, listStr=viewlist.getList())
      )
