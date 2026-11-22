# 8. Write a function to rephrase a sentence by replacing words with their synonyms from a dictionary.
# Input: sent="the quick dog jumped over the lazy fox", syns={"quick": ["fast"], "lazy": ["idle"]}
# Output: the fast dog jumped over the idle fox

def rephraseSentence(sentence: str, synonyms: dict):
    words = sentence.split()
    new_words = []
    for w in words:
        if w in synonyms and len(synonyms[w]) > 0:
            new_words.append(synonyms[w][0])
        else:
            new_words.append(w)
    return " ".join(new_words)

if __name__ == "__main__":
    syns = {"quick": ["fast", "rapid"], "lazy": ["idle", "sluggish"]}
    sent = "the quick dog jumped over the lazy fox"
    print(rephraseSentence(sent, syns))
