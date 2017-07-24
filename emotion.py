import numpy as np
import copy
import cv2
import urllib

face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
fishface = cv2.face.createFisherFaceRecognizer()

try:
	fishface.load("emoclassifier.xml")
except:
	print "Not able to load the classifier!! May be missing"


cap = cv2.VideoCapture(0)
#url = "http://192.168.1.101:8080/shot.jpg"

facedict = {}
emotions = ["angry", "happy", "sad", "surprise"]


def crop_face(gray,face_detect):
	for (x,y,w,h) in face_detect:
		faceslice = gray[y:y+h,x:x+w]
		faceslice = cv2.resize(faceslice,(350,350))
	return faceslice	
print "fine1"
#frame = cv2.imread("test\pen.jpg",1)
def getface():
	while True:
		ret, frame = cap.read()
		#img_res = urllib.urlopen(url)
		#img_array = np.array(bytearray(img_res.read()),dtype=np.uint8)
		#frame = cv2.imdecode(img_array,-1)
		
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
		clahe_frame = clahe.apply(gray)
		face_detect = face.detectMultiScale(clahe_frame,1.3,5)
		"""if not face_detect:
			temp = 0	
		else:
			temp = 1	
		#print temp"""
		#temp = 1
		#if temp:
		for (x,y,w,h) in face_detect:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				#faceslice = gray[y:y+h,x:x+w]
		#else:
		#	print "no face detected"
		#	exit()
		if len(face_detect)==1:
			faceslice = crop_face(gray,face_detect)
			#faceslice = cv2.resize(faceslice,(350,350))
			facedict["face%s" %(len(facedict)+1)] = faceslice
		else:
			pass
		#cv2.imshow("rec",frame)		
		#if len(facedict)==1:
		#	break
		
		cv2.imshow("gfd",frame)
		if (cv2.waitKey(10) & 0xFF == ord('q')) or (len(facedict)==40):
			break
	#cap.release()
	return x,y,frame



print "fine2"

def emotion_recognize():
	x1 , y1, frame = getface()
	prediction = []
	confidence = []
	for n in facedict.keys():
		pred, conf = fishface.predict(facedict[n])
		cv2.imwrite("images\\%s.jpg" %n, facedict[n])
		prediction.append(pred)
		confidence.append(conf)
		x = max(set(prediction), key=prediction.count)
		font = cv2.FONT_HERSHEY_COMPLEX
		cv2.putText(frame,emotions[x],(x1,y1),font,0.6,(0,0,255),1)
		print "fine3"
		#cv2.imshow("Camera",frame)
	print "you're feeling %s"  %(emotions[x])
	 
emotion_recognize()	

#print "working"
#k=cv2.waitKey(10)
print len(facedict)
#cap.release()
cv2.destroyAllWindows()	
