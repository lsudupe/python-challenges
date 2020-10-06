'''Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
Your task is to process a string with "#" symbols.'''

string = 'abc#d##c'


'''def clean_string(s):
    list = [i for i in s]
    print(list)
    index = [idx-1  for (idx,char) in enumerate(list) if char == '#']
    print(index)
    one_list = [i3 for (i2,i3) in enumerate(list) if i2 not in index] 
    for a in one_list:
        if a == '#':
            one_list.remove(a)
    print(one_list)      ''' 
   
    


'''def clean_string(s):
    list = [chac for chac in s]
    for i in list:
        if i == '#':
            list.remove(i-1) and list.remove(i)
    print(list)'''

def clean_string(s):
    list = [i for i in s]
    #while '#' in list:
    for i2, i3 in enumerate(list):
        if i3 == '#':
                        print(list)
            list.remove(list[i2-1])
                        list.remove(i3)
            
    print(list)
clean_string(string)



'''a = [1, 2, 'e', 4, 't', 6, 7]

print( 'e' in a)'''