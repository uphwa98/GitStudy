# -*- coding:utf-8 -*-
import openpyxl
from lxml import etree

members = []
albums = []

# Load XML
tree = etree.parse("test.xml")
root = tree.getroot()

# Get data
kids = root.getchildren()

for child in kids:
    if child.tag == "name":
        gname = child.text
    elif child.tag == "members":
        for x_member in child:
            members.append(x_member.text)
    elif child.tag == "albums":
        for x_album in child:
            albums.append([x_album.get("order"), x_album.text])

for keyword in members:
    print("member : %s" % keyword)
# Print
print("걸그룹 %s에 대한 정보는 다음과 같습니다:" % gname, end="\n\n")


filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []

for keyword in members:
    for row in sheet.rows:
        for col in row:
            if col.value is not None:
                if col.value == keyword:
                    print("-----------found %s ---------------" % keyword)
#               else:
#                    print(col.value)
#                    print("--- %s" % keyword)
            else:
                continue



    #data.append([row[0].value, row[9].value])
"""
del data[0]
del data[1]
del data[2]

data.sorted(data, key=lambda x:x[1])

for i, a in enumerate(data):
    if (i >= 5):break
    print(i + 1, a[0], int(a[1]))
"""

