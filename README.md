# RDF-File-Downloader
RDF File Downloader: A Python script for downloading RDF files from a list of URIs, automating the retrieval and storage of structured data from the web.
This Python script is designed to download RDF (Resource Description Framework) files from a list of URIs (Uniform Resource Identifiers) specified in a text file. RDF is a standard model for data interchange on the web and is often used to represent metadata or structured data.

## Usage
1. **URI List File**: Create a text file containing a list of URIs, with each URI on a separate line. Append the appropriate file extension to each URI to indicate the desired RDF serialization format (e.g., **`.nt`**, **`.rdf`**, **`.ttl`**, **`.xml`**, etc.). The script will read this file to determine which RDF files to download.

2. **Output Folder**: Specify the folder where you want the downloaded RDF files to be saved. If the folder does not exist, the script will create it.

3. **Run the Script**: Execute the script with the appropriate parameters, namely the path to the URI list file and the output folder path.

## Script Explanation
- The script begins by importing necessary modules: **`os`** for file system operations and **`requests`** for making HTTP requests.

- The **`download_rdf_files`** function is defined to handle the downloading of RDF files. It takes two parameters: **`uri_list_file`** (the path to the URI list file) and **`output_folder`** (the folder where RDF files will be saved).

- Within the function:

  - It first checks if the output folder exists. If not, it creates the folder. </br>
  - It reads the URI list file line by line and stores the URIs in a list. </br>
  - It iterates through each URI in the list, strips any leading or trailing whitespace, and constructs the filename for the downloaded RDF file based on the URI. </br>
  - It attempts to download the RDF file corresponding to each URI using the **`requests.get`** method. </br>
  - If the download is successful (HTTP status code 200), it saves the content of the response to a file in the output folder. </br>
  - If the download fails or encounters an error, it prints an appropriate error message.

## Example Usage:
~~~~
uri_list_file = "C:/Users/userName/Documents/fetchUri/uri.txt"  # Path to your URI list file </br>
output_folder = "C:/Users/userName/Documents/fetchUri/rdf_batch"  # Output folder to save RDF files </br>
download_rdf_files(uri_list_file, output_folder)
~~~~
Replace the **`uri_list_file`** and **`output_folder`** variables with the paths specific to your system and execute the script. The RDF files corresponding to the URIs listed in the URI list file will be downloaded to the specified output folder, with the appropriate file extension for the desired RDF serialization format. </br>

## License
Source code is made available under the [BSD 3-Clause License](LICENSE). For questions, contact [Darnelle Melvin](https://github.com/darnelleMelvin). 
