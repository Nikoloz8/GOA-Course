#For Loop-ის მეშვეობით გამოიტანეთ 1-დან 20-მდე ციფრები, გამოიყენეთ <=

for i in range(20): #თუ 20-ის ჩათვლით, მაშინ range(21)
    if i > 0:
        print(i)

#```შექმენით ცვლადი, რომელსაც გაუტოლებთ 0-ს, შემდეგ კი While loop-ის მეშვეობით დაპრინტეთ 
# რაიმე წინადადება, სანამ შექმნილი ცვლადი არ გახდება 20-ის ტოლი```

variable = 0
while variable <= 20:
    print("რაიმე წინადადება")
    variable = variable + 1