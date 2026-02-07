# Script for downloading NEXRAD radar files through the AWS Database with fsspec and S3

# Author: Brandon Weart, Northern Illinois University

# Date created: 08/23/2024

# Last updated: 01/07/2025

"""
This script allows users to download NEXRAD radar files from the AWS Database using the fsspec library. 
The user is prompted to enter the start date and time (yyyy-mm-dd HH:MM in UTC), end date and time, radar station code (E.G. KLOT), and the directory to save the radar files.
To run the script, you can either download this and change it to an .ipynb file by changing the extension...
Or you could run it in a terminal as a .py file by doing python /your/path/here/nexrad_download.py
 
"""

import fsspec
import os
from datetime import datetime, timedelta

# Set up the S3 filesystem
fs = fsspec.filesystem("s3", anon=True)

def get_user_input():
    start_date = input("Enter start date and time (YYYY-MM-DD HH:MM): ").strip()
    end_date = input("Enter end date and time (YYYY-MM-DD HH:MM): ").strip()
    station = input("Enter radar station code (e.g., KLOT): ").strip()
    download_dir = input("Enter directory to save radar files: ").strip()

    return start_date, end_date, station, download_dir

def download_radar_files(start_date_str, end_date_str, station, download_dir):
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M')

    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Generate the list of files for the specified date and hour range
    current_date = start_date
    files_downloaded = 0

    while current_date <= end_date:
        date_str = current_date.strftime("%Y/%m/%d")
        date_str_compact = current_date.strftime("%Y%m%d")

        if current_date.date() == start_date.date():
            start_hour = start_date.hour
        else:
            start_hour = 0

        if current_date.date() == end_date.date():
            end_hour = end_date.hour
        else:
            end_hour = 23

        for hour in range(start_hour, end_hour + 1):
            hour_str = f"{hour:02d}"
            all_files = fs.glob(
                f"s3://noaa-nexrad-level2/{date_str}/{station}/{station}{date_str_compact}_{hour_str}*"
            )
            filtered_files = [f for f in all_files if not f.endswith("_MDM")]

            for file in filtered_files:
                local_filename = os.path.join(download_dir, os.path.basename(file))
                try:
                    with fs.open(file, "rb") as f_in, open(local_filename, "wb") as f_out:
                        f_out.write(f_in.read())
                    print(f"Downloaded {local_filename}")
                    files_downloaded += 1
                except Exception as e:
                    print(f"Failed to download {file}: {e}")

        current_date = current_date.replace(hour=0) + timedelta(days=1)

    print(f"Download completed. Total files downloaded: {files_downloaded}")

if __name__ == "__main__":
    start_date_str, end_date_str, station, download_dir = get_user_input()
    download_radar_files(start_date_str, end_date_str, station, download_dir)
