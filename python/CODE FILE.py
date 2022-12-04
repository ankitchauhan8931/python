from datetime import date

def get_diff(date1,date2):
    delta=date2-date1
    print("\n")
    print("\t\t\t\t",delta.days,"days")

    
print("                                 welcome to age calculator     ")


ch="y"
while ch == "y":
    print("\n\n")
    #taking input from the user in dd/mm/yyyy format
    
    date1=list(map(int,input("enter date of birth in (dd/mm/yyyy) format ::>> ").split("/")))
    date2=list(map(int,input("enetr present  date in (dd/mm/yyyy) format ::>> ").split("/")))

    #d1="yyyy/mm/dd"
    d1 = date(date1[2],date1[1],date1[0])
    d2 = date(date2[2],date2[1],date1[0])

    #calling get_diff function
    get_diff(d1,d2)
    
    print("\n\n")
    ch=input("do you want to calculate one more (y/n)::>>")
print("Thankyou for using our calculator")
