# Testing & Debugging Workshop

In this workshop, you will gain hands-on experience applying unit testing and code coverage
concepts (discussed in class) to support the testing and maintenance of software. By the end
of this workshop, you should gain a deeper understanding of:


| Task | Skill | Stack |
|------|-------|-------|
| 1 | Debug code with unit tests | Python + pytest |
| 2 | Measure and improve test coverage | Python + pytest-cov |
| 3 | Explore AI-generated tests | Python + Ollama |
| 4 | Build an AI testing agent | Python + Ollama  |

## Testing Overview

Testing is the process of exercising a program with the intent of:
* _Discovery:_ Executing a program or system with the intent of finding errors.
* _Verification:_ Evaluating an attribute or capability of a program and determining that it meets its required results.

There are two main types of testing:
1. **Black Box Testing:** ignores the internals of the program and focuses on functionality.
2. **White Box Testing:** uses code to guide testing.

This workshop primarily focuses on white box testing, specifically unit testing with Python and the pytest framework. General knowledge of these are required to complete the activities, and a brief overview is provided below.

## pytest

**pytest**[^1] is a popular testing framework for Python that "helps you write better programs". It allows you to create tests using functions that automatically verify your code does what you expect by checking for expected outcomes and generating detailed reports on test results.

In pytest, test cases are typically defined as functions prefixed by `test_`. You can use assertions to verify that the output of a function matches the expected result. For example:

```python no-copy-button
def test_addition():
    assert add(2, 3) == 5

def test_addition2():
    assert add(2, 2) == 5
```

These functions test an add function to ensure it returns the correct sum. Unlike other languages, pytest uses Python's plain `assert` keyword to support testing. Running the tests using the `pytest` command will generate a report of passing and failing tests (see the output for these tests below). 

```plaintext no-copy-button
============================= test session starts =============================
collected 1 item

test_example.py F                                                      [100%]

================================== FAILURES ===================================
_________________________________ test_addition ________________________________

    def test_addition():
>       assert add(2, 2) == 5
E       assert 4 == 5

test_example.py:3:7
=========================== short test summary info ============================
FAILED test_example.py::test_addition - assert 4 == 5
============================== 1 failed in 0.01s ==============================
```


More advanced arguments can be provided to generate more detailed reports, as we will see in Task 2. If an assertion fails, pytest also shows you which values were compared, which can be helpful for debugging. For the most part, any Python boolean can be used in pytest with the proceeding `assert` command (i.e., `assert x in list`, `assert a > b`, etc.). For instance, the `test_addition2` function will fail and raise an AssertionError, indicating incorrect program behavior: in thise case, the expected value would not equal the actual value.

## Verify Your Environment

Work through these steps before starting Task 1. Everything should be pre-installed, but let Dr. Brown know if you face any issues.

1. Confirm Python is installed (needed for all tasks):

    ```bash
    python3 --version
    ```

2. Confirm pytest is available (pre-installed in this workspace):

    ```bash
    pytest --version
    ```

3. Confirm the Ollama service is reachable (needed for Tasks 3 and 4):

    ```bash
    curl -s http://ollama:11434/api/tags | python3 -m json.tool
    ```

> [!TIP]
> Take a moment to explore the workspace in the file tree. Each task lives in its own
> subdirectory: `task1-python/`, `task2-python/`, and `task3-agent/`.

You're ready — move on to **Task 1** when all three commands above succeed.

[^1]: https://docs.pytest.org/