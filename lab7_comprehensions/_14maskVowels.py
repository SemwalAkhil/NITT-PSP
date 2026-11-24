# 14. Write a program to mask vowels in a given phrase with underscores using string comprehension.
# Input: ("hello world"), ("python")
# Output: h_ll_ w_rld, pyth_n

string = input("Enter a phrase: ")
masked = "".join(["_" if i.lower() in "aeiou" else i for i in string ]) 
print(masked)
