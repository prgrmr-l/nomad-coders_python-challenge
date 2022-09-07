# # 1. get_yearly_revenue (연간 매출 계산)

# # monthly_revenue (월간 매출) 취하고. revenue for a year (연간 매출)를 리턴.

# # 2. get_yearly_expenses (연간 비용 계산)

# # monthly_expenses (월간 비용) 취하고 expenses for a year (연간 비용)를 리턴.

# # 3. get_tax_amount (세금 계산)

# # profit (이익) 취하고 tax_amount (세금 금액) 를 리턴.

# # 4. apply_tax_credits (세액 공제 적용)

# # tax_amount (세금 금액) 그리고 tax_credits (세액 공제율) 취하고 amount to discount (할인된 금액)를 리턴.

# # Requirements (요구사항)

# # get_tax_amount 함수는 if/else 를 사용해야한다.
# # 만약 (if) profit이 100,000 이상이면. 세율은 25%가 되어야한다.
# # 아닌 경우에는 (else). 세율은 15%가 되어야한다.


# # Write your code here:

# # Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

# # # .............................................

# def get_yearly_revenue(monthly_revenue):
#     return monthly_revenue*12

# def get_yearly_expenses(monthly_expenses):
#     return monthly_expenses*12

# def get_tax_amount(profit):
#     if profit >=100000:
#         return profit*0.25
#     else:
#         return profit*0.15

# def apply_tax_credits(tax_amount, tax_credits):
#     return tax_amount-tax_amount*tax_credits

    
# # -----------------------------------------------------

# monthly_revenue = 5500000
# monthly_expenses = 2700000
# tax_credits = 0.01

# profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

# tax_amount = get_tax_amount(profit)

# final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

# print(f"Your tax bill is: ${final_tax_amount}")

