# -*- coding: utf-8 -*-

import os
import glob

def getList(dir):
    files = os.listdir(dir)  # data폴더에 저장된 것들 리스트로 불러옴
    listStr = ''

    for item in files:
        listStr = listStr + \
            '''
            <input type="submit" name="pageId" value="{}"><br>
            '''.format(item)
    return listStr


def getCsvList(subdir):
    files = [os.path.basename(raw) for raw in glob.glob(subdir + '/*.csv')]

    if 'crawl' in subdir:
        acrawllist = ''
        mcrawllist = ''
        for file in files:
            if 'member' not in file:
                acrawllist += file + ',<br>'
            else:
                mcrawllist += file + ',<br>'
        return acrawllist, mcrawllist
    else:
        arawlist = []
        mrawlist = []
        for file in files:
            if 'D171' in file:
                arawlist.append('{}'.format(file))
            else:
                mrawlist.append('{}'.format(file))
        return arawlist, mrawlist
