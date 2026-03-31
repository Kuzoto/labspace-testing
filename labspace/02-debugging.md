# Task 1: Debugging with Unit Tests 🐍

Testing is an essential practice in software development that significantly aids in debugging. In today's workshop, you will use automated tests to identify and fix bugs in a provided program. 

## The Application

The `task1-python/` directory contains a `Calculator` class and a pytest test suite. The tests are
correct — but the implementation has several bugs. Your job is to run the tests, read the failure
output, find the bugs, and fix them in the source code.


Open :fileLink[calculator.py]{path="task1-python/calculator.py"} and read through it. The class provides a simple calculator with seven core operations:

- **`add(a, b)`** — Returns the sum of a and b
- **`subtract(a, b)`** — Returns the difference of a and b
- **`multiply(a, b)`** — Returns the product of a and b
- **`divide(a, b)`** — Returns the quotient of a and b
- **`power(a, n)`** — Returns a to the power of n
- **`is_prime(n)`** — Returns if n is a prime number
- **`is_even(n)`** — Returns if n is an even number
- **`is_fizzbuzz(n)`** — Returns if n is divisible by three and five, based on the classic programming problem[^1]

## Step 1: Run the Test Suite

```bash
cd task1-python && pytest test_calculator.py -v
```

You'll see output like:

```plaintext no-copy-button
PASSED test_calculator.py::test_addition
...
FAILED test_calculator.py::test_fizzbuzz
```

## Step 2: Read the Failure Report

For each failing test, pytest shows:

- **Which test method failed**
- **The assertion that failed** — including the expected value and the actual value returned
- **The line in the test where the failure occurred**

> [!TIP]
> Read the failure message before looking at the source code. The "assert X == Y" line in the
> output directly tells you what the function returned vs. what it should have returned — use
> that as your starting point for tracing the bug.

## Step 3: Investigate and Fix the Bugs

Open :fileLink[calculator.py]{path="task1-python/calculator.py"} and examine the methods that correspond to
the failing tests.

There are **five bugs** in `calculator.py`. Find and fix them.

> [!IMPORTANT]
> You may add additional tests to help detect the bug and verify the fix, but do **not** modify the existing `test_calculator.py` test cases. The tests specify the correct behavior — your job is to fix the implementation to match them.

## Step 4: Verify All Tests Pass

After making your changes, re-run the test suite:

```bash
pytest test_calculator.py -v
```

All tests should pass:

```plaintext no-copy-button
PASSED test_calculator.py::test_addition
PASSED test_calculator.py::test_subtraction
...
13 passed in X.XXs
```

> [!TIP]
> If a test still fails, re-read that specific failure message. The expected vs. actual values
> narrow down exactly which method and which case still has the issue.

## Reflection

Create a `reflections.txt` file which will be used to reflect on each task for this workshop and submit with this workshop. For Task 1, respond to the following questions:

- Briefly describe the five errors. How did running the tests help or hurt with debugging the problems in the code?
- Which errors were more difficult to detect than others?
- Conduct a brief review of the code and tests. How can the code and `calculator.py` and test cases in `test_calculator.py` be improved?
- **With a partner or small group, discuss the following:** What is your general experience with unit testing? What tools and frameworks have you used? Do you have prior experience with pytest?


When you're ready, move on to **Task 2**.

[^1]: https://leetcode.com/problems/fizz-buzz/