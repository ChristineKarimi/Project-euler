#Problem: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#solution:

def smallest_m():

	start=1

	while True:

		if start%2==0 and start%3==0 and start%4==0 and start%5==0 and start%5==0 and start%6==0 and start%7==0 and start%8==0 and start%9==0 and start%10==0 and start%11==0 and start%12==0 and start%13==0 and start%14==0 and start%15==0 and start%16==0 and start%17==0 and start%18==0 and start%19==0 and start%20==0:

			print(start)