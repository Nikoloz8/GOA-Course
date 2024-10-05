# 1) შექმენით სია, რომელიც თავდაპირველად იქნება ცარიელი, შემდეგ კი ამ სიაში ჩაამატეთ 10 ელემენტი.
list = []
list.append([1, 2, 3, 4, 5])

# 2) შექმენით ორი სია, ერთში თქვენი ხელით ჩაწერეთ ლუწი რიცხვები, მეორეში კენტი რიცხვები, შემდეგ კი ეს ორი სია გააერთიანეთ extend ის გამოყენებით.
even_list = [2, 4, 6, 8]
odd_list = [3, 5, 7, 9]
even_list.extend(odd_list)

# 3) შექმენით სია, რომელშიც იქნება 20 ელემენტი, შემდეგ კი დაბეჭდეთ თითოეული სათითაოდ for loopის გამოყენებით.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in numbers:
    print(numbers)
# 4) შექმენით რიცხვებით სავსე სია, რომელშიც იქნება 1 დან 20მდე ყველა რიცხვი, შემდეგ კი ამ სიიდან ამოშალეთ ყველა კენტი რიცხვი, ორივე სია დაბეჭდეთ.
full_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(full_of_numbers)
full_of_numbers.remove(1)
full_of_numbers.remove(3)
full_of_numbers.remove(5)
full_of_numbers.remove(7)
full_of_numbers.remove(9)
full_of_numbers.remove(11)
full_of_numbers.remove(13)
full_of_numbers.remove(15)
full_of_numbers.remove(17)
full_of_numbers.remove(19)
print(full_of_numbers)    


