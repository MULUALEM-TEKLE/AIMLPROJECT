import Question as qn 
import Train
import time
import xml.dom.minidom

def test():
      qsn=qn.Question()
      print("\n\tEnter The File name and The brain dump name\n\tor Press Enter to use the default")
      filename=input("file name >> ")
      if(filename!=""):qsn=qn.Question(filename)
      _input=input("XAD:~#")
      while _input!="exit":
            questn={"question":_input,"date":time.time()}
            response = qsn.answer(questn)
            print("question: ",response["question"],"\n","answer: ",response["answer"])
            print("date: ",response["date"],"\n","Accuracy: ",response["Accuracy"])
            _input = input("XAD:~#")


def train():
      print("Enter the  file Name or press Enter to use the default")
      train=Train.Train()
      filename=input("filename >> ")
      if(filename!=""): train=Train.Train(filename)
      print("Enter\n 1 to train\n 2 to search\n 3 to publish\n exit to exit ")
      _input=input("XAD:~#")
      while _input!="exit":
            if(int(_input)==1):
                 set_conversation(train)
            elif(int(_input)==2):
                  search_tag(train)
            elif(int(_input)==3):
                  train.publish()
            print("Enter\n 1 to train\n 2 to search\n 3 to publish\n exit to exit ")
            _input = input("XAD:~#")


def set_conversation(train):
      patt=input("Pattern :")
      topic= input("Topic :")
      if topic=="": topic=None 
      that=input("That :")
      if that=="": that=None
      print("if the Template is a String\n Enter 1 ")
      _input=input(" XAD:~#")
      if _input.isdigit() and int(_input)==1:
            temp=input("Template :")
            train.add_conversation_t1(patt,temp,that,topic)
      else: set_other_conversations(train,patt,that,topic)


def set_other_conversations(train,patt,that,topic):
      print("Enter \n\t1.for learn,srai and think elements\n\t2. for a random\n\t3.for a condition")
      _input=input("XAD:~#")
      if int(_input)==1 :
            type_name=input("Type name >> ") 
            response=input("Type value >> ")  
            train.add_conversation_t2(patt,type_name,response,that,topic)
      elif(int(_input)==2):
            setRandom(train,patt,that,topic)
      elif (int(_input)==3):
            setCondition(train,patt,that,topic)


def setCondition(train,patt,that,topic):
      conditions=[None,[],[]]
      conditions[0]=input("Enter the Name of the condition variable :")
      print("Enter the condition state value and the response message \n\t or exit for state to exit")
      state=input("state value >> ") 
      response=input("response value >> ")      
      while state!="exit":
            conditions[1].append(state)
            conditions[2].append(response)
            state=input("state value >> ") 
            response=input("response value >> ") 
      train.add_conversation_t2(patt,"condition",conditions,that,topic)


def setRandom(train,patt,that,topic):
      random=[]
      print("Enter the random values \n\t or exit to exit")
      state=input("random value >> ") 
      while state!="exit":
            random.append(state)
            state=input("random value >> ") 
      train.add_conversation_t2(patt,"random",random,that,topic)


def search_tag(train):
      tagName=input("Tag Name >> ")
      attribNam=input("Attribute Name  >> ")
      attribVal=input("Attribute Value >> ")
      tagContent=input("Tag Content >> ")
      if(tagContent==""):tagContent="<>"
      train.searchCatagories(tagName,attribNam,attribVal,tagContent)
      ans=input("Enter \n 1. to update tag value >> ")
      if(ans.isdigit() and int(ans)==1): update_tag(train)


def update_tag(train):
      index=int(input("Tag Index >> "))
      ans=input("Enter\n 1.To update tag value\n 2.To update attribute value\n 3.To add new Tag\n\t Enter >> ")
      if(ans.isdigit() and int(ans)==1):
            tagName=input("Tag Name >> ")
            tagContent=input("Tag Content >> ")
            train.updateText(tagName,tagContent,index)
      elif(ans.isdigit() and int(ans)==2):
            tagName=input("Tag Attribute Name >> ")
            tagContent=input("Tag Attribute Value >> ")
            train.updateAttrib(tagName,tagContent,index)
      elif(ans.isdigit() and int(ans)==3):
            ptagName=input("Parent Tag  Name >> ")
            tagName=input("Tag  Name >> ")
            tagContent=input("Tag  Value >> ")
            train.add_new_tag(tagName,tagContent,ptagName,index)


def structure_xml(filename="standard/basics.aiml"):
      formatted=open(filename,"r").read()
      while(formatted.find("\n")!=-1 or formatted.find("\t")!=-1):
            formatted=formatted.replace("\n","")
            formatted=formatted.replace("\t","")
      x=open(filename,"w")
      x.write(formatted)
      x.close()
      dom=xml.dom.minidom.parse(filename)
      formatted=dom.toprettyxml()      
      open(filename,"w").write(formatted)


def main():   
    print("Enter\n 1 to Test\n 2 to Train\n 3 to Format")
    _input=input("XAD:~#")
    while True:
      if(int(_input)==1):
            test()
      elif(int(_input)==2):
            train()
      elif((int(_input)==3)):
            structure_xml()
      print("Enter\n 1 to Test\n 2 to Train\n 3 to Format")
      _input=input("XAD:~#")


main()
