# Author: Alex Grams
#
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
    