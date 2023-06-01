# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(len(data),0,-1):
        currentElementIndex = i
        canSwap = True
        while canSwap:
            if currentElementIndex < 2:
                canSwap = False
                break
            parentElement = data[currentElementIndex//2-1]
            currentElement = data[currentElementIndex-1]

            if currentElement < parentElement:
                data[currentElementIndex-1], data[currentElementIndex//2-1] = data[currentElementIndex//2-1],data[currentElementIndex-1]
                swaps.append([currentElementIndex//2-1,currentElementIndex-1])
                currentElementIndex = currentElementIndex//2
            else:
                canSwap = False
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    # implement input form keyboard and from files
    inpMethod = input()
    # let user input file name to use, don't allow file names with letter a
    text = input("I or F: ")
    if "I" in text[:1]:
        n = int(input("number: "))
        # input from keyboard
        data = list(map(int, input().split()))
    elif "F" in text[:1]:
        filename = "test/" + input("Fails: ")
        file = open(filename, "r")
        n = int(file.readline())
        data = file.readline()
        data = list(map(int, data.split()))



    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()