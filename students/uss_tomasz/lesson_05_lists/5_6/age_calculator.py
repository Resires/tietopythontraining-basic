# Problem Age calculator
from random import randint, seed


def age_calculator(peoples_age_list):
    """For given list of people's ages calculate
    average age of adults (age >= 18)
    count the children (age < 18)
    """
    adults_list = [i for i in peoples_age_list if i >= 18]
    average_adult = sum(adults_list)/len(adults_list)
    children_count = len([i for i in peoples_age_list if i < 18])
    return average_adult, children_count


seed(1)
group_of_people = [randint(1, 30) for i in range(10)]
print("Randomly chosen group of people (age) = ", group_of_people)
print("Average adult is {0[0]:.2f} years ald. "
      "There are {0[1]} children in this group".format(age_calculator(group_of_people)))
