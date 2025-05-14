# DataParyavaran 🌍

**A Climate Data Analysis Tool for the International Coding Olympiad**

**Submission for Climate Data Analysis Challenge (14-19 yrs) - Deadline: May 15, 2025**

## Project Overview

**DataParyavaran** is a Python-based climate data analysis tool developed by the **NDJ Protocol** team from **Spring Dale International School**, Beharbari, Guwahati, Assam – 781028. The project focuses on analyzing Air Quality Index (AQI) and Emissions data from Thermal Power Plants in India, sourced from the Indian Government Open Data API at [data.gov.in](https://api.data.gov.in). It provides functionalities for data fetching, prediction, and visualization, making it a comprehensive tool for environmental data analysis.

### Team Members
- **Naija Sona Brahma** (Class 12 - Science)
- **Debaniv Talukdar** (Class 12 - Commerce)
- **Jahnab Dewri** (Class 12 - Science)
- **Mentor:** Mr. Ankur Hazarika

### Project Timeline
- **Start Date:** Early April 2025
- **Completion Date:** May 14, 2025
- **Submission Deadline:** May 15, 2025

---

## Project Purpose

The goal of **DataParyavaran** is to provide an accessible tool for students and researchers to analyze climate data, focusing on:
1. **Air Quality Index (AQI):** Fetch real-time AQI data, predict next-day PM2.5 levels for a city, and visualize PM2.5 trends.
2. **Emissions from Thermal Power Plants:** Fetch historical emissions data, predict future CO2 emissions, and visualize pollutant trends (CO2, SO2, NOx).

This project was developed for the **Climate Data Analysis Challenge (14-19 yrs)** as part of the International Coding Olympiad, aiming to raise awareness about environmental issues through data-driven insights.

---

## Development Journey

### Initial Setup
- **Objective:** Create a tool to fetch, predict, and visualize AQI and Emissions data.
- **Data Source:** [data.gov.in API](https://api.data.gov.in).
- **Tools Used:** Python, pandas, matplotlib, aiohttp for asynchronous API calls.
- **Directory Structure:**
  ```
  DataParyavaran/
  ├── data/
  │   ├── api_data/          # Fresh data fetched from API
  │   └── SavedData/         # User-saved data
  ├── plots/                 # Generated plots
  ├── api.py                 # API fetching logic
  ├── prediction.py          # Prediction logic
  ├── plotting.py            # Plotting logic
  └── app.py                 # Main application
  ```

### Phase 1: Data Fetching (`api.py`)
- **Objective:** Fetch AQI and Emissions data from data.gov.in API.
- **Implementation:**
  - Used `aiohttp` for asynchronous API calls to improve performance.
  - Added a progress bar to simulate download progress.
  - Implemented retry logic (3 retries with exponential backoff) to handle API instability.
- **Challenges:**
  - The API was unstable, often failing to respond.
  - Solution: Added retry logic and fallback to saved data.
- **Code Snippet (`api.py`):**
  ```python
  async def fetch_data_async(url, topic, retries=3, backoff_factor=2):
      print(f"🚀 Initiating {topic} data fetch from data.gov.in...")
      for attempt in range(retries):
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(url) as response:
                      if response.status == 200:
                          data = await response.json()
                          return pd.DataFrame(data['records'])
                      else:
                          raise Exception(f"Failed to fetch {topic} data: HTTP {response.status}")
          except Exception as e:
              if attempt < retries - 1:
                  wait_time = backoff_factor ** attempt
                  print(f"❌ Attempt {attempt + 1} failed: {str(e)}. Retrying in {wait_time} seconds...")
                  await asyncio.sleep(wait_time)
              else:
                  raise e
  ```

### Phase 2: Main Application (`app.py`)
- **Objective:** Create a user-friendly CLI interface to interact with the tool.
- **Implementation:**
  - Designed a menu-driven interface with options for AQI and Emissions analysis.
  - Added submenus for each topic with options to fetch data, predict, and plot.
  - Implemented data source selection (API fresh data or saved data) and overwrite options.
- **Flowchart:**
  ```mermaid
  flowchart TD
      A[Start] --> B[Display Welcome Message]
      B --> C[Main Menu]
      C -->|1| D[AQI Submenu]
      C -->|2| E[Emissions Submenu]
      C -->|0| F[Exit]
      D -->|1| G[Fetch AQI Data]
      D -->|2| H[Predict PM2.5]
      D -->|3| I[Plot AQI Graphs]
      D -->|0| C
      E -->|1| J[Fetch Emissions Data]
      E -->|2| K[Predict CO2]
      E -->|3| L[Plot Emissions Graphs]
      E -->|0| C
      G --> M[Save to api_data/]
      M --> N[Overwrite SavedData/?]
      N -->|Yes| O[Update SavedData/]
      N -->|No| D
      J --> P[Save to api_data/]
      P --> Q[Overwrite SavedData/?]
      Q -->|Yes| R[Update SavedData/]
      Q -->|No| E
      H --> S[Choose Data Source]
      S --> T[Run Prediction]
      K --> U[Choose Data Source]
      U --> V[Run Prediction]
      I --> W[Choose Data Source]
      W --> X[Generate Plots]
      L --> Y[Choose Data Source]
      Y --> Z[Generate Plots]
      F --> AA[Close All Plots]
      AA --> AB[End]
  ```

### Phase 3: Prediction (`prediction.py`)
- **Objective:** Add prediction capabilities for AQI PM2.5 and Emissions CO2.
- **Implementation:**
  - For AQI: Predict next-day PM2.5 levels for a user-selected city using a simple averaging method.
  - For Emissions: Predict CO2 emissions for a future year using linear extrapolation.
  - Added `is_file_valid` to validate data files before processing.
- **Comparison Table: Prediction Methods**
  | Feature            | AQI Prediction (PM2.5)       | Emissions Prediction (CO2)    |
  |--------------------|------------------------------|-------------------------------|
  | Method             | Average of historical data   | Linear extrapolation          |
  | Input Data         | PM2.5 avg_value by city      | CO2 ton_per_capita_day by year|
  | Output             | Next-day PM2.5 (µg/m³)       | CO2 for future year (ton/capita/day) |
  | Accuracy           | Basic (assumes stability)    | Basic (assumes linear trend)  |
  | Future Improvement | Machine Learning model       | Polynomial regression         |

### Phase 4: Visualization (`plotting.py`)
- **Objective:** Visualize AQI and Emissions data using matplotlib.
- **Initial Attempt by Student (Jahnab Dewri):**
  - Created scatter and bar plots for Emissions data (CO2 per capita over years).
  - Code Snippet (Original):
    ```python
    import matplotlib.pyplot as plt
    import csv
    x = []
    y = []
    with open('emissions_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x.append(int(row['year']))
            y.append(float(row['gaseous_pollutants___carbon_dioxide___ton_per_capita_day']))
    plt.title("Gaseous Pollutants", fontsize=20)
    plt.xlabel("Years", fontsize=15)
    plt.ylabel("CO2", fontsize=15)
    plt.scatter(x, y, color="green", edgecolor="black", label="Ton per capita day")
    plt.legend(loc=2)
    plt.show()
    ```
  - **Feedback:** Good start, but lacked variety in plot types, used `csv` instead of `pandas`, and didn’t save plots.

- **Enhancements:**
  - Switched to `pandas` for data loading.
  - Added multiple plot types:
    - **AQI Plots (PM2.5):** Line, Scatter, Bar, Area, Histogram.
    - **Emissions Plots (CO2, SO2, NOx):** Line, Scatter, Bar, Area.
  - Saved plots to `plots/` directory.
  - Displayed all plots for a topic simultaneously, closing previous plots when switching topics.
- **Comparison Table: Plot Types**
  | Plot Type  | AQI (PM2.5)       | Emissions (CO2, SO2, NOx) | Purpose                       |
  |------------|-------------------|---------------------------|-------------------------------|
  | Line       | ✅ Cities vs. PM2.5 | ✅ Years vs. Pollutants    | Show trends over time/series  |
  | Scatter    | ✅ Cities vs. PM2.5 | ✅ Years vs. CO2          | Highlight individual data points |
  | Bar        | ✅ Cities vs. PM2.5 | ✅ Years vs. CO2          | Compare discrete values       |
  | Area       | ✅ Cities vs. PM2.5 | ✅ Years vs. Pollutants    | Show cumulative trends        |
  | Histogram  | ✅ PM2.5 Distribution | ❌                        | Show data distribution        |

- **Flowchart: Plotting Process**
  ```mermaid
  flowchart TD
      A[Start Plotting] --> B[Close Previous Plots]
      B --> C[Load Data with pandas]
      C -->|AQI| D[Filter PM2.5 Data]
      C -->|Emissions| E[Extract CO2, SO2, NOx]
      D --> F[Create AQI Plots]
      E --> G[Create Emissions Plots]
      F --> H[Line, Scatter, Bar, Area, Histogram]
      G --> I[Line, Scatter, Bar, Area]
      H --> J[Save to plots/]
      I --> J
      J --> K[Display All Plots Together]
      K --> L[End Plotting]
  ```

### Phase 5: Final Enhancements
- **Window Management:**
  - Added logic to close previous plot windows when switching topics or re-entering the same topic.
  - Ensured all plot windows are closed on program exit.
- **Error Handling:**
  - Added validation for data files (existence, non-empty, valid content).
  - Handled API failures with retries and error messages.

---

## Installation

### Prerequisites
- Python 3.8+
- Required libraries:
  ```bash
  pip install pandas matplotlib aiohttp
  ```

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/NDJ-Protocol/DataParyavaran.git
   cd DataParyavaran
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` with: `pandas`, `matplotlib`, `aiohttp`)*
3. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

### Running the Application
1. Launch the app:
   ```bash
   python app.py
   ```
2. The welcome screen displays:
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
- **2. Emissions from Thermal Power Plants:** Analyze Emissions data.
- **0. Exit:** Close the application.

### AQI Submenu
- **1. Fetch AQI Data:** Fetch data from the API and save to `data/api_data/aqi_data.csv`. Option to overwrite `data/SavedData/aqi_data.csv`.
- **2. Predict Next-Day PM2.5 for a City:** Predict PM2.5 levels for a selected city.
- **3. Plot Graphs:** Generate and display five plots (Line, Scatter, Bar, Area, Histogram) for PM2.5 data.
- **0. Back to Main Menu**

### Emissions Submenu
- **1. Fetch Emissions Data:** Fetch data from the API and save to `data/api_data/emissions_data.csv`. Option to overwrite `data/SavedData/emissions_data.csv`.
- **2. Predict Future CO2 Emissions:** Predict CO2 emissions for a future year.
- **3. Plot Graphs:** Generate and display four plots (Line, Scatter, Bar, Area) for CO2, SO2, and NOx.
- **0. Back to Main Menu**

### Example Interaction
#### Fetching AQI Data
```
🔍 AQI Analysis Options:
  1. Fetch AQI Data
  2. Predict Next-Day PM2.5 for a City
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 1
🚀 Initiating AQI data fetch from data.gov.in...
[==================================================] 100%  Speed: 1000.0 KB/s
✅ Data fetched from data.gov.in API and saved to data/api_data/aqi_data.csv

💡 Would you like to update the Saved AQI Data with this newly fetched data? (y/n):
> y
✅ Saved AQI Data updated with new data at data/SavedData/aqi_data.csv
```

#### Plotting AQI Graphs
```
🔍 AQI Analysis Options:
  1. Fetch AQI Data
  2. Predict Next-Day PM2.5 for a City
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 3
🔍 Choose data source for AQI:
  1. API Fresh Data
  2. Old Saved Data
  0. Cancel
💡 Enter the number (e.g., 1, 2, 0):
> 2

📊 Displaying all AQI plots...
[Five windows open: Line, Scatter, Bar, Area, Histogram]

✅ AQI plots saved to the 'plots/' directory:
  - plots/aqi_pm25_line.png
  - plots/aqi_pm25_scatter.png
  - plots/aqi_pm25_bar.png
  - plots/aqi_pm25_area.png
  - plots/aqi_pm25_histogram.png
```

#### Switching to Emissions Plots
```
🔍 AQI Analysis Options:
  1. Fetch AQI Data
  2. Predict Next-Day PM2.5 for a City
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 0

🔍 Select a topic to explore:
  1. Air Quality Index (AQI)
  2. Emissions from Thermal Power Plants
  0. Exit
💡 Enter the number (e.g., 1, 2, 0):
> 2

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

[All AQI plot windows close]

📊 Displaying all Emissions plots...
[Four windows open: Line, Scatter, Bar, Area]

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
- **Columns:**
  - `country`, `state`, `city`, `station`, `last_update`, `latitude`, `longitude`, `pollutant_id`, `min_value`, `max_value`, `avg_value`
- **Focus:** PM2.5 data for prediction and visualization.
- **Sample:**
  ```
  country,state,city,station,last_update,latitude,longitude,pollutant_id,min_value,max_value,avg_value
  India,Andhra_Pradesh,Anantapur,Gulzarpet, Anantapur - APPCB,13-05-2025 23:00:00,14.675886,77.593027,SO2,13,15,14
  India,Andhra_Pradesh,Anantapur,Gulzarpet, Anantapur - APPCB,13-05-2025 23:00:00,14.675886,77.593027,OZONE,8,32,24
  ```

### Emissions Data (`emissions_data.csv`)
- **Source:** [data.gov.in API](https://api.data.gov.in/resource/38af56a8-1abb-44ad-b83d-cce79168fd4e)
- **Columns:**
  - `year`, `installed_capacity__as_on_march_`, `gaseous_pollutants___carbon_dioxide___ton_day`, `gaseous_pollutants___carbon_dioxide___ton_per_capita_day`, `gaseous_pollutants___sulphur_dioxide___ton_day`, `gaseous_pollutants___sulphur_dioxide___kg_per_capita_per_day`, `gaseous_pollutants___nitrogen_oxides___ton_day`, `gaseous_pollutants___nitrogen_oxides___kg_per_capita_per_day`
- **Focus:** CO2, SO2, NOx for prediction and visualization.
- **Sample:**
  ```
  year,installed_capacity__as_on_march_,gaseous_pollutants___carbon_dioxide___ton_day,gaseous_pollutants___carbon_dioxide___ton_per_capita_day,gaseous_pollutants___sulphur_dioxide___ton_day,gaseous_pollutants___sulphur_dioxide___kg_per_capita_per_day,gaseous_pollutants___nitrogen_oxides___ton_day,gaseous_pollutants___nitrogen_oxides___kg_per_capita_per_day
  2016,185172.88,2210000,0.00182,24620.5,0.02033,25331.6,0.02092
  2017,192162.88,2320000,0.00192,25549.9,0.0211,26287.8,0.02171
  ```

---

## Future Improvements
- **Advanced Predictions:** Use machine learning models (e.g., ARIMA, LSTM) for more accurate predictions.
- **Alternative Data Sources:** Integrate **DhartiMetrics** or other APIs for more reliable data.
- **GUI Interface:** Replace the CLI with a graphical interface using Tkinter or Flask.
- **Real-Time Updates:** Add real-time data fetching and visualization.

---

## Acknowledgments
- **Spring Dale International School** for providing resources and support.
- **data.gov.in** for providing open access to environmental data.
- **International Coding Olympiad** for organizing the Climate Data Analysis Challenge.
- **Mentor Mr. Ankur Hazarika** for guidance and encouragement.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Team NDJ Protocol**  
**Spring Dale International School**  
**May 14, 2025**

