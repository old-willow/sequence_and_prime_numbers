# -*- conding:utf-8 -*-


l = []
for i in xrange(1, 8):
    l.append(i)

print(l)

new_list = []

result_list = []
result_collection = []
#remain = []
first = None

def find_all():
    global result_list
    global result_collection

    #if not result_collection:
    #    one_pass(l)
    #else:
    #    one_pass(l)
    one_pass(l)
    one_pass(l)
    one_pass(l)


def one_pass(the_list):
    """Recursive function."""
    global first
    global result_list
    global result_collection
    remain = []

    #already_checked = False

    tmp_remain = the_list

    if not first:
        first = l[0]  # If running for the first time per combination.
    #else:
        # The last element is used if we use recursion.
        #first = the_list[-1]

    for j in the_list:
        if j not in result_list and first != j:
            second = j
            #print("first: " + str(first) + " ; second: " + str(second))

            # This whole condition is ignored for the first pass.
            if first == the_list[0] and result_collection and check_pair(first, second):
                #print("already have collection")
                #already_checked = True
                remain.append(second)
                continue

            # this is for first pass
            #print("no collection yet")
            result = first + second
            if is_prime(result):
                if first not in result_list:
                    result_list.append(first)
                result_list.append(second)
                first = result_list[-1]
            else:
                remain.append(second)

    # This is out of loop.
    # If we didn't finished the pass start recursion.
    if remain and remain != tmp_remain:
        #print("recursion")
        one_pass(remain)
    else:
        result_collection.append(result_list)
        first = None
        second = None  # Not sure if this has any affect?
        result_list = []
        remain = []
        #already_checked = False
        #print result_collection

def check_pair(first, second):
    #print("first: " + str(first) + " ; second: " + str(second))
    for element in result_collection:
        #if element[:2] == [first, second]:
        if element[0] == first and element[1] == second:
            return True
    return False


def print_is_prime():
    """Print only the prime numbers from given list."""
    for i in l:
        yes_prime = is_prime(i)
        if yes_prime:
            print(str(i) + ' is  a prime number.')

def main():
    #print_is_prime()
    #do_the_math()
    find_all()


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
    print result_collection
