principal=int(input("Enter the Principal Amount(in rupees):"))
rate_of_interest=float(input("Enter the Rate of Interest(in percentage per annum):"))
time=int(input("Enter the Time(years):"))
SI=(principal*rate_of_interest*time)/100
print(f'The Interest is Rs{SI}')
final_amt=SI+principal
print(f'The final amount is Rs{final_amt}')