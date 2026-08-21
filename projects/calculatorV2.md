# Exercise Challenges — Building a Robust Number Calculator

## Objective

Improve a basic number-calculation program so that it can:

* Accept an unlimited number of inputs.
* Handle invalid user input safely.
* Prevent division by zero.
* Display the complete calculation.
* Provide useful statistics about the entered numbers.

---

## Challenge 1 — Unlimited Numbers

Instead of asking:

> How many numbers do you want to calculate?

Allow the user to enter numbers **one at a time** until they decide to stop.

### Expected behavior

```text
Enter numbers one by one.
Type "done" when you are finished.

Enter number: 10
Enter number: 20
Enter number: 5
Enter number: 15
Enter number: done

Result: 50
```

## Challenge 2 — Division by Zero

Prevent the user from dividing by zero.

### Example

```text
Enter number: 10
Enter number: 0

Error: Cannot divide by zero!
```

The program should **continue working** instead of crashing.

### Requirements

* Detect division by zero.
* Display an appropriate error message.
* Allow the user to continue using the calculator.

---

## Challenge 3 — Show the Complete Calculation

Do not display only the final result.

Instead of:

```text
Result: 50
```

Display the complete calculation:

```text
10 + 20 + 5 + 15 = 50
```

For multiplication:

```text
2 × 5 × 10 = 100
```


### Examples

**Addition:**

```text
10 + 20 + 5 + 15 = 50
```

**Multiplication:**

```text
2 × 5 × 10 = 100
```

---

## Challenge 5 — Number Statistics

After the calculation is complete, display statistics about the numbers entered.

### Example

```text
Numbers entered: 4
Smallest number: 5
Largest number: 20
Average: 12.5
```

### Requirements

Calculate and display:

* The total number of values entered.
* The smallest number.
* The largest number.
* The average.

### Useful Python functions

```python
min()
max()
sum()
len()
```

The average can be calculated using:

```python
sum(numbers) / len(numbers)
```

---

## Final Challenge — Combine Everything

Once all five challenges are completed, integrate them into **one robust calculator program**.

The final program should:

* Accept unlimited numbers.
* Allow the user to type `done` to finish.
* Reject invalid numbers without crashing.
* Prevent division by zero.
* Display the complete calculation.
* Display the final result.
* Display statistics about the entered numbers.
* Continue running correctly after recoverable errors.
* Handle edge cases such as entering `done` before any valid number.

### Goal

The final program should feel like a small, reliable calculator rather than a simple demonstration program.
