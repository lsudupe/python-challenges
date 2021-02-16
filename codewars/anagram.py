'''Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none.'''


def anagrams(word, words):
    dic1 = {}
    list2 = []

    for i in word:
        dic1[i] = dic1.get(i, 0) + 1
    print(dic1)

    for letter in words:
        dic2 = {}
        for i in letter:
            dic2[i] = dic2.get(i, 0) + 1
        list2.append(dic2)
    print(list2)       




print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
#anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) 
#anagrams('laser', ['lazing', 'lazy',  'lacer']) 
