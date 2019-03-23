import os
import aiml
import xml.etree.ElementTree as et

class XmlPr:
    def __init__(self,filename="standard/basics.aiml"):
        self.filename=filename
        self.root=None
        self.Values=None
        self.xmlObj=None
        self.parent=None
        self.getFile()
    
    def getFile(self):
        try:
            self.xmlObj = et.parse(self.filename)
            self.root=self.xmlObj.getroot()
            return self.xmlObj
        except:
            f=open(self.filename,"w")
            f.write('<aiml  version="1.0" ></aiml>')
            f.close()
            self.getFile()

    def setValues(self,Values):
        self.Values=Values

    def setTopic(self): 
        self.parent=self.root
        if(self.Values.get("topic") !=None):
             new_topic = et.SubElement(self.root,"topic")
             new_topic.attrib["name"]=self.Values["topic"]
             self.parent=new_topic
    
    def setCatagory(self):
        new_category = et.SubElement(self.parent,"category")
        self.parent=new_category
        new_pattern = et.SubElement(new_category,"pattern")
        new_pattern.text = self.Values["pattern"]

    def setThat(self):
        if(self.Values.get("that")!=None):
            new_that = et.SubElement(self.parent,"that")
            new_that.text=self.Values["that"]
    
    def setTemplate(self):
        if(self.Values.get("template")!=None): # if only a message exist!!
            self.parent=self.setStar(self.Values["template"],"template",self.parent)
            return True
        else:
            self.parent = et.SubElement(self.parent,"template")
            return False


    def setSrai(self):
        if(self.Values.get("srai")!=None):
            self.setStar(self.Values["srai"],"srai",self.parent)


    def setRandom(self):
        if(self.Values.get("random")!=None):
            new_random = et.SubElement(self.parent,"random")
            for val in self.Values["random"]:
                self.setStar(val,"li",new_random)


    def setThink(self):
        if(self.Values.get("think")!=None):
            self.setStar(self.Values["think"],"think",self.parent)


    def setCondition(self): # condition dictionary value contain...
        if(self.Values.get("condition")!=None): # ...a list of condition name
            state_name=self.Values["condition"][0] # ... ,condition list and response text.
            cond_list=self.Values["condition"][1]
            response_list=self.Values["condition"][2]
            for i in range(len(cond_list)):
                attrib={"name":state_name,"value":cond_list[i]}
                self.setStar(response_list[i],"condition",self.parent,attrib)

    def setLearn(self):
        if(self.Values.get("learn")!=None):
            new_learn = et.SubElement(self.parent,"learn")
            new_learn.text=self.Values["learn"]

    def addtag(self,tagName,tagvalue,parent):
        return self.setStar(tagvalue,tagName,parent)

    def setStar(self,strval,tagName,parent,attribute={}): # trainers  write *1 or * ....
        strval=strval.split("*")
        str_element="<"+tagName+"> "
        for i in range(len(strval)):
            str_element+=strval[i]
            if(i+1<len(strval) and len(strval[i+1])>=1 and strval[i+1][0].isdigit()):
                str_element+='<star index="'+strval[i+1][0]+'" />'
                strval[i+1]=strval[i+1][1:]
            elif i+1<len(strval):
                str_element+='<star index="1" />'
        str_element+="</"+tagName+"> "
        ett=et.fromstring(self.setGetter(self.setSetter(str_element)))
        ett.attrib=attribute
        parent.append(ett)
        return parent


    def setSetter(self,value): # this is how {name:value} to set value
        if(-1!=value.find("{") and -1!=value.find("}") and -1!=value.find(":")):
            set_str=value[:value.find("{")]+' <set name="'+value[value.find("{")+1:value.find(":")]+'" > '
            set_str+= value[value.find(":")+1:value.find("}")]+" </set>"+value[value.find("}")+1:]
            return set_str
        return value

    def setGetter(self,value): # this is how [name] to get value
        if(-1!=value.find("[") and -1!=value.find("]")):
            get_str=value[:value.find("[")]+' <get name="'+value[value.find("[")+1:value.find("]")]+'" /> '
            get_str+= value[value.find("]")+1:]
            return get_str
        return value

    def findTagWithContents(self,tagName="catagory",attribN="",attribV="", tagContent="<>"):
        list_Of_tags=[]
        for sub_tag in self.root:
            if(sub_tag.tag=="topic"):
               for ssub_tag in sub_tag:
                    self.findInnerTag(tagName,attribN,attribV, tagContent,ssub_tag,ssub_tag,list_Of_tags)
            else:self.findInnerTag(tagName,attribN,attribV, tagContent,sub_tag,sub_tag,list_Of_tags)
        return list_Of_tags


    def findInnerTag(self,tagName,attribN,attribV, tagContent,parent,root,list_Of_tags):
        if (parent.tag==tagName or parent.attrib.get(attribN)==attribV 
            or (parent.text!=None and parent.text.find(tagContent)!=-1)):
            list_Of_tags.append(root)
        for sub_tag in parent.getchildren():
            self.findInnerTag(tagName,attribN,attribV, tagContent,sub_tag,root,list_Of_tags)


    def replaceText(self,tagName,tagvalue,parent):
        for tag in parent:
            if (tag.tag==tagName): 
                parent.remove(tag)
                self.addtag(tagName,tagvalue,parent)
                return parent
            else: self.replaceText(tagName,tagvalue,tag)


    def replaceAttrib(self,attribName,attribValue,parent):
        for tag in parent:
            if (tag.attrib.get(attribName)!=None): 
                tag.attrib[attribName]=attribValue
                return parent
            else: self.replaceAttrib(attribName,attribValue,tag)
        return parent


    def add_inner_tag(self,tagName,tagValue,parent,p_tag):
        if(parent.tag==p_tag):
            return self.setStar(tagValue,tagName,parent)
        for tag in parent:
            if (tag.tag==p_tag): 
                self.addtag(tagName,tagValue,tag)
                return parent
            else: self.add_inner_tag(tagName,tagValue,tag,p_tag)
    
    
    def generateXml(self):
        self.setTopic()
        self.setCatagory()
        self.setThat()
        val=self.setTemplate()
        if(not val):
            self.setSrai()
            self.setLearn()
            self.setRandom()
            self.setCondition()
            self.setThink()

    def saveXml(self,BRAIN_FILE="brain.dump" ):  
        if os.path.exists(BRAIN_FILE):
            print("Deleting Existing file...")
            os.remove(BRAIN_FILE)
        self.xmlObj.write(self.filename)

