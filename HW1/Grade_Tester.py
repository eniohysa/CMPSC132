# Name: Enio Hysa
# Course: CMPSC132
# File Name: Grade_Tester.py and Grade.py
# Date: 1/9/24
#
# Short Description: Calculate the average of 5 grades and print the letter grade
import Grade


def main():
    # Create a list to store user scores
    scores = []
    for i in range(5):
        # Get 5 scores from user and append them to a list
        score = int(input(f'Enter grade #{i + 1}: '))
        # Make sure the scores are valid
        while score > 100 or score < 0:
            score = int(input(f'Must be between 0-100. Enter grade {i + 1}: '))
        scores.append(score)

    # Call the functions from the Grade module and print the average and letter grade
    average = Grade.calc_average(scores)
    letter_grade = Grade.converter(average)
    print(f'Average: {average}\nLetter Grade: {letter_grade}')


if __name__ == '__main__':
    main()
    while True:
        # Prompt user to rerun the code by typing Y or y
        rerun = input(f'Type \'Y\' to try new grades. Type anything else to close\n')
        if rerun == 'Y' or rerun == 'y':
            main()
        else:
            break

''' Testing Run Data:
Enter grade #1: 101
Must be between 0-100. Enter grade 1: 100
Enter grade #2: 97
Enter grade #3: 99
Enter grade #4: 45
Enter grade #5: 89
Average: 86.0
Letter Grade: B
Type 'Y' to try new grades. Type anything else to close
n
'''