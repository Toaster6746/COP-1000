#input
employeesName = str(input())
numberOfShifts = int(input())
numberOfTransactions = int(input())
transactionDollarValue = float(input())
productivityScore = transactionDollarValue /  numberOfTransactions / numberOfShifts
employeeBonus = 0
#if statments
if productivityScore <= 30:
    employeeBonus = 50
if 31 <= productivityScore <= 69:
    employeeBonus = 75
if 70 <= productivityScore <= 199:
    employeeBonus = 100
if productivityScore >= 200:
    employeeBonus = 200
#output
print("Employee Name: {0}".format(employeesName))
print("Employee Bonus: ${0}".format(employeeBonus))
