questions = [
["Who Is Shah Rukh Khan?","WWE Wrestler","Actor","Astronaut","Plumber",2],
["What is The Capital of india","UP","New Delhi","Mumbi","Haryana",2],
["What is The Square Root Of 64:","6","8","10","12",1],
["Which Country is Know AS The Land Of The Rising Sun?","China","Japan","South Korea","India",2],
["Who Painted The Mona Lisa","Vincent Van Gogh","Pablo Picasso","Leonardo da vinci","claude Monet",3]
]


prize=[100000,10000,1000,200000,32000]
i=0
sum=0
for question in questions:

    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    #Check Whether The Answer Is Correct Or Not
    a=int(input("Enter Your Answer:1 for a, 2 for b, 3 for c, 4 for d:"))
    if (question[5])==a:
        print(f"Correct Answer:{question[5]}")
    else:
        print(f"Incorrect Answer, The Correct Answer was {question[5]}")
        print("Better Luck Next Time:")
        break
    sum+=prize[i]
    print(f"You Won {sum}")
    i+=1
    