# initializing variables

markPass = 0
markDefer = 0
fail_mark = 0

# recalling the function
def mark():
    if markPass % 20 == 0 and markDefer % 20 == 0 and fail_mark % 20 == 0:

        if markPass + markDefer + fail_mark == 120:

            if markPass == 120:
               print("progress")
                

            elif markPass == 100:
               print("progress-module trailer")
               

            elif markPass < 100 and markPass + markDefer < fail_mark:
                print("Exclude")
            

            else:
                print("Do not progress- module retriever")
                

        else:
            print("total incorrect")
            
    else:
        print("range Error")
        
    return


# user inputs
while True :
    try:
        markPass = int(input("Enter the pass marks: "))
        markDefer = int(input("Enter the defer marks: "))
        fail_mark = int(input("Enter the fail marks: "))


        mark()

    except:
       print("integer required")
        
