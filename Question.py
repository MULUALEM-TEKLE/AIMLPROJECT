
class Question:
    def __init__(self , user , question_str):
        self.user = user 
        self.question_str = question_str
        self.accuracy = 0.0
        self.related_nodes = []
        pass
    
    def answer(self):
        # persist the qn 
        user.add_qn(self)
        # returns the answer
        pass

    # this functionality will be done later dont bother about it
    def add_related_qn_node(self , qn):
        if add_related_qn_node.length <=4:
            self.related_nodes.add(qn)
        else:
            # cannot preceed
        pass

    # this function is used for node navigation
    def move(self , index):
        qn = self.related_nodes[index]
        qn.add(self)
        return qn
