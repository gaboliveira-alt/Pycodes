
from datetime import datetime

from dateutil.relativedelta import relativedelta

loan_amount: int = 1000000
loan_date = datetime.strptime("2020-12-20", "%Y-%m-%d")
loan_date_final = datetime.strptime("2025-12-20", "%Y-%m-%d")

dates_loan = relativedelta(loan_date, loan_date_final)

date_installments: list[datetime] = []
while loan_date <= loan_date_final:
    date_installments.append(loan_date)
    loan_date += relativedelta(months=+1)

installments_number: int = len(date_installments)
installment_value: float = loan_amount / installments_number

for date in date_installments:
    print(date.strftime("%Y/%m/%d"), f"R${installment_value:,.2f}")
