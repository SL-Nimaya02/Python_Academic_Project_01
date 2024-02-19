#Author - Nimaya Hansani
#Student ID - 20221392 - w1956125
#4COSC006C : Software Development
#Coursework - Part 1

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
        elif (pass_credits==100):
            print("Progress(module trailer)")
            trailer+=1
        elif (fail_credits<=60):
            print("Module retriever")
            retriever+=1
        else:
            fail_credits>=80
            print("Exclude")
            Exclude+=1

    print()
    print("Would you like to enter another set of data?")
    another_set = input("Enter 'y' for yes or 'q' to quit and view results :")
    print()
    
print("-----------------------------------------------------------")

print("Histogram")


print("Progress ",Progress,"  : ",Progress*"*")
print("Trailer ",trailer,"   : ",trailer*"*")
print("Retriever ",retriever," : ",retriever*"*")
print("Excluded ",Exclude,"  : ",Exclude*"*")
 
print()
Outcome_total = Progress + trailer + retriever + Exclude
print(Outcome_total," Outcomes in total.")

print("-----------------------------------------------------------")











        
    
    
    
    
    
    
    
            
                
