# Check the truth of the statement ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z for all values of the predicate

x = [True, False]
y = [True, False]
z = [True, False]
check = 1
for i in x:
    for j in y:
        for k in z:
            if (not(x[i] or y[j] or [k]) == (not x[i] and not y[j] and not z[k])):
                print("True")
            else:
                print("False")
                check = 0
if check != 0:
     print('Expression is true')
else:
     print(' Expression is false')