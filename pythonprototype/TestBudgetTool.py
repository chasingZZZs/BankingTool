# -*- coding: utf-8 -*-
"""
Test script for checking code and determine optimal loan schedule

Created on Sat Apr 27 19:12:15 2013

@author: joshua
"""

import LoanEquation

""" Initialise accounts """

""" Initialise events """

""" Calculate accounts """

""" Plot accounts """

"""*************************************************************************"""
""" General back of envelope calcs """

""" BreakFree package vs standard variable total payments """ 
bf = LoanEquation.periodicPayment(300, 0.0533, False, 336000, 0, 360, 12, 0)
bf_total = bf * 360
norm = LoanEquation.periodicPayment(24*30, 0.064, False, 336000, 0, 360, 24, 0)
norm_total = norm * 360
diff_loan = bf_total - norm_total

norm_fees = 600+5*360 + 10 * 360 
bf_fees = 375 * 30

total_bf = -bf_total + bf_fees
total_norm = -norm_total + norm_fees

total_diff = total_bf - total_norm

simp = LoanEquation.periodicPayment(360, 0.057, False, 300000, 0, 12, 12, 0)
simp_total = simp * 360
simp_fees = 600

total_simp = -simp_total + simp_fees