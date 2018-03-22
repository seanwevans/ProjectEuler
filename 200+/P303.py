# For a positive integer n, define f(n) as the least positive multiple of n that, written in base 10, uses only digits = 2.
# Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.
# Sum([f(n)//n for n in range(1,101)]) == 11363107
# Find Sum([f(n)//n for n in range(1,10001)])

# Try something smarter.
# Build a function F(N) which finds out the smallest number with {0, 1, 2} digits which is divisible by N.
# So for a given N the number which we are looking for can be written as SUM = 10^n * dn + 10^(n-1) * dn-1 .... 10^1 * d1 + 1*d0 (where di are the digits of the number).
# so you have to find out the digits such that SUM % N == 0 basically each digits contributes to the SUM % N with (10^i * di) % N
# I am not giving any more hints, but the next hint would be to use DP. Try to figure out how to use DP to find out the digits.
# for all numbers between 1 and 10000 it took under 1sec in C++. (in total)
