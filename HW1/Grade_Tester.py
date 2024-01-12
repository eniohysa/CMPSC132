# Name: Enio Hysa
# Course: CMPSC132
# File Name: Grade_Tester.py and Grade.py
# Date: 1/9/24
#
# Short Description: Calculate the average of 5 grades and print the letter grade
import Grade


def main():
    scores = []
    for i in range(5):
        score = input(f'Enter grade #{i + 1}: ')
        scores.append(score)

    average = Grade.calc_average(scores)
    letter_grade = Grade.converter(average)
    print(f'Average: {average}\nLetter Grade: {letter_grade}')


if __name__ == '__main__':
    main()
    while True:
        rerun = input(f'Type \'Y\' to try new grades. Type anything else to close\n')
        if rerun == 'Y' or rerun == 'y':
            main()
        else:
            break
