# Quiz 1

**1.What is the output of the following code?**

```python
x = 5
y = 3
x = y
y = x + 2
print(x, y)
```

- 3 5
- 5 3
- 2 3
- 3 2

**Explanation:** Initially, x is assigned the value 5 and y is assigned the value 3. Then, x is reassigned the value of y, which is 3. Finally, y is updated by adding 2 to the current value of x (which is 3). Therefore, the final values of x and y are 3 and 5, respectively.

**2.What is the output of the following code?**

```python

a = 10
b = 5
c = a // b
d = a % b
print(c, d)
```

- 10 5
- 10 2
- 5 2
- 2 0

**Explanation:** In this code, the floor division operator // is used to divide a by b, resulting in 2. The modulus operator % is used to calculate the remainder of the division, which is 0. Thus, the values of c and d are 2 and 0, respectively.

**3.What is the output of the following code?**

```python

x = 5
y = 10
x = y
y = 20
print(x)
```

- 5
- 10
- 20
- None

Explanation: In the code, x is initially assigned the value 5, y is assigned the value 10, and then x is reassigned the value of y. So, after the assignment x = y, x will have the value 10. The subsequent assignment y = 20 does not affect the value of x. Therefore, when we print x, it will output 10.

**4.What is the output of the following code snippet?**

```python
x = 5
y = 10
if x > y:
    print("x is greater")
else:
    print("y is greater")
```

- x is greater
- y is greater
- Error
- None

**Explanation:** In the code, the condition x > y evaluates to False since 5 is not greater than 10. Therefore, the code executes the else block and prints "y is greater" as the output.

**5.What will be the output of the given code?**

```python
sum = 0
for i in range(1, 6):
    sum += i
print(sum)
```

- 15
- 10
- 5
- 30

**Explanation:** In the code, the for loop iterates over the range from 1 to 5 (excluding 5). In each iteration, the variable i takes the values 1, 2, 3, 4, and 5. The statement sum += i adds each value of i to the variable sum. After the loop, the sum of these numbers is printed as the output, which is 15.

**6.What will be the output of the given code?**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

- 0 1 2 3 4
- 1 2 3 4 5
- 0 1 2 3 4 5
- Error

**Explanation:** In the code, the while loop continues as long as the condition count < 5 is True. Inside the loop, count is printed, starting from 0, and then count is incremented by 1. This process continues until count reaches 5. Since the loop breaks when count is no longer less than 5, the output will be 0, 1, 2, 3, and 4.

**7.What will be the output of the given code if x = 10?**

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

- x is greater than 5
- x is equal to 5
- x is less than 5
- Error

**Explanation:** In the code, the first condition x > 5 evaluates to True since 10 is greater than 5. Therefore, the code executes the corresponding if block and prints "x is greater than 5" as the output. The elif and else blocks are not executed in this case.

**8.Which of the following data types in Python is mutable?**

- int
- float
- tuple
- list

**Explanation:** In Python, lists are mutable, which means you can modify their elements after they are created. You can add, remove, or change elements within a list.

9.Which of the following data types in Python is immutable?

- set
- dict
- list
- str

**Explanation:** In Python, strings are immutable, which means you cannot modify their characters after they are created. Once a string object is created, any changes to the string will result in the creation of a new string object.

**10.Which of the following operations can be performed on immutable objects?**

- Appending new elements
- Removing elements
- Modifying elements
- None of the above

**Explanation:** Immutable objects cannot be modified once they are created. Operations like appending new elements, removing elements, or modifying elements are not applicable to immutable objects. Instead, these operations create new objects.

**11.What happens when you assign a new value to an existing variable of an immutable data type?**

- The existing object is modified with the new value.
- A new object is created with the new value and assigned to the variable.
- An error occurs as you cannot assign a new value to an existing variable of an immutable data type.
- None of the above.

**Explanation:** A new object is created with the new value and assigned to the variable. In Python, when you assign a new value to an existing variable of an immutable data type, a new object is created with the new value, and the variable is reassigned to reference the new object. The existing object remains unchanged.

**12.Consider the following code:**

```python

my_list = [1, 2, 3]
new_list = my_list
new_list.append(4)
print(my_list)
```

What will be the output of the above code?

- [1, 2, 3]
- [1, 2, 3, 4]
- [1, 2, 3, 3, 4]
- Error

**Explanation:** In the code, my_list and new_list initially reference the same list object. Therefore, any modifications made to the list through one variable will be reflected in the other variable as well. When we append the value 4 to new_list, it also affects the list referenced by my_list. Hence, the output will be [1, 2, 3, 4].
