# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:14:20 2024

@author: dmelvin
"""

import os
import requests

def download_rdf_files(uri_list_file, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the URI list file
    with open(uri_list_file, 'r') as file:
        uris = file.readlines()

    # Download RDF files for each URI
    for uri in uris:
        uri = uri.strip()  # Remove leading/trailing whitespace
        filename = os.path.join(output_folder, os.path.basename(uri) )
        try:
            response = requests.get(uri)
            if response.status_code == 200:
                with open(filename, 'wb') as rdf_file:
                    rdf_file.write(response.content)
                print(f"Downloaded {uri}")
            else:
                print(f"Failed to download {uri}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading {uri}: {e}")

# Example usage:
uri_list_file = "FILE_PATH_TO_INPUT.txt"  # Path to your URI list file
output_folder = "FILE_PATH_TO_OUTPUT_FOLDER"  # Output folder to save RDF files
download_rdf_files(uri_list_file, output_folder)
