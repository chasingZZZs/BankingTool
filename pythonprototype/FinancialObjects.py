# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:05:03 2013

FinancialObject class definitions.

Base class FinancialObject - A financial object should have a 
name, description and balance. It must have methods to calculate 
debits(-) and credits (+) as well as a way to get the state of
the state of the account at a particular time as well as a 
list of state objects for a range of dates.

Abstract Class BankProduct - A Bank product should have fees, 
an interest rate and the date it was created/opened. 

Class Cash - Cash should just be the balance and be creditable 
or debitable.

@author: Joshua Chan
@version: 0.1
"""

from datetime import datetime

class FinancialObject:
    """
    FinancialObject Class
    A FinancialObject base class. 
    Includes the name, description and the balance.
    """

    name = u'Untitled'                  # Name of account
    description = u'No description.'    # Description of account
    
    def __init__(self, name, description, dateOpened):
        self.name = name
        self.description = description
        self.dateOpened = dateOpened
    
    def __call__(self):
        """Returns name and balance of Instrument."""        
        return self.name + ': ' + u'${:.2f}'.format(self.balance)
    
    def getStateIterator(self, events, dateFrom, dateTo):
        """ Returns an interator object of the state of the
        product for the range of dates given"""
        raise NotImplementedError
    
    def getState(self, events, date):
        """ Returns the state of the product at the given date"""
        raise NotImplementedError

    def printBalance(self):
        if self.balance >= 0:
            return u'${:.2f} CR'.format(self.balance)
        else:
            return u'${:.2f} DR'.format(self.balance)

class BankProduct(FinancialObject):
    """
    BankProduct Class
    Describes a product such as a bank account or loan 
    that is offered by a bank. 
    Intended to be used as an abstract class because 
    a loan may treat debits and dredits differently.
    """

    interestRate = 0.0
    fees = 0.0
    dateOpened = datetime.now()
    
    def __init__(self, \
                 name, description, \
                 interestRate, \
                 fees, chargePeriod, dateOpened):
        super(BankProduct, self).__init__(name, description, dateOpened)
        self.interestRate = interestRate
        self.fees = fees                # Dicstionary of fees with names
        self.chargePeriod = chargePeriod # Dictionary of charge periods and names

    
    def getStateIterator(self, events, dateFrom, dateTo):
        """ Returns an iterator object of the state of the
        product for the range of dates given"""
        pass
    
    def getState(self, events, date):
        """ Returns the state of the product at the given date"""
        pass
    
    
class Loan(BankProduct):
    def __init__(self, \
                 name, description, \
                 interestRate, \
                 fees, chargePeriod, offsetAccount, endDate, \
                 interestOnly, PMT, paymentPeriod, dateOpened):
        super(Loan, self).__init__(name, description, \
                                   interestRate, \
                                   fees, chargePeriod, dateOpened)
        self.offsetAccount = offsetAccount
        self.endDate = endDate
        self.interestOnly = interestOnly
        self.PMT = PMT
        self.paymentPeriod = paymentPeriod
    
    def getStateIterator(self, events, dateFrom, dateTo):
        """ Returns an iterator object of the state of the
        product for the range of dates given"""
        pass
    
    def getState(self, events, date):
        """ Returns the state of the product at the given date"""
        pass
    
    def getPayment(self, date):
        pass

    
class Equity(FinancialObject):
    def __init__(self, name, description, dateOpened):
        super(Equity, self).__init__(name, description, dateOpened)
    
    def getStateIterator(self, events, dateFrom, dateTo):
        """ Returns an interator object of the state of the
        product for the range of dates given"""
        pass
    
    def getState(self, events, date):
        """ Returns the state of the product at the given date"""
        pass
    
if __name__ == '__main__':
    """TODO: Test cases"""