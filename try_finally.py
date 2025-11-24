def main(): 
    try:
        a = int(input("Hello, Enter a Number: "))
        print(a)
    except Exception as e:
        print(e)
    else:  
        print("Than You valid input") 
    finally:
        print("Have a nice day")           


main()        