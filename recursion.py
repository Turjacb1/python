def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    country=["ban","india","srilanka","maldip"]

    
    print_list(country)
