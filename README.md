# Student Grade Calculator
Takes student names and marks, calculates average, 
and outputs a grade. Results are saved to results.txt.

## Features
- Reads student data from a .txt file
- Calculates average marks per student
- Assigns grade based on average
- Handles file not found and invalid data errors

## Project Structure
Grade Calculator
   Data
      Students.txt
      results.txt
    src
       __init__.py
       grades.py
    main.py
    readme.md

## How to run it

1. Clone the repo
   git clone 

2. Create virtual environment
   python -m venv myenv
   myenv\Scripts\activate --windows

3. Install dependencies
   No external dependencies needed. Uses Python built-in libraries only.

4. Run
   python main.py

## Sample Output
Bindu - Average:45.0 - Grade:F
Chandu - Average:91.67 - Grade:A
Dharani - Average:61.67 - Grade:C

## Grade Logic
Average ≥ 90 → A
Average ≥ 75 → B
Average ≥ 50 → C
Below 50 → F

## What I Learned
- How to handle FileNotFoundError using try/except
- How to read and parse structured data from a .txt  file
- How to organise code into functions across multiple modules
- How Python packages work using __init__.py
- How to round floats for clean output using round()