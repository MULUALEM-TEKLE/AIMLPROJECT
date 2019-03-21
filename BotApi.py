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