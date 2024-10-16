# Volume Adjustment Tool

This project is a simple command-line tool written in C that modifies the volume of an audio file in the WAV format. The program reads an input WAV file, adjusts the volume by a specified factor, and writes the result to an output WAV file.

## Files

- `volume.c`: The main C program that performs the volume adjustment.

## How It Works

1. **Command-Line Arguments**: The program expects three command-line arguments:
    - The input WAV file.
    - The output WAV file.
    - The volume adjustment factor (a float).

2. **Reading and Writing the Header**: The program reads the 44-byte header from the input WAV file and writes it unchanged to the output WAV file. This header contains important metadata about the audio file.

3. **Adjusting the Volume**: The program reads each audio sample from the input file, multiplies it by the specified factor to adjust the volume, and writes the modified sample to the output file.

## Usage

To compile the program, use a C compiler like `gcc`:

```sh
gcc -o volume volume.c
```

To run the program, use the following command:

```sh
./volume input.wav output.wav factor
```

- `input.wav`: The path to the input WAV file.
- `output.wav`: The path to the output WAV file.
- `factor`: The volume adjustment factor (e.g., `1.5` to increase the volume by 50%, `0.5` to decrease the volume by 50%).

## Example

```sh
./volume input.wav output.wav 1.5
```

This command will read `input.wav`, increase the volume by 50%, and write the result to `output.wav`.

## Error Handling

The program includes basic error handling for:

- Incorrect number of command-line arguments.
- Failure to open the input or output files.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project is part of the CS50x course by Harvard University.
