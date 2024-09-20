Questions=[
   
    ["Which language was used to create fb?","python","French","Java-Script","Php",4 ],

    ["Which language was used to create Website?","python","Web-development","Java-Script","Php",2],

    ["Which language was used to create game?","python-js","French-eng","Java-Script-C++","Php-Web",3],

    ["Which language was used to create Linux?","python-js","C Language","Java-Script-C++","Python-C Language",2],

    ["Which of the following is used to store collection of different data types? ","String","Array","Character","Structure",4],

    ["What is the correct value to return to the operating system upon the successful completion of a program? ","Program don't return any value",0,1,2,2],

    ["Who invented C programming language? ","Charles Babbage","Dennis Ritchie","Bill Gates","Lady Lovelace Ada",2],

    ["What is the capital of France? ","Paris","Italy","Canada","Mexico",1],

    ["Which planet is known as red planet? ","Venus","Mercury","Mars","Jupiter",3],

    ["Who is the present prime minister of india ?", "Narendra das Modi","Amit Shah","Aditya yoginath","jay-Shankar",1],
    
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,125000,2500000,5000000,10000000]

money=0
for i in range(0,len(Questions)):
    Question=Questions[i]
    print(f"\n -: Question for Rs.{levels[i]} :- \n")
    print(f"Question no.{i+1} :-> {Question[0]}")

    print(f"a. {Question[1]}     b. {Question[2] } ")
    print(f"c. {Question[3]}     d. {Question[4]} ")

    reply=int(input("Enter your answer (1-4) or 0 to Quit the game:- "))

    if(reply==0):
        money = levels[i-1]
        print("You entered zero to quit the game...")
  
    if(reply==Question[-1]): # Here Question[-1] is length of Questions which is 6 so (6-1=5),always index[5] element choice option is correct
        print(f"Congrat..it is Correct answer🥳🎊..You have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong Answer!😒🤦‍♂️..")
        break
print(f"You take home money is {money}")