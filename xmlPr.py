import os
import xml.etree.ElementTree as et
import aiml

class XmlPr:
    def __init__(self,filename="standard/basics.aiml"):
        self.filename=filename
        self.root=None
        self.Values=None
        self.xmlObj=None
        self.parent=None
        self.getFile()

    def getFile(self):
        self.xmlObj = et.parse(self.filename)
        self.root=self.xmlObj.getroot()
        return self.xmlObj

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

    def setCondition(self): # condition dictionary value contain a list of condition name , condition list and response text.
        if(self.Values.get("condition")!=None):
            state_name=self.Values["condition"][0]
            cond_list=self.Values["condition"][1]
            response_list=self.Values["condition"][2]
            for i in range(len(cond_list)):
                new_condition = et.SubElement(self.parent,"condition")
                new_condition.attrib["name"]=state_name
                new_condition.attrib["value"]=cond_list[i]
                # new_condition=self.setStar(response_list[i],new_condition)
                new_condition.text=response_list[i]

    def setLearn(self):
        if(self.Values.get("learn")!=None):
            new_learn = et.SubElement(self.parent,"learn")
            new_learn.text=self.Values["learn"]
    
    def setStar(self,strval,tagName,parent): # trainers  write *1 or * ....
        strval=strval.split("*")
        str_element="<"+tagName+"> "
        for i in range(len(strval)):
            str_element+=strval[i]
            if(i+1<len(strval)):
                if(len(strval[i+1])>=1 and strval[i+1][0].isdigit()):
                    str_element+='<star index="'+strval[i+1][0]+'" />'
                    strval[i+1]=strval[i+1][1:]
                else:
                    str_element+='<star index="1" />'
        str_element+="</"+tagName+"> "
        parent.append(et.fromstring(str_element))
        return parent

    def setSetter(self,name,value,element): 
        setter=et.SubElement(element,"set")
        setter.attrib["name"]=name
        # setter=self.setStar(value,setter)
        setter.text=value
        return setter

    def setGetter(self,name,element):
        getter=et.SubElement(element,"get")
        getter.attrib["name"]=name
        return getter

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
            _kernel= aiml.Kernel()
            if os.path.exists(BRAIN_FILE):
                print("Deleting Existing file...")
                os.remove(BRAIN_FILE)
            self.xmlObj.write(self.filename)
            