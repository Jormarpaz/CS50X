# Fiftyville Project

## Overview

The Fiftyville project is a SQL-based application designed to help users investigate and solve a fictional crime in the town of Fiftyville. This project involves querying a database to gather clues and piece together the events leading up to the crime.

## Features

- **Database Setup:** Create and populate the Fiftyville database with relevant data.
- **Clue Gathering:** Perform SQL queries to gather clues from various tables.
- **Crime Solving:** Analyze the gathered clues to solve the crime.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/fiftyville.git
    ```

2. Navigate to the project directory:

    ```sh
    cd fiftyville
    ```

3. Set up the database:

    ```sh
    sqlite3 fiftyville.db < schema.sql
    ```

## Usage

To use the Fiftyville project, follow these steps:

1. Open the SQLite database:

    ```sh
    sqlite3 fiftyville.db
    ```

2. Perform SQL queries to gather clues:

    ```sql
    SELECT * FROM table_name WHERE condition;
    ```

3. Analyze the gathered clues to solve the crime.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```sh
    git checkout -b feature-branch
    ```

3. Make your changes and commit them:

    ```sh
    git commit -m "Description of changes"
    ```

4. Push to the branch:

    ```sh
    git push origin feature-branch
    ```

5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Happy coding!
