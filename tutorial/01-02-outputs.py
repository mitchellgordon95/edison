from edison import task, FileName, reach

# Chapter 1: Basics
# Lesson 2:  Writing output files


# A task that writes to multiple output files
@task
def named_output_files(x: FileName(), y: FileName("y.txt")):
    print(x)  # './named_output_files/x
    print(y)  # './named_output_files/y.txt

    with open(x, 'w+') as xf:
        print("hello", file=xf)
    with open(y, 'w+') as yf:
        print("world", file=yf)


reach(named_output_files)
