def swap(nums, i):
    current_number = nums[i]
    previous = nums[i - 1]
    nums[i] = previous
    nums[i - 1] = current_number
    return nums


def main():
    file = open("../_data/input.txt", "r")
    foo = file.readlines()
    nums = [int(x.strip()) for x in foo]
    print(nums)
    for i in range(1, len(nums)):
        for k in range(i, 0, -1):
            if nums[k] < nums[k - 1]:
                nums = swap(nums, k)
    print(nums)
    out_file = open("../_data/output.txt", "r")
    out_content = out_file.readlines()
    expected_output = [int(x.strip()) for x in out_content]

    success = True
    for i in range(len(nums) - 1):
        if expected_output[i] != nums[i]:
            success = False

    if success:
        print("SORTED SUCCESSFULLY! :D")
    else:
        print("Failed to sort :(")


if __name__ == "__main__":
    main()
