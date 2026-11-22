# 8. Write a program to map words to their halved-and-reversed forms using dictionary comprehension.
# Input: ("hello world"), ("python course")
# Output: {'hello': 'llohe', 'world': 'rldwo'}, {'python': 'honpyt', 'course': 'rsecou'}

print(
    {word:word[len(word)//2:]+word[:len(word)//2] for word in input("Enter a sentence: ").split()}
)