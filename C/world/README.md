# Hello World Project

This project contains a simple C program that prints "hello, world" to the console. It is a basic example often used to introduce beginners to programming in C.

## File Structure

- `hello.c`: The main C file containing the code to print "hello, world".

## Code Explanation

```c
#import <stdio.h>
#import <cs50.h>

string s = "hello, world";

int main(void)
{
    printf("%s\n", s);
}
```

### Libraries Used

- `#import <stdio.h>`: Standard Input Output library in C, used for functions like `printf`.
- `#import <cs50.h>`: A library provided by CS50, which includes custom data types and functions.

### Variables

- `string s = "hello, world";`: Declares a string variable `s` and initializes it with "hello, world".

### Main Function

- `int main(void)`: The main function where the program execution begins.
- `printf("%s\n", s);`: Prints the string `s` followed by a newline character.

## How to Compile and Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing `hello.c`.
3. Compile the program using a C compiler, for example:

   ```sh
   gcc hello.c -o hello
   ```

4. Run the compiled program:

   ```sh
   ./hello
   ```

## Conclusion

This project serves as a foundational step in learning C programming. It demonstrates the basic structure of a C program, including variable declaration, library inclusion, and the use of the `printf` function.
