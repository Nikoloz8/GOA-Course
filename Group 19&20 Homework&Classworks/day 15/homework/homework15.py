# კაჰუტი რაც გავაკეთეთ ამ კაჰუტზე ივარჯიშეთ, ჩნააწერი ნახეთ ხელახლა, 
# ამოიწერეთ ყველა კითხვა და დეტალურად ახსენით კომენტარის სახით პასუხი.


#კითხვა 1 

#რომელ ბიბლიოთეკას ვიყენებთ პითონში გეომეტრიული ფიგურების ასაგებად? 

#ეს არის turtle (from turtle import * )   

#კითხვა 2 

#რომელ ფუნქციას ვიყენებთ, როდესაც გვინდა, რომ terminal-ში მოვახდინოთ დაბეჭვდა?

#ვიყენებთ print ფუნქციას.

#კითხვა 3

#პითონის გამოყენებით შეუძლებელია ალგორითმების შექმნა.

#false (როგორც მინიმუმ შეგვიძლია გამოვიყენოთ if-else)

#კითხვა 4 

#ათწილადებზე სამუშაოდ რომელ მონაცემთა ტიპს ვიყენებთ?

#ვიყენებთ float-ს.

#კითხვა 5 

#რომელია პითონისთვის სწორი კომენტარი

#ჩემი ნაწერებიდან თითოეული კომენტარის მაგალითია :დ

#კითხვა 6 

#რომელ ფუქნციას ვიყენებთ მომხმარებლისგან terminal-ში ტექსტის მისაღებად?

#ჩვენ ვიყენებთ input-ს.

#კითხვა 7 

#input - იდან მიღებული ინფორმაცია ინახება String-ის სახით.

#its true

#კითხვა 8 

#როგორ ვამოწმებთ მონაცემთა ტიპს?

#მონაცემთა ტიპს ვამოწმებთ type ფუნქციით.

#კითხვა 9 

#რომელი ცვლადი ინახავს ათწილადს?

#პასუხია x = 10/2. x ცვლადის სახელს მინიჭების ოპერატორის დახმარებით გადაეცა მათემატიკური ოპერაცია 10/2.
#პითონში default გაყოფა აუცილებლად იძლევა float-ს, ანუ ამ შემთხვევაში 5.0.

#კითხვა 10

#რომელ ვარიანტშია პითონის ცვლადი სწორად შექმნილი?

#სწორია x = 12. აქაც, ცვლადის სახელს - x-ს მინიჭების ოპერატორის დახმარებით გადაეცემა integer 12.

#კითხვა 11 

#რას გამოიტანს კოდი? 

name = "Goal"

surname = "Orientadze"

age = 100

print(name + surname + age)

#ეს კოდი გამოიტანს error-ს. თავიდან ბოლომდე, რომ ავხსნათ კოდი: 
#name ცვლადს მინიჭების ოპერატორის დახმარებით გადაეცემა სტრინგის სახის Goal.
#ამის შემდეგ ცვლად surname-ს კვლავ მინიჭების ოპერატორის დახმარებით გადაეცემა სტრინგი Orientadze.
#ახლა კი გვაქვს age ცვლადი, რომელსაც ისევ მინიჭების ოპერატორის საშუალებით გადაეცემა 100, integer-ის სახით.
#ბოლოს კი ამ ყველაფერს ვპრინტავთ პრინტ ფუნქციის საშუალებით. აქ სწორედ იმის გამო იქნება error,
#რომ string-სა და integer-ს შორის ვერ მოხდება კონკატინაცია.

#კითხვა 12 

#რას გამოიტანს კოდი?

num1 = 10

num2 = 20

print(str(num1) + str(num2))

#ეს კოდი გამოიტანს 1020-ს და ახლა აგიხსნით რატომ. num1 ცვლადს მინიჭების ოპერატორის საშუალებით გადაეცემა integer-ი 10. num2-ს კი 20. 
#შემდეგ კი პრინტ ფუნქციაში num1-სა და num-2 ცვლადებში მოცემულ რიცხვებს ეცვლებათ მონაცემთა ტიპები ფუნქცია str-ს საშუალებით.
#საბოლოოდ ხდება string-ების კონკატინაცია, ანუ შედეგად მივიღებთ 10-ისა და 20-ის არა ჯამს, არამედ ნაერთს.

#კითხვა 13

#რას გამოიტანს კოდი, როდესაც მომხმარებელი შეიტანს 7-ს?

num1 = float(input("Enter number: "))
print(type(num1))

#აქ კოდი გამოიტანს <class 'int'> - ს და ავხსნი რატომ. ცვლად num1 - ს გადაეცემა input ფუნქცია, რომელიც მოთავსებულია float ფუნქციაში.
#float ფუნქცია input-ში მოცემულ სტრინგს შეუცვლის მონაცემთა ტიპს და იგი გახდება float.
#საბოლოოდ print ფუნქციის დახმარებით ჩვენ ტერმინალში ვითხოვთ num1-ში მყოფ input-ში მომხმარებლის მიერ შეტანილი 7-იანის ტიპს.
#print-ი, რომ ყოფილიყო type-ფუნქციის გარეშე, ჩვენ მივიღებდით 7.0-ს.

#კითხვა 14

#რას გამოიტანს კოდი

x = ((True and False) or (False or False))
y = ((False or True) and (False and True))
print((x and y) or True) 

#კოდი გამოიტანს True-ს. მოკლედ, რომ ავხსნათ, print ფუნქციაში მოცემული or და true-ც მიგვანიშნებს ამას.
#ვინაიდან და რადგანაც or ლოგიკურ ოპერატორს, თუ გვერდით ეყოლება 1 True მაინც, იგი საბოლოოდ True-ს გამოგვიტანს.

#კითხვა 15

#რას გამოიტანს კოდი, როდესაც მომხმარებელი შეიყვანს 20-ს.

age = int(input("Enter your age: "))
print(age > 18)

#თუ მომხმარებელი 20-ს ჩაწერს, კოდი გამოიტანს True-ს. მარტივად რომ ავხსნათ, 
#age ცვლადს გადავცემთ int ფუნქციაში მოქცეულ input ფუნქციას. აქედან გამომდინარე,
#input-ში მოქცეულ ნებისმიერ რიცხვზე შეგვიძლია ჩავატაროთ მათემატიკური ოპერაცია.
#ბოლოს print ფუნქციას გადავცემთ შედარებას age-სა და 18-ს შორის. თუ მომხმარებელი input-ში შეიტანს 20-ს,
#ეს იგივე იქნება, რაც print(20 > 18). ვინაიდან და რადგანაც 20 მართლაც მეტია 18-ზე, პასუხი აუცილებლად იქნება boolean ტიპის True.

#Done!!!