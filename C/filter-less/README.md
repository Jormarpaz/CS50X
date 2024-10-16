# CS50X Week Projects

## Overview

This week's projects focus on image filtering techniques. You will implement various filters to manipulate images in different ways.

## Projects

### 1. Grayscale Filter

**Description:** Converts a color image to grayscale.
**Usage:**

```bash
./filter -g input.bmp output.bmp
```

### 2. Sepia Filter

**Description:** Applies a sepia tone to the image.
**Usage:**

```bash
./filter -s input.bmp output.bmp
```

### 3. Reflect Filter

**Description:** Reflects the image horizontally.
**Usage:**

```bash
./filter -r input.bmp output.bmp
```

### 4. Blur Filter

**Description:** Blurs the image using a box blur algorithm.
**Usage:**

```bash
./filter -b input.bmp output.bmp
```

## How to Use

1. Compile the code using `make`:

    ```bash
    make filter
    ```

2. Run the desired filter with the appropriate flag and input/output file names.

## Notes

- Ensure your input file is in BMP format.
- The output file will be generated in BMP format.

Happy coding!
