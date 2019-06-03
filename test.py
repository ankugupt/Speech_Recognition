import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

"""
#path to training data
source   = "development_set/"   
modelpath = "speaker_models/"
test_file = "development_set_test.txt"        
file_paths = open(test_file,'r')
"""
#path to training data
source   = "SampleData/"   

#path where training speakers will be saved
modelpath = "Speakers_models/"

gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models    = [cPickle.load(open(fname,'r')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
              in gmm_files]

error = 0
total_sample = 0.0


#print "Do you want to Test a Single Audio: Press '1' or The complete Test Audio Sample: Press '0' ?"
#take = int(raw_input().strip())
#if take == 1:
	#print "Enter the File name from Test Audio Sample Collection :"
path = "hey.wav"  
print "Testing Audio : ", path
sr,audio = read(source + path)
vector   = extract_features(audio,sr)
    
log_likelihood = np.zeros(len(models)) 
    
for i in range(len(models)):
        	gmm    = models[i]  #checking with each model one by one
        	scores = np.array(gmm.score(vector))
        	log_likelihood[i] = scores.sum()
    
winner = np.argmax(log_likelihood)
print "\tdetected as - ", speakers[winner]

#time.sleep(1.0)

import pyttsx
engine = pyttsx.init()
engine.say("hey")
engine.say(speakers[winner])
engine.runAndWait()
