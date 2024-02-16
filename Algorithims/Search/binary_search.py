def binary_search(arr: list[int], target: int) -> int:
    low: int = 0
    high: int = len(arr) - 1

    while(low <= high):
        middle: int = int(low + (high - low)/2)
        value = arr[middle]

        print(f"middle: {value}")

        if(value == target):
            return middle
        elif value < target:
            low = middle + 1
        elif value > target:
            high = middle -1
    return -1

def main():
    arr: list[int] = []

    # create arr with 100 numbers from 0-100 
    for i in range(0, 1000000):
        arr.append(i)

    index: int = binary_search(arr, 1001)

    if index != -1:
        print(f"index of target is: {index}")
    else:
        print("Target not found")

if __name__ == "__main__":
    main()