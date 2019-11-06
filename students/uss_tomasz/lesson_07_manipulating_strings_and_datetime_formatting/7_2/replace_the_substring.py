message = "Given a string. Replace in this string all the numbers 1 by the word one. Even if it is 11."
print("Original message =", message)
while message.find("1") != -1:
    position = message.find("1")
    message = message[:position] + "one" + message[position+1:]
print("Replaced '1' with 'one' =", message)
