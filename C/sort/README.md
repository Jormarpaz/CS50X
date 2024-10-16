# Sort Algorithm Analysis

This project is part of the CS50X course and focuses on analyzing the performance of different sorting algorithms. The analysis is based on the time taken by each algorithm to sort different types of input files: `random.txt`, `sorted.txt`, and `reversed.txt`.

## Sorting Algorithms

### Bubble Sort (sort1)

- **Identification**: The time spent sorting `random.txt` is significantly higher compared to the other two files.
- **Explanation**: Bubble sort has a worst-case and average-case time complexity of O(n²), which makes it inefficient for large datasets, especially when the data is randomly ordered.

### Merge Sort (sort2)

- **Identification**: The time spent sorting all three files (`random.txt`, `sorted.txt`, and `reversed.txt`) is much lower compared to the other algorithms.
- **Explanation**: Merge sort has a consistent time complexity of O(n log n) for all cases, making it efficient for large datasets regardless of their initial order.

### Selection Sort (sort3)

- **Identification**: The time spent sorting `sorted.txt` is significantly different from the time spent on `random.txt` and `reversed.txt`.
- **Explanation**: Selection sort has a time complexity of O(n²) for all cases, but it performs better on nearly sorted data compared to completely random or reversed data.

## Files

- `random.txt`: Contains a list of numbers in random order.
- `sorted.txt`: Contains a list of numbers in ascending order.
- `reversed.txt`: Contains a list of numbers in descending order.

## Conclusion

This project demonstrates the varying efficiencies of different sorting algorithms based on the nature of the input data. Understanding these differences is crucial for selecting the appropriate algorithm for a given problem.

## Author

Jorge

## License

This project is licensed under the MIT License.
