import re
hashtags = input("Enter hashtag: ").split()
print("\n".join(map(lambda x: " ".join(re.findall("([A-Z][a-z]*)",x)),hashtags)))