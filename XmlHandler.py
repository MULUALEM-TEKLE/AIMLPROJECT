import os
import xml.etree.ElementTree as et
import aiml

def getFile(file_name):
    xmlObj = et.parse(file_name)
    return xmlObj


def findallInTag(xmlObj, tag):
    contents = xmlObj.findall(tag)

    for c in contents:
        print(c.text)



def viewTag(xmlObj):
    root = xmlObj.getroot()
    print(root[0].tag, root[0].attrib)
    


def writeXml(root,contentPat, contentTemp,contentThat=" ",contentTopic="",filename="standard/basics.aiml"):    
        new_topic = et.SubElement(root,"topic")
        new_category = et.SubElement(new_topic,"category")
        new_pattern = et.SubElement(new_category,"pattern")
        new_template = et.SubElement(new_category,"template")
        new_that = et.SubElement(new_category,"that")
        new_pattern.text = contentPat.upper()
        new_that.text=contentThat
        new_topic.attrib["name"]=contentTopic
        new_template.text = contentTemp

def writeCategoryLrn(root,contentPat, contentLrn):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_learn = et.SubElement(new_template,"learn")
    new_pattern.text = contentPat.upper()
    new_learn.text = contentLrn


def writeCategory(root,contentPat,contentTemp):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_pattern.text = contentPat.upper()
    new_template.text = contentTemp


def writeCategorySrai(root,contentPat, contentSrai):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_srai = et.SubElement(new_template,"srai")
    new_pattern.text = contentPat.upper()
    new_srai.text = contentSrai



def writeCategoryRand(root,contentPat, *contentLi):
    new_category = et.SubElement(root,"category")
    new_pattern = et.SubElement(new_category,"pattern")
    new_template = et.SubElement(new_category,"template")
    new_random = et.SubElement(new_template,"random")
    for li in contentLi:
        new_li = et.SubElement(new_random,"li")
        new_li.text = li

    new_pattern.text = contentPat.upper()



def saveXml(xmlObj,filename="standard/basics.aiml"): 
        BRAIN_FILE="brain.dump"  
        _kernel= aiml.Kernel()
        
        if os.path.exists(BRAIN_FILE):
            print("Deleting Existing file")
            os.remove(BRAIN_FILE)
        xmlObj.write(filename)
        