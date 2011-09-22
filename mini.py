#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

param = sys.argv

input = open(param[1],'rb')
output = open(param[2],'wb')

text = input.read()
print text
text = text.replace("\v","")
text = text.replace("\f","")
text = text.replace("\t","")
text = text.replace("\n","")
text = text.replace(" ","")
print text

output.write(text)

input.close()
output.close()

