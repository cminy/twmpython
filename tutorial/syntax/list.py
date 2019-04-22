#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

print("content-type:text/html; charset=utf-8\n")

s = [1, 'one', 9, 16, '25']
print(s)
print(s[1])
print(len(s))

s[1] = 4
print(s)

print(s[1] * s[4])  # 25는 문자로 인식

s[4] = 25  # 숫자로 인식
print(s[1] * s[4])

del s[2]  # index로 지우기
print(s)

s.append('minyoung')  # 제일 뒤에 data 추가
print(s)

s.insert(2, 89)
print(s)

s.remove(89)  # 값으로 지우기
print(s)
