message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

print(len(message))

for i in range(len(message)):
    chunk = message[i:i + 12]
