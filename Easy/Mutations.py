'''

Task
Read a given string, change the character at a given index and then print the modified string.
'''

def mutation_str(string, position, character):

    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    string = input('')
    position = int(input(''))
    character = input('')
    print(mutation_str(string, position,character))
