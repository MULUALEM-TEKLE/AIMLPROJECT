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
    


#write a simple category including 'learn' tag in file
def writeCategoryLrn(contentPat, contentLrn):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_learn = et.SubElement(new_template,"learn")

    new_pattern.text = contentPat.upper()
    new_learn.text = contentLrn

    xmlObj.write('reed.xml')

#write a simple category in file
def writeCategory(contentPat,contentTemp):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")

    new_pattern.text = contentPat.upper()
    new_template.text = contentTemp

    xmlObj.write('reed.xml')

    
#wrire a catagory with 'srai' tag
def writeCategorySrai(contentPat, contentSrai):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_srai = et.SubElement(new_template,"srai")

    new_pattern.text = contentPat.upper()
    new_srai.text = contentSrai
    xmlObj.write('reed.xml')

#write a category with 'random' and 'li'
def writeCategoryRand(contentPat, *contentLi):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_random = et.SubElement(new_template,"random")
    for li in contentLi:
        new_li = et.SubElement(new_random,"li")
        new_li.text = li

    new_pattern.text = contentPat.upper()
    xmlObj.write('reed.xml')


#write a category with 'that' tag
def writeCategoryThat(contentPat, contentThat,contentTemp):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_that = et.SubElement(new_category,"that")
    new_template = et.SubElement(new_category,"template")

    new_pattern.text = contentPat.upper()
    new_that.text = contentThat
    new_template.text = contentTemp
    xmlObj.write('reed.xml')


#write a new topic
def writeTopic(contentPat,contentTemp, topicName):
    new_topic = et.SubElement(root,"topic")
    new_category = et.SubElement(new_topic,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")

    new_pattern.text = contentPat.upper()
    new_template.text = contentTemp
    new_topic.attrib["name"]=topicName
    xmlObj.write('reed.xml')
'''
for elem in root.findall('.//child/grandchild'):
    # How to make decisions based on attributes even in 2.6:
    if elem.attrib.get('name') == 'foo':
        result = elem.text
        break
'''
#find a tag which contains a specific content
def findTagWithContent(tagName, tagContent):
    for tag in root.iter():
        if (tag.tag==tagName and tag.text==tagContent):
            return tag
        return "Tag not found"

#find tag based on attribute value
def findTagWithAttribute(tagName, attributeName, attributeValue):
    for tag in root.iter():
        if(tag.tag == tagName and tag.attrib[attributeName]==attributeValue):
            return tag
    return "Tag not found"
'''
gotTag=findTagWithAttribute("topic", "name", "topic1")
print(gotTag.tag)

gotTag=findTagWithContent("pattern", "LOAD AIML B")
print(gotTag.tag)

for tag in root.iter():
    print(tag.tag+"   "+tag.text)
'''
