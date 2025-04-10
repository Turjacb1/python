word="turja"
with open("sample.txt","r") as f:
    data=f.read()
    newdata=data.replace("programmer","codder")
    if(newdata.find(word)!=-1):
        print("found")
    else:
        print("not found")


        
    print(newdata)

    with open("sample.txt","w")as f:
        f.write(newdata)
