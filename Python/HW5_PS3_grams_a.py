# Alex Grams
# 1163814
# Uses OOP to calculate a loan for a car

class Loan:
    def __init__(self, interestRate:float, loanDuration:float, loanAmount:float, borrowerName:str)->None:
        self.__interestRate = interestRate
        self.__loanDuration = loanDuration
        self.__loanAmount = loanAmount
        self.__borrowerName = borrowerName


    def getInterestRate(self)->float:
        return self.__interestRate


    def getLoanDuration(self)->float:
        return self.__loanDuration


    def getLoanAmount(self)->float:
        return self.__loadAmount


    def getBorrowerName(self)->str:
        return self.__borrowerName


    def setInterestRate(self, rate:float)->None:
        self.__interestRate = rate


    def setLoanDuration(self, years:float)->None:
        self.__loanDuration = years


    def setLoanAmount(self, amt:float)->None:
        self.__loanAmount = amt


    def setBorrowerName(self, name:str)->None:
        self.__borrowerName = name


    def getMonthlyPayment(self)->float:
        monthlyInterest = self.__interestRate / 1200
        monthlyPayment = self.__loanAmount * monthlyInterest / (1 - (1 /(1 + monthlyInterest) ** (self.__loanDuration * 12)))

        return monthlyPayment


    def getTotalPayment(self)->float:
        totalPayment = self.getMonthlyPayment() * self.__loanDuration * 12

        return totalPayment

def printLoan(loan:Loan)->None:
    """Prints inputted loan data"""
    print("The loan is for", loan.getBorrowerName())
    print("The montly payment is", format(loan.getMonthlyPayment(), '0,.2f'))
    print("The total payment is", format(loan.getTotalPayment(), '0,.2f'))


def main():
    interestRate = float(input("Enter yearly interest rate: "))
    loanDuration = float(input("Enter number of years as an integer: "))
    loanAmount = float(input("Enter loan amount: "))
    borrowerName = input("Enter borrower's name: ")
    loan = Loan(interestRate, loanDuration, loanAmount, borrowerName)
    
    printLoan(loan)
    cngLoan = input("Do you want to change the loan amount? Y for yes or enter to quit ")
    if cngLoan.lower() == "y":
        loanAmount = float(input("Enter new loan amount "))

        loan.setLoanAmount(loanAmount)
        printLoan(loan)


if __name__ == "__main__":
    main()


# Output
##>>> 1
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW5/HW5_PS3_grams_a.py ====
##Enter yearly interest rate: 2.5
##Enter number of years as an integer: 5
##Enter loan amount: 1000.00
##Enter borrower's name: John Jones
##The loan is for John Jones
##The montly payment is 17.75
##The total payment is 1,064.84
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 5000
##The loan is for John Jones
##The montly payment is 88.74
##The total payment is 5,324.21
##>>> 2
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW5/HW5_PS3_grams_a.py ====
##Enter yearly interest rate: 1.5
##Enter number of years as an integer: 10
##Enter loan amount: 10000
##Enter borrower's name: Joe
##The loan is for Joe
##The montly payment is 89.79
##The total payment is 10,774.98
##Do you want to change the loan amount? Y for yes or enter to quit 
##>>> 3
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW5/HW5_PS3_grams_a.py ====
##Enter yearly interest rate: 2.5
##Enter number of years as an integer: 20
##Enter loan amount: 5000
##Enter borrower's name: John Cena
##The loan is for John Cena
##The montly payment is 26.50
##The total payment is 6,358.83
##Do you want to change the loan amount? Y for yes or enter to quit 
##>>> 4
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW5/HW5_PS3_grams_a.py ====
##Enter yearly interest rate: 10
##Enter number of years as an integer: 5
##Enter loan amount: 1000
##Enter borrower's name: John Doe
##The loan is for John Doe
##The montly payment is 21.25
##The total payment is 1,274.82
##Do you want to change the loan amount? Y for yes or enter to quit 
##>>> 5
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW5/HW5_PS3_grams_a.py ====
##Enter yearly interest rate: 3.2
##Enter number of years as an integer: 7
##Enter loan amount: 20000
##Enter borrower's name: Charlie Brown
##The loan is for Charlie Brown
##The montly payment is 266.07
##The total payment is 22,350.10
##Do you want to change the loan amount? Y for yes or enter to quit y
##Enter new loan amount 30000
##The loan is for Charlie Brown
##The montly payment is 399.11
##The total payment is 33,525.15
