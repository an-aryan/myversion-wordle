import random

with open("word.txt", 'r') as file:
    alltext = file.readlines()
    # print(alltext[45])
    my_word = random.choice(alltext)
    # print(f"word selected is {my_word}")
    ans = []
    for letter in my_word:
        if(letter!='\n'):
            ans.append(letter)
    # print(ans)
    for i in range(6):	
        
        while True:
            guess = input('Enter a five letter word: ')
            flag = False
            if (guess+"\n") not in alltext:
                print("Word not found in list")
                flag = True
            for x in guess:
                    if x.lower() < 'a' or x.lower() > 'z':
                        flag = True
            if flag == True:
                print("This is not a valid word")
            elif len(guess)==5:
                break
            else:
                print('This is not a five letter word')     
        guess1 = []
        for letter in guess:
            guess1.append(letter)

        print(guess1)
        
        import colorama
        from colorama import Back, Fore, Style

        checker=[0,0,0,0,0]
        for x in range(5):
            for y in range(5):
                if(guess1[x]==ans[y]):
                    if(x==y):
                        checker[x] = 1
                        break
                    else:
                        checker[x]= 2
            
        for x in range(5):
            if checker[x]==1:
                print(Fore.GREEN+ guess[x])
                print(Style.RESET_ALL)
            elif checker[x]==2:
                print(Fore.BLUE+ guess[x])
                print(Style.RESET_ALL)
            else:
                print(Fore.RED+ guess[x])
                print(Style.RESET_ALL)
        check = True
        for x in range(5):
            if(checker[x]!=1):
                check  = False
        
        if check == True:
            print("\n*************************************YOU WIN************************************")
            break
        else:
            print(f"\n{6-i-1} chances left!!\n")
            print("***********************************************************************************")
    print(ans)

                


    
# import random
# with open("word.txt", 'r') as file:
#     alltext = file.readlines()
#     # print(alltext[45])
#     my_word = random.choice(alltext)
#     # print(f"word selected is {my_word}")
#     ans = []
#     for letter in my_word:
#         if(letter!='\n'):
#             ans.append(letter)
#     print(ans)
#     for i in range(6):
#         print("THIS IS YOUR {} TRY\n".format(i+1))	
        
#         while True:
#             guess = input('Enter a five letter word: ')
#             flag = False
#             for x in guess:
#                     if x.lower() < 'a' or x.lower() > 'z':
#                         flag = True
#             if flag == True:
#                 print("This is not a valid word")
#             elif len(guess)==5:
#                 break
#             else:
#                 print('This is not a five letter word')     
#         # print(guess)
#         guess1 = []
#         for letter in guess:
#             guess1.append(letter)

#         print(guess1)
        
#         import colorama
#         from colorama import Fore, Back, Style

#         flag = 0
#         for x in range(5):
#             flag = 0
#             for y in range(5):
#                 if(guess1[x]==ans[y]):
#                     if(x==y):
#                         flag = 1
#                         break
#                     else:
#                         flag = 2
#             if flag==1:
#                 print(Fore.GREEN+ guess[x])
#                 print(Style.RESET_ALL)
#             elif flag==2:
#                 print(Fore.BLUE+ guess[x])
#                 print(Style.RESET_ALL)
#             else:
#                 print(Fore.RED+ guess[x])
#                 print(Style.RESET_ALL)
#         check = 0
#         for x in range(5):
#             if(guess1[x]!=ans[x]):
#                 check = 1
        
#         if check == 0:
#             print("**************************************!!YOU WON!!***********************************")
#             break
#         else:
#             print(f"\n{6-i-1} tries remaining!!\n")
#             print("****************************************************************\n")
        

