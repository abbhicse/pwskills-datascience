# Quiz

**1.To open a file c:\scores.txt for reading, we use _____:**

- `.infile = open(“c:\scores.txt”, “r”)`
- `.infile = open(“c:\\scores.txt”, “r”)`
- `infile = open(file = “c:\scores.txt”, “r”)`
- `infile = open(file = “c:\\scores.txt”, “r”)`

**Explanation:** Execute help(open) to get more details.

**2.Which of the following statements are true?**

- `When you open a file for reading, if the file does not exist, an error occurs`
- `When you open a file for writing, if the file does not exist, a new file is created`
- `When you open a file for writing, if the file exists, the existing file is overwritten with the new file`
- `All of the mentioned`

**Explanation:** The program will throw an error.

**3.Which one of the following is not attributes of file?**

- `closed`
- `softspace`
- `rename`
- `mode`

**Explanation:** 

- `rename` is not the attribute of file rest all are files attributes. Attribute Description file.
- `closed` Returns true if file is closed, false otherwise. 
- `mode` Returns access mode with which file was opened. file.name Returns name of the file. 
- `softspace` Returns false if space explicitly required with print, true otherwise.

**4.Which of these methods are used to read in from file?**

- `open()`
- `read()`
- `scan()`
- `readFileInput()`

**Explanation:** Each time `read()` is called, it reads a single byte from the file and returns the byte as an integer value. `read()` returns `-1` when the end of the file is encountered.

**5.the logging …….. In python.**

- `function`
- `module`
- `variable`
- `datatype`

**Explanation:** The logging module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams. It is used by most of the third-party Python libraries, so you can integrate your log messages with the ones from those libraries to produce a homogeneous log  for your application.

**6.which one of the following is the lowest level of logging?**

- `debug`
- `warming`
- `error`
- `none of the above`

**Explanation:** `Debug` is the lowest logging level, it's used to log some diagnostic information about the application.

**7.Which of the following is not a logging function in Python?**

- `logger`
- `filter`
- `critical`
- `All the above`

**Explanation:** `filter` is not a logging function in Python. It is actually a logging concept that allows you to control the flow of log messages based on a set of rules. Filters can be used to exclude certain log messages, based on their logging level, source, or any other criterion. Filters are specified using the addFilter method of a logger object

**8.which of these is not involved in the process of debugging?**

- `Fixing`
- `Isolating`
- `Identifying`
- `Testing`

**Explanation:** `Testing` is a different process and is different from `debugging.` Debugging involves `identifying`, `isolating` and `fixation` of the problems or errors.

**9.What is the purpose of of the import statement in python?**

- `import the statement into a python program`
- `import the function into a python program`
-`import the module into a python program`
- `none of the above`

**Explanation:** The import statement is used to import a module into a Python program, allowing you to use its definitions and statements. By using the import statement, you can access all the variables, functions, and classes defined in the imported module. You can then use them in your program as if they were defined locally.

**10.How can you reload a module in Python?**

- `importlib.reload function.`
- `import reload`
- `import logging`
- `none of the above`

**Explanation:** The importlib.reload function reloads a previously imported module, allowing you to pick up changes that have been made to the module's code. This is useful in situations where you are developing a module and need to test changes without restarting your program.

**11.Which of these class contains the methods used to write in a file?**

- `FileStream`
- `FileInputStream`
- `BUfferedOutputStream`
- `FileBufferStream`

**Explanation:** In `Java`, the `FileOutputStream` and `FileWriter` classes can be used to write to a file. The `BufferedOutputStream` class provides a `buffering layer` on top of an `OutputStream`, which can improve performance when writing to a file.

**12.What is the purpose of the try and except keywords in Python?**

- `To handle errors and exceptions in a program`
- `To perform conditional operations`
- `To create user-defined functions`
- `To import modules`

**Explanation:** The try and except keywords are used to handle errors and exceptions in a program. The try block contains the code that might raise an exception, and the except block contains the code that will handle the exception if it occurs.

**13.What happens if an exception is raised in the try block?**

- `The except block will be executed`
- `The program will continue to run`
- `The program will stop executing`
- `The program will stop executing`

**Explanation:** If an exception is raised in the try block, the program will immediately jump to the except block to handle the exception. If no exception is raised, the code in the except block will not be executed.

**14.What happens if no exception is raised in the try block?**

- `The except block will be executed`
- `The program will continue to run`
- `The program will stop executing`
- `None of the above`

**Explanation:** If no exception is raised in the try block, the code in the except block will not be executed, and the program will continue to run normally.

**15.What is the use of the finally keyword in exception handling?**

- `To handle exceptions and errors`
- `To specify a block of code that will be executed regardless of whether an exception was raised or not`
- `To create user-defined functions`
- `None of the above`

**Explanation:** The finally keyword can be used to specify a block of code that will be executed regardless of whether an exception was raised or not. The code in the finally block will always be executed, even if an exception is raised in the try block or if an error occurs in the except block.

**16.What is a custom exception in Python?**

- `A built-in exception`
- `A user-defined exception`
- `Both A and B`
- `none of the above`

**Explanation:** A custom exception in Python is a user-defined exception that can be raised and caught in the same way as built-in exceptions.

**17.can you create a custom exception in Python?**

- `By using the raise statement`
- `By using the assert statement`
- `Both A and B`
- `none of the above`

**Explanation:** To create a custom exception in Python, you need to define a new exception class that inherits from the built-in Exception class. You can then raise the custom exception by using the raise statement.

**18._____ is a type of errors produce in python programs.**

- `compile time error`
- `run time error`
- `both (a) and (b)`
- `none of the above`

**Explanation:** A compile-time error generally refers to the errors that correspond to the semantics or syntax. A runtime error refers to the error that we encounter during the code execution during runtime. We can easily fix a compile-time error during the development of code. A compiler cannot identify a runtime error.

**19.What exception is raised when a name is not found in the local or global namespace?**

- `TypeError`
- `NameError`
- `ValueError`
- `ImportError`

**Explanation:** NameError is raised when a name is not found in the local or global namespace.

**20.What exception is raised when an attempt is made to divide a number by zero?**

- `ZeroDivisionError`
- `KeyError`
- `IndexError`
- `TypeError`

**Explanation:** `ZeroDivisionError` is raised when an attempt is made to divide a `number` by `zero.`

**21.What exception is raised when a file or directory is requested but does not exist?**

- `SyntaxError`
- `FileNotFoundError`
- `AttributeError`
- `ImportError`

**Explanation:** `FileNotFoundError` is raised when a file or directory is requested but does not exist.

**22.What exception is raised when an attribute reference or assignment fails?**

- `ZeroDivisionError`
- `KeyError`
- `AttributeError`
- `TypeError`

**Explanation:** `AttributeError` is raised when an attribute reference or `assignment fails.`

**23.Look at the following code and select the correct description of error shown while executing it:**

```python
X = int(input("Enter a Number")) 
R = X*X 
print "Square=",R
```

- `can only concatenate str (not "int") to str`
- `missing parenthesis in call to 'print'`
- `name 'Print' is not defined`
- `none of the above`

**Explanation:** `missing parenthesis` in call to `'print'.`

**24.What is multithreading in Python?**

- `A process of running multiple threads simultaneously within a single process.`
- `A process of running multiple processes simultaneously within a single thread.`
- `A process of running multiple processes simultaneously within multiple threads.`
- `A process of running a single process within multiple threads.`

**Explanation:** A is the correct answer, as multithreading in Python is the process of running multiple threads simultaneously within a single process.

**25.What is the purpose of multithreading in Python?**

- `To improve the performance of a program by using multiple CPUs or CPU cores.`
- `To improve the memory utilization of a program by using multiple CPUs or CPU cores.`
- `To improve the overall efficiency of a program by using multiple CPUs or CPU cores.`
- `To improve the input/output operations of a program by using multiple CPUs or CPU cores.`

**Explanation:** A is the correct answer, as the primary purpose of multithreading in Python is to improve the performance of a program by using multiple CPUs or CPU cores.

**26.Which module is used to create and manage threads in Python?**

- `threading`
- `multiprocessing`
- `concurrent.futures`
- `queue`

**Explanation:** A is the correct answer, as the `threading` module is used to `create` and `manage` threads in Python.

**27.What is a mutex in multithreading?**

- `A type of thread that performs a specific task.`
- `A type of thread that runs in the background to handle incoming requests.`
- `A synchronization primitive used to protect shared resources from being accessed by multiple threads at the same time.`
- `A built-in function in Python that is used to release the Global Interpreter Lock.`

**Explanation:** C is the correct answer, as a `mutex` is a `synchronization primitive` used to protect `shared resources` from being accessed by `multiple threads` at the same time.

**28.Which method is used to start a new thread in Python?**

- `start()`
- `run()`
- `create()`
- `begin()`

**Explanation:** A is the correct answer, as the `start()` method is used to `start` a new `thread` in Python.

**29.What is the Global Interpreter Lock (GIL) in Python?**

- `A lock used to protect shared resources from being accessed by multiple threads at the same time.`
- `A mechanism used by Python to ensure that only one thread executes Python bytecode at a time.`
- `A thread that runs in the background to handle incoming requests.`
- `A type of thread that performs a specific task.`

**Explanation:** B is the correct answer, as the `Global Interpreter Lock (GIL)` is a mechanism used by Python to ensure that only one thread executes `Python bytecode` at a time.

**30.What is multiprocessing in Python?**

- `A process of running multiple threads simultaneously within a single process.`
- `A process of running multiple processes simultaneously within a single thread.`
- `A process of running multiple processes simultaneously within multiple threads.`
- `A process of running a single process within multiple threads.`

**Explanation:** B is the correct answer, as multiprocessing in Python is the process of running multiple processes simultaneously within a single thread.

**31.What is the purpose of multiprocessing in Python?**

- `To improve the performance of a program by using multiple CPUs or CPU cores.`
- `To improve the memory utilization of a program by using multiple CPUs or CPU cores.`
- `To improve the overall efficiency of a program by using multiple CPUs or CPU cores.`
- `To improve the input/output operations of a program by using multiple CPUs or CPU cores.`

**Explanation:** A is the correct answer, as the `primary` purpose of `multiprocessing` in Python is to improve the `performance` of a program by using `multiple CPUs` or `CPU cores.`

**32.Which module is used to create and manage processes in Python?**

- `multiprocessing`
- `threading`
- `concurrent.futures`
- `queue`

**Explanation:** A is the correct answer, as the multiprocessing module is used to create and manage processes in Python.

**33.What is a process pool in multiprocessing?**

- `A group of threads that share the same set of variables.`
- `A group of processes that share the same set of variables.`
- `A set of processes that can be executed concurrently to perform a specific task.`
- `A set of threads that can be executed concurrently to perform a specific task.`

**Explanation:** C is the correct answer, as a process pool is a set of processes that can be executed concurrently to perform a specific task.

**34.Which method is used to start a new process in Python?**

- `start()`
- `run()`
- `create()`
- `begin()`

**Explanation:** A is the correct answer, as the `start()` method is used to start a new process in Python.

**35.What is the difference between multiprocessing and multithreading in Python?**

- `Multithreading runs multiple threads simultaneously within a single process, while multiprocessing runs multiple processes simultaneously within a single thread.`
- `Multithreading runs multiple processes simultaneously within a single thread, while multiprocessing runs multiple threads simultaneously within a single process.`
- `Multithreading and multiprocessing are the same thing.`
- `Multiprocessing is used for CPU-bound tasks, while multithreading is used for I/O-bound tasks.`

**Explanation:** `A` is the correct answer, as the primary difference between `multiprocessing` and `multithreading` in Python is that `multiprocessing` runs `multiple processes` simultaneously within a `single thread`, while `multithreading runs multiple threads` simultaneously within a `single process`. The other options are incorrect.
