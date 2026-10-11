print(
    {word:word[len(word)//2:]+word[:len(word)//2] for word in input("Enter a sentence: ").split()}
)