# -*- coding: utf-8 -*-

import os
import glob

def getList():
    files = os.listdir('./testdata')  # data폴더에 저장된 것들 리스트로 불러옴
    listStr = ''

    for item in files:
        listStr = listStr + \
            '''
            <li><a href="subdirpg.py?id={name}">{name}</a></li>
            '''.format(name=item)
    return listStr


def getCsvList(subdir):
    files = [os.path.basename(raw) for raw in glob.glob(subdir + '/*.csv')]

    if 'crawl' in subdir:
        acrawllist = ''
        mcrawllist = ''
        for file in files:
            if 'member' not in file:
                acrawllist += file + ','
            else:
                mcrawllist += file + ','
        return acrawllist, mcrawllist
    else:
        arawlist = ''
        mrawlist = ''
        for file in files:
            if 'D171' in file:
                arawlist += file + '\n'
            else:
                mrawlist += file + '\n'
        return arawlist, mrawlist

        # for file in files:
        #     if 'D171' in file:
        #         arawlist.append('{}'.format(file))
        #     else:
        #         mrawlist.append('{}'.format(file))
        # return arawlist, mrawlist
