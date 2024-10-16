# Speller

This project implements a spell-checker in C, which is part of the CS50x course. The spell-checker reads a text file and checks each word against a dictionary to identify misspelled words.

## Files

### `speller.c`

This is the main file that drives the spell-checker. It handles the following tasks:

- Parsing command-line arguments to determine the dictionary and text file to use.
- Loading the dictionary into memory.
- Reading the text file and checking each word against the dictionary.
- Reporting misspelled words.
- Measuring the time taken for various operations (loading, checking, etc.).
- Unloading the dictionary from memory.

### `dictionary.c`

This file implements the functionality of the dictionary. It includes:

- A hash table to store the words from the dictionary.
- Functions to load the dictionary, check if a word is in the dictionary, get the size of the dictionary, and unload the dictionary from memory.

### `dictionary.h`

This header file defines the interface for the dictionary functions used in `dictionary.c`.

## Usage

To compile the program, use the following command:

```sh
make speller
```

To run the spell-checker, use:

```sh
./speller [DICTIONARY] text
```

- `DICTIONARY` is an optional argument specifying the dictionary file to use. If not provided, a default dictionary is used.
- `text` is the text file to be spell-checked.

## Example

```sh
./speller dictionaries/large text.txt
```

This command will use the `large` dictionary to spell-check `text.txt`.

## Performance

The program measures and reports the time taken for the following operations:

- Loading the dictionary.
- Checking the words in the text file.
- Determining the size of the dictionary.
- Unloading the dictionary.

## License

This project is part of the CS50x course and is intended for educational purposes.
