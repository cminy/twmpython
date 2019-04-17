#변수사용
bodyname = 'eyes'
ver = '1'
print('''
version : '''+ver+'''

안녕 안 바쁘면 나와
나 시간이 조금 떠
잠깐이라도 좋아
마주 앉아 있고 싶어

I can’t take my '''+bodyname+''' off you
''')

#positional formatting
print('''
version : {}

안녕 안 바쁘면 나와
나 시간이 조금 떠
잠깐이라도 좋아
마주 앉아 있고 싶어

I can’t take my {} off you
'''.format(2,'아이즈'))

#named placeholder #degit
print('''
version : {version:d}

안녕 안 바쁘면 나와
나 시간이 조금 떠
잠깐이라도 좋아
마주 앉아 있고 싶어

I can’t take my {body} off you
'''.format(version = 30, body = 'eyes'))
