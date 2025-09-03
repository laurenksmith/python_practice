# Control flow examples
"""
Equality operators:

    Operator    |         Meaning        |       Example
    ==          |           equal to     |       4 == 4 (True)
    !=          |         not equal to   |       4 != 3 (True)
     >          |        greater than    |       3 > 4 (False)
     <          |         less than      |       3 < 4 (True)
    >=          |greater than or equal to|       5 >= 5 (True)
    <=          | less than or equal to  |       5 <= 4 (False)
"""

# customer_age = 19
#
# if customer_age <= 12:
#     print('U, PG and 12 films are available')
# elif customer_age <= 15:
#     print('U, PG, 12 and 15 films are available')
# else:
#     print('All films are available')

time_of_day = 18

if time_of_day >= 5 and time_of_day < 12:
    print('Good morning')
elif time_of_day >= 12 and time_of_day < 17:
    print('Good afternoon')
elif time_of_day >= 17 and time_of_day < 20:
    print('Good evening')