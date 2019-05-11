def sum(num):
    '''
    This function returns the sum from 0 to a number
    exemple: num = 3, sum = 6
    '''
    a_sum = 0
    for x in range(num + 1):
        a_sum += x
    return a_sum


print(sum(2))  # test


def is_triangle(a, b, c):
    '''
    This function takes 3 lengths and returns if wether or not they can create a triangle
    '''
    return a + b > c


print(is_triangle(2, 3, 5))  # test


def toJadenCase(string):
    '''
    This function is made to capitalize each word of a string
    '''
    alist = [word[0].capitalize() + word[1:] for word in string.split()]
    x = ' '.join(alist)
    return x


astring = 'her name is her'
print(toJadenCase(astring))  # test


def getCount(inputStr):
    '''
    This function returns the number of vowels contained in a string
    '''
    num_vowels = 0
    lst_vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in inputStr:
        for vowel in lst_vowels:
            if letter == vowel:
                num_vowels += 1

    return num_vowels


astr = 'Je mappelle sammy'
print(getCount(astr))  # test


def find_smallest_int(arr):
    '''
    This functions returnrs the smallest element of a list/array
    '''
    return min(arr)


alist = [23, 45, 3, 445, 765, 1]
print(find_smallest_int(alist))


def no_space(x):
    '''
    This function removes the spaces of a string and returns it
    '''
    lst = x.split()
    return ''.join(lst)


astr = 'The apple is red'
print(no_space(astr))


def DNA_strand(dna):
    '''
    This functions returns the complementary string of a dna string
    '''
    c_dna = []
    for letter in dna:
        if letter == 'A':
            c_dna.append('T')
        elif letter == 'T':
            c_dna.append('A')
        elif letter == 'C':
            c_dna.append('G')
        elif letter == 'G':
            c_dna.append('C')

    return ''.join(c_dna)


def Descending_Order(num):
    '''
    This function takes an integer and returrns it with its digits in descending order
    '''
    ls = []
    for numb in str(num):
        ls.append(numb)
    ls.sort(reverse=True)  # sorts list in reverse (descending order)
    return int(''.join(ls))


print(Descending_Order(1234))


def array_diff(a, b):
    '''
    This function subtracts one list from another and returns the result
    '''
    c = []
    for x in a:
        if x not in b:
            c.append(x)
    return c


print(array_diff([1, 2, 3], [2, 3]))


def is_prime(num):
    if num <= 1:
        return False
    else:
        for x in range(1, num + 1):
            if num % x == 0:
                if x == num:
                    return True


print(is_prime(2))

alist = [1, 2, 5, 4, 5]


def queue_time(customers, n):
    '''
    This customer determines the longest wait time possible on a queue, customers is a list of customers with their respective
    amount of time taken in the queue, n is the number of checkout tills
    '''
    alist = []

    if len(customers) == 0:  # if there is no customer
        return 0
    elif len(customers) <= n:  # if theres less customers than the number of checkout tills (or =)
        return max(customers)
    else:
        for i in range(n):
            alist.append(customers[i])
        for i in range(n, len(customers)):
            alist[alist.index(min(alist))] += customers[
                i]  # The smallest value of alist (smallest amount of time) is incremented with time
        # of next customer
        return max(alist)  # returns the max amount of time, or total time taken to go through all customers


def spin_words(sentence):
    '''
    This function returns a sentence with words that have 5 or more letters reversed
    '''
    ls = sentence.split()
    mystring = ''
    for i in range(len(ls)):
        if len(ls[i]) >= 5:
            ls[i] = (str(ls[i])[::-1])

    return ' '.join(ls)


mysentence = 'It is cold outside'
print(spin_words(mysentence))  # Test


# or

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


def make_readable1(seconds):
    '''
    This functin takes an integer and returns its equivalent in time-readable HH:MM:SS
    '''
    s = seconds % 60
    m = int(((seconds / 60) % 60))
    h = int(seconds / 3600)

    if s < 10:
        s = '0' + str(s)
    else:
        s = str(s)
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)

    return h + ':' + m + ':' + s


test = 86399
print(make_readable1(test))


# Or

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


def order_weight(strng):
    '''
    This function takes a string and finds the sum of digits of every number contained in the string
    '''
    sum = 0
    alist = strng.split()
    newlist = [0]*len(alist)
    for  nnum in newlist:
        for anum in alist:
            for number in anum:
                nnum += int(number)


    print(newlist)


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    ls = []
    sum = 0
    for num in range(a, b + 1):
        string = str(num)
        for y in range(len(string)):
            sum += int(string[y])**(y+1)
            if sum == num:
                ls.append(sum)
        sum = 0
    return ls



print(sum_dig_pow(1,100))

def productFib(prod):
    '''
    This function takes an int computes if it is fibonacci number or not
    '''
    def if_Fib(n):
        '''
        This function returns wether or not n is fibonacci number or not (True/False)
        '''
        sum1 = 0
        sum2 = 1
        sum3 = 0
        answer = False
        for i in range(2,n):
            sum3 = sum2 + sum1
            sum1 = sum2
            sum2 = sum3
            if sum3 == n:
                answer = True
        return answer


def if_Fib(n):
    '''
    This function returns wether or not n is fibonacci number or not (True/False)
    '''
    sum1 = 0
    sum2 = 1
    sum3 = 0
    answer = False
    for i in range(2,n):
        sum3 = sum2 + sum1
        sum1 = sum2
        sum2 = sum3
        if sum3 == n:
            answer = True
    return answer

print(if_Fib(233))


def removNb(n):
    ls = []
    sum = 0
    for x in range(0,n):
        sum += x
    x = 0
    y =1
    while y == n:
        if x*y == sum-x-y:
            ls.append(x)
            ls.append(y)

    return ls

print(removNb(26))
