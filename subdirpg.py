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
pageId = form["id"].value

# filelist 가져오기
desc, descmem = viewlist.getCsvList('./testdata/{}'.format(pageId))

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
  <p style="margin-top:45px;">
    <form action="agency_update.py" method="post" style="float:left">
        <fieldset>
            <legend> {title} _ agency info _ csv files : </legend>
            <input type="text" name="agency" value={csv_file_list} readonly style="width:100%">
            <p><input type="submit"></p>
        </fieldset>
    </form>
    <form action="member_update.py" method="post" style="float:left">
        <fieldset>
            <legend> {title} _ realtor info _ csv files : </legend>
            <input type="text" name="member" value={mem_csv_file_list} readonly style="width:100%">
            <p><input type="submit"></p>
        </fieldset>
    </form>
  </p>
</body>

</html>

'''.format(title=pageId, listStr=viewlist.getList(), csv_file_list=desc, mem_csv_file_list=descmem))
