#!/usr/bin/env python
# encoding: utf-8

from math import log,sqrt,exp
from scipy.stats import norm

def call_option_pricer(spot,strike,maturity,r,vol):
    d1=(log(spot/strike)+(r+0.5*vol*vol)*maturity)/vol/sqrt(maturity)
    d2=d1-vol*sqrt(maturity)
    price=spot*norm.cdf(d1)-strike*exp(-r*maturity)*norm.cdf(d2)
    return price

'''
当前价 spot : 2.45
行权价 strike : 2.50
到期期限 maturity : 0.25
无风险利率 r : 0.05
波动率 vol : 0.25
'''


print('期权价格:%.4f'%call_option_pricer(spot=2.45,strike=2.5,maturity=0.25,r=0.05,
                                    vol=0.25))
