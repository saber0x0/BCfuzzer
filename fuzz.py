import sys

from mph.program import Program
from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer
import binop

PATH_TO_NAME = "/Users/huahua/PycharmProjects/lpy/fuzzer/BCfuzzer/name"   # fill this in yourself


def run(string):
    """
    Sends the provided string to the `name` program and runs it with that
    input. Returns the return value `name` gives us
    """
    prog = Program(PATH_TO_NAME, [])
    prog.append_string_stdin(string)
    prog.exec()

    return prog.retval


def generate_input(n):
    """
    Returns an alphanumeric string with a length no greater than n.
    """
    fuzzer = AlphaNumericFuzzer(0, n)

    return fuzzer.generate()


if __name__ == "__main__":
    # usage
    if len(sys.argv) != 3:
        print("usage: python3 fuzz.py num_cases max_length")
        exit(1)

    # command-line arguments
    num_cases = int(sys.argv[1])  # number of test cases to run
    max_length = int(sys.argv[2])  # maximum length of each string
    # path_name = str(sys.argv[3])
    results = []  # list for storing the result of each test

    # main loop
    for i in range(num_cases):
        usr_input = generate_input(max_length)  # generate input string
        return_value = run(usr_input)  # run name with our input

        # save test results to our global results list
        test_result = {"num": i, "input": usr_input, "output": return_value}
        results.append(test_result)

    # print summary
    for test in results:
        print("Case #{:d}:".format(test["num"]))
        print("	IN: " + test["input"])
        print("	OUT: {:4d}".format(test["output"]))
        # print("\n")
