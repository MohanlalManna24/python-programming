# check spam massage

p1 = "Make a lot of mony"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

massage = input("Enter the message: ")
if (p1 in massage or 
    p2 in massage or 
    p3 in massage or 
    p4 in massage):
    print("This is a spam message")

else:
    print("This is not a spam message")    



if (p1.lower() in massage.lower() or 
    p2.lower() in massage.lower() or 
    p3.lower() in massage.lower() or 
    p4.lower() in massage.lower()):
    print("This is a spam message")

else:
    print("This is not a spam message")    