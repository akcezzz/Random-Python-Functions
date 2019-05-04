def sum(num):
    '''
    This function returns the sum from 0 to a number
    exemple: num = 3, sum = 6
    '''
    a_sum = 0
    for x in range(num+1):
        a_sum += x
    return a_sum

print(sum(2)) #test

def is_triangle(a,b,c):
    '''
    This function takes 3 lengths and returns if wether or not they can create a triangle
    '''
    return a+b>c

print(is_triangle(2,3,5)) #test



def toJadenCase(string):
    '''
    This function is made to capitalize each word of a string
    '''
    alist = [word[0].capitalize() + word[1:] for word in string.split()]
    x = ' '.join(alist)
    return x

astring = 'her name is her'
print(toJadenCase(astring)) #test


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
print(getCount(astr)) #test

def find_smallest_int(arr):
    '''
    This functions returnrs the smallest element of a list/array
    '''
    return min(arr)

alist = [23,45,3,445,765,1]
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
        elif letter =='T':
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
    ls.sort(reverse = True) #sorts list in reverse (descending order)
    return int(''.join(ls))

print(Descending_Order(1234))

def array_diff(a, b):
    '''
    This function subtracts one list from another and returns the result
    '''
    c =[]
    for x in a:
        if x not in b:
            c.append(x)
    return c

print(array_diff([1,2,3],[2,3]))

