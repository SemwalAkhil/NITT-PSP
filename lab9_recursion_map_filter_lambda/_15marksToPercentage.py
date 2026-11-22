# 15. Write a program to calculate percentage scores from student marks using map and lambda.
# Input: None (data defined in the script)
# Output:
#   1:60.0%
#   2:60.0%
#   3:32.5%

marks = {
    1 : [60,80,30,70],
    2 : [90,60,50,40],
    3 : [10,50,30,40],
}
print("\n".join(map(lambda x: f"{x}:{sum(marks[x])/len(marks[x])}%",marks.keys())))
