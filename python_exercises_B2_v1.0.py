"""
to do : [02, 20, 24, 26, 27, 39, 43, 52, 53, 56, 69, 70, 82, 86, 93, 95, 98, 106, 107, 113]
from: https://www.w3resource.com/python-exercises/basic/
"""

from collections import deque
from itertools import permutations
import math

#===================================================== FUNCTIONS ===================================================================#

def exercise_b2_2():
    """
        Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
    """
    letters = ['a', 'e', 'i', 'o', 'u', 'u']
    combinations = list(permutations(letters))
    uniq_combinations = set(combinations)
    total_possibilities = len(combinations)
    total_uniq_possibilities = len(uniq_combinations)
    print("\nThere are %s possible combinations and %s unique combinations for this set\n" 
            % (total_possibilities, total_uniq_possibilities))
    return

def exercise_b2_20():
    """
        Write a Python program to find the number of zeros at the end of a factorial of a given positive number. 
        Range of the number(n): (1 <= n <= 2*109).
    """
    number = input("Insert the number to be factored: ")
    if 1 <= int(number) <= (2*109): 
        total = 0
        factorial = math.factorial(int(number))
        list_factorial = list(str(factorial))
        for i in list_factorial[::-1]:
            if i == '0':
                total += 1
            else: 
                break
    else:
        print("The inserted number is invalid")

    print("\nThe total of zeros are: %s " % total)
    
    return

def exercise_b2_24():
    """
        Write a Python program to find the number of divisors of a given integer is even or odd.
    """
    number = input("Insert the number: ")
    flag = 0
    count = 0
    divisors_list =[]
    while flag <= int(number):
        flag +=1
        if (int(number) % flag) == 0:
            count += 1
            divisors_list.append(flag)
    print("""\nThe amount of divisors are: %s"""
        """\nThe numbers are: %s\n""" % (count, divisors_list))
    return

def exercise_b2_26():
    """
        Write a Python program to compute the summation of the absolute difference of 
        all distinct pairs in an given array (non-decreasing order).
        Sample array: [1, 2, 3]
        Then all the distinct pairs will be:
        1 2
        1 3
        2 3
    """
    pass

def exercise_b2_27():
    """
        Write a Python program to find the type of the progression (arithmetic progression/geometric progression) 
        and the next successive member of a given three successive members of a sequence. 
        According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers such that the difference of 
        any two successive members of the sequence is a constant. 
        For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common difference 2. 
        For this problem, we will limit ourselves to arithmetic progression whose common difference is a non-zero integer.
        On the other hand, a geometric progression (GP) is a sequence of numbers where each term after the first is found 
        by multiplying the previous one by a fixed non-zero number called the common ratio. 
        For example, the sequence 2, 6, 18, 54, . . . is a geometric progression with common ratio 3. 
        For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer.
    """
    pass

def exercise_b2_39():
    """
        Write a program to compute the radius and the central coordinate (x, y) of a circle 
        which is constructed by three given points on the plane surface.
        Input:
        x1, y1, x2, y2, x3, y3 separated by a single space.
        Input three coordinate of the circle:
        9 3 6 8 3 6
        Radius of the said circle:
        3.358
        Central coordinate (x, y) of the circle:
        6.071 4.643
    """
    pass

def exercise_b2_43():
    """
        Write a Python program to test whether two lines PQ and RS are parallel. 
        The four points are P(x1, y1), Q(x2, y2), R(x3, y3), S(x4, y4). 
        Input:
        x1,y1,x2,y2,x3,y3,xp,yp separated by a single space
        Input x1,y1,x2,y2,x3,y3,xp,yp:
        2 5 6 4 8 3 9 7
        PQ and RS are not parallel
    """
    pass

def exercise_b2_52():
    """
        Write a Python program to compute the sum of first n given prime numbers.
        Input:
        n ( n <= 10000). Input 0 to exit the program.
        Input a number (n<=10000) to compute the sum:(0 to exit)
        25
        Sum of first 25 prime numbers:
        1060
    """
    pass

def exercise_b2_53():
    """
        Write a Python program that accept an even number (>=4, Goldbach number) from the user and create a combinations
        that express the given number as a sum of two prime numbers. Print the number of combinations. 
        Goldbach number: A Goldbach number is a positive even integer that can be expressed as the sum of two odd primes.
        [4] Since four is the only even number greater than two that requires the even prime 2 
        in order to be written as the sum of two primes, another form of the statement of Goldbach's conjecture is that
        all even integers greater than 4 are Goldbach numbers.
        The expression of a given even number as a sum of two primes is called a Goldbach partition of that number. 
        The following are examples of Goldbach partitions for some even numbers:
        6 = 3 + 3
        8 = 3 + 5
        10 = 3 + 7 = 5 + 5
        12 = 7 + 5
        ...
        100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
        Input an even number (0 to exit):
        100
        Number of combinations:
        6
    """
    pass

def exercise_b2_56():
    """
        Write a Python program to sum of all numerical values (positive integers) embedded in a sentence.
        Write a Python program to create maximum number of regions obtained by drawing n given straight lines. 
        Input:
        Sentences with positive integers are given over multiple lines. Each line is a character string containing one-byte alphanumeric characters, symbols, spaces, or an empty line. However the input is 80 characters or less per line and the sum is 10,000 or less.
        Input some text and numeric values ( to exit):
        Sum of the numeric values: 80
        None
        Input some text and numeric values ( to exit):
        Sum of the numeric values: 17
        None
        Input some text and numeric values ( to exit):
        Sum of the numeric values: 10
        None
    """
    pass

def exercise_b2_69():
    """
        In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence 
        between the elements of the groups in a way that respects the given group operations. 
        If there exists an isomorphism between two groups, then the groups are called isomorphic.
        Two strings are isomorphic if the characters in string A can be replaced to get string B
        Given "foo", "bar", return false.
        Given "paper", "title", return true.
        Write a Python program to check if two given strings are isomorphic to each other or not. 
        Sample Input:
        ("foo", "bar")
        ("bar", "foo")
        ("paper", "title")
        ("title", "paper")
        ("apple", "orange")
        ("aa", "ab")
        ("ab", "aa")
        Sample Output:
        False
        False
        True
        True
        False
        False
        False
    """
    pass

def exercise_b2_70():
    """
        Write a Python program to find the longest common prefix string amongst a given array of strings. 
        Return false If there is no common prefix.
        For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
        Sample Input:
        ["abcdefgh","abcefgh"]
        ["w3r","w3resource"]
        ["Python","PHP", "Perl"]
        ["Python","PHP", "Java"]
        Sample Output:
        abc
        w3r
        P
    """
    pass

def exercise_b2_82():
    """
    Write a Python program to calculate the median from a list of numbers.
    Sample Input:
    [1,2,3,4,5]
    [1,2,3,4,5,6]
    [6,1,2,4,5,3]
    [1.0,2.11,3.3,4.2,5.22,6.55]
    [1.0,2.11,3.3,4.2,5.22]
    [2.0,12.11,22.3,24.12,55.22]
    Sample Output:
    3
    3.5
    3.5
    3.75
    3.3
    22.3
    """
    pass

def exercise_b2_86():
    """
    Write a Python program to count the number of equal numbers from three given integers. Go to the editor
    Sample Input:
    (1, 1, 1)
    (1, 2, 2)
    (-1, -2, -3)
    (-1, -1, -1)
    Sample Output:
    3
    2
    0
    3
    """
    pass

def exercise_b2_93():
    """
        Write a Python program to find the middle character(s) of a given string. If the length of the string is odd return the middle character and return the middle two characters if the string length is even. Go to the editor
        Sample Input:
        ("Python")
        ("PHP")
        ("Java")
        Sample Output:
        th
        H
        av
    """
    pass

def exercise_b2_95():
    """
        Write a Python program to check whether every even index contains an even number and every odd index
        contains odd number of a given list. 
        Sample Input:
        [2, 1, 4, 3, 6, 7, 6, 3]
        [2, 1, 4, 3, 6, 7, 6, 4]
        [4, 1, 2]
        Sample Output:
        True
        False
        True
    """
    pass

def exercise_b2_98():
    """
        Write a Python program to check whether a sequence of numbers has an increasing trend or not.
        Sample Input:
        [1,2,3,4]
        [1,2,5,3,4]
        [-1,-2,-3,-4]
        [-4,-3,-2,-1]
        [1,2,3,4,0]
        Sample Output:
        True
        False
        False
        True
        False
    """
    pass

def exercise_b2_106():
    """
        Write a Python program to test whether a given integer is pandigital number or not. Go to the editor
        From Wikipedia,
        In mathematics, a pandigital number is an integer that in a given base has among its significant 
        digits each digit used in the base at least once.
        For example,
        1223334444555556666667777777888888889999999990 is a pandigital number in base 10.
        The first few pandigital base 10 numbers are given by:
        1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987, 1023457689
        Sample Input:
        (1023456897)
        (1023456798)
        (1023457689)
        (1023456789)
        (102345679)
        Sample Output:
        True
        True
        True
        True
        False
    """
    pass

def exercise_b2_107():
    """
        Write a Python program to check whether a given number is Oddish or Evenish.
        A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum 
        of all of its digits is even.
        Sample Input:
        (120)
        (321)
        (43)
        (4433)
        (373)
        Sample Output:
        Oddish
        Evenish
        Oddish
        Evenish
        Oddish
    """
    pass

def exercise_b2_113():
    """
        Write a Python program to reverse all the words which have even length.
        Sample Input:
        ("The quick brown fox jumps over the lazy dog")
        ("Python Exercises")
        Sample Output:
        The quick brown fox jumps revo the yzal dog
        nohtyP Exercises
    """
    pass



#======================================================== BODY =====================================================================#

functions_dict = {'2': exercise_b2_2, '20': exercise_b2_20, '24': exercise_b2_24}

exercise_number = input("Insert the exercise number: ")

functions_dict[exercise_number]()