from edison import task, reach

# Chapter 1: Basics
# Lesson 3:  Tasks are pure functional


b = 3
@task
def this_breaks():
    # You cannot reference globals or closure variables inside task. This is
    # because tasks may run in different processes on different machines
    print(5 + b)


@task
def import_math():
    # This means all imports must happen *inline* inside a task.
    import math
    print(math.sqrt(2))


# reach(this_breaks)
reach(import_math)
