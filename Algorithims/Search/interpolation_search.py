def interpolation_search(arr: list[int], target: int) -> int:
    low: int = 0
    high: int = len(arr) - 1

    while(arr[low] <= target and target <= arr[high] and low <= high):
        probe: int = int(low + (high - low) * (target - arr[low]) / (arr[high] - arr[low]))

        print(probe)
        if arr[probe] == target:
            return probe
        elif arr[probe] < target:
            low = probe + 1
        else:
            high = probe - 1

    return -1

def main():
    arr: list[int] = [1,2,3,4,5,6,7,8,9]
    index: int = interpolation_search(arr, 8); 

    if index != -1:
        print(f"index of target is: {index}")
    else:
        print("target is not on list")

if __name__ == "__main__":
    main()