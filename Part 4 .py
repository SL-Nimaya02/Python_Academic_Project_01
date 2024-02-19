acceptable_inputs = (0, 20, 40, 80, 100, 120)
pass_credits = 0
defer_credits = 0
fail_credits = 0
total = 0
Progress = 0
trailer = 0
retriever = 0
Exclude = 0
Outcome_total = 0
another_set = 'y'
dict_list=[]
final=[]


while another_set == 'y':
    dict = {'ID':0 , 'Outcome':0 , 'marks':0}
    Student_ID = str(input('Enter Your Student ID Number : '))
    dict['ID']=Student_ID

    try:
        pass_credits = int(input("Please enter your credits at pass :  "))
        defer_credits = int(input("Please enter your credits at defer :  "))
        fail_credits = int(input("Please enter your credits at fail : "))
    except ValueError:
        print('Integer Required')

        
    total = total= pass_credits + defer_credits + fail_credits


    if total != 120:
        print("Total incorrect.")

        
        
    else:
        total ==120
        if pass_credits == 120:
            print("Progress")
            marks=[pass_credits,defer_credits,fail_credits]
            dict['marks']=marks
            dict['Outcome']='Progress'
        elif pass_credits == 100:
            print("Progress (module trailer)")
            marks=[pass_credits,defer_credits,fail_credits]
            dict['marks']=marks
            dict['Outcome']='Progress (module trailer)'
        elif fail_credits >= 80:
            print("Exclude")
            marks=[pass_credits,defer_credits,fail_credits]
            dict['marks']=marks
            dict['Outcome']='Exclude'
        else:
            fail_credits <= 60
            print("Module retriever")
            marks=[pass_credits,defer_credits,fail_credits]
            dict['marks']=marks
            dict['Outcome']='Do not progress - module retriever'
    dict_li=[dict['ID'],dict['Outcome'],dict['marks']]
    dict_var= (f"{dict['ID']}:{dict['Outcome']}-{str(dict['marks'])[1:-1]}")
    dict_list.append(dict_var)
    print()
    print("Would you like to enter set of data?")
    another_set = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
    print()

print(' '.join(dict_list))



