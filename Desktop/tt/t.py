data=[]
count=0
with open ("一百萬則資料.txt",mode="r" ) as file :
    for line in file:
        data.append(line)

    wc={}
    for d in data:
        words=d.split(" ")
        for word in words:
            if word in wc:
                wc[word]+=1
            else:
                wc[word]=1#新增key進字典
         
    for word in wc:
        if wc[word]>100:
            print(word,wc[word])

print(len(wc))
print(wc["the"])
    
    
while True:
    word=input("請問要查什麼字：")
    if word=="q":
        break
    if word in wc:
        print(word,"出現了",wc[word],"次")
    else:
        print("這個字沒在字典裡喔～")
    
print("感謝使用本查詢功能")
