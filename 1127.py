# c = 0
# b = 0
# t = 0
# d = 0
# while True:
#     a = list()  
#     d = 0
#     n = int(input())
#     if n == -1:
#         break
#     for i in range(1, n):
#         if n%i == 0:
#             d = d+i
#             a.append(i)
#     if d != n or n == 0:
#         print(str(n) + " is NOT perfect.")
#     else:
#         answer = str(n)
#         for i in range(0, len(a)):
#             if t == 0:
#                 answer += " = " + str(a[i])
#                 t += 1
#             else:
#                 answer += " + " + str(a[i])

#         print(answer)
while True:
    n = int(input())
    
    f = []

    if n == -1:
        break
    
    for i in range(1, n):
        if n % i  == 0:
            f.append(i)
    
    if sum(f) == n:
        output = f"{n} = {f[0]}"
        for i in range(1, len(f)):
            output += f" + {f[i]}"
        print(output)
        
    else:
        print(f"{n} is NOT perfect.")