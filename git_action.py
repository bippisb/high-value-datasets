# use this https://ckan.indiadataportal.com/api/3/action/package_search?rows=1000
# libraries

import requests
import json
import pandas as pd

# read the high_value_datasets.xlsx file
df = pd.read_excel("high_value_datasets.xlsx")

# get response from api_url
api_url = "https://ckan.indiadataportal.com/api/3/action/package_search?rows=1000"
response = requests.get(api_url)
json_data = response.json()

# Open the high-value-datasets.md markdown file
markdown_file = 'high-value-datasets.md'

with open(markdown_file, 'w') as file:
    file.write("# High Granular Datasets at the India Data Portal\n\n")


# Ensure the request was successful
if response.status_code == 200 and json_data.get('success'):
    packages = json_data['result']['results']  # Extract the list of packages from the JSON response
    
    # Initialize a list to store the matching package and resource info
    matching_results = []

    # Iterate through the Excel file to match SKUs
    for sku in df['sku']:
        for package in packages:
            for resource in package.get('resources', []):
                if resource.get('sku') == sku:
                    package_name = package['name']
                    resource_name = resource['name']
                    resource_description = resource['description']
                    granularity = resource['granularity']
                    frequency = resource['frequency']
                    resource_url = resource['url']
                    file.write(f"---")  # Add a separator between datasets
                    file.write(f"\n\n")
                    file.write(
                        f"Collection Name: {package_name} \n\n")  # Add the collection name to the markdown file
                    file.write(
                        f"Dataset Name: {resource_name} \n\n"  # Add the dataset name to the markdown file
                    )
                    file.write(
                        f"Dataset Description: {resource_description} \n\n"  # Add the dataset description to the markdown file
                    )
                    file.write(
                        f"Granularity: {granularity} \n\n"  # Add the granularity to the markdown file
                    )
                    file.write(
                        f"Frequency: {frequency} \n\n"  # Add the frequency to the markdown file
                    )
                    file.write(
                        f"Resource URL: {resource_url} \n\n"  # Add the resource URL to the markdown file
                    )
                    # matching_results.append({
                    #     'sku': sku,
                    #     'package_name': package_name,
                    #     'resource_name': resource_name,
                    #     'resource_desc': resource_description,
                    #     'granularity': granularity,
                    #     'frequency': frequency,
                    #     'resource_url': resource_url
                    # })
