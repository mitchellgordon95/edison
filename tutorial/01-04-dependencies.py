from edison import task, Filename, reach
# Chapter 1: Basics
# Lesson 4:  Running tasks with dependencies


# Write some numbers to a file named numbers
@task
def first(numbers=Filename):
    print(numbers)  # ./first/numbers

    with open(numbers, 'w+') as numbersf:
        for i in range(10):
            print(i, file=numbersf)


# Read the numbers from the file
@task
def and_then(numbers=first.numbers):
    print(numbers)  # ./first/numbers

    with open(numbers, 'r') as af:
        for line in af:
            print(line)


reach(and_then)
