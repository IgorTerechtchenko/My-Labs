#!/usr/bin/python2.7
import argparse
import sys

import sort
import storage
import text_statistics
import fib

parser = argparse.ArgumentParser()
parser.add_argument("-fib", help = "Display fibs up to FIB", type = int)
parser.add_argument("-sto", help = "Work with collection of unique elements.", action = "store_true")
parser.add_argument("-text", help = "Display the statistics of text from TEXT file")
parser.add_argument("-sort", help = "Use various sorting algorythms to sort array in SORT file")

if len(sys.argv) == 1:
    parser.print_help()
    exit
args = parser.parse_args()

if args.fib:
    print fib.generate_fib_sequence(args.fib)

if args.sto:
    storage = storage.Storage()
    while input != "exit": 
        input = raw_input("Enter command:")
        items = input.split()
        if len(items) == 0:
            print "Command required"
            continue
        command = items[0]
        del(items[0])
        if command == "add":
            for x in items:
                storage.add(x)
        elif command == "remove":
            for x in items:
                storage.remove(x)
        elif command == "find":
            for x in items:
                storage.find(x)
        elif command == "list":
            storage.list()
        elif command == "save":
            print items[0]
            storage.save(items[0])
        elif command == "load":
            storage.load(items[0])
        elif command == "grep":
            storage.grep(items[0])    
        elif command != "exit":
            print "Invalid command"

if args.text:
    try:
        with open(args.text, "r") as file:
            text = file.read()
    except IOError:
        print "File {} doesn't exist".format(args.text)

    print "Average wordcount:{}".format(text_statistics.average_wordcount(text))
    print "Median wordcount: {}".format(text_statistics.median_wordcount(text))
    print "Word count: {}".format(text_statistics.count_words(text))
    try: 
        n = raw_input("Enter N:")
        number = raw_input("Enter K:")
        print "Top {0} of {1}-grams is:".format(number, n) 
        print text_statistics.top_ngrams(text, int(n), int(number))
    except ValueError:
        print "Invalid input. Integer required!"

if args.sort:
    try: 
        with open(args.sort, "r") as file:
            ara = file.read().replace("\n", "").replace(" ", "").split(",")
            ara = map(int, ara)
    except IOError:
        print "File {} doesn't exist".format(args.sort)
    print "quick sort"
    sort.demo(ara, sort.quick_sort)
    print "merge sort"
    sort.demo(ara, sort.merge_sort)
    print "radix sort"
    sort.demo(ara, sort.radix_sort)
