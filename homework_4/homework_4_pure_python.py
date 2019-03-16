##################### 4.1 #####################

resolution = int(input("Please enter the audio resolution in bit: "))
samplingRate = int(input("Please enter the sampling rate in Hz: "))
channelCount = int(input("Please enter the number of audio channels: "))
length = int(input("Please enter the length of the audio file in seconds: "))

# resolution tells us, how many bits we can use per smallest encoded unit
# sampling rate tells us, how many of these we can read in one second of audio
# channel count tells us, how many audio channels will play the and all need their own data stream
# Now we have the storage size of one second of audio ([samRate] times per second we save [res] bits [chCount] times)
# If we want the storage size of the whole thing we just need to multiply the result with the total seconds of the audio
# We now have the size in bit and divide by 8 (Bytes) * 1024 (KibiBytes) * 1024 (MibiBytes) so that we get the right number
fileSize = (resolution * samplingRate * channelCount * length) / (8 * 1024 * 1024)

print(f"\nThe .wav file will have a size of about {round(fileSize, 3)} MiB")

# In practice the file size will be larger than this, because there's file metadata associated to it.
# This includes a file name, artist or album information, possibly an album cover and all sorts of useful additional info


##################### 4.2 #####################

morseDict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..',
    'j': '.---','k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'r': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}

sentence = input("Please input your sentence here: ").lower()
print()
output = sentence.replace(' ', '/ ')

for morseCode in morseDict:
    if morseCode in sentence:
        output = output.replace(morseCode, f"{morseDict[morseCode]} ").strip()
        
print(f"The sentence \"{sentence}\" is \"{output}\" in morse code.")