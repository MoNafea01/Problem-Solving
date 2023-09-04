'''
Given a Number N corresponding to a person's age (in days). Print his age in years, months and days, followed by its respective message "years", "months", "days".
Note: consider the whole year has 365 days and 30 days per month.

Input
Only one line containing a number N (0 ≤ N ≤ 106).

Output
Print the output, like the following examples.
'''
c1 = int(input())
years = c1 // 365
months = c1 % 365 // 30
days = c1 - months * 30 - years * 365
print(years,'years')
print(months,'months')
print(days,'days')
