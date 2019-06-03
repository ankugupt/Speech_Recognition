from pydub import AudioSegment
from pydub.utils import make_chunks
import time
name=raw_input()
myaudio = AudioSegment.from_file(name + ".wav" , "wav") 
chunk_length_ms = 3000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

file= open("trainingDataPath.txt","a+")

for i, chunk in enumerate(chunks):
    chunk_name = (name + "_sample{0}.wav").format(i)
    file.write(name + "_sample%d.wav\n"% (i))
    print "exporting", chunk_name
    chunk.export(chunk_name, format="wav")
print "spilliting files completed"
print ".txt file overwrite complete"
