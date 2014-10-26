# -*- coding: utf-8 -*-
"""
LoanEquation

Functions to calculate the various properties of a loan; the interest rate
payments, future value and other valuse of interest.
Based on the equation and solutions at
http://www.http://gnucash.org/docs/v2.4/C/gnucash-guide/loans_calcs1.html.
Created on Sat Apr 27 14:08:45 2013

@author: Joshua Chan
@version: 1.0
"""

from __future__ import division
from math import log, e, fabs


def toEffectiveRate(i, cont, CF, PF):
    if cont:
        ieff = e ** (i / PF) - 1.0            # Continuous compounding
    else:
        ieff = (1 + i / CF) ** (CF / PF) - 1.0  # Discrete compounding

    return ieff


def toNominalRate(ieff, cont, CF, PF):
    if cont:
        i = log((1 + ieff) ** PF)            # Continuous compounding
    else:
        i = CF * ((1 + ieff) ** (PF / CF) - 1.0)   # Discrete compounding

    return i


def payPeriods(i, cont, PV, PMT, FV, CF, PF, x):
    """
    Calculates n, the number of payment periods given the other parameters.
    All parameters positive.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    B = (1 + ieff * x) / ieff
    C = PMT * B

    return log((C - FV) / (C + PV)) / log(1 + ieff)


def presentValue(n, i, cont, PMT, FV, CF, PF, x):
    """
    Calculates PV, the present value of the loan given the other parameters.
    All parameters positive.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    A = (1 + ieff) ** n - 1
    B = (1 + ieff * x) / ieff
    C = PMT * B

    return -(FV + A * C) / (A + 1)


def periodicPayment(n, i, cont, PV, FV, CF, PF, x):
    """
    Calculates PMT, the periodic payments given the other parameters.
    All parameters positive.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    A = (1 + ieff) ** n - 1
    B = (1 + ieff * x) / ieff

    return -(FV + PV * (A + 1)) / (A * B)


def futureValue(n, i, cont, PV, PMT, CF, PF, x):
    """
    Calculates FV, the future value given the other parameters.
    All parameters positive.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    A = (1 + ieff) ** n - 1
    B = (1 + ieff * x) / ieff
    C = PMT * B

    return -(PV + A * (PV + C))


def equation(n, i, cont, PV, PMT, FV, CF, PF, x):
    """
    Definition of the equation for use with the iterative solver for the
    the interest rate.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    A = (1 + ieff) ** n - 1
    B = (1 + ieff * x) / ieff
    C = PMT * B

    return A * (PV + C) + PV + FV


def derivative(n, i, cont, PV, PMT, FV, CF, PF, x):
    """
    Definition of the equation for use with the iterative solver for the
    the interest rate.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    A = (1 + ieff) ** n - 1
    B = (1 + ieff * x) / ieff
    C = PMT * B
    D = (A + 1) / (1 + ieff)

    return n * D * (PV + C) - (A * C) / ieff


def nominalInterest(n, cont, PV, PMT, FV, CF, PF, x):
    """
    Calculates i, the nominal interest given the other parameters.
    All parameters positive.
    """

    if PMT == 0:
        ieff = (FV / PV) ** (1.0 / n) - 1.0
    else:
        """Solve iteratively for ieff using Newton-Raphson method"""
        """ Calculate initial guess """
        if PMT * FV >= 0:
            icurr = fabs((n * PMT + PV + FV) / (n * PV))
        else:
            if PV == 0:
                icurr = fabs((FV + n * PMT) /
                             3 * (PMT * (n - 1) ** 2 + PV - FV))
            else:
                icurr = fabs((FV - n * PMT) / 3 *
                             (PMT * (n - 1) ** 2 + PV - FV))

        """Calculate using Newton-Raphson method"""
        while True:
            diff = equation(n, icurr, cont, PV, PMT, FV, CF, PF, x)\
                / derivative(n, icurr, cont, PV, PMT, FV, CF, PF, x)
            inext = icurr - diff

            if fabs(diff) < 10 ** -10:
                break
            else:
                icurr = inext

        ieff = inext

    """Calculate nominal interest rate"""
    i = toNominalRate(ieff, cont, CF, PF)

    return i


def interestDue(i, cont, PV, PMT, CF, PF, x):
    """
    Calculates the interest due on a loan for the payment period.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    return (PV + x * PMT) * ieff


def principalPayed(i, cont, PV, PMT, CF, PF, x):
    """
    Calculates the principal component of a payment made for a loan.
    """

    """ Calculate effective interest rate """
    ieff = toEffectiveRate(i, cont, CF, PF)

    return PMT + (PV + x * PMT) * ieff
