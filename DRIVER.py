import os
import json
import aiml
import Question as qn 
import time
import Train


def test():
  qsn=qn.Question()
  _input=input("XAD:~#")
  while _input!="exit":
        questn={"question":_input,"date":time.time()}
        response = qsn.answer(questn)

        print("question: ",response["question"])
        print("answer: ",response["answer"])
        print("date: ",response["date"])
        print("Accuracy: ",response["Accuracy"])
        _input = input("XAD:~#")



def train():
  train=Train.Train()
  print("Enter\n 1 to train\n 2 to publish\n exit to exit ")
  _input=input("XAD:~#")
  while _input!="exit":
        if(int(_input)==1):
            patt=input("Pattern :")
            topic= input("Topic :")
            if topic=="": topic=None 
            that=input("That :")
            if that=="": that=None
            print("if the Template is a String enter 1....")
            _input=input("XAD:~#")
            if not _input.isdigit():
                  print("Enter \n\t1.for learn,srai and think elements\n\t2.for a condition\n\t3. for a random")
                  _input=input("XAD:~#")
                  if int(_input)==1 :
                        type_name=input("Type name >> ") 
                        response=input("Type value >> ")  
                        train.add_conversation_t2(patt,type_name,response,that,topic)
                  elif(int(_input)==2):
                        setRandom(train,patt,that,topic)
                  elif (int(_input)==3):
                        setCondition(train,patt,that,topic)
            elif int(_input)==1:
                  temp=input("Template :")
                  train.add_conversation_t1(patt,temp,that,topic)
        elif(int(_input)==2):
              train.publish()

        print("Enter\n 1 to train\n 2 to publish\n exit to exit ")
        _input = input("XAD:~#")

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


def main():
   
    print("Enter\n 1 to Test\n 2 to Train")
    _input=input("XAD:~#")
    while True:
        if(int(_input)==1):
            test()
        else:
            train()
        print("Enter\n 1 to Test\n 2 to Train")
        _input=input("XAD:~#")

main()
