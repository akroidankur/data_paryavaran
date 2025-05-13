import os
import pandas as pd

def is_file_valid(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return False
    try:
        df = pd.read_csv(file_path)
        return not df.empty
    except (pd.errors.EmptyDataError, Exception):
        return False

def predict_aqi(df, city):
    city = city.title()
    city_data = df[df['city'].str.lower() == city.lower()]
    if city_data.empty:
        return None, f"No data found for city: {city}"
    
    avg_value = float(city_data.iloc[0]['avg_value'])
    simulated_prior_days = [avg_value - 2, avg_value - 1, avg_value]
    predicted_value = sum(simulated_prior_days) / len(simulated_prior_days)
    
    impacts = []
    if predicted_value < 35:
        impacts.append("Health: Good air quality, minimal health risks.")
        impacts.append("Environmental: Minimal smog, no significant impact on ecosystems.")
        impacts.append("Economic: Low healthcare costs due to reduced pollution-related illnesses.")
    elif 35 <= predicted_value <= 50:
        impacts.append("Health: Moderate air quality, potential respiratory issues for sensitive groups.")
        impacts.append("Environmental: Smog formation reduces visibility and affects plant photosynthesis.")
        impacts.append("Economic: Potential increase in healthcare costs due to pollution-related illnesses.")
    else:
        impacts.append("Health: Unhealthy air quality, widespread respiratory risks.")
        impacts.append("Environmental: Severe smog, significant ecosystem degradation.")
        impacts.append("Economic: High healthcare costs and productivity losses.")
    
    return predicted_value, impacts

def predict_emissions(df, year):
    latest_year = 2019
    latest_co2 = float(df[df['year'] == latest_year].iloc[0]['gaseous_pollutants___carbon_dioxide___ton_day'])
    
    annual_rate = 0.0467
    years_diff = year - latest_year
    predicted_co2 = latest_co2 * (1 + annual_rate) ** years_diff
    
    impacts = []
    if predicted_co2 < 2500000:
        impacts.append("Climate Change: Moderate impact, manageable heatwave risks.")
        impacts.append("Air Quality: Limited contribution to PM2.5 and acid rain.")
        impacts.append("Economic: Moderate costs for climate adaptation.")
    elif 2500000 <= predicted_co2 <= 3000000:
        impacts.append("Climate Change: Significant impact, increased heatwaves affecting agriculture.")
        impacts.append("Air Quality: Increased SO2 and NOx, worsening PM2.5 levels.")
        impacts.append("Economic: Higher costs for climate adaptation and emission controls.")
    else:
        impacts.append("Climate Change: Severe impact, extreme weather events and ecosystem stress.")
        impacts.append("Air Quality: Major contribution to PM2.5 and acid rain, degrading air quality.")
        impacts.append("Economic: Significant costs for climate adaptation and mitigation measures.")
    
    return predicted_co2, impacts

def run_aqi_prediction(data_path):
    try:
        df = pd.read_csv(data_path)
        if df.empty:
            print(f"❌ No data found in {data_path}. Please fetch AQI data again (Option 1).\n")
            return False
    except pd.errors.EmptyDataError:
        print(f"❌ Data file at {data_path} contains no valid data. Please fetch AQI data again (Option 1).\n")
        return False
    except Exception as e:
        print(f"❌ Error reading data from {data_path}: {str(e)}. Please fetch AQI data again (Option 1).\n")
        return False
    
    while True:
        print("\nAvailable cities:", ", ".join(df['city'].unique()))
        city = input("Enter city name (e.g., Kadapa): ").strip()
        predicted_value, result = predict_aqi(df, city)
        if predicted_value is not None:
            print(f"\nPredicted PM2.5 for {city.title()} on May 14, 2025: {predicted_value:.1f} µg/m³")
            print("Impacts:")
            for impact in result:
                print(f"  - {impact}")
        else:
            print(f"❌ {result}\n")
        print("\n💡 Would you like to predict for another city? (y/n):")
        continue_choice = input("> ").strip().lower()
        if continue_choice != 'y':
            break
    return True

def run_emissions_prediction(data_path):
    try:
        df = pd.read_csv(data_path)
        if df.empty:
            print(f"❌ No data found in {data_path}. Please fetch Emissions data again (Option 1).\n")
            return False
    except pd.errors.EmptyDataError:
        print(f"❌ Data file at {data_path} contains no valid data. Please fetch Emissions data again (Option 1).\n")
        return False
    except Exception as e:
        print(f"❌ Error reading data from {data_path}: {str(e)}. Please fetch Emissions data again (Option 1).\n")
        return False
    
    while True:
        year = input("Enter year to predict CO2 emissions (e.g., 2025): ").strip()
        try:
            year = int(year)
            if year <= 2019:
                print("❌ Please enter a future year (after 2019).\n")
                continue
            predicted_co2, impacts = predict_emissions(df, year)
            print(f"\nPredicted CO2 emissions for {year}: {predicted_co2:,.0f} tons/day")
            print("Impacts:")
            for impact in impacts:
                print(f"  - {impact}")
            print("\n💡 Would you like to predict for another year? (y/n):")
            continue_choice = input("> ").strip().lower()
            if continue_choice != 'y':
                break
        except ValueError:
            print("❌ Please enter a valid year (e.g., 2025).\n")
    return True