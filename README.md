# Visitor IP and Port Logger

This is a simple web application built with Flask that logs and displays the IP addresses and port numbers of visitors to the website. It uses a SQLite database to store the visitor information.

## Features

- Logs the IP address and port number of each visitor
- Displays a table of all visitors' IP addresses and port numbers
- Simple and clean user interface

## Requirements

- Python 3.x
- Flask
- SQLite

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/visitor-ip-logger.git
    cd visitor-ip-logger
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install Flask
    ```

4. **Initialize the database:**

    ```bash
    python app.py
    ```

    This will create a `database.db` file with the required tables.

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and visit:**

    ```
    http://127.0.0.1:5000/
    ```

    You will see a table displaying the IP addresses and port numbers of visitors.

## Project Structure

visitor-ip-logger/
├── app.py
├── templates/
│ └── index.html
└── database.db


- **app.py:** The main Flask application file.
- **templates/index.html:** The HTML template for the webpage.
- **database.db:** The SQLite database file (created when you run the application for the first time).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Author

Misbah  (https://github.com/misbah7172)
