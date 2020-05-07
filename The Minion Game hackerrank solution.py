def minion_game(string):
    vowel = 0
    consonant = 0
    for i in range(len(string)):
        if(string[i] in 'AEIOU'):
            vowel = vowel + len(string) - i
        else:
            consonant = consonant + len(string) - i
    if vowel < consonant :
        print("Stuart {}".format(consonant))
    elif vowel > consonant :
        print("Kevin {}".format(vowel))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
