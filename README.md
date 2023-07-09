# Flask CRUD Operations Backend

This is a simple backend application implemented using Flask, a Python web framework. The application provides basic CRUD (Create, Read, Update, Delete) operations for managing data.

## Features

- **Create**: Add new items to the database or locally.
- **Read**: Retrieve data from the database or locally.
- **Update**: Modify existing data in the database or locally.
- **Delete**: Remove data from the database or locally.

## Technologies Used

- Python
- Flask

## Getting Started

### Prerequisites

- Python 3.11.4
- Flask 2.0.1

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Amanmandal-M/Python_Flask.git


2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


## Configuration

### Usage

1. Start the Flask application:

    ```bash
    python app.py

2. Access the API endpoints using a REST client or tools like Postman:
   
   - Create: Send a POST request to `/create` with the item data in the request body.
   
   - Read: Send a GET request to `/` , `/read` to retrieve all items or `/greet/<username>` , `/farewell/<username>` to retrieve a specific item.
   
   - Update: Send a PUT request to `/update/<int:id>` with the updated item data in the request body.
   
   - Delete: Send a DELETE request to `/delete/<int:id>` to remove an item from the database or locally database.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

 - Fork the repository.
 - Create a new branch for your feature or bug fix.
 - Make the necessary changes and commit them.
 - Push your changes to your forked repository.
 - Submit a pull request explaining the changes you've made

## Contact

For any inquiries or questions, please contact:

Aman Kumar - amanmandal644@gmail.com
