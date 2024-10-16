# Caesar Cipher Project

This project is a part of the CS50x course and focuses on implementing the Caesar cipher in C. The Caesar cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypts plaintext using a specified shift value.
- Handles both uppercase and lowercase letters.
- Preserves non-alphabetic characters without modification.

## Usage

1. Compile the program:

    ```sh
    gcc -o caesar caesar.c
    ```

2. Run the program with a shift value:

    ```sh
    ./caesar <shift>
    ```

3. Enter the plaintext to be encrypted.

## Example

```sh
$ ./caesar 3
plaintext:  HELLO
ciphertext: KHOOR
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- CS50x by Harvard University
- Inspiration and guidance from the CS50x course materials
- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
