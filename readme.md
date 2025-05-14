# DataParyavaran 🌿

**A Climate Data Analysis Tool for the International Coding Olympiad**

**Submission for Climate Data Analysis Challenge (14-19 yrs) - Deadline: May 15, 2025**

## Project Overview

**DataParyavaran** is a Python-based climate data analysis tool developed by the **NDJ_Protocol** team from **Spring Dale International School**, Beharbari, Guwahati, Assam – 781028. The project focuses on analyzing **Air Quality Index (AQI)** and **Emissions from Thermal Power Plants** using data from the Indian Government Open Data API at [data.gov.in](https://api.data.gov.in). It provides features for data fetching, prediction of future trends, and visualization of air quality and emissions data to highlight environmental impacts.

### Team Members
- **Naija Sona Brahma** (Class 12 - Science)
- **Debaniv Talukdar** (Class 12 - Commerce)
- **Jahnab Dewri** (Class 12 - Science)
- **Mentor:** Mr. Ankur Hazarika (developerankurhazarika@gmail.com)

### Project Timeline
- **Start Date:** Early May 2025
- **Completion Date:** May 14, 2025
- **Submission Deadline:** May 15, 2025

---

## Project Purpose

**DataParyavaran** aims to empower users to explore critical environmental data through:
1. **Air Quality Index (AQI):** Analyze PM2.5 levels across Indian cities, predict next-day PM2.5 values, and visualize air quality trends to understand health and environmental impacts.
2. **Emissions from Thermal Power Plants:** Assess CO2, SO2, and NOx emissions from 2015–2019, predict future CO2 emissions, and visualize emission trends to highlight climate change and air quality impacts.

This project was developed for the **Climate Data Analysis Challenge (14-19 yrs)** as part of the International Coding Olympiad, aiming to raise awareness about air pollution and climate change through data-driven insights.

---

## Features

- **Data Fetching:** Retrieve real-time data from data.gov.in API with a progress bar and retry logic for reliability.
- **Prediction:**
  - Predict next-day PM2.5 levels for a selected city using historical averages.
  - Predict future CO2 emissions from thermal power plants using a growth rate model.
- **Visualization:**
  - Generate Line, Scatter, Bar, Area, and Histogram plots for AQI (PM2.5) by city.
  - Produce Line, Scatter, Bar, and Area plots for Emissions (CO2, SO2, NOx) over years.
- **User-Friendly CLI:** Menu-driven interface for easy navigation.
- **Error Handling:** Validates data files and handles API failures gracefully.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Required libraries: `pandas`, `matplotlib`, `aiohttp`

### Setup Instructions
1. **Unzip the Project Folder:**
   - Extract the `DataParyavaran.zip` file to a folder on your computer (e.g., `C:\DataParyavaran` on Windows or `Documents/DataParyavaran` on macOS/Linux).
   - Move to the extracted `DataParyavaran` folder.

2. **Note:** A `requirements.txt` file is already included in the folder with the following content:
   ```
   pandas
   matplotlib
   aiohttp
   ```

3. **Install Dependencies:** Follow the instructions for your operating system below.

### Running on Different Operating Systems

#### Windows
1. Ensure Python is installed on your computer. (Download and install Python 3.8 or higher from [python.org](https://www.python.org/downloads/) if not already installed.)
2. Double-click the `setup.bat` file in the `DataParyavaran` folder to install all required libraries globally.
   *Note:* The `setup.bat` file contains:
   ```
   pip install -r requirements.txt
   ```
3. To run the application, double-click the `run.bat` file in the `DataParyavaran` folder, or open a Command Prompt in the folder and type:
   ```
   python app.py
   ```

#### Linux
1. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python3 app.py
   ```

#### macOS
1. Open the Terminal application (search for "Terminal" in Spotlight).
2. Navigate to the `DataParyavaran` folder using the Finder, then drag the folder into the Terminal and press Enter to set the path.
3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python3 app.py
   ```

---

## Usage

### Running the Application
Launch the app using the appropriate method for your OS (as shown above). The welcome screen will display:
```
🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
      🌟 Welcome to Spring Dale International School 🌟
             Beharbari, Guwahati, Assam – 781028
🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍

                  📊 Project: DataParyavaran 📊
A climate data analysis tool for the International Coding Olympiad.
            Focus: Air Quality and Emissions.

         📡 Data Source: https://api.data.gov.in (Indian Government Open Data)

                       🌿 Team: NDJ_Protocol 🌿
                           👥 Members:
                 - Naija Sona Brahma (Class 12 - Science)
                 - Debaniv Talukdar (Class 12 - Commerce)
                   - Jahnab Dewri (Class 12 - Science)
                  - Mentor: Mr. Ankur Hazarika

🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
```

### Main Menu
- **1. Air Quality Index (AQI):** Analyze AQI data.
- **2. Emissions from Thermal Power Plants:** Analyze emissions data.
- **0. Exit:** Close the application.

### AQI Submenu
- **1. Fetch AQI Data:** Fetch data from the API and save to `data/api_data/aqi_data.csv`. Option to overwrite `data/SavedData/aqi_data.csv`.
- **2. Predict Next-Day PM2.5 for a City:** Predict PM2.5 levels for a selected city.
- **3. Plot Graphs:** Generate Line, Scatter, Bar, Area, and Histogram plots for PM2.5 by city.
- **0. Back to Main Menu**

### Emissions Submenu
- **1. Fetch Emissions Data:** Fetch data from the API and save to `data/api_data/emissions_data.csv`. Option to overwrite `data/SavedData/emissions_data.csv`.
- **2. Predict Future CO2 Emissions:** Predict CO2 emissions for a future year.
- **3. Plot Graphs:** Generate Line, Scatter, Bar, and Area plots for CO2, SO2, and NOx over years.
- **0. Back to Main Menu**

### Example Interaction
#### Predicting AQI
```
🔍 AQI Analysis Options:
  1. Fetch AQI Data
  2. Predict Next-Day PM2.5 for a City
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 2
🔍 Choose data source for AQI:
  1. API Fresh Data
  2. Old Saved Data
  0. Cancel
💡 Enter the number (e.g., 1, 2, 0):
> 2

Available cities: Kadapa, Mumbai, Delhi, ...
Enter city name (e.g., Kadapa): Kadapa
Predicted PM2.5 for Kadapa on May 14, 2025: 32.5 µg/m³
Impacts:
  - Health: Good air quality, minimal health risks.
  - Environmental: Minimal smog, no significant impact on ecosystems.
  - Economic: Low healthcare costs due to reduced pollution-related illnesses.
💡 Would you like to predict for another city? (y/n):
> n
```

#### Plotting Emissions
```
🔍 Emissions Analysis Options:
  1. Fetch Emissions Data
  2. Predict Future CO2 Emissions
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 3
🔍 Choose data source for Emissions:
  1. API Fresh Data
  2. Old Saved Data
  0. Cancel
💡 Enter the number (e.g., 1, 2, 0):
> 2

📊 Displaying all Emissions plots...
[Four windows: Line, Scatter, Bar, Area]

✅ Emissions plots saved to the 'plots/' directory:
  - plots/emissions_line.png
  - plots/emissions_co2_scatter.png
  - plots/emissions_co2_bar.png
  - plots/emissions_area.png
```

---

## Data Details

### AQI Data (`aqi_data.csv`)
- **Source:** [data.gov.in API](https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69)
- **Columns:** `city`, `pollutant_id`, `avg_value`, etc.
- **Focus:** PM2.5 levels (µg/m³) for prediction and visualization.
- **Sample:** (Based on typical AQI data structure)
  ```
  city,pollutant_id,avg_value
  Kadapa,PM2.5,35
  Mumbai,PM2.5,50
  ```

### Emissions Data (`emissions_data.csv`)
- **Source:** [data.gov.in API](https://api.data.gov.in/resource/38af56a8-1abb-44ad-b83d-cce79168fd4e)
- **Columns:** `year`, `gaseous_pollutants___carbon_dioxide___ton_per_capita_day`, `gaseous_pollutants___sulphur_dioxide___kg_per_capita_per_day`, `gaseous_pollutants___nitrogen_oxides___kg_per_capita_per_day`
- **Focus:** CO2, SO2, and NOx emissions for prediction and visualization.
- **Sample:** (Based on typical emissions data structure)
  ```
  year,gaseous_pollutants___carbon_dioxide___ton_per_capita_day,gaseous_pollutants___sulphur_dioxide___kg_per_capita_per_day,gaseous_pollutants___nitrogen_oxides___kg_per_capita_per_day
  2015,2.1,0.5,0.3
  2016,2.2,0.6,0.4
  ```

---

## Future Improvements
- **Enhanced Predictions:** Implement linear regression or machine learning models for more accurate predictions.
- **Additional Data Sources:** Integrate more APIs to expand the dataset.
- **GUI Interface:** Develop a graphical user interface using Tkinter or Flask.
- **Interactive Visualizations:** Use Plotly for interactive plots.

---

## Acknowledgments
- **Spring Dale International School** for providing support and resources.
- **data.gov.in** for open access to environmental data.
- **International Coding Olympiad** for organizing the Climate Data Analysis Challenge.
- **Mentor Mr. Ankur Hazarika** for guidance and encouragement.

---

**Team NDJ_Protocol**  
**Spring Dale International School**  
**May 14, 2025**

---
