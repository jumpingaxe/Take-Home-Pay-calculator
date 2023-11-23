"""Take Home Pay calculator - Tax Evaders
  katherine Donnelly    
  karl Ely              
  Alex Murphy           
  Libby Salter         

  key:
  taxinc = taxable income         taxpay = the amount of tax paid
  nat_ins = national insurance    takehome = take home pay
  tax40 = amount taxed at 40%     tax20 = amount taxed at 20%
  diff = difference over £100,000  reduced = half of difference
  untax = untaxable income        stu_lo = student loan repayment
  mon_break = monthly break down   nat_break = monthly break down of national insurance
  stu_break = monthly break down of student loans

  notes:
  - we calculated national insurance as 12% of taxable income based
  on information gathered from the goverment website.
  - we calculated student loan repayments based of plan 2
  the threshold is £27,295 and anything earnt over this amount is taxed at 9%
  based on information gathered from the save the student website
  """

income = float(input("What is your income? £"))
if income <= 12500:
    print("No taxable income")
    print("You don't pay national insurance")
    print("student loan repayment threshold not reached, so no repayment taken.")
    takehome = income
    nat_ins = 0
    stu_lo = 0
elif 12500 < income <= 50000:
    taxinc = income - 12500
    taxpay = taxinc * 0.2  # taxed at 20%
    nat_ins = taxinc * 0.12  # national insurance is 12% of your taxable income
    # used a nested if statement as in this bracket not all salaries may reach threshold for student loan repayments
    if income <= 27295:
        print("student loan repayment threshold not reached, so no repayment taken.")
        stu_lo = 0
    else:
        stu_lo = (income - 27295) * 0.09
    takehome = income - taxpay - nat_ins - stu_lo
elif 50000 < income <= 100000:
    taxinc = income - 12500  # taxable income
    tax40 = (income - 50000) * 0.4  # whatever is earnt over £50,000 is taxed at 40%
    tax20 = (50000 - 12500) * 0.2  # anything earnt under £50,000 is taxed at 20% after the tax free allowance
    taxpay = tax40 + tax20
    nat_ins = taxinc * 0.12
    stu_lo = (income - 27205) * 0.09
    takehome = income - taxpay - nat_ins - stu_lo
elif 100000 < income <= 150000:
    diff = income - 100000  # finding amount over £100,000
    reduced = diff / 2  # £1 is taxed for every £2
    untax = 12500 - reduced  # how much of the income is tax free
    tax40 = (income - 50000 + untax) * 0.4  # taxed at 40%
    tax20 = (50000 - 12500) * 0.2  # taxed at 20%
    totaltax = tax20 + tax40  # total tax paid
    taxinc = income - untax
    nat_ins = taxinc * 0.12
    stu_lo = (income - 27205) * 0.09
    takehome = income - totaltax - nat_ins - stu_lo
elif 150000 < income <= 10000000:
    tax20 = (50000 - 12500) * 0.2  # tax at 20% for the £50,000
    tax40 = (12500 + 100000) * 0.4  # add the £12,500 back on to the £100,000 then tax at 40%
    tax45 = (income - 150000) * 0.45  # tax whatever is above £150,000 at 45%
    total_tax = tax20 + tax40 + tax45
    nat_ins = income * 0.12  # no tax free allowance so whole salary is used to calculate national insurance
    stu_lo = (income - 27205) * 0.09
    takehome = income - total_tax - nat_ins - stu_lo

print(f"""your yearly take home pay is £{takehome}

you pay £{nat_ins} annually in national insurance contributions

your student loan repayment is £{stu_lo} annually
""")

# monthly break down of salary one:
mon_break = income / 12  # total take home pay each month
nat_break = nat_ins / 12  # monthly national insurance contributions
stu_break = stu_lo / 12  # monthly student loan repayments
print(f"""
your monthly take home pay is £{mon_break}

you pay £{nat_break} monthly in national insurance contributions

you pay £{stu_break} monthly in student loans
""")

# following is code that calculates take home pay for a second salary

income_2 = float(input("What income would you like to compare it to? £"))

if income_2 <= 12500:
    print("No taxable income")
    print("You don't pay national insurance")
    print("student loan repayment threshold not reached, so no repayment taken.")
    takehome_2 = 0
    nat_ins_2 = 0
    stu_lo_2 = 0
elif 12500 < income_2 <= 50000:
    taxinc = income_2 - 12500
    taxpay = taxinc * 0.2
    nat_ins_2 = taxinc * 0.12
    if income_2 <= 27295:
        print("student loan repayment threshold not reached, so no repayment taken.")
        stu_lo_2 = 0
    else:
        stu_lo_2 = (income_2 - 27295) * 0.09
    takehome_2 = income_2 - taxpay - nat_ins_2 - stu_lo_2
elif 50000 < income_2 <= 100000:
    taxinc = income_2 - 12500
    tax40 = (income_2 - 50000) * 0.4
    tax20 = (50000 - 12500) * 0.2
    taxpay = tax40 + tax20
    nat_ins_2 = taxinc * 0.12
    stu_lo_2 = (income_2 - 27205) * 0.09
    takehome_2 = income_2 - taxpay - nat_ins_2 - stu_lo_2
elif 100000 < income_2 <= 150000:
    diff = income_2 - 100000
    reduced = diff / 2
    untax = 12500 - reduced
    tax40 = (income_2 - 50000 + untax) * 0.4
    tax20 = (50000 - 12500) * 0.2
    totaltax = tax20 + tax40
    taxinc = income_2 - untax
    nat_ins_2 = taxinc * 0.12
    stu_lo_2 = (income_2 - 27205) * 0.09
    takehome_2 = income_2 - totaltax - nat_ins_2 - stu_lo_2
elif 150000 < income_2 <= 10000000:
    tax20 = (50000 - 12500) * 0.2  # tax at 20% for the £50,000
    tax40 = (12500 + 100000) * 0.4  # add the £12,500 back on to the £100,000 then tax at 40%
    tax45 = (income_2 - 150000) * 0.45  # tax whatever is above £150,000 at 45%
    total_tax = tax20 + tax40 + tax45
    nat_ins_2 = income_2 * 0.12
    stu_lo_2 = (income_2 - 27205) * 0.09
    takehome_2 = income_2 - total_tax - nat_ins_2 - stu_lo_2

print(f"""Your yearly take home pay for you second salary is £{takehome_2}

you pay £{nat_ins_2} anually in national insurance contributions with this salary

with this salary your student loan repayment is £{stu_lo_2} annually
""")

# calculation to compare the two slaries depending on which is bigger
if takehome < takehome_2:
    comparison = takehome_2 - takehome
    print(f"there is a £{comparison} difference between the two yearly take home pays")
elif takehome > takehome_2:
    comparison = takehome - takehome_2
    print(f"there is a £{comparison} difference between the two  yearly take home pays")
elif takehome == takehome_2:
    print("the two incomes have the same yearly take home pay")

# monthly break down of salary two:
mon_break2 = income_2 / 12  # total take home pay each month
nat_break2 = nat_ins_2 / 12  # monthly national insurance contributions
stu_break2 = stu_lo_2 / 12  # monthly student loan repayments
print(f"""
for this salary:
your monthly take home pay is £{mon_break2}

you pay £{nat_break2} monthly in national insurance contributions

you pay £{stu_break2} monthly in student loans""")

"""
  references:

  gov.uk (2022), [available at URL: https://www.gov.uk/national-insurance/how-much-you-pay] 
  (accessed, 29th december 2022) used to find information about how to calculate national insurance

 Bushi, R. and Van Hout,N., 2022. student loan repayment guide 2022. save the student [online]. 25th october.
 [available at URL: https://www.savethestudent.org/student-finance/student-loan-repayments.html#plan2] 
 (acessed, 2nd january 2023) used to gather information about calculating student loan repayments.

"""
