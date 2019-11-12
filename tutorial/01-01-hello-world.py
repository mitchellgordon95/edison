from edison import task, reach

# Chapter 1: Basics
# Lesson 1:  Running a single command

# Define a single task in the task graph
@task
def hello_world():
  # Will run inside a directory called ./hello_world/
  # Standard out will print to a file called ./hello_world/std_out.txt
  print("hi")
  print("hello")


# Run this task, including all dependencies.
# Since there are no dependencies, just runs the task.
reach(hello_world)


# If the task completes successfully, this should do nothing.
reach(hello_world)
