import os
import xml.etree.ElementTree as et

#xml object
xmlObj = None

#get xml from path and put it on xmlObj
def getFile(file_name):
    xmlObj = et.parse(file_name)
    return xmlObj

xmlObj = getFile('reed.xml')
root = xmlObj.getroot()

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
    


#viewTag(xmlObj)
def writeXml(contentPat, contentLrn):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_learn = et.SubElement(new_template,"learn")

    new_pattern.text = contentPat
    new_learn.text = contentLrn

    xmlObj.write('reed.xml')


writeXml("pattern1", "learn1")
