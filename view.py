import os
import html_sanitizer


def getList():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')  # data폴더에 저장된 것들 리스트로 불러옴
    listStr = ''

    for item in files:
        item = sanitizer.sanitize(item)
        listStr = listStr + \
            '<li><a href="index.py?id={name}">{name}</a></li>'.format(
                name=item)

    return listStr
