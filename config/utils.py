from config.constants import (
    PAYCHECK_AMOUNT,
    PAYCHECKS_PER_YEAR,
    EMPLOYEE_BENEFIT_COST,
    DEPENDANT_COST,
)


def calculate_expected_benefits(dependants: int):
    yearly_salary = PAYCHECK_AMOUNT * PAYCHECKS_PER_YEAR

    yearly_benefits = EMPLOYEE_BENEFIT_COST + (dependants * DEPENDANT_COST)

    per_paycheck_gross = yearly_salary / PAYCHECKS_PER_YEAR
    per_paycheck_benefits = yearly_benefits / PAYCHECKS_PER_YEAR
    per_paycheck_net = per_paycheck_gross - per_paycheck_benefits

    return per_paycheck_gross, per_paycheck_benefits, per_paycheck_net, yearly_salary