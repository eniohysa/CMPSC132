def calc_average(scores):
    # Calculate the average by iterating through the inputted list and adding the scores to a counter
    counter = 0
    for score in scores:
        counter += int(score)
    return counter/len(scores)


def converter(grade):
    # Make sure score from calc_average function is valid
    if grade < 0 or grade > 100:
        letter_grade = 'Invalid. Grade must be from 0-100.'
    # Assign letter grade based on score
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
