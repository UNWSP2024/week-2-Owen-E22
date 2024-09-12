
def average_age():
    # Get User Input
    age1 = int(input('Age of friend 1:'))
    age2 = int(input('Age of friend 2:'))
    age3 = int(input('Age of friend 3:'))
    age4 = int(input('Age of friend 4:'))
    age5 = int(input('Age of friend 5:'))

    # Sum ages
    ages_total = age1 + age2 + age3 + age4 + age5
    print('Age total:', ages_total)
    # Average the ages
    mean = ages_total / 5
    # Print the results
    print('Average age is ',mean)
# Line which calls the above function.
average_age()