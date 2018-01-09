"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
There are <count> different telephone numbers in the records."""

d={}

for text,call in texts,calls:
    if text[0], call[0] in d:
        d[text[0]]+=1
        d[call[0]]+=1
    else:
        d[text[0]]=1
        d[call[0]]=1
    if text[1], call[1] in d:
        d[text[1]]+=1
        d[call[1]]+=1
    else:
        d[text[1]]=1
        d[call[1]]=1

print("There are " + str(len(d)) + " different telephone numbers in the records.")
