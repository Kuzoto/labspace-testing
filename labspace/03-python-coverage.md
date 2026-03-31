# Task 2: Improving Test Coverage 📊

The `task2-python/` directory contains a `Leaderboard` class and a small test suite. The existing
tests all pass — but they only exercise a fraction of the code. Your goal is to raise coverage
to **85% or higher**.

## The Leaderboard Class

Open :fileLink[leaderboard.py]{path="task2-python/leaderboard.py"} and read through it. The class
manages players in a competitive gaming or hackathon setting and supports:

- Registering players and setting initial scores (`add_player`)
- Recording match outcomes with point transfers (`record_match`)
- Querying ranks and top-N standings (`get_rank`, `get_top_n`)
- Computing percentile rankings (`get_percentile`)
- Applying score multipliers / bonuses (`apply_bonus`)
- Calculating win rates (`get_win_rate`)
- Resetting the board (`reset`)

Most methods raise exceptions for invalid inputs. Pay close attention to those branches — they
are the most likely to be uncovered.

## Step 1: Run the Existing Tests and See the Coverage Report

```bash
cd task2-python && pytest test_leaderboard.py --cov=leaderboard --cov-report=term-missing -v
```

You'll see output like:

```plaintext no-copy-button
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
leaderboard.py      XX     XX    XX%   18, 22-25, 34-36, ...
```

Note the **Missing** column — those line numbers are your targets.

## Step 2: Understand What's Not Being Tested

Cross-reference the missing line numbers with
:fileLink[leaderboard.py]{path="task2-python/leaderboard.py"}. Look for:

- **Error-handling branches** — `raise ValueError(...)` and `raise KeyError(...)` lines that
  are never triggered
- **Untested methods** — entire methods whose lines all appear in the Missing column
- **Edge cases** — e.g., a player with no games played, score floored at zero, single-player
  percentile

> [!TIP]
> Group the missing line numbers by method. A consecutive block of lines all in one method
> means that method has zero test coverage and needs at least one new test.

## Step 3: Write Additional Tests

Open :fileLink[test_leaderboard.py]{path="task2-python/test_leaderboard.py"} and add new test
functions. Work through the uncovered lines systematically.

For each missing code path, ask:

1. What input causes execution to reach that line?
2. What is the expected outcome — a return value, a state change, or an exception?
3. What assertion confirms the correct behavior?

Use `pytest.raises()` to test exception-raising paths:

```python no-run-button
def test_record_match_unregistered_player_raises():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(KeyError):
        lb.record_match("Alice", "Ghost")
```

> [!NOTE]
> You don't need to reach 100% coverage. Focus on meaningful paths: error conditions, boundary
> values, and every method that currently has zero coverage. Avoid trivial tests that execute a
> line without asserting anything useful. 

## Step 4: Check Your Progress

After adding tests, re-run the coverage report:

```bash
pytest test_leaderboard.py --cov=leaderboard --cov-report=term-missing -v
```

Repeat Steps 3–4 until coverage reaches **85% or higher**. **Take a screenshot of your results to include with the workshop submission!**

## Reflection

- Which uncovered code paths were most likely to hide real bugs? Why?
- This activity only focuses on line coverage. Add the `--cov-branch` argument to include branch coverage for this test suite. What is the branch coverage of the updated test suite, and how would you modify the test cases to increase the branch/path coverage for this program? 

```bash
pytest test_leaderboard.py --cov=leaderboard --cov-branch --cov-report=term-missing -v
```
> (`Branch` = total possible branches, `BrPart` = partially covered branches)


- Compare your experience here to Task 1: if `calculator.py` had a coverage report before you started, would it have pointed you directly to the buggy lines?
- How can the concepts of test coverage and unit testing affect your future development practices?

When you're ready, continue to **Task 3**.
