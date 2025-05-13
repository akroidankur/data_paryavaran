import os
import asyncio
import shutil
from api import fetch_aqi_data, fetch_emissions_data
from prediction import is_file_valid, run_aqi_prediction, run_emissions_prediction

os.makedirs("data/api_data", exist_ok=True)
os.makedirs("data/SavedData", exist_ok=True)

def display_welcome():
    border = "🌍" * 25
    print(f"\n{border}")
    print("🌟 Welcome to Spring Dale International School 🌟".center(50))
    print("Beharbari, Guwahati, Assam – 781028".center(50))
    print(f"{border}\n")
    print("📊 Project: DataParyavaran 📊".center(50))
    print("A climate data analysis tool for the International Coding Olympiad.".center(50))
    print("Focus: Air Quality and Emissions.".center(50))
    print('\n')
    print("📡 Data Source: https://api.data.gov.in (Indian Government Open Data)".center(50))
    print("\n🌿 Team: NDJ Protocol 🌿".center(50))
    print("👥 Members:".center(50))
    print("  - Naija Sona Brahma (Class 12 - Science)".center(50))
    print("  - Debaniv Talukdar (Class 12 - Commerce)".center(50))
    print("  - Jahnab Dewri (Class 12 - Science)".center(50))
    print("  - Mentor: Mr. Ankur Hazarika".center(50))
    print(f"\n{border}\n")

def display_main_menu():
    print("\n🔍 Select a topic to explore:")
    print("  1. Air Quality Index (AQI)")
    print("  2. Emissions from Thermal Power Plants")
    print("  0. Exit")
    print("\n💡 Enter the number (e.g., 1, 2, 0):")

def display_aqi_submenu():
    print("\n🔍 AQI Analysis Options:")
    print("  1. Fetch AQI Data")
    print("  2. Predict Next-Day PM2.5 for a City")
    print("  0. Back to Main Menu")
    print("\n💡 Enter the number (e.g., 1, 2, 0):")

def display_emissions_submenu():
    print("\n🔍 Emissions Analysis Options:")
    print("  1. Fetch Emissions Data")
    print("  2. Predict Future CO2 Emissions")
    print("  0. Back to Main Menu")
    print("\n💡 Enter the number (e.g., 1, 2, 0):")

def display_data_source_options(data_type):
    print(f"\n🔍 Choose data source for {data_type} prediction:")
    print("  1. API Fresh Data")
    print("  2. Old Saved Data")
    print("  0. Cancel")
    print("\n💡 Enter the number (e.g., 1, 2, 0):")

def display_overwrite_option(data_type):
    print(f"\n💡 Would you like to update the Saved {data_type} Data with this newly fetched data? (y/n):")
    choice = input("> ").strip().lower()
    return choice == 'y'

def get_numeric_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"❌ Invalid choice. Please select one of: {', '.join(valid_choices)}.\n")

def main():
    display_welcome()
    
    while True:
        display_main_menu()
        choice = get_numeric_choice("> ", ["0", "1", "2"])
        
        if choice == "0":
            print("\n🌱 Exiting DataParyavaran. Goodbye! 🌱")
            break
        elif choice == "1":
            while True:
                display_aqi_submenu()
                sub_choice = get_numeric_choice("> ", ["0", "1", "2"])
                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    try:
                        df = asyncio.run(fetch_aqi_data())
                        api_path = 'data/api_data/aqi_data.csv'
                        df.to_csv(api_path, index=False)
                        print(f"✅ Data fetched from data.gov.in API and saved to {api_path}\n")
                        if is_file_valid(api_path):
                            if display_overwrite_option("AQI"):
                                saved_path = 'data/SavedData/aqi_data.csv'
                                shutil.copy2(api_path, saved_path)
                                print(f"✅ Saved AQI Data updated with new data at {saved_path}\n")
                        else:
                            print(f"❌ Fetched AQI data at {api_path} is empty or invalid. Cannot use this data.\n")
                    except Exception as e:
                        print(f"❌ Failed to fetch AQI data: {str(e)}\n")
                elif sub_choice == "2":
                    display_data_source_options("AQI")
                    source_choice = get_numeric_choice("> ", ["0", "1", "2"])
                    if source_choice == "0":
                        continue
                    if source_choice == "1":
                        data_path = 'data/api_data/aqi_data.csv'
                    else:
                        data_path = 'data/SavedData/aqi_data.csv'
                    
                    if not os.path.exists(data_path):
                        print(f"❌ Data file not found at {data_path}. Please fetch AQI data first (Option 1).\n")
                        continue
                    if os.path.getsize(data_path) == 0:
                        print(f"❌ Data file at {data_path} is empty. Please fetch AQI data again (Option 1).\n")
                        continue
                    
                    run_aqi_prediction(data_path)
        elif choice == "2":
            while True:
                display_emissions_submenu()
                sub_choice = get_numeric_choice("> ", ["0", "1", "2"])
                if sub_choice == "0":
                    break
                elif sub_choice == "1":
                    try:
                        df = asyncio.run(fetch_emissions_data())
                        api_path = 'data/api_data/emissions_data.csv'
                        df.to_csv(api_path, index=False)
                        print(f"✅ Data fetched from data.gov.in API and saved to {api_path}\n")
                        if is_file_valid(api_path):
                            if display_overwrite_option("Emissions"):
                                saved_path = 'data/SavedData/emissions_data.csv'
                                shutil.copy2(api_path, saved_path)
                                print(f"✅ Saved Emissions Data updated with new data at {saved_path}\n")
                        else:
                            print(f"❌ Fetched Emissions data at {api_path} is empty or invalid. Cannot use this data.\n")
                    except Exception as e:
                        print(f"❌ Failed to fetch Emissions data: {str(e)}\n")
                elif sub_choice == "2":
                    display_data_source_options("Emissions")
                    source_choice = get_numeric_choice("> ", ["0", "1", "2"])
                    if source_choice == "0":
                        continue
                    if source_choice == "1":
                        data_path = 'data/api_data/emissions_data.csv'
                    else:
                        data_path = 'data/SavedData/emissions_data.csv'
                    
                    if not os.path.exists(data_path):
                        print(f"❌ Data file not found at {data_path}. Please fetch Emissions data first (Option 1).\n")
                        continue
                    if os.path.getsize(data_path) == 0:
                        print(f"❌ Data file at {data_path} is empty. Please fetch Emissions data again (Option 1).\n")
                        continue
                    
                    run_emissions_prediction(data_path)

if __name__ == '__main__':
    main()