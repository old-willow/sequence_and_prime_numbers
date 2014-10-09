# -*- conding:utf-8 -*-


l = []
for i in xrange(1, 8):
    l.append(i)

print(l)

new_list = []

def do_the_math():
    l1 = l[:]
    l2 = l[:]
    k = None

    res_list = []
    global_result = []

    for k in l:
        first = k
        #res_list.append(first)

        for i in xrange(len(l)):
            #print "result list", len(res_list)
            #print "basic list", len(l)
            if len(res_list) == len(l):
                global_result.append(res_list)
                res_list = []
            #if l[i] not in res_list:
            #print("first: " + str(first))
            for j in xrange(len(l)):
                # This is the first and normal pass
                if l[j] not in res_list and first != l[j]:
                    second = l[j]
                    res = first + second
                    #print "first:", first, "second:",second, "result:", res
                    #print("res: " + str(res))

                    if is_prime(res):
                        #print "first:", first, "second:",second, "result:", res
                        if first not in res_list:
                            # This is only for the first pass...
                            res_list.append(first)
                        #res_list.append(l[j])
                        res_list.append(second)
                        # prepare for next turn.
                        first = res_list[-1]
                        break
        #print "=" * 10
        #first = k


    for ls in global_result:
        if len(ls) == len(l):
            print("result list: " + str(ls))
        #print("res_list: " + str(res_list))


#def sum_of_neighbours():
#    for i in l:
#        first = i
#        for j in l:
#            if i == j:
#                continue
#            second = i
#            sum = first + second
#            isprime_number = is_prime(sum)
#            if isprime_number:
#                new_list.append(first)
#                new_list.append(second)
#                print(first + ', ' + second)

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
    #if number % (int(number**0.5) + 1) == 0:
    #    print("number: " + str(number))
    #    print("divider: " + str(int(number**0.5)))
    #    return False

    return True


if __name__ == '__main__':
    main()
