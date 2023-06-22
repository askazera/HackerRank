'''

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.


'''


def cont_substrings(strings, substring):
    count = 0
    for i in range(len(strings)):
        if strings[i:i + len(substring)] == substring:
            count += 1
    return count


x = input()
sub = input()
print(cont_substrings(x, sub))