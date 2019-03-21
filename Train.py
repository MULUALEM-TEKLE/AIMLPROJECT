import xmlPr as xml

# # Possible Values :: ["topic","category","pattern","that","template","srai","random","think","condition","learn"]

class Train:
    def __init__(self,filename="standard/basics.aiml"):
        self.xml_Parser=xml.XmlPr(filename)
        self.listOfTag=[]

    def add_conversation_t1(self, pattern,template,that=None,topic=None):
        values={"topic":topic,"pattern":pattern.upper(),"that":that,"template":template}
        self.xml_Parser.setValues(values)
        self.xml_Parser.generateXml()

    def add_conversation_t2(self,pattern,value_type,actual_value,that=None,topic=None):
        values={"topic":topic,"pattern":pattern.upper(),"that":that,value_type:actual_value}
        self.xml_Parser.setValues(values)
        self.xml_Parser.generateXml()

    def publish(self):
        self.xml_Parser.saveXml()

    def searchCatagories(self,tagName,attribN,attribV, tagContent):
        self.listOfTag=self.xml_Parser.findTagWithContents(tagName,attribN,attribV, tagContent)
        for counter in range(len(self.listOfTag)):
            count=1 # there should be no print statement on the final code ^
            print(str(counter+1)+".","---------------------------------------------------------------------------------")
            self.display_tags(count,self.listOfTag[counter])       
            print("------------------------------------------------------------------------------------")   

    def display_tags(self,tab,tag):
        print(("\t"*tab),"Tag Name :",tag.tag)
        if len(tag.getchildren())==0:
            if list(tag.attrib.keys()):print(("\t"*tab),"\tTag attributes :")
            for j in list(tag.attrib.keys()):
                print(("\t"*tab),"\t\t",j," :", tag.attrib[j]) 
        else:
            tab+=1
            for sub_tag in tag.getchildren():
                self.display_tags(tab,sub_tag)
        if(tag.text!=None):print(("\t"*tab),"\tInner Value: ",tag.text)

    def updateText(self,tagName,tagvalue,index):
        el=self.listOfTag[index-1]
        el=self.replaceText(tagName,tagvalue,el)    
        count=1
        self.display_tags(count,el)
    
    def replaceText(self,tagName,tagvalue,parent):
        for tag in parent:
            if (tag.tag==tagName): 
                tag.clear()
                tag.text=tagvalue
                return parent
            else: 
                self.replaceText(tagName,tagvalue,tag)

    def updateAttrib(self,attribName,attribValue,index):
        el=self.listOfTag[index-1]
        el=self.replaceAttrib(attribName,attribValue,el)   
        count=1
        self.display_tags(count,el)
        
    def replaceAttrib(self,attribName,attribValue,parent):
        for tag in parent:
            if (tag.attrib.get(attribName)!=None): 
                tag.clear()
                tag.attrib[attribName]=attribValue
                return parent
            else: 
                self.replaceText(attribName,attribValue,tag)

    def add_new_tag(self,tagName,tagValue,p_tag,index):
        el=self.listOfTag[index-1]
        self.add_inner_tag(tagName,tagValue,el,p_tag)
        count=1
        self.display_tags(count,el)

    def add_inner_tag(self,tagName,tagValue,parent,p_tag):
        for tag in parent:
            if (tag.tag==p_tag): 
                self.xml_Parser.addtag(tagName,tagValue,tag)
                return parent
            else: 
                self.add_inner_tag(tagName,tagValue,tag,p_tag)

