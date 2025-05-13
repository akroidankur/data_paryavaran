import matplotlib.pyplot as plt
import pandas as pd
import os

current_topic = None

def set_current_topic(topic):
    global current_topic
    current_topic = topic

def plot_emissions_data(data_path):
    os.makedirs("plots", exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    x = df['year'].astype(int)  # Years
    y_co2 = df['gaseous_pollutants___carbon_dioxide___ton_per_capita_day'].astype(float)  # CO2
    y_so2 = df['gaseous_pollutants___sulphur_dioxide___kg_per_capita_per_day'].astype(float)  # SO2
    y_nox = df['gaseous_pollutants___nitrogen_oxides___kg_per_capita_per_day'].astype(float)  # NOx
    
    plots = [
        ("Line Plot", lambda: plt.plot(x, y_co2, color="green", label="CO2 (ton/capita/day)") and
                          plt.plot(x, y_so2, color="blue", label="SO2 (kg/capita/day)") and
                          plt.plot(x, y_nox, color="red", label="NOx (kg/capita/day)"),
         "emissions_line.png"),
        ("Scatter Plot", lambda: plt.scatter(x, y_co2, color="green", edgecolor="black", label="Ton per capita day"),
         "emissions_co2_scatter.png"),
        ("Bar Plot", lambda: plt.bar(x, y_co2, color="green", edgecolor="black", label="Ton per capita day"),
         "emissions_co2_bar.png"),
        ("Area Plot", lambda: plt.stackplot(x, y_co2, y_so2, y_nox, labels=["CO2 (ton/capita/day)", "SO2 (kg/capita/day)", "NOx (kg/capita/day)"],
                                            colors=["green", "blue", "red"], alpha=0.5),
         "emissions_area.png")
    ]
    
    saved_files = []
    for plot_title, plot_func, filename in plots:
        plt.figure(figsize=(8, 6))
        plot_func()
        plt.title("Gaseous Pollutants", fontsize=20)
        plt.xlabel("Years", fontsize=15)
        plt.ylabel("Pollutant Levels", fontsize=15)
        plt.legend(loc=2)
        plt.grid(True)
        
        save_path = os.path.join('plots', filename)
        plt.savefig(save_path)
        saved_files.append(save_path)
    
    print("\n📊 Displaying all Emissions plots...")
    plt.show(block=False)
    
    print("\n✅ Emissions plots saved to the 'plots/' directory:")
    for file in saved_files:
        print(f"  - {file}")

def plot_aqi_data(data_path):
    os.makedirs("plots", exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    pm25_df = df[(df['pollutant_id'] == 'PM2.5') & (df['avg_value'] != 'NA')]
    if pm25_df.empty:
        print("❌ No valid PM2.5 data available for plotting.\n")
        return
    
    x = pm25_df['city']  # Cities
    y = pm25_df['avg_value'].astype(float)  # PM2.5 average values
    
    plots = [
        ("Line Plot", lambda: plt.plot(x, y, color="green", label="PM2.5 (µg/m³)"),
         "aqi_pm25_line.png"),
        ("Scatter Plot", lambda: plt.scatter(x, y, color="green", edgecolor="black", label="PM2.5 (µg/m³)"),
         "aqi_pm25_scatter.png"),
        ("Bar Plot", lambda: plt.bar(x, y, color="green", edgecolor="black", label="PM2.5 (µg/m³)"),
         "aqi_pm25_bar.png"),
        ("Area Plot", lambda: plt.fill_between(x, y, color="green", alpha=0.5, label="PM2.5 (µg/m³)"),
         "aqi_pm25_area.png"),
        ("Histogram", lambda: plt.hist(y, bins=10, color="green", edgecolor="black", alpha=0.7, label="PM2.5 (µg/m³)"),
         "aqi_pm25_histogram.png")
    ]
    
    saved_files = []
    for plot_title, plot_func, filename in plots:
        plt.figure(figsize=(10, 6))
        plot_func()
        title = "AQI: PM2.5 Levels by City" if "histogram" not in filename.lower() else "AQI: PM2.5 Distribution"
        xlabel = "Cities" if "histogram" not in filename.lower() else "PM2.5 (µg/m³)"
        ylabel = "PM2.5 (µg/m³)" if "histogram" not in filename.lower() else "Frequency"
        plt.title(title, fontsize=20)
        plt.xlabel(xlabel, fontsize=15)
        plt.ylabel(ylabel, fontsize=15)
        if "histogram" not in filename.lower():
            plt.xticks(rotation=45, ha='right')
        plt.legend(loc=2)
        plt.grid(True)
        plt.tight_layout()
        
        save_path = os.path.join('plots', filename)
        plt.savefig(save_path)
        saved_files.append(save_path)
    
    print("\n📊 Displaying all AQI plots...")
    plt.show(block=False)
    
    print("\n✅ AQI plots saved to the 'plots/' directory:")
    for file in saved_files:
        print(f"  - {file}")