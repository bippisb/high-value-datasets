import requests
import json
import pandas as pd
import os

# Read the high_value_datasets.xlsx file
# df = pd.read_excel("high_value_datasets.xlsx")
# # Load API key from environment variable
API_KEY = os.getenv("CKAN_API_KEY")    

# Get response from api_url
api_url = "https://ckandev.indiadataportal.com/api/3/action/organization_show?id=high-value-datasets&include_datasets=True"
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    "Authorization": f"{API_KEY}"
}
# Make the request
response = requests.get(api_url, headers=headers)

if response.status_code != 200:
    print(f"Error: Received HTTP {response.status_code}")
    print(f"Response text: {response.text}")
else:
    try:
        json_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not valid JSON")
        print(f"Raw response: {response.text}")

# Open the index markdown file for writing
markdown_file = 'docs/index.md'

# Ensure the request was successful
if response.status_code == 200 and json_data.get('success'):
    packages = json_data['result']['packages']  # Extract the list of packages from the JSON response
    
    # Open the file for writing
    with open(markdown_file, 'w') as file:
        # delete everything in the file

        file.write("# High Granular Datasets - India Data Portal\n\n")

        # iterate through the list of packages
        for package in packages:
            package_title = package['title']
            package_name = package['name']
            package_description = package.get('notes', 'No description available')
            package_url = f"https://dev.indiadataportal.com/p/{package_name}"
            source = package.get('source_name', 'Not specified')
            sector = package.get('sector', 'Not specified')
            file.write(f"## {package_title}\n\n")
            # file.write(f"{package_description}\n\n")
            # file.write(f"[IDP Link]({package_url})\n\n")
            file.write(f"Source: {source}\n\n")
            file.write(f"Sector: {sector}\n\n")
            # file.write(f"---\n\n")
            # get request for getting resource details using package_show api call
            # https://ckandev.indiadataportal.com/api/3/action/package_show?id=minimum-support-price-msp
            api_url = f"https://ckandev.indiadataportal.com/api/3/action/package_show?id={package_name}"
            response = requests.get(api_url)
            json_data = response.json()
            # Ensure the request was successful
            if response.status_code == 200 and json_data.get('success'):
                resources = json_data['result']['resources']  # Extract the list of resources from the JSON response
                for resource in resources:
                    resource_name = resource['name']
                    resource_description = resource.get('description', package_description)
                    granularity = resource.get('granularity', 'Not specified')
                    frequency = resource.get('frequency', 'Not specified')
                    # resource_url = f"https://dev.indiadataportal.com/p/{package_name}/r/{resource_name}"
                    # file.write(f"### {resource_name}\n\n")
                    file.write(f"Granularity: {granularity}\n\n")
                    file.write(f"Frequency: {frequency}\n\n")
                    file.write(f"{resource_description}\n\n")
                    # file.write(f"[IDP Link]({resource_url})\n\n")
                    file.write(f"---\n\n")
        # write "please reach out to gursharan_sigh@isb.edu if you need any of the dataset"
        file.write("Please reach out to gursharan_sigh@isb.edu if you need any of the dataset")

        # # for sku in df['sku']:
        #     for package in packages:
        #         for resource in package.get('resources', []):
        #             if resource.get('sku') == sku:
        #                 package_title = package['title']
        #                 package_name = package['name']
        #                 resource_name = resource['name']
        #                 resource_description = resource.get('description', 'No description available')
        #                 granularity = resource.get('granularity', 'Not specified')
        #                 frequency = resource.get('frequency', 'Not specified')
        #                 source = package.get('source_name', 'Not specified')
        #                 resource_url = f"https://indiadataportal.com/p/{package_name}/r/{sku}"
                        
        #                 # Write dataset information to the markdown file
        #                 file.write(f"---\n\n")  # Add a separator between datasets
        #                 file.write(f"`Collection Name:` {package_title} \n\n")  # Add the collection name
        #                 file.write(f"`Dataset Name:` {resource_name} \n\n")  # Add the dataset name
        #                 file.write(f"`Dataset Description:` {resource_description} \n\n")  # Add the description
        #                 file.write(f"`Granularity:` {granularity} \n\n")  # Add the granularity
        #                 file.write(f"`Frequency:` {frequency} \n\n")  # Add the frequency
        #                 file.write(f"`Source:` {source} \n\n")  # Add the source
        #                 file.write(f"`Dataset URL:` [IDP Link]({resource_url}) \n\n")  # Add the resource URL
        #                 # file.write(f"`Wasabi URL:` [S3 Bucket]({wasabi_url}) \n\n")  # Add the Wasabi URL
