#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi, cgitb, html_sanitizer
import view

print("content-type:text/html; charset=utf-8\n")  # headers
print()

# id값 가져오기
cgitb.enable(display=1)  # script traceback
# cgitb.enable(display=0, logdir="../logdir")

sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()

if 'id' in form:
    title = pageId = form["id"].value
    description = open('../data/' + pageId, 'r').read()
    # xss처리
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id=' + pageId + '">update</a>'
    delete_action = '''
    <form action = "process_delete.py" method = "post" >
        <p><input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete""></p>
    </form>
    '''.format(pageId)
else:
    pageId = 'welcome'
    description = 'hello web'
    update_link = ''
    delete_action = ''

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
  <h2>{title}</h2>
  <a href="create.py">create</a>
  {update_link} {delete_action}
  <p style="margin-top:45px;">
    {desc}
  </p>
</body>

</html>

'''.format(title=pageId, desc=description, listStr=view.getList(), update_link=update_link, delete_action=delete_action)
      )
