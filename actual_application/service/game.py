from data import creature as data

def get_word()->str:
    word = data.get_random_creature_name()
    return word

def get_score(word, guess)->str:
    if len(guess) != len(word):
        return 'M' * len(word)
    H, C, M = 'H', 'C', 'M'
    score = []
    for i in range(len(guess)):
        if word[i] == guess[i]:
            score.append(H)
        elif guess[i] in word:
            score.append(C)
        else:
            score.append(M)
    return ''.join(score)