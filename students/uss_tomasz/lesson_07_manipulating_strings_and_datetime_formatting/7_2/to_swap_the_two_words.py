two_word_message = "Run Forrest"
space_position = two_word_message.find(" ")
new_message = two_word_message[(space_position+1):] + " " + two_word_message[:space_position]
print("Original message = ", two_word_message)
print("Swapped message =  ", new_message)
