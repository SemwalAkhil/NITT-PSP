# Convert sentence's words to piglatin
print(
        {
            word:word[1:]+word[0]+'x' for word in input("Enter sentence: ").split()
        }
    )