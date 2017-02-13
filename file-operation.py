#!/usr/bin/python
# -*- coding: UTF-8 -*-
#the short introduction of python I/O
fo=open("F:\Python27\python-code\wang.txt","r+")#打开一个文件用于读写。文件指针将会放在文件的开头
str1=fo.name#文件名
print "the file name is：",str1
#read the file content
str2=fo.read()
print "the content of the file is：",str2
#read the string of the file based on the definited number of the char
str3=fo.read(5)
print "the reading string is:",str3#you can see that the result is None, because the pointer is at the final of the file
#utilize the function of seek() to adjust the pointer to the front of the file
fo.seek(0,0)
str4=fo.read(5)
print str4 #now you can get the result
# let we see how to use the function of readline()
fo.seek(0,0)
line1=fo.readline()#read the first line of the file
print line1
#you can also read based on the number of the chars
fo.seek(0,0)
line2=fo.readline(5)
print line2
#the function of readlines() is used to read all line of the file
fo.seek(0,0)
line3=fo.readlines()
print line3
#use the function of write() to add some contents to the file
fo.write("you are a good student in the school")# the content is from the final of the original file to start
#because the pointer is at the final due to the former operation
#but now the content has not been writed in the file, it now in the buffer
#we can use the function of the flush() to send it to the file quickly
fo.flush()#Now the content is adding to the file
#let we talk about the function of truncate(), it used to intercepte the string of the file
fo.seek(0,0)
line4=fo.readline()
print line4
fo.truncate()
line5=fo.readline()
print "Now the result you can is:" %(line5)# the result is None you getted
