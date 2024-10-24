import requests
import json
import pandas as pd

# Read the high_value_datasets.xlsx file
df = pd.read_excel("high_value_datasets.xlsx")

# Get response from api_url
api_url = "https://ckan.indiadataportal.com/api/3/action/package_search?rows=1000"
response = requests.get(api_url)
json_data = response.json()

# Open the index markdown file for writing
markdown_file = 'docs/index.md'

# Ensure the request was successful
if response.status_code == 200 and json_data.get('success'):
    packages = json_data['result']['results']  # Extract the list of packages from the JSON response
    
    # Open the file for writing
    with open(markdown_file, 'w') as file:
        # delete everything in the file

        file.write("# High Granular Datasets at the India Data Portal\n\n")

        # Iterate through the Excel file to match SKUs
        for sku in df['sku']:
            for package in packages:
                for resource in package.get('resources', []):
                    if resource.get('sku') == sku:
                        package_title = package['title']
                        package_name = package['name']
                        resource_name = resource['name']
                        resource_description = resource.get('description', 'No description available')
                        granularity = resource.get('granularity', 'Not specified')
                        frequency = resource.get('frequency', 'Not specified')
                        source = package.get('source_name', 'Not specified')
                        resource_url = f"https://indiadataportal.com/p/{package_name}/r/{sku}"
                        
                        # Write dataset information to the markdown file
                        file.write(f"---\n\n")  # Add a separator between datasets
                        file.write(f"`Collection Name:` {package_title} \n\n")  # Add the collection name
                        file.write(f"`Dataset Name:` {resource_name} \n\n")  # Add the dataset name
                        file.write(f"`Dataset Description:` {resource_description} \n\n")  # Add the description
                        file.write(f"`Granularity:` {granularity} \n\n")  # Add the granularity
                        file.write(f"`Frequency:` {frequency} \n\n")  # Add the frequency
                        file.write(f"`Source:` {source} \n\n")  # Add the source
                        file.write(f"`Dataset URL:` [IDP Link]({resource_url}) \n\n")  # Add the resource URL
                        # file.write(f"`Wasabi URL:` [S3 Bucket]({wasabi_url}) \n\n")  # Add the Wasabi URL
