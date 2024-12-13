#! /usr/bin/env python3
"""
https://projecteuler.net/problem=21
Paired with Brian at RC
"""

MAX = 10000

dict = {}
for num in range(0, MAX):
    sum_of_proper_divisors = 0
    for div in range(1, num):
        if num % div == 0:
            sum_of_proper_divisors += div
    dict[num] = sum_of_proper_divisors
# print(dict[220])  # should be 284
# print(dict[284])  # should be 220

sum_amicable = 0
for num in range(0, MAX):
    for num2 in range(num + 1, MAX):
        if dict[num] == num2 and dict[num2] == num:
            sum_amicable += num + num2

print(sum_amicable)

# Out of curiosity
# for num in range(0, MAX):
#     if num == dict[num]:
#         print("amicable with itself:", num)
