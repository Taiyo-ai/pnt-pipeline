import dotenv
import logging
from datetime import datetime
from dependencies.scraping.scraper import scrape_world_bank_data
from dependencies.cleaning.cleaning import clean_data
from dependencies.geocoding.geocoder import geocode_data
from dependencies.standardization.standardizer import standardize_data
import csv

dotenv.load_dotenv(".env")
logging.basicConfig(level=logging.INFO)

def step_1():
    # Step 1: Scraping Metadata
    logging.info("Scraping Metadata")
    metadata, _ = scrape_world_bank_data()
    # Process metadata if needed

def step_2():
    # Step 2: Scraping Main Data
    logging.info("Scraping Main Data")
    _, raw_data = scrape_world_bank_data()
    # Process raw_data if needed

def step_3():
    # Step 3: Cleaning Main Data
    logging.info("Cleaning Main Data")
    cleaned_data = clean_data(raw_data)
    # Process cleaned_data if needed

def step_4():
    # Step 4: Geocoding Cleaned Data
    logging.info("Geocoding Cleaned Data")
    geocoded_data = geocode_data(cleaned_data)
    # Process geocoded_data if needed

def step_5():
    # Step 5: Standardizing Geocoded Data
    logging.info("Standardizing Geocoded Data")
    standardized_data = standardize_data(geocoded_data)
    # Process standardized_data if needed

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--step", help="Step to be chosen for execution")

    args = parser.parse_args()

    if args.step:
        step_function = globals().get(f"step_{args.step}")
        if step_function:
            step_function()
        else:
            logging.error(f"Invalid step: {args.step}")

    logging.info(
        {
            "last_executed": str(datetime.now()),
            "status": "Pipeline executed successfully",
        }
    )
