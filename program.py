import os
import xml.etree.ElementTree as et

xmlObj = None 
def getFile(file_name):
    xmlObj = et.parse(file_name)
    return xmlObj

xmlObj = getFile('reed.xml')



def findallInTag(xmlObj, tag):
    contents = xmlObj.findall(tag)

    for c in contents:
        print(c.text)



findallInTag(xmlObj,'course/title')




