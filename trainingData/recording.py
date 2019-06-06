import pyaudio 
import wave 
import time 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 45
name= raw_input()
WAVE_OUTPUT_FILENAME = name + ".wav"


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* Say Something for 60 seconds ")
time.sleep(1)
print("* WELCOME TO BARC")
print("Promoted by three industry associations,to develop a reliable television audience measurement system for India")
print("Broadcast Audience Research is a puzzle that has vexed broadcasters, advertisers, and advertising and media agencies in India for decades") 
print("A country with an estimated television audience of 183 million homes and growing, needed to have credible information about television viewing habits.BARC India is solving this puzzle uniquely")
print("Funded by the apex bodies representing the key stakeholders, it uses the latest technology in a transparent framework to give the Indian advertising and broadcast industry the ratings they so desperately need")
print("We draw our inspiration from Rubik’s Cube, and invite you to join us in Solving the complex Puzzle of broadcast audience measurement")


frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
