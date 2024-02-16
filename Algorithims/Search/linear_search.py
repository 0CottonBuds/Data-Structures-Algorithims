def linear_search(arr: list[int], value: int) -> int:
    for i in range(0, len(arr)):
       if arr[i] == value:
           return[i]
    return -1 

def main():
    arr: list[int] = [9,1,3,4,5,7,0]
    index: int = linear_search(arr, 7)

    print(index)

if __name__ == "__main__":
    main()