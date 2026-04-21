# Air Quality Tool (ACC102 Track4)
AIR QUALITY ANALIYSIS AND INTERACTIVE VISUALIZATION TOOLS

---

## 1. Problem & User
### BACKGROUND AND PROBLEMS
With the acceleration of urbanization, the problem of air pollution has attracted more and more attention, but it is often difficult for ordinary users to quickly and intuitively understand complex air quality data and cannot clearly understand the distribution and change trends of air quality pollutants in the region.


### TARGET USERS
-General citizens who care about air quality, hoping to understand air quality conditions for their daily travel.

-Students or researchers in environmental-related fields who need quick data analysis and visualization tools.

-Beginners interested in data visualization who can learn Python & Streamlit application development through this tool.

### TOOL VALUE
Through an interactive interface, users can quickly view, filter air quality data, generate visual charts, and obtain intuitive analysis conclusions without professional coding basics. This helps users better understand and use air quality data more efficiently.

---

## 2. Data
### DATA SOURCE
The dataset used in this project is a public urban air quality monitoring dataset. The data comes from historical air quality data publicly released by the China National Environmental Monitoring Center and sorted into CSV format files.

### DATA TIME RANGE
The data covers from January 1, 2023 to December 31, 2023, including complete annual air quality monitoring data.

### Key Field Description
| Field Name | Description |
|-----------|-----------|
| `Date` | Monitoring date (in YYYY-MM-DD format) |
| `City` | Name of the monitored city |
| `AQI` | Air Quality Index; higher values indicate more severe pollution |
| `PM2.5` | Fine particulate matter concentration (μg/m³) |
| `PM10` | Inhalable particulate matter concentration (μg/m³) |
| `SO2` | Sulfur dioxide concentration (μg/m³) |
| `NO2` | Nitrogen dioxide concentration (μg/m³) |
| `CO` | Carbon monoxide concentration (mg/m³) |
| `O3` | Ozone concentration (μg/m³) |
| `Quality_Level` | Air quality grade (Good / Moderate / Light Pollution / Moderate Pollution / Heavy Pollution / Severe Pollution) |

### Data Preprocessing
- Removed missing values and outliers (values exceeding the normal monitoring range)
- Standardized the date format to facilitate time series analysis
- Added season and month fields for grouped statistics in the time dimension
    
---

## 3. Methods
This project is developed using Python, and the main tools and methods used are as follows:

### Data Processing
- Used the `pandas` library for data cleaning, filtering, grouping, and statistical analysis, including missing value handling, data type conversion, multi-dimensional data aggregation, and other operations.

 ### Data Visualization
- Used the `matplotlib` and `plotly` libraries to implement various interactive visual charts, including:
- Line chart: showing the time trend of AQI and major pollutants
- Bar chart: comparing the average air quality index across different cities and months
- Pie chart: showing the proportion distribution of different air quality levels throughout the year
- Box plot: analyzing the distribution differences of pollutant concentrations in different seasons
 
 ### Interactive Application Development
- Used the `streamlit` library to build an interactive web application with the following functions:
- Filtering by city and time range
- Dynamic selection of pollutants and indicators
- One-click generation of visual charts and statistical summaries
- Responsive interface, supporting access on different devices
     
 ---
 
## 4. Key Findings
Through the analysis of the dataset, the following core conclusions are drawn:

1.  **Time Trend Characteristics**: The AQI index shows obvious seasonal variations. Air quality is the worst in winter (December-February) and the best in summer (June-August). The main reasons are increased pollutant emissions from winter heating and the diffusion effect of strong convective weather on pollutants in summer.

2.  **Pollutant Distribution**: PM2.5 is the primary pollutant affecting air quality, accounting for more than 70% of days exceeding standards during heavy pollution events. Ozone (O₃) is more prominent in the afternoon during summer and becomes the main pollutant in summer.

3.  **City Comparison**: Air quality varies significantly across different cities. The average AQI of industrial cities is significantly higher than that of tourist cities. Differences in PM10 concentrations are an important factor leading to the air quality gap between cities.

4.  **Grade Proportion**: Days with "Excellent" and "Good" air quality account for about 65% of the whole year, while days with light pollution or above account for about 35%. Among them, heavy pollution days are mainly concentrated in January and December.
  
---

## 5. How to Run
### 1. Environment Setup
>Ensure your computer has Python 3.8 or higher installed, then run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. RUN the APP LOCALLY
Execute the following command in the project root directory to launch the Streamlit application：
```bash
streamlit run app.py
```
## 6. Product Link / Demo
- Streamlit App LINK：`https://acc102-track4-jzbqjiksapppzswzdy89flt.streamlit.app/`
