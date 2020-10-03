'''Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
Your task is to process a string with "#" symbols.'''

string = 'ab#c###db'









def backspaces(s):
    list = [chac for chac in enumerate(s)]
    clean = []
    for i,i2 in list:
        if i2 == '#':
            clean.append(list.remove(list[i2] and list[i2 - 1])
print(clean)
    final_string = ''.join(clean))
    return final_string

print(backspaces(string))



