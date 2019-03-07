import os
import xml.etree.ElementTree as et

#xml object
xmlObj = None

#get xml from path and put it on xmlObj
def getFile(file_name):
    xmlObj = et.parse(file_name)
    return xmlObj

xmlObj = getFile('reed.xml')


#find by tag and print content
def findallInTag(xmlObj, tag):
    contents = xmlObj.findall(tag)

    for c in contents:
        print(c.text)

#findallInTag(xmlObj,'course/title')


#view tag and attributs in the xml
def viewTag(xmlObj):
    root = xmlObj.getroot()
    print(root[0].tag, root[0].attrib)
    


viewTag(xmlObj)
