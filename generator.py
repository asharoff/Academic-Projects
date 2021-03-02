import csv
#import math
import random
import numpy as math_stuff
import string
unique1 = []
unique2 = []
def convert(unique):
    i = 6
    z = 0
    count = 0
    the_range = 7
    result = []
    temp = []
    for e in range(the_range):
        temp.append("A")
    for p in range(the_range):
        result.append("A")
    while (unique > 0):
        rem = unique%26
       # print(rem)
        z = ord("A") + rem
        temp[i] = chr(z)
        unique = int(unique/26)
        i = i - 1
        count = count + 1
    j = 0
    # while (j != count):
    #     result[j] = temp[i]
    #     j = j + 1
    #     i = i + 1
    return temp
def generate_relation (num_tuples, generator, prime):
    unique1 = 0
    i = 0
    the_seed = generator
    for i in range(num_tuples):
        the_seed = random.seed(a = the_seed, version = num_tuples)
        unique1 = the_seed - 1
        unique2 = i
def data_generator(num_tuples, the_header):
    generator = 0
    prime = 0
    #if (tupCount <= 1000):
    #    generator = 279
    #    prime = 1009
    #elif (tupCount <= 10000):
    #    generator = 2969
    #    prime = 10007
    #elif (tupCount <= 100000):
    #    generator = 21395
    #    prime = 100003
    #elif (tupCount <= 1000000):
    #    generator = 2107
    #    prime = 1000003
    #elif (tupCount <= 10000000):
    #     generator = 211
    #     prime = 10000019;
    #elif (tupCount <= 100000000):
    #    generator = 21
    #    prime = 100000007;
    #else:
    #     print("too many rows requested")
    #     exit()
    #generate_relation(num_tuples, generator, prime)
    unique1 = []
    unique2 = []
    unique1 = math_stuff.random.permutation(num_tuples)
    for i in range(num_tuples):
        unique2.append(i)
    with open("THE_TENKTUP1.csv", "wt", newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=the_header)
        writer.writeheader()
        counter = 0
        string4_values = ["AAAA","HHHH", "OOOO", "VVVV"]
        the_string4_counter = 0
        z = []
        q = []
        for i in range(45):
            z.append('x')
        for i in range(48):
            q.append('x')
        for i in range(num_tuples):
            stringu1 = ''.join(convert(unique1[i]))
       #     print("string u1 type = ", type(stringu1))
            stringu2 = ''.join(convert(unique2[i]))
            string4 = string4_values[the_string4_counter]
        #    print("string4  type = ", type(string4))
            the_string4_counter = the_string4_counter + 1
            if (the_string4_counter == 4):
                the_string4_counter = 0
            stringu1 = stringu1 + ''.join(z)
         #   print(stringu1)
            string4 = string4 + ''.join(q)
        #    print(string4)
            stringu2 = stringu2 + ''.join(z)
        #    print("string u2 type = ", type(stringu2))
        #    print(stringu2)
            writer.writerow({
                "unique1": unique1[i],
                "unique2": unique2[i],
                "two": unique1[i]%2,
                "four": unique1[i]%4,
                "ten": unique1[i]%10,
                "twenty": unique1[i]%20,
                "onePercent": unique1[i]%100,
                "tenPercent": unique1[i]%10,
                "twentyPercent": unique1[i]%5,
                "fiftyPercent": unique1[i]%2,
                "unique3": unique1[i],
                "evenOnePercent": ((unique1[i]%100)*2),
                "oddOnePercent": ((unique1[i]%100)*2)+1,
                "stringu1": stringu1,
                "stringu2": stringu2,
                "string4": string4,
            })
num_tuples=10000
the_header=["unique1", "unique2", "two", "four", "ten", "twenty",
            "onePercent", "tenPercent", "twentyPercent", "fiftyPercent",
            "unique3", "evenOnePercent", "oddOnePercent", "stringu1", "stringu2", "string4"]
data_generator(num_tuples, the_header)
