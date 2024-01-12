def calc_average(scores):
    counter = 0
    for score in scores:
        counter += int(score)
    return counter/len(scores)


def converter(grade):
    if grade < 0 or grade > 100:
        letter_grade = 'Invalid. Grade must be from 0-100.'
    elif grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade
