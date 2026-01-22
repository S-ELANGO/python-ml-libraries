import numpy as np

months= np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

sales=[]

print("Enter the sales (in $1000) or each month")

while True:
    for month in months:
        value =float(input(f"{month}: "))
        sales.append(value)

    sales=np.array(sales) 
    print('\n --companysales analysis--')    
    print(f"Total sales: {sales.sum()}")
    print(f"Average sales: {sales.mean()}")
    print(f"Maximum sales: {sales.max()}")
    print(f"Minimum sales: {sales.min()}")
    
    best_month=months[sales.argmax()]
    worst_month=months[sales.argmin()]
    print('Best month sales',best_month)
    print('Best month sales',worst_month)

    above_avg=months[sales>sales.mean()]
    below_avg=months[sales<sales.mean()]

    print('Months above average sales',above_avg)
    print('Months below average sales',below_avg)

    break
