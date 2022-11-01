# your code goes here
def counting_on_list(x):
    prime_number=list()
    even_number=list()
    odd_number=list()
    def prime(t):
        number = int(t)
        is_prime = True
        if number <= 1 or number != 2 and number % 2 == 0:
            is_prime = False
        for i in range(3, number, 2):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_number.append(number)
    for y in x:
        if y%2==0:
            even_number.append(y)
            prime(y)
        else:
            odd_number.append(y)
            prime(y)
    return len(odd_number), len(even_number), len(prime_number)
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
    odd_number, even_number, prime_number = counting_on_list(numbers)
    print("Total no. of odd numbers:",odd_number)
    print("Total no. of even numbers:",even_number)
    print("Total no. of prime numbers:",prime_number)
    
if __name__ == "__main__":
    main()
