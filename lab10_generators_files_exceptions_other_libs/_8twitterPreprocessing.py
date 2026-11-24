import re
from functools import reduce

compose = lambda *fs: reduce(lambda f, g: lambda x: g(f(x)), fs)

lower = lambda t: t.lower()
no_url = lambda t: re.sub(r"http\S+", "", t)
no_tags = lambda t: re.sub(r"@\w+|#", "", t)
only_alpha = lambda t: re.sub(r"[^a-z\s]", "", t).strip()
no_stops = lambda t: [w for w in t.split() if w not in {"is", "the", "a", "at"}]

preprocess = compose(lower, no_url, no_tags, only_alpha, no_stops)

tweet = input("Enter tweet: ")
print(preprocess(tweet))
