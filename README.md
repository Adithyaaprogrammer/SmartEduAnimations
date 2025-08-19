# SmartEdu Animations App

## Overview
SmartEdu Animations App is a web application designed to generate educational animations using the Manim library. The application leverages the ChatGroq model to provide code generation and problem-solving capabilities, making it easier for users to visualize complex mathematical concepts.

## Features
- Generate Python code for Manim animations based on user-defined problem statements.
- Provide detailed explanations and solutions to mathematical problems.
- User-friendly API for seamless interaction with the application.

## Project Structure
```
smartedu-animations-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── api
│   │   └── routes.py          # API routes for handling requests
│   ├── services
│   │   ├── code_generation.py  # Functions for code generation
│   │   └── solution_generation.py # Functions for generating solutions
│   ├── models
│   │   └── __init__.py        # Data models or schemas
│   └── utils
│       └── __init__.py        # Utility functions
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables
└── README.md                   # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd smartedu-animations-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add your API keys and configuration settings.

## Usage
1. Start the application:
   ```
   python src/main.py
   ```

2. Access the API:
   - The API will be available at `http://localhost:5000` (or the port specified in your configuration).

3. Send requests to generate code or solutions:
   - Use tools like Postman or curl to interact with the API endpoints defined in `src/api/routes.py`.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.