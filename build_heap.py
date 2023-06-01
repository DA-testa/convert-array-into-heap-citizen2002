# python3

def build_heap(data):
    swaps = []
    
    for i in range(len(data),0,-1):
        currentElemIndex = i
        swap = True
        while swap:
            if currentElemIndex < 2:
                swap = False
                break
            parentElem = data[currentElemIndex//2-1]
            currentElem = data[currentElemIndex-1]

            if currentElem < parentElem:
                data[currentElemIndex-1], data[currentElemIndex//2-1] = data[currentElemIndex//2-1],data[currentElemIndex-1]
                swaps.append([currentElemIndex//2-1,currentElemIndex-1])
                currentElemIndex = currentElemtIndex//2
            else:
                swap = False
    return swaps

def main():
    impMethod = input()
    text = input("I or F: ")
    if "I" in text[:1]:
        n = int(input("number: "))
        data = list(map(int, input().split()))
    elif "F" in text[:1]:
        filename = "test/" + input("File: ")
        file = open(filename, "r")
        n = int(file.readline())
        data = file.readline()
        data = list(map(int, data.split()))

    assert len(data) == n

    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # ...

    # output all swaps
    print(len(swaps))
    for a, b in swaps:
        print(a, b)


if __name__ == "__main__":
    main()
