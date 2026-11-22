# 17. Write a program to mask vowels and spaces in a given phrase with underscores.
# Input: ("hello world"), ("nit trichy")
# Output: h_ll__w_rld, n_t_tr_chy

string = input("Enter a phrase: ")
masked = string.replace("a", "_")
masked = masked.replace("e", "_")
masked = masked.replace("i", "_")
masked = masked.replace("o", "_")
masked = masked.replace("u", "_")
masked = masked.replace(" ", "_")
print(masked)
