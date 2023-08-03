import random
name=input("Enter your name:")
print(f"Hello,{name} \n There are 5 questions")
def gen_question():
    num1= random.randint(1,20)
    num2= random.randint(1,20)
    op=random.choice('+','-','*','/')

    if op=='+':
        ans= num1+num2
    elif op=='-':
        ans= num1-num2
    elif op=='*':
        ans= num1+num2
    else:
        ans= num1/num2
    return f"What is {num1} {op} {num2}", ans

def main():
    num_questions=5
    score=0
    for i in range(num_questions):
        question, crt_ans= gen_question()
        user_ans= int(input(question))

        if user_ans==crt_ans:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong! The correct answer is {crt_ans}\n")
    print(f"You got{score}/{num_questions} questions correct!")
 
    if __name__=="__main__":
       main()