class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # tax=0
        # lower=0
        # idx=0

        # while income>0:
        #     br=brackets[idx]
        #     idx+=1
        #     upper=br[0]
        #     percent=br[1]

        #     taxable=min(income,upper-lower)
        #     tax+=taxable*(percent/float(100))
        #     lower=upper
        #     income=income-taxable
        # return tax

        remaining_salary = income
        total_tax = 0
        previous_tax_bracket = 0

        for bracket_limit, tax_rate in brackets:
            if bracket_limit is None:
                total_tax += remaining_salary * tax_rate
                break
            if remaining_salary <= 0:
                break

            taxable_bracket = min(
                remaining_salary, bracket_limit - previous_tax_bracket
            )

            total_tax += taxable_bracket * (tax_rate / float(100))

            remaining_salary -= taxable_bracket
            previous_tax_bracket = bracket_limit
        return total_tax
        # time complexity is O(n)
        # space complexity is O(n)
