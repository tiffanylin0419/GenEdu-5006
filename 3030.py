num=float(input())
adjust=10*num**0.5

print("Original: %.2f"%num)
print("Adjusted: %.2f(+"%adjust,"%.0f)"%(adjust-num),sep="")
