# This class handles everything that is related with aiml proccessing
import os
import json
import aiml
import time

class AimlParser:
    def __init__(self, fileName="standard/basics.aiml",brainName="brain.dump"):
        self._kernel= aiml.Kernel()
        if os.path.exists(brainName):
            print("Loading from brain file: " + brainName)
            self._kernel.loadBrain(brainName)
        else:
            print("Parsing aiml files...")
            self._kernel.bootstrap(learnFiles=fileName)
            print("Saving brain file: " + brainName)
            self._kernel.saveBrain(brainName)

    def getKernel(self):
        return self._kernel
        
    def get_response(self , message):
       return self._kernel.respond(message)

    
    


