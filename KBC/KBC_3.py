import file_of_KBC
from file_of_KBC import *
def kbc(i=0,j=0,k=0):   
    print(f"{i+1}.{question[i]}")
    print(f"a.{answer[k]}                b.{answer[k+1]}")
    print(f"c.{answer[k+2]}            d.{answer[k+3]}    ")
    user_answer=input(" Please Answer for above question : ")
    if (user_answer==corr_answer[j]or user_answer==corr_answer[j+1] or user_answer==corr_answer[j+2]):
        print("Answer is correct ")
        print(f" You have Won'{money[i]}'")
        kbc(i+1,j+3,k+4)
    else:
        print ("wrong Answer")
        print(f" You have Won'{money[i-1]}'")

kbc()