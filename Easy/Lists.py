"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types
listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

N = int(input('numero:'))
l = []
for i in range(N):
    comand = input().split() #função slipt cria uma lista com as strings inseridas no input
    if comand[0] == 'insert':
        l.insert(int(comand[1]), int(comand[2]))
    elif comand[0] == 'print':
        print(l)
    elif comand[0] == 'remove':
        l.remove(int(comand[1]))
    elif comand[0] == 'append':
        l.append(int(comand[1]))
    elif comand[0] == 'sort':
        l.sort()
    elif comand[0] == 'pop':
        l.pop()
    elif comand[0] == 'reverse':
        l.reverse()

