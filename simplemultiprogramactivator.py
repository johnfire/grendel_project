#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:52:02 2020

@author: christopher
"""

import subprocess

import sys
sys.path.append('../')

p1 = subprocess.Popen(['./grendelAIandDecisionProgram/decisionProgram.py'])
p2 = subprocess.Popen(['./grendelPhysicalOperationProgram/firstLevelProcessor.py'])
me_run = True
while(me_run is True):
    print("p1 id is " + str(p1))
    print("p2 id is " + str(p2))
    answer = input("q to terminate programs  anything else to run")
    if answer == "q":
        p2.terminate()
        p1.terminate()
        me_run = False