def can_provide_change(bills):
    five_count = 0
    ten_count = 0
    
    for bill in bills:
        if bill == 5:
            five_count += 1
        elif bill == 10:
            if five_count > 0:
                five_count -= 1
                ten_count += 1
            else:
                return False
        elif bill == 20:
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False
    
    return True

n=int(input())
bills =list(map(int,input().split()))
print(can_provide_change(bills))
'''
LEVEL-2/MEDIUM/POINTS: 40
Color Soda
Program Description :
You are an owner of a color soda shop, each color soda costs 5/-. Customers are standing in a queue to buy from you and buy one at a time. Each customer will only buy one soda and pay with either a 5/-, 10/-, or 20/- bill. You must provide the correct change to each customer so that the net transaction is that the customer pays 5/-.

NOTE: At first, you do not have any bill to provide changes with. You can provide changes from the bills that you get from the previous customers. 

Input Format :
 First line contains the length of the bills array.

  Second line contains an array of bills. 

Output Format :
Print a single line output containing True or False.

Input :
6

5 5 10 20 5 10


Output :
True


Constraints :
1< N <=10^6

0<= N[i] <=10^4
'''
