# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:53:18 2013

Events Modules
Implements the banking events engine. Includes class with methods
to process events on implemented financial instruments.
Includes classes for States of accounts.


@author: Joshua Chan
@version: 1.0
"""

""" Events """

class Event:
    def __init__(self, value, description, date):
        self.value = value;
        self.description = description;
        self.date = date

class TransferEvent(Event):
    def __init__(self, value, description, date, debitAccs, creditAccs):
        super(Event, self).__init__(value, description, date)
        self.debitAccs = debitAccs
        self.creditAccs = creditAccs
        
class UpdateEvent(Event):
    def __init__(self, value, description, date, account, field):
        super(Event, self).__init__(value, description, date)
        self.account = account
        self.field = field

class RecurringEvent:
    def __init__(self, event, frequency, dateEnd):
        self.event = event
        self.frequency = frequency
        self.dateEnd = dateEnd
 
""" States"""
       
class State:
    def __init__(self, date, balance):
        self.date = date
        self.balance = balance

class SingleState(State):
    def __init__(self, date, balance, financialObject):
        super(SingleState, self).__init__(date, balance)
        self.financialObject = financialObject
     
class StateList:
    def __init__(self, states, financialObject):
        self.states = states
        self.financialObject = financialObject
        

""" Processing Outputs from States and Events """



