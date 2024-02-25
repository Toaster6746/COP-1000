# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
stateTax = salary*0.065
print ("State Tax: $" + str(stateTax))
federalTax = salary*0.28
print ("Federal Tax: $" + str(federalTax))
dependentDeduction = 0.025 * salary * numDependents
print ("Dependents: $" + str(dependentDeduction))
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
