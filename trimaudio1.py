





from pydub import AudioSegment


#importing file from location by giving its path
sound = AudioSegment.from_mp3(file="lakshya.mp3")
AudioSegment.converter="ffmpeg.exe"
AudioSegment.ffmpeg="ffmpeg.exe"
AudioSegment.ffprobe="ffprobe.exe"

#Selecting Portion we want to cut
StrtMin = 0
StrtSec = 8

EndMin = 0
EndSec = 22

# Time to milliseconds conversion
StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = StrtMin*60*1000+EndSec*1000

# Opening file and extracting portion of it
extract = sound[StrtTime:EndTime]

# Saving file in required location
extract.export("lakshya1.mp3", format="mp3")

# new file portion.mp3 is saved at required location


