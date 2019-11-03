def reverse():
    number = int(input("Enter the number for sequence. Insert 0 when finished:"))
    if number == 0:
        print("End of sequence detected. Reversed sequnce:")
        return False
    else:
        reverse()
    print(number)


reverse()
