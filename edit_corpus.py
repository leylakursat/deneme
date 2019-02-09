f = open('corpus1.txt')

message = f.read()

cases = message.split('\n')

print(cases)

f.close()





###SpeakerA(\d+).(\d+)?t(\d+)(.\d+)?/g