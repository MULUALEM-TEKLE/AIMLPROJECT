import Question as qn 
import Train

class BotApi:
    def  __init__(self,filename="standard/basics.aiml"):
        self.filename=filename
        self.question=qn.Question(self.filename)
        self.train=Train.Train(self.filename)
    
    def ask_question(self,questionDict):
        return self.question.answer(questionDict) 

    def train_converstion_type1(self,pattern,template,that,topic):
        self.train.add_conversation_t1(pattern,template,that,topic)
    
    def train_converstion_type2(self,pattern,type_tag_name,bot_response_object,that,topic):
        self.train.add_conversation_t2(pattern,type_tag_name,bot_response_object,that,topic)
    
    def searchCatagories(self,tagName,attribN,attribV, tagContent):
        self.train.searchCatagories(tagName,attribN,attribV, tagContent)

    def get_searched_catagories(self):
        return self.train.listOfTag

    def update_tag_text(self,tagName,tagvalue,index):
        self.train.updateText(tagName,tagvalue,index)

    def update_tag_attrib(self,attribName,attribValue,index):
        self.train.updateAttrib(attribName,attribValue,index)
    
    def add_new_tag_to_catagory(self,tagName,tagValue,p_tag,index):
        self.train.add_new_tag(tagName,tagValue,p_tag,index)

    def publish_changes(self):
        self.train.publish()