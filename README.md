AT&T Employee ID Enumerator

This repository contains two Python scripts that help generate employee IDs based on T9 format for initials. The scripts use a predefined T9 mapping to convert initials into a numeric ID, and append a 4-digit random number at the end. The two scripts are as follows:

1. **main.py**: This is the main script that prompts the user to enter their initials, and then generates an employee ID based on those initials. The employee ID is constructed from the T9 values of the initials (first, middle, and last letters) followed by a 4-digit random number.

2. **enumerate.py**: This script generates and enumerates all possible combinations of employee IDs. It creates every combination of three letters (from a to z), converts them to their corresponding T9 numeric values, and appends a random 4-digit number to each combination. The total number of combinations is 26^3 = 17,576.

How to Use:

1. Clone the repository:
   git clone https://github.com/SleepTheGod/AT-T-Employee-ID-Enumerator/

2. Navigate to the project directory:
   cd AT-T-Employee-ID-Enumerator

3. Run the main script:
   python main.py

   The script will prompt you to enter your initials, and will output your generated employee ID.

4. To generate all possible employee IDs:
   python enumerate.py

   This will output all combinations of employee IDs. You can modify the script to save the output to a file if needed.

Requirements:
- No external dependencies required. The scripts only use Python's built-in libraries.

License:
This project is licensed under the MIT License.

Feel free to fork the repository, make modifications, or contribute to the project.
