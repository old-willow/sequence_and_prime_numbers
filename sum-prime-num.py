# -*- conding:utf-8 -*-


l = []
for i in xrange(1, 8):
    l.append(i)

print(l)

new_list = []

result_list = []
result_collection = []
remain = []
first = None

def one_pass(the_list):
    """Recursive function."""
    global first
    tmp_remain = the_list
    if not first:
        first = l[0]
    else:
        first = the_list[-1]

    for j in the_list:
        if j not in result_list and first != j:
            second = j
            result = first + second
            if is_prime(result):
                if first not in result_list:
                    result_list.append(first)
                result_list.append(second)
                first = result_list[-1]
            else:
                remain.append(second)

    if remain and remain != tmp_remain:
        one_pass(remain)
    else:
        result_collection.append(result_list)
        print result_collection


def print_is_prime():
    """Print only the prime numbers from given list."""
    for i in l:
        yes_prime = is_prime(i)
        if yes_prime:
            print(str(i) + ' is  a prime number.')

def main():
    #print_is_prime()
    #do_the_math()
    one_pass(l)


def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if not number & 1:
        return False

    # This algorithm is called Sieve of Eratosthenes
    for x in xrange(3, int(number**0.5) + 1, 2):
        if number % x == 0:
            return False

    return True


if __name__ == '__main__':
    main()
