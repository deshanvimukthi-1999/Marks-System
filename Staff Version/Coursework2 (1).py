# initializing variables

markPass = 0
markDefer = 0
fail_mark = 0

progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0

# recalling the function
def mark():
    global progress_count, trailer_count, exclude_count, retriever_count
    if markPass % 20 == 0 and markDefer % 20 == 0 and fail_mark % 20 == 0:

        if markPass + markDefer + fail_mark == 120:

            if markPass == 120:
               print("progress")
               progress_count = progress_count+1

            elif markPass == 100:
               print("progress-module trailer")
               trailer_count = trailer_count+1

            elif markPass < 100 and markPass + markDefer < fail_mark:
                print("Exclude")
                exclude_count = exclude_count+1

            else:
                print("Do not progress- module retriever")
                retriever_count = retriever_count+1
        else:
            print("total incorrect")
    else:
        print("range Error")
    return
# user inputs
def user_input():
    global markDefer,markPass,fail_mark
    while True:
        try:
            markPass = int(input("Enter the pass marks: "))
            markDefer = int(input("Enter the defer marks: "))
            fail_mark = int(input("Enter the fail marks: "))
        except:
            print("integer required")
        break;
def histrogram():
    global progress_count, trailer_count, exclude_count, retriever_count
    print("progress", progress_count, ":", "*" * progress_count)
    print("trailing", trailer_count, ":", "*" * trailer_count)
    print("retiever", retriever_count, ":", "*" * retriever_count)
    print("exclude", exclude_count, ":", "*" * exclude_count)

    print("Total :", progress_count + retriever_count + trailer_count + exclude_count)

STOP = True

while STOP: #True
    user_input()
    mark()
    stop = input("Press any key to Enter data again,Press'q' to Quit")
    if stop == 'q':
        STOP = False
    else:
        continue;
histrogram()

