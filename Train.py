import xmlPr as xml

# # Possible Values :: ["topic","category","pattern","that","template","srai","random","think","condition","learn"]

class Train:
    def __init__(self):
        self.xml_Parser=xml.XmlPr("standard/basics.aiml")
        
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


