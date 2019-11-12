from edison import task, reach, Branch, Filename

# Chapter 1: HyperWorkflows
# Lesson 5:  Experimental Branches


# We can do this task either with big data or small data.
@task
def has_branches(
    dataset=Branch(
        big_data="big.txt",
        small_data="small.txt"),
    output=Filename()):

    print(dataset)  # Either big.txt or small.txt

    # The output will be appropriately namespaced depending on the branch.
    if dataset == "big.txt":
        print(output)  # ./has_branches/dataset.big_data/output
    else:
        print(output)  # ./has_branches/dataset.small_data/output


# We might want to post process the results.
# This task will be run twice, once for each upstream branch.
@task
def post_process(previous=has_branches.output):

    print(previous)
    # ./has_branches/dataset.big_data/output
    # OR
    # ./has_branches/dataset.small_data/output

    # Do something with the upstream output
    print("Some result")

    # Output will write to either
    # ./post_process/dataset.big_data/std_out.txt
    # OR
    # ./post_process/dataset.small_data/std_out.txt
