# BMI Calculation Project

This project is a BMI  calculation form built using Python's Tkinter for the GUI and Matplotlib for the graphical representation of BMI categories.
The application collects user details, calculates BMI, categorizes it, and displays a pie chart showing the distribution of BMI categories.

## Features

- **User Input Form:** Collects user information such as name, age, weight, and height.
- **BMI Calculation:** Computes BMI based on the user's weight and height.
- **BMI Categorization:** Classifies the BMI into categories: Underweight, Normal weight, Overweight, and Obesity.
- **Data Saving:** Saves the user details and BMI category into a CSV file.
- **Pie Chart Display:** Shows a pie chart of BMI categories using data from the CSV file.
- **Data Validation:** Ensures that all input fields are filled and contain valid data.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Matplotlib

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/anushamulukutla/BMI_GUI_PROJECT
    cd BMI_GUI_PROJECT
    ```

2. **Install the required packages:**
    ```bash
    pip install matplotlib
    ```
3.**IDE:
   Pycharm IDE
    

## Usage

1. **Run the application:**
    Run the application in Pycharm IDE
   
  

3. **Enter user details:**
    - Name
    - Age
    - Height (in meters)
    - Weight (in kilograms)

4. **Save data:**
    - Click the "Save" button to save the data and calculate the BMI.

5. **Clear entries:**
    - Click the "Continue" button to clear the input fields for new data entry.

6. **Show graph:**
    - Click the "Show Graph" button to display a pie chart of the BMI categories.

## File Structure

- **bmi_calculation_form.py:** The main Python script containing the application code.
- **bmidata.csv:** The CSV file where user data and BMI categories are saved.

## Functions

- **BMI_cal(weight, height):** Calculates BMI using weight and height.
- **bmi_category(bmi):** Returns the BMI category based on the calculated BMI.
- **user_details():** Gathers user input and validates it.
- **write_csv_file(Bmdata):** Writes user data to the CSV file.
- **save_data():** Handles the data saving process.
- **clear_entries():** Clears the input fields.
- **get_list_of_category():** Reads BMI categories from the CSV file.
- **show_graph_pie():** Generates and displays the pie chart in the GUI.

## Screenshots
 Screen_shot_GUL_BMI_Project.pdf
 Screen_shots_Images_BMI_GUI_PROJECT.pdf


## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [Matplotlib](https://matplotlib.org/) for the graphing capabilities.

