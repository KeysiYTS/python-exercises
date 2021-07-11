"""
 Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""

import sys
import datetime
from datetime import datetime as dt
import calendar
import math
import hashlib


def exercise2():
    return sys.version

def exercise3():
    return dt.now()

def exercise4():
    radius = input("Insert the radius: ")
    radius = float(radius)
    area = ((radius**2)*math.pi)
    return area

def exercise5():
    name = input("Insert your first and last name: ")
    sep_name = str.split(name)
    inverted_name = " "
    inverted_name = inverted_name.join(sep_name[::-1])
    return inverted_name

def exercise6():
    numbers = input("Write the digits comma separated: ")
    number_list = numbers.split(sep=',')
    number_tuple = tuple(number_list)
    print('The list is: %s' % number_list)
    print('The tuple is: %s' % str(number_tuple))
    return

def exercise7():
    filename = input("Insert the file name: ")
    file_extension = filename.split('.', 1)
    print("The extensionis '.%s'" % file_extension[1])
    return

def exercise8():
    colour_list = ["Red","Green","White" ,"Black"]
    print('The first and last colours are: %s and %s' % (colour_list[0], colour_list[-1]))
    return

def exercise9():
    exam_st_date = (11, 12, 2014)
    string_date = datetime.date(year=exam_st_date[2], month=exam_st_date[1], day=exam_st_date[0])
    print('The date is: %s' % (string_date.strftime("%d/%m/%Y")))
    return

def exercise10():
    digit = input("Insert the digit: ")
    n1 = int(str('%s') % digit)    
    n2 = int(str('%s%s') % (digit,digit))
    n3 = int(str('%s%s%s') % (digit,digit,digit))
    print(n1 + n2 + n3)
    return

def exercise12():
    calendar.prmonth(2021,6)
    return

def exercise14():
    start_date = (2014, 7, 2) 
    end_date = (2014, 7, 11)
    date1 = datetime.date(year=start_date[0], month=start_date[1], day=start_date[2])
    date2 = datetime.date(year=end_date[0], month=end_date[1], day=end_date[2])
    delta = date2 - date1
    print("Difference in days: %s" % delta.days)
    return

def exercise15():
    str_radius = input("Insert the radius: ")
    float_radius = float(str_radius)
    volume = ((4*math.pi)*float_radius**3)/3
    print("The volume of the sphere with radius %s is: %s" % (str_radius,volume))
    return

def exercise25():
    list1 = [1, 5, 8, 3]
    digit = input("\nWhat number must be compared found in the list? ")
    if int(digit) in list1:
        print("%s is in the list!" % digit)
    else:
        print("%s is not in the list!" % digit)
    return

def exercise28():
    numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 237, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
    for i in numbers:
        if i == 237:
            print(i)
            break
        else:
            print(i)
    return

def exercise29():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    for i in color_list_1:
        if i not in color_list_2:
            print(i)
    return

def exercise38():
    x = 4
    y = 3
    result = (x + y)**2
    print(result)
    return

def exercise40():
    p1 = [4, 0]
    p2 = [6, 6]
    distance = math.sqrt( ((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2) ) 
    print(distance)
    return

def exercise74():
    hash_value = hashlib.sha256(b"Keysi Santos").hexdigest()
    print(hash_value)
    return

#____________MAIN_______________________


# Write a Python program to get the Python version you are using
#print(exercise2())
#-----------------------------------------------------------------------------------------------------

# Exercise 3
"""
    Write a Python program to display the current date and time.
    Sample Output :
    Current date and time :
    2014-07-05 14:34:14
"""
#print(exercise3())
#-----------------------------------------------------------------------------------------------------

# Exercise 4
"""
    Write a Python program which accepts the radius of a circle from the user and compute the area.
    Sample Output :
    r = 1.1
    Area = 3.8013271108436504
"""
#print("The area of the circle is: %s " % exercise4())
#-----------------------------------------------------------------------------------------------------

#Exercise 5
"""
    Write a Python program which accepts the user's first and last name 
    and print them in reverse order with a space between them
"""
#print("The inverted name is: %s" % exercise5())
#-----------------------------------------------------------------------------------------------------

# Exercise 6
"""
    Write a Python program which accepts a sequence of comma-separated numbers 
    from user and generate a list and a tuple with those numbers.
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
"""
#exercise6()
#-----------------------------------------------------------------------------------------------------

# Exercise 7
"""
    Write a Python program to accept a filename 
    from the user and print the extension of that.
"""
#exercise7()
#-----------------------------------------------------------------------------------------------------

# Exercise 8
"""
    Write a Python program to display the first and last colors from the following list.
    color_list = ["Red","Green","White" ,"Black"]
"""
#exercise8()
#-----------------------------------------------------------------------------------------------------

# Exercise 9
"""
    Write a Python program to display the examination schedule. (extract the date from exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014
"""
#exercise9()
#-----------------------------------------------------------------------------------------------------

# Exercise 10
"""
    Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
    Sample value of n is 5
    Expected Result : 615
"""
#exercise10()
#-----------------------------------------------------------------------------------------------------

# Exercise 12
"""
    Write a Python program to print the calendar of a given month and year.
    Note : Use 'calendar' module.
"""
#exercise12()
#-----------------------------------------------------------------------------------------------------

# Exercise 14
"""
    Write a Python program to calculate number of days between two dates.
    Sample dates : (2014, 7, 2), (2014, 7, 11)
    Expected output : 9 days
"""
#exercise14()
#-----------------------------------------------------------------------------------------------------

# Exercise 15
"""
    Write a Python program to get the volume of a sphere with radius 6.
    formula = (4*pi*r**3)/3
"""
# exercise15()
#-----------------------------------------------------------------------------------------------------

# Exercise 25
"""
    Write a Python program to check whether a specified 
    value is contained in a group of values. 
    Test Data :
    3 -> [1, 5, 8, 3] : True
    -1 -> [1, 5, 8, 3] : False
"""

#exercise25()
#-----------------------------------------------------------------------------------------------------

# Exercise 28
"""
    Write a Python program to print all even numbers from 
    a given numbers list in the same order and stop the printing if any numbers that
    come after 237 in the sequence.
    Sample numbers list :

    numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
""" 
#exercise28()
#-----------------------------------------------------------------------------------------------------

# Exercise 29 
"""
    Write a Python program to print out a set containing all the colors from 
    color_list_1 which are not present in color_list_2. 
    Test Data :
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    Expected Output :
    {'Black', 'White'}
"""
#exercise29()

#-----------------------------------------------------------------------------------------------------

# Exercise 38

"""
    Write a Python program to solve (x + y) * (x + y).
    Test Data : x = 4, y = 3
    Expected Output : (4 + 3) ^ 2) = 49
"""
#exercise38()
#-----------------------------------------------------------------------------------------------------

# Exercise 40
"""
    Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
"""
#exercise40()
#-----------------------------------------------------------------------------------------------------

# Exercise 74
"""
    Write a Python program to hash a word
"""
exercise74()