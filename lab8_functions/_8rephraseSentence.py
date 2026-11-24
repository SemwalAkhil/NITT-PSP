# 8. Write a function to rephrase a sentence by replacing words with their synonyms from a dictionary.
# Input: ("the quick dog jumped over the lazy fox" 2 quick fast lazy idle), ("a good day" 1 good great)
# Output: the fast dog jumped over the idle fox, a great day

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
    sent = input("Enter sentence: ")
    n_words = int(input("Enter number of synonym words: "))
    syns = {}
    for i in range(n_words):
        word = input("Enter word: ")
        syn_list = input(f"Enter synonyms for {word}: ").split()
        syns[word] = syn_list
    print(rephraseSentence(sent, syns))
