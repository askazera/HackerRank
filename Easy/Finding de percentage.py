'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.


Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks
obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

2 <= n <= 10
0 <= marks[i] <= 100
lenght of marks arrays = 3


Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0

56.00

'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        key, *value = input().split
        value = list(map(float,value))
        student_marks[key] = value
    query_name = input()
    output = student_marks[query_name]
    per = sum(output)/len(output)
    print("%.2f" % per)
