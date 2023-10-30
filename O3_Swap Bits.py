'''
Swap Bits
Program Description :
You are developing a utility function for a computer system that allows users to swap a specified number of bits at two given positions (measured from the right side) in the binary representation of a number X. Your task is to write a Python program that takes the following inputs:

X: The decimal number for which you need to perform the bit swap.

pos1: The first position (0-based index) from the right side.

pos2: The second position (0-based index) from the right side.

N: The number of bits to swap.

The program should perform the following steps:

Convert the decimal number X into its binary representation.

Swap the N bits at the given positions pos1 and pos2 from the right side.

Convert the modified binary representation back to a decimal number.

Return the resulting decimal number.

Input Format :
You will be given X, P1, P2, N separated by a space.
 

Output Format :
A number result in a single line.
 

Input :
47 1 5 3


Output :
227


Constraints :
1<= X <=10^6

1<= p1, p2 <=32
'''
def swapBits(x, p1, p2, n):
	set1 = (x >> p1) & ((1<< n) - 1)
	set2 = (x >> p2) & ((1 << n) - 1)
	xor = (set1 ^ set2)
	xor = (xor << p1) | (xor << p2)
	result = x ^ xor
	return result
x,p1,p2,n=map(int,input().split())
res = swapBits(x,p1,p2,n)
print(res)
