
"""

@author: UNISEPP
"""
#Calculating the financial metrics

import numpy as np

#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

revenue = np.array(revenue)
expenses = np.array(expenses)

# Profit for each month
prof = revenue - expenses
print(prof)

# Profit after tax for each month (tax = 30%)
prof_aftertax = 0.7 * prof
print(prof_aftertax)

# Profit margins for each month
prof_margins = prof_aftertax / revenue
print(prof_margins)

# Good month - Bad month
mean_year = prof_aftertax.mean()
for i in range (12):
    if prof_aftertax[i] > mean_year:
        print('good month')
    else : print('bad month')
    
# Best month
best_month = prof_aftertax.max()
print("The best month has this much profit after tax : ",best_month)

# Worst month
worst_month = prof_aftertax.min()
print("The worst month has this much profit after tax : ",worst_month)