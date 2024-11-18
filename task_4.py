def shell_sort(arr, ascending=True):
    n = len(arr)
    gap = n // 2 

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            if ascending:
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
           
            else:
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap

            arr[j] = temp
        gap //= 2 

    return arr

if __name__ == "__main__":
  
    example_list = [23, 12, 1, 8, 34, 54, 2, 3]

    sorted_list_ascending = shell_sort(example_list[:], ascending=True)
    print("Сортування за зростанням:", sorted_list_ascending)

    sorted_list_descending = shell_sort(example_list[:], ascending=False)
    print("Сортування за спаданням:", sorted_list_descending)
