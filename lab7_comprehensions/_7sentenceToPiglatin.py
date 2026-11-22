# 7. Write a program to map words in a sentence to their Pig Latin forms using dictionary comprehension.
# Input: ("hello world"), ("python lab")
# Output: {'hello': 'ellohx', 'world': 'orldwx'}, {'python': 'ythonpx', 'lab': 'ablx'}

print(
        {
            word:word[1:]+word[0]+'x' for word in input("Enter sentence: ").split()
        }
    )