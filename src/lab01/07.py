instr=input("string: ")
answer=""
A=0
B=0
for i in range(len(instr)):
    if instr[i].isupper():
        answer+=instr[i]
        A=i
        for I in range(len(instr[A]),len(instr)):
            if instr[I] in "0123456789":
                B=I+1
                break
        for j in range(len(instr[B]), len(instr), B-A):
            answer+=instr[j]
    # if answer[-1]==".":
    #     break
print(answer)