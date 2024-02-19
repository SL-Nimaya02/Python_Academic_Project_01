#Author - Nimaya Hansani
#Student ID - 20221392 - w1956125
#4COSC006C : Software Development
#Coursework - Part 2
#Meyer,M.(2022).How to take nested list as an input.?.Stackoverflow .
#Available from https://stackoverflow.com/questions/73477643/how-to-take-nested-list-as-an-input [ Accessed 29 November 2022 ].
another_set = 'y'
pass_credits = 0
defer_credits = 0
fail_credits = 0
total = 0
Progress = 0
trailer = 0
retriever = 0
Exclude = 0
Outcome_total = 0

Progress_list = []
module_trailer_list = []
module_retriever_list = []
Exclude_list = []



while another_set == 'y':
    while True:
            pass_credits = input("Please enter your credits at pass : ")
            if pass_credits.isdigit():
                pass_credits=int(pass_credits)
                if pass_credits not in range (0,121,20):
                    print ('Out of range.')
                else:
                    pass_credits=int(pass_credits)
                    break
            else:
                print("Intger required")
                

    while True:
            defer_credits=input("Please enter your credits at defer : ")
            if defer_credits.isdigit():
                defer_credits=int(defer_credits)
                if defer_credits not in range (0,121,20):
                    print("Out of range.")
                else:
                    defer_credits=int(defer_credits)
                    break
            else:
                print("Intger required")

    while True:
        fail_credits=input("Please enter your credits at fail :")
        if fail_credits.isdigit():
            fail_credits=int(fail_credits)
            if fail_credits not in range (0,121,20):
                print("Out of range.")
            else:
                fail_credits=int(fail_credits)
                break
        else:
            print("Intger required")
        
    total=pass_credits+defer_credits+fail_credits
    if (total!=120):
        print("Total incorrect.")
    else:
        total==120
        if pass_credits==120:
            print("Progress")
            Progress+=1
            Progress_list.append(pass_credits)
            Progress_list.append(defer_credits)
            Progress_list.append(fail_credits)
            
        elif (pass_credits==100):
            print("Progress(module trailer)")
            trailer+=1
            module_trailer_list.append(pass_credits)
            module_trailer_list.append(defer_credits)
            module_trailer_list.append(fail_credits)
            
        elif (fail_credits<=60):
            print("Module retriever")
            retriever+=1
            module_retriever_list.append(pass_credits)
            module_retriever_list.append(defer_credits)
            module_retriever_list.append(fail_credits)


        else:
            fail_credits>=80
            print("Exclude")
            Exclude+=1
            Exclude_list.append(pass_credits)
            Exclude_list.append(defer_credits)
            Exclude_list.append(fail_credits) 




    print()
    
    print("Would you like to enter another set of data?")
    another_set = input("Enter 'y' for yes or 'q' to quit and view results :")
    
    print()






Progress_length = int(len(Progress_list) / 3)

u = 0

for i in range(Progress_length):
    print("Progress - ",Progress_list[u],",",Progress_list[u+1],",",Progress_list[u+2])
    u = u + 3



module_trailer_length = int(len(module_trailer_list) / 3)

v = 0

for i in range(module_trailer_length):
    print("Progress (module trailer) - ",module_trailer_list[v],",",module_trailer_list[v+1],",",module_trailer_list[v+2])
    v = v + 3



module_retriever_length = int(len(module_retriever_list) / 3)

w = 0

for i in range(module_retriever_length):
    print("Module retriever - ",module_retriever_list[w],",",module_retriever_list[w+1],",",module_retriever_list[w+2])
    w = w + 3



Exclude_length = int(len(Exclude_list) / 3)

x = 0

for i in range(Exclude_length):
    print("Exclude - ",Exclude_list[x],",",Exclude_list[x+1],",",Exclude_list[x+2])
    x = x + 3
    

