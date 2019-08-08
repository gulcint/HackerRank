"""
Given the names and grades for each student in a Physics class of  students,
 store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, 
and the second line contains their grade."""



if __name__ == '__main__':

    n = int(input())
    students_list = []

    for _ in range(n):
        name = input()
        score = float(input())
        students_list.append([name,score])

    scores = set(students_list[i][1] for i in range(n))
    scores = list(scores)
    scores.sort()
    
    students_list = [i[0] for i in students_list if i[1] == scores[1]]
    students_list.sort()

    for i in students_list:
        print(i)