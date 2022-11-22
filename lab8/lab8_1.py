# your code goes here
def count_multiple_occurrence(numbers):
    tuple_numbers=tuple(sorted(numbers))
    #print(tuple_numbers)
    counts=dict()
    for i in range(len(tuple_numbers)):
        if tuple_numbers[i] not in counts:
            counts[tuple_numbers[i]]=1
        else:
            counts[tuple_numbers[i]]=counts[tuple_numbers[i]]+1
    #print(counts)
    for result_name,result_number in sorted(counts.items(),key=lambda item:item[1],reverse=True):
        if result_number>1:
            print("The occurrence of",result_name,"is",result_number)


# Output Generation. You are not allowed to modify the following codes
def main():
    numbers = [
        951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725,
        547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390,
        984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236,
        375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,
        918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,
        67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440,
        380, 126, 721, 328, 753, 470, 743, 527
    ]
    count_multiple_occurrence(numbers)
if __name__ == "__main__":
    main()
