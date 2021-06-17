

# this function is how i was able to find the number of empty spaces in the row
# for example: "      *" = 5 spaces
a = [1, 3, 5, 6, 7, 4, 9, 10]

def pattern(x):
    biggest = max(x)
    for i in x:
        spaces = biggest - i
        if i != biggest:
            print(spaces * " " + "*" * i)
        if i == biggest:
            print("*" * i)


# Creating the diamond:

def diamond():
    x = int(input("diamond size? "))

    for i in range(1, x + 1):
        if i == 1:
            print((" " * (x - 1) + "*" * i))
        print((" " * (x - i)) + "*" * i * 2)

    # print((" " * (x - i)) + "*" * i * 2) is:
        # first we find the empty spaces by lessing i from the biggest number we are working with, and that number is simply
        # the number the user inputs, when we have the result we multiply 1 space by the result then we add that to the *
        # printed, and the multiplication by 2 at the end is just to make the diamond shape

    # this for is to make the bottom half of the diamond
    # as you can see the [::-1] is applied to the range
    # for the code to run the range backwards, to be honest i am surprised it worked on a range function
    for n in range(1, x)[::-1]:
        print((" " * (x - n)) + "*" * n * 2)
        if n == 1:
            print((" " * (x - n)) + " *" * n)



