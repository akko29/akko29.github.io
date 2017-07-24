import glob
import os
from shutil import copy

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] #Define emotion order
participants = glob.glob("source_emotion\\Emotion\\*") #Returns a list of all folders with participant numbers

for x in participants:
    part = "%s" %x[0:] #store current participant number
    for sessions in glob.glob("%s\\*" %x): 
        #print sessions#Store list of sessions for current participant
        #print "fine1"
        for files in glob.glob("%s\\*.txt" %sessions):
            #current_session = files[20:-30]
            file1 = open(files, 'r')
            #print current_session
            #print "fine2"
            emotion = int(float(file1.readline())) #emotions are encoded as a float, readline as float, then convert to integer.
            #print emotion
            temp1 = x[23:]
            temp2 = sessions[28:]
            #print temp1,temp2
            sourcefile_emotion = glob.glob("source_images\\%s\\%s\\*" %(temp1,temp2))[-1] #get path for last image in sequence, which contains the emotion
            sourcefile_neutral = glob.glob("source_images\\%s\\%s\\*" %(temp1,temp2))[0] #do same for neutral image
            print sourcefile_emotion
            print sourcefile_neutral
            
            dest_neut = "sorted_set\\neutral" #Generate path to put neutral image
            dest_emot = "sorted_set\\%s" %(emotions[emotion]) #Do same for emotion containing image

            copy(sourcefile_neutral, dest_neut) #Copy file
            copy(sourcefile_emotion, dest_emot) #Copy file