def calculateGPA():
    # ask user how many classes they are taking
    numClasses = input("How many classes are you taking? ")
    # create array for storing Letter grades to be converted
    userLetterGrades = [] 
    # create array for storing user number grades
    userGrades = []
    # create array for storing credits per class
    userCredits = []
    # initialize total creditpoints to 0
    totalCredits = 0

    # loop asking for grades and credits per class and adding them to appropriate array
    for i in range(0, int(numClasses)):
        classGrade = input(f"Please enter the letter grade for class {i + 1}: ").upper()
        userLetterGrades.append(classGrade)

        classCredit = input(f"Please enter the # of credits for class {i + 1}: ")
        userCredits.append(int(classCredit))

    # dictionary with grade letters as keys and numbers as values
    grades = {"A":4.0, "A-":3.667, "B+":3.33, "B":3.0, "B-":2.67, "C+":2.333, "C":2.0, "C-":1.67, "D+":1.333, "D":1.0, "F":0.0}
   
    # loop to add the grade number to array storing number per class
    for item in userLetterGrades:
        userGrades.append(grades.get(item))
    
    #array for storing quality points -- each course's points multiplied by its credit hours
    qualityPoints = []
    #loops through the usersgrades and calculates the qualityPoints per class
    for i in range(0,len(userGrades)):
        g = userGrades[i] * userCredits[i]
        qualityPoints.append(g)

    qp = 0.0
    #loop to add qualityPoints for total points
    for item in qualityPoints:
        qp += item

    #loop to add up total number of userCredits
    for item in userCredits:
        totalCredits += item

    # variable to store the final gpa number
    final = float(qp/totalCredits)

    return final

# prints the calculateGPA function
print(calculateGPA())
