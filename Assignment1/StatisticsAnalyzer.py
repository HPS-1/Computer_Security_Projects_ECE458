class letter_freq_pair:
    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq


ciphertext = ""
N = int(input("Please specify the value of N: "))

#read cipher text
try:
    f = open("CipherText.txt", "r")
except FileNotFoundError:
    print("Error: CipherText.txt not found!")
else:
    ciphertext = f.read()
    f.close()
    print("CipherText successfully retrieved")

subsequences = {}
cipherlen = len(ciphertext)

#initialize subsequences
for group_index in range(N):
    subsequences.update({group_index:""})

text_index = 0
temp1 = 'a'

#retrieving subsequences
while text_index < cipherlen:
    for group_index in range(N):
        temp1 = ciphertext[text_index]
        subsequences[group_index] = subsequences[group_index] + temp1
        text_index += 1
        if text_index >= cipherlen:
            break

#print subsequences
print("Subsequences are:")
for group_index in range(N):
    print("Subsequence", group_index, ":",subsequences[group_index])

temp2 = 'a'
key_guess = ""
flag = True
#analyze subsequences
letter_freqs = []
f1 = open("Statistics.txt", "w")
for group_index in range(N):
    letter_freqs = []
    for letter_index in range (26):
        temp2 = chr(97 + letter_index)
        letter_freqs.append(letter_freq_pair(temp2, subsequences[group_index].count(temp2)/len(subsequences[group_index])))
    letter_freqs.sort(key=lambda x: x.freq, reverse=True)
    f1.write("////////////////////////////////////////\nSubsequence " + str(group_index) + " statistics:\n")
    print("Subsequence", str(group_index), "statistics:")
    for letter_index in range (26):
        f1.write("Letter: " + str(letter_freqs[letter_index].letter) + "   freq: " + str(letter_freqs[letter_index].freq) + " \n")
        print("Letter:", letter_freqs[letter_index].letter, "freq:", letter_freqs[letter_index].freq)
    if ord(letter_freqs[0].letter) >= 101:
        key_guess += chr(97 + ord(letter_freqs[0].letter) - 101)
    else:
        key_guess += chr(ord(letter_freqs[0].letter) - 97 + 119)
    if letter_freqs[0].freq < 0.1:
        flag = False
f1.write("////////////////////////////////////////\nKey guessed based on the highest-frequency letter in each subsequence is: " + key_guess)
print("Key guessed based on the highest-frequency letter in each subsequence is:", key_guess)
f1.close()
if flag:
    print("Bingo!")
else:
    print("Bruhhhhhhhhh")
print("Statistics analyzation completed. The statistics is stored in Statistics.txt")
        

