
# imports
import csv 


# global variables
data = []
groupID = input("Enter group ID: ")
serviceProviderID = input("Enter service provider ID: ")
domain = input("Enter domain: ")
taskCount = 1

# sourceCode________
# reads in the file data and adds it to the data list
with open('Files/data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # reads a line to miss the header
    next(csvfile)

    # reads in the data and adds it to the data list
    for row in csvreader:
        data.append(row[0])

# asks user which method they would like to use
userAnswer = input('''
    How would you like to format the users, option 1 or option 2? 

    Option 1:
        <fullNumber>@<domain>
    Option 2:
        <lastFourDigits>@<domain>

    Please enter 1 or 2: ''')

# depending on the user's answer, the script will format the users
if userAnswer == '1':
    
    with open('Files/data.csv', 'w') as dataFile:
        
        csvwriter = csv.writer(dataFile)

        dataFile.write('task' + ',' + 'userId' + ',' + 'serviceProviderId' + ',' 'groupId' + ',' + 'index' + '\n')

        for row in data:
            dataFile.write('user.delete' + ',' + (str(row) + '@' + str(domain)) + ',' + serviceProviderID + ',' + groupID + ',' + str(taskCount) + '\n')
            taskCount = taskCount + 1

# depending on the user's answer, the script will format the users
elif userAnswer == '2': 
    with open('Files/data.csv', 'w') as dataFile:
        
        csvwriter = csv.writer(dataFile)

        dataFile.write('task' + ',' + 'userId' + ',' + 'serviceProviderId' + ',' 'groupId' + ',' + 'index' + '\n')

        for row in data:
            dataFile.write('user.delete' + ',' + (str(row[-4:]) + '@' + str(domain)) + ',' + serviceProviderID + ',' + groupID + ',' + str(taskCount) + '\n')
            taskCount = taskCount + 1

# prints to terminal the script has worked
print('Files/data.csv is ready for upload')