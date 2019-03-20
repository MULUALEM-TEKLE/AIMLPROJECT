import time
import AimlParser
class Question:
    def __init__(self,filename="standard/basics.aiml",brainName="brain.dump"):
        self.Aiml=AimlParser.AimlParser(filename,brainName)
        self.accuracy = 0.0
        self.related_nodes = []
        self.response=dict()
    
    def answer(self,question_dict):
        self.response["answer"]= self.Aiml.get_response(question_dict["question"].upper()).upper()#.lower().capitalize()
        self.response["question"]=question_dict["question"]
        self.response["Accuracy"]="1%"
        self.response["date"]=time.time()
        return self.response
        






    # this functionality will be done later dont bother about it
    # def add_related_qn_node(self , qn):
    #     if add_related_qn_node.length <=4:
    #         self.related_nodes.add(qn)
    #     else:
    #         return
    #         # cannot preceed
    #         pass

    # this function is used for node navigation
    # def move(self , index):
    #     qn = self.related_nodes[index]
    #     qn.add(self)
    #     return qn
