# Finance Project

## Overview

The Finance project is a web application designed to simulate a stock trading platform. Users can buy and sell stocks, view their portfolio, and check stock prices in real-time. The project is implemented using Flask, a lightweight web framework for Python.

## Features

- **User Authentication:** Secure user registration and login system.
- **Stock Quotes:** Fetch real-time stock prices using an external API.
- **Buy/Sell Stocks:** Users can buy and sell stocks, and their transactions are recorded.
- **Portfolio Management:** View current holdings and their market value.
- **Transaction History:** Track all past transactions.

## Installation

To install and run this project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/finance.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd finance
    ```

3. **Set up a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Set up the database:**

    ```sh
    flask db upgrade
    ```

6. **Run the application:**

    ```sh
    flask run
    ```

## Usage

To use this project, follow these steps:

1. **Register an account:** Create a new user account.
2. **Log in:** Access your account using your credentials.
3. **Get stock quotes:** Search for stock symbols to get real-time prices.
4. **Buy stocks:** Purchase stocks by entering the stock symbol and quantity.
5. **Sell stocks:** Sell stocks from your portfolio.
6. **View portfolio:** Check your current holdings and their market value.
7. **Transaction history:** Review your past transactions.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**

    ```sh
    git checkout -b feature-branch
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m "Description of changes"
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature-branch
    ```

5. **Open a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
