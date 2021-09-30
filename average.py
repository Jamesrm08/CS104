testScore = int(0)
howManyEntered = int(0)
total = int(0)
average = int(0)

#Ask user for number of test scores, store as how many
howMany = int(input('How many test scores would you like to enter  '))
#As long as the amount of test scores the suer has entered is less than
#the amount of tests they want to enter
while (howManyEntered < howMany):
    testScore = int(input('Test Score  '))
    total += testScore
    howManyEntered += 1

average = float(total/howMany)
print('Your average is' + str(average))
