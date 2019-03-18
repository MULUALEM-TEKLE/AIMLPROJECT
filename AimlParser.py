# This class handles everything that is related with aiml proccessing
import os
import json
import aiml
import time

BRAIN_FILE="brain.dump"
class AimlParser:
    def __init__(self):
        self._kernel= aiml.Kernel()
        if os.path.exists(BRAIN_FILE):
            print("Loading from brain file: " + BRAIN_FILE)
            self._kernel.loadBrain(BRAIN_FILE)
        else:
            print("Parsing aiml files")
            self._kernel.bootstrap(learnFiles="standard/basics.aiml", commands="load aiml b")
            print("Saving brain file: " + BRAIN_FILE)
            self._kernel.saveBrain(BRAIN_FILE)

    def getKernel(self):
        return self._kernel
        
    def get_response(self , message):
       return self._kernel.respond(message)

    
    


