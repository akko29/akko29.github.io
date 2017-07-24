import cv2
import numpy as np
import glob

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
face1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face2 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
face3 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
face4 = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

def getface(emotion):
	filenumber = 0
	path = glob.glob("sorted_set\\%s\\*" %emotion)
	for i in path:
		img = cv2.imread(i)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		face_detect1 = face1.detectMultiScale(gray,1.5,5)
		face_detect2 = face2.detectMultiScale(gray,1.5,5)
		face_detect3 = face3.detectMultiScale(gray,1.5,5)
		face_detect4 = face4.detectMultiScale(gray,1.5,5)

		if len(face_detect1)==1:
			face_detect = face_detect1
		elif len(face_detect2)==1:
			face_detect = face_detect2
		elif len(face_detect3)==1:
			face_detect = face_detect3
		elif len(face_detect4)==1:
			face_detect = face_detect4
		else:
			face_detect =""				
		for (x,y,w,h) in face_detect:
			print "face found in file %s"%(i)
			gray = gray[y:y+h,x:x+w]

			try:
				
				out = cv2.resize(gray,(350,350))
				cv2.imwrite("dataset\\%s\\%s.png" %(emotion,filenumber),out)
			except:
				print "face not found"
			filenumber+=1
		
				
for emotion in emotions:
	getface(emotion)