#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import cgi, cgitb
import view
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
  <a href="create.py">create</a>
  <p style="margin-top:45px;">
    <form action="process_update.py" method="post">
        <p><input type="hidden" name="pageId" value="{form_default_title}">
        <input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_desc}</textarea></p>
        <p><input type="submit"></p>
    </form>
  </p>
</body>

</html>

'''.format(title=pageId, listStr=view.getList(), form_default_title=pageId, form_default_desc=description))
