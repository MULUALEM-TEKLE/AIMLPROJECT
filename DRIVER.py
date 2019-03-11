import User as usr
import PersonalInfo as pi
import os
import aiml
import Question as qn 

BRAIN_FILE="brain.dump"



def main():
    # Takes the user SID from another source
    personal_info = pi.PersonalInformation()
    SID = "1234"
    k = aiml.Kernel()
    # check the presence of the brain file and bootstrap from it
    if os.path.exists(BRAIN_FILE):
        print("Loading from brain file: " + BRAIN_FILE)
        k.loadBrain(BRAIN_FILE)
    else:
        print("Parsing aiml files")
        k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
        print("Saving brain file: " + BRAIN_FILE)
        k.saveBrain(BRAIN_FILE)
    # creates the user object 
    user = usr.User(SID , personal_info)
    # while true
    while True:
        input_text = input("XAD:~#")
        qsn = qn.Question(user , input_text , k)
        response = qsn.answer()
        print(response)
        # takes the qn of the uesr and create qn object and injects it with user obj 
        # returns the answer


    # now lets try to implement the training part 

main()
