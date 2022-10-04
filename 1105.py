score=[[76,73,85],[88,84,76],[92,82,92],[82,91,85],[72,74,73]]
total=0
high=0
high_avg=0
for i in range(len(score)):
    print("student",i+1)
    summ=0
    for j in range (len(score[i])):
        print(" ",j+1,": ",score[i][j],sep="")
        summ+=score[i][j]          
    print(" sum:",summ)
    print(" avg: %.2f"%(summ/len(score[i])))
    total+=summ
    if(high_avg<summ/len(score[i])):
        high=j
        high_avg=summ/len(score[i])
    
print("total: ",total,", avg: %.2f"%(total/(len(score)*len(score[i]))),sep="")
print("highest avg: student %d: %.2f"%(high+1,high_avg))
