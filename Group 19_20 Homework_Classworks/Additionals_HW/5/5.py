#Codewars solutions!

# 1)

def solution(string):
    reversed_string = ""
    length = len(string)
    while length > 0:
        length = length - 1
        reversed_string = reversed_string + string[length] 
    return reversed_string

# 2)

def summation(num):
    num = num + 1
    sum = 0
    while num > 0:
        num = num - 1
        sum = sum + num
    return sum

# 3) 
arr = [-3, 7, -9, 51, 59] #ეს სია შევქმენი მაგალითად.
def find_smallest_int(arr):
    smallest = arr[0] # აქ ვქმნი ცვლადს, რომელსაც ვუტოლებ arr სიაში მყოფ პირველ ელემენტს.
    for i in range(1, len(arr)): #აქ ვქმნი ციკლს 1 დან arr ლისთის სიგრძემდე.
        element = arr[i] #აქ ვქმნი element ცვლადს, რომელსაც ვუტოლებ arr ლისთში მყოფი ელემენტებიდან პირველის გარდა ყველას.
        if element < smallest: #აქ ვქმნი პირობას, რომ თუ ელემენტი ნაკლებია პირველ ელემენტზე, მაშინ იგი გაუტოლდება smallest ცვლადს. 
            smallest = element #ამის შემდეგ თუ ამ პირობას კიდევ შეხვდება ლისთში smallest ცვლადში მყოფ მნიშვნელობაზე ნაკლები რიცხვი,    იგი ყოველთვის გაუტოლდება smallest ცვლადს.
    return smallest