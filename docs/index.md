# High Granular Datasets - India Data Portal

## VAHAN Vehicle Registrations

Source: Ministry of Road Transport and Highways

Sector: ['Economy', 'Transportation']

### VAHAN Vehicle Registrations

Granularity: Regional Transport Office

Frequency: Monthly

The "VAHAN Vehicle Registrations" dataset provides comprehensive data on vehicle registrations across India, offering insights into various aspects such as vehicle norms, manufacturers, fuel types, categories, and classes. This dataset includes key variables like the date of registration, state names and codes, Regional Transport Office (RTO) names and codes, vehicle manufacturers, fuel types (e.g., petrol, diesel, electric), vehicle categories (e.g., two-wheeler, four-wheeler), and vehicle classes. Additionally, it categorizes data by specific norms, vehicle types, and other criteria, detailing the number of registrations for each category. This resource is invaluable for policymakers, transportation authorities, analysts, and the automotive industry, enabling them to monitor and understand trends in vehicle registrations, compliance with regulations, and the environmental impact of fuel usage across different regions and RTOs in India.

| Variable Name    | Variable Description | Variable Type |
|------------------|----------------------|---------------|
| date             | Date                 | DATE          |
| state_name       | State Name           | TEXT          |
| state_code       | State Code           | TEXT          |
| office_name      | RTO Name             | TEXT          |
| office_code      | RTO Code             | TEXT          |
| type             | Fuel                 | TEXT          |
| category         | Category             | TEXT          |
| registrations    | Registrations        | NUMERIC       |


---

## Exports and Imports of India

Source: Directorate General of Commercial Intelligence and Statistics

Sector: ['Commerce']

### Exports and Imports of India

Granularity: Country

Frequency: 

The "Exports and Imports of India" dataset provides a comprehensive view of trade exports and imports of India across the globe. This dataset covers the periodical monthly data of exports in terms of value in both USD and INR and also in terms of quantity. Each record provides the date, target country, type of product (both in terms of HS code and the commodity name), the value of the commodity, and the quantity of the commodity being exported. 


---

## Daily Non-Renewable Power Generation

Source: Ministry of Power

Sector: ['Energy']

### Daily Non-Renewable Power Generation

Granularity: Power Station

Frequency: Daily

Power Generation data is taken from nuclear, thermal and hydro power stations across india. The data is collected on daily basis. It contains generation data by state, sector, power station type, individual power station and unit level. The data field includes installed capacity, day's power generaiton target, actual generation etc. for each power station.
| Variable Name                          | Variable Description                    | Variable Type | Unit Of Measurement |
|----------------------------------------|------------------------------------------|---------------|---------------------|
| date                                   | Date                                     | DATE          |                     |
| state_name                             | State Name                               | TEXT          |                     |
| state_code                             | State Code                               | TEXT          |                     |
| sector                                 | Sector of Power Station                  | TEXT          |                     |
| power_station_type                     | Type of Power Station                    | TEXT          |                     |
| power_station                           | Name of Power Station                    | TEXT          |                     |
| power_station_unit                      | Power Station Unit                       | TEXT          |                     |
| monitored_cap_in_mw                    | Total Monitored Capacity                 | NUMERIC       | Mega Watt           |
| todays_power_generation_programe_in_mu | Program of Today's Power Generation      | NUMERIC       | Mega Unit           |
| todays_actual_power_generation_in_mu   | Today's Actual Power Generation          | NUMERIC       | Mega Unit           |

[Dataset Summary](https://dev.indiadataportal.com/p/power/r/mop-power_generation-pl-dl-abc#dataset-summary)

---

## Bank Outlets and ATM's

Source: Reserve Bank of India

Sector: ['Banking', 'Economy', 'Financial Inclusion']

### Bank Outlets and ATM's

Granularity: Point

Frequency: Other

The Banking Outlet section of the Reserve Bank of India's Database on Indian Economy (DBIE) provides comprehensive data on the distribution and reach of banking services across India. It includes the location (latitude and longitude) of banking outlets, along with associated information such as bank name, bank type (Branch, CSP, Office, Business Correspondent, Digital Banking Unit [DBU], NAIO), bank group (e.g., foreign, public, private, payment banks, regional, local), their IFSC codes, date of opening, population group (metropolitan, urban, rural, semi-urban) associated with the outlet, and whether the outlet is a domestic or overseas branch. This dataset supports analyses of financial inclusion, accessibility, and the expansion of banking infrastructure.  
| Variable Name        | Variable Description     | Variable Type |
|----------------------|--------------------------|---------------|
| region               | Region                   | TEXT          |
| center               | Center                   | TEXT          |
| branch               | Branch                   | TEXT          |
| address              | Address                  | TEXT          |
| longitude            | Longitude                | NUMERIC       |
| latitude             | Latitude                 | NUMERIC       |
| bank_group           | Bank Group               | TEXT          |
| population_group     | Population Group         | TEXT          |
| domestic_overseas    | Branch Service Type      | TEXT          |
| type                 | Service Unit             | TEXT          |
| status_type          | Status                   | TEXT          |
| bank                 | Bank Name                | TEXT          |
| micrcode             | MICR Code                | TEXT          |
| license_number       | License Number           | TEXT          |
| ifsccode             | IFSC Code                | TEXT          |
| part_1_code          | Part-1 Code              | TEXT          |
| closed_reason        | Reason for Closed        | TEXT          |
| license_date         | License Date             | TEXT          |
| actual_open_date     | Open Date                | TEXT          |
| state_code           | State Code               | TEXT          |
| state_name           | State Name               | TEXT          |
| district_code        | District Code            | TEXT          |
| district_name        | District Name            | TEXT          |
| subdistrict_code     | Sub District Code        | TEXT          |
| subdistrict_name     | Sub District Name        | TEXT          |


---

## CGWB - Changes in Depth to Water Level

Source: Ministry of Jal Shakti

Sector: ['Climate and Weather']

### CGWB - Changes in Depth to Water Level

Granularity: Station

Frequency: Quarterly

Central Ground Water Board monitors groundwater levels throughout the country on a regional scale, four times in a year during the months of March/April/May, August, November and January.This data is collected under the mode of acquisition “Manual”.  For monitoring of ground water level, CGWB has a dedicated network of about 25000 monitoring stations called “National Hydrograph Network Stations (NHNS)”, which comprises open dug wells and purpose-built bore/tube wells for water level monitoring called piezometers.  Similarly, CGWB has initiated automatic high frequency monitoring by installing Digital Water Level Recorders (DWLR) with telemetry systems under the National Hydrology Project (NHP).   This data is collected under the mode of acquisition “Telemetry”.
| Variable Name    | Variable Description      | Variable Type | Unit Of Measurement |
|------------------|---------------------------|---------------|---------------------|
| date             | Date                      | Date          |                     |
| state_name       | State Name                | TEXT          |                     |
| state_code       | State Code                | TEXT          |                     |
| district_name    | District Name             | TEXT          |                     |
| district_code    | District Code             | TEXT          |                     |
| station_name     | Station Name              | TEXT          |                     |
| latitude         | Latitude                  | NUMERIC       |                     |
| longitude        | Longitude                 | NUMERIC       |                     |
| basin            | Basin                     | TEXT          |                     |
| sub_basin        | Sub Basin                 | TEXT          |                     |
| source           | Source                    | TEXT          |                     |
| currentlevel     | Depth to Water Level      | NUMERIC       | Meters              |
| level_diff       | Level Difference          | NUMERIC       |                     |


---

## Mission Antyodaya 2020

Source: Ministry of Rural Development

Sector: ['Socio Economic']

### Mission Antyodaya 2020

Granularity: Village

Frequency: Yearly

The Mission Antyodaya dataset offers an extensive overview of village-level infrastructure, socio-economic indicators, and resource availability across India. This comprehensive dataset, collected under the Mission Antyodaya initiative, aims to uplift the most underprivileged rural communities by providing detailed insights into various aspects of rural life. This dataset serves as a crucial tool for policymakers, researchers, and development practitioners, providing a holistic view of rural development needs and achievements. By capturing diverse aspects of village life, the dataset facilitates comprehensive monitoring, planning, and implementation of initiatives aimed at improving rural infrastructure and services, thereby contributing to poverty alleviation and sustainable development in India's rural areas.

| Variable Name           | Variable Description                            | Variable Type |
|-------------------------|--------------------------------------------------|---------------|
| year                    | Year                                             | TEXT          |
| state_code              | State Code                                       | TEXT          |
| state_name              | State Name                                       | TEXT          |
| district_code           | District Code                                    | TEXT          |
| district_name           | District Name                                    | TEXT          |
| block_code              | Block Code                                       | TEXT          |
| block_name              | Block Name                                       | TEXT          |
| gp_code                 | Gram Panchayat Code                              | TEXT          |
| gp_name                 | Gram Panchayat Name                              | TEXT          |
| village_code            | Village Code                                     | TEXT          |
| village_name            | Village Name                                     | TEXT          |
| tot_pop                 | Total Population                                 | NUMERIC       |
| pop_male                | Male Population                                  | NUMERIC       |
| pop_female              | Female Population                                | NUMERIC       |
| tot_hh                  | Total Households                                 | NUMERIC       |
| bank                    | Bank                                             | TEXT          |
| bank_distance           | Nearest Bank Distance                            | TEXT          |
| bc_w_internet           | Business Correspondent with Internet             | TEXT          |
| atm                     | ATM                                              | TEXT          |
| internet_bb             | Internet / Broadband Facility                    | TEXT          |
| all_weather_road        | Connected To All Weather Road                    | TEXT          |
| cc_road                 | Internal Pucca Roads (Cc/ Brick Road)            | TEXT          |
| pub_trans               | Public Transport                                 | TEXT          |
| railway                 | Railway Station                                  | TEXT          |
| csc_avail               | Common Service Centre                            | TEXT          |
| elec_domes              | Domestic Electricity                             | TEXT          |
| elec_msme               | Electricity Supply to MSME units                 | TEXT          |
| pds                     | Public Distribution System                       | TEXT          |
| avl_market              | Markets                                          | TEXT          |
| tap_water               | Piped Tap Water                                  | TEXT          |
| telefone                | Telephone Services                               | TEXT          |
| clean_energy_hhs        | HHs using Clean Energy(LPG/Biogas)               | NUMERIC       |
| solar_wind_elect        | Solar / Wind Energy For Electrification          | TEXT          |
| kuccha_hhs              | HHs with Kuccha Wall and Kuccha Roof             | NUMERIC       |
| po_sub_po               | Post Office / Sub-Post Office                    | TEXT          |
| panch_bhawan            | Panchayat Bhawan                                 | TEXT          |
| pib                     | Public Information Board                         | TEXT          |
| prim_school             | Primary School                                   | TEXT          |
| middle_school           | Middle School                                    | TEXT          |
| high_school             | High School                                      | TEXT          |
| high_second_school      | Higher / Secondary School                         | TEXT          |
| degree_clg              | Degree College                                   | TEXT          |
| public_library          | Public Library                                   | TEXT          |
| rec_sports              | Recreational Centre / Sports Playground          | TEXT          |
| vocational              | Vocational Educational Centre                    | TEXT          |
| subcentre               | Sub Centre                                       | TEXT          |
| subcentre_dist          | Nearest Sub Centre                               | TEXT          |
| veterinary              | Veterinary Clinic Hospital                       | TEXT          |
| veterinary_dist         | Nearest Veterinary Clinic                        | TEXT          |
| drainage                | Drainage Facilities                              | TEXT          |
| pcomm_pasture           | Common Pastures                                  | TEXT          |

---

## SHG Financial and Member Profile Details

Source: Ministry of Rural Development

Sector: ['Financial Inclusion', 'Rural Development']

### SHG Financial and Member Profile Details

Granularity: SHG

Frequency: Other

This dataset provides an extensive and nuanced profile of Self-Help Groups (SHGs) across diverse geographic and socio-economic contexts. It includes detailed information on the SHG's location, specifying the state, district, block, Gram Panchayat, and village, alongside a unique SHG identifier and its name. Key administrative details such as the date of formation, type of SHG, promoting entity, and banking informationâ€”including the bank name, branch, and account opening dateâ€”are also recorded. The dataset meticulously documents membership demographics, including total membership counts, gender distribution, and classifications by social categories such as Scheduled Caste, Scheduled Tribe, Other Backward Classes, and Other Social Categories. Additionally, it captures data on members with disabilities, both self-disabled and those with disabled family members, and provides insights into religious affiliations (Hindu, Christian, Muslim, Sikh, Buddhist, Jain, Parsi) and economic status, distinguishing between Above Poverty Line (APL), Below Poverty Line (BPL), and Poorest of the Poor under the PIP category.

Metadata -
 | Variable Name                     | Variable Description                                           | Variable Type | Unit Of Measurement | 
|-----------------------------------|---------------------------------------------------------------|---------------|---------------------| 
| state_name                        | State Name                                                    | TEXT          |                     | 
| district_name                     | District Name                                                 | TEXT          |                     | 
| block_name                        | Block Name                                                    | TEXT          |                     | 
| gp_name                           | Gram Panchayat Name                                           | TEXT          |                     | 
| village_name                      | Village Name                                                  | TEXT          |                     | 
| shg_name                          | Self Help Group Name                                          | TEXT          |                     | 
| shg_id                            | Self Help Group ID                                            | TEXT          |                     | 
| formation_date                    | Date of Formation of SHG                                      | DATE          |                     | 
| shg_type                          | Type of SHG                                                    | TEXT          |                     | 
| promoted_by                       | SHG Promoted By                                               | TEXT          |                     | 
| bank_name                         | Name of the bank where SHG is registered                      | TEXT          |                     | 
| bank_branch                       | Name of the bank branch where SHG is registered               | TEXT          |                     | 
| acc_opening_date                  | Date of opening of Bank Account                               | TEXT          |                     | 
| total_members                     | Number of members in SHG                                      | NUMERIC       | Numerical           | 
| female                            | Number of female members in SHG                               | NUMERIC       | Numerical           | 
| male                              | Number of male members in SHG                                 | NUMERIC       | Numerical           | 
| sc                                | Number of Scheduled Caste members in SHG                      | NUMERIC       | Numerical           | 
| st                                | Number of Scheduled Tribe members in SHG                      | NUMERIC       | Numerical           | 
| obc                               | Number of members belonging to Other Backward Classes         | NUMERIC       | Numerical           | 
| other_category                    | Number of members belonging to Other Social Categories        | NUMERIC       | Numerical           | 
| disabled                          | Number of members with disabilities                           | NUMERIC       | Numerical           | 
| family_mem_disabled               | Number of members with a disabled family member               | NUMERIC       | Numerical           | 
| hindu                             | Number of Hindu members                                       | NUMERIC       | Numerical           | 
| christian                         | Number of Christian members                                   | NUMERIC       | Numerical           | 
| muslim                            | Number of Muslim members                                      | NUMERIC       | Numerical           | 
| sikh                              | Number of Sikh members                                        | NUMERIC       | Numerical           | 
| buddhist                          | Number of Buddhist members                                    | NUMERIC       | Numerical           | 
| jain                              | Number of Jain members                                        | NUMERIC       | Numerical           | 
| parsi                             | Number of Parsi members                                       | NUMERIC       | Numerical           | 
| apl                               | Number of members categorized as Above Poverty Line (APL)     | NUMERIC       | Numerical           | 
| bpl                               | Number of members categorized as Below Poverty Line (BPL)     | NUMERIC       | Numerical           | 
| pop                               | Number of members categorized as Poorest of the Poor under PIP category | NUMERIC       | Numerical           | 
| poor                              | Number of members categorized as Poor under PIP category      | NUMERIC       | Numerical           | 

---

## Road Connectivity-PMGSY

Source: Ministry of Rural Development

Sector: ['Rural Development', 'Socio Economic']

### Road Connectivity-PMGSY

Granularity: Road

Frequency: Yearly

: The dataset provides comprehensive financial and physical progress information for all road projects that are being implemented under the Pradhan Mantri Gram Sadak Yojana (PMSGY) in India. PMSGY is a government-led initiative aimed at connecting all unconnected habitations in rural areas with all-weather roads, which is critical to the socio-economic development of rural India. The dataset includes information such as the total cost of the project, the amount of funds allocated, the expenditure incurred so far, the length of the road constructed, the percentage of the road completed, and the quality of the construction work. This information can be used to monitor the progress of each project and to identify any areas where improvements are needed. 
| Variable Name                         | Variable Description                                            | Variable Type | Unit Of Measurement | Constant Unit / Changing Unit |
|--------------------------------------|----------------------------------------------------------------|--------------|---------------------|------------------------------|
| state_name                           | State                                                          | TEXT         |                     | True                         |
| state_code                           | State Code                                                     | TEXT         |                     | True                         |
| district_name                        | District                                                       | TEXT         |                     | True                         |
| district_code                        | District Code                                                  | TEXT         |                     | True                         |
| block_name                           | Block                                                          | TEXT         |                     | True                         |
| block_code                           | Block Code                                                     | TEXT         |                     | True                         |
| habitation_name                      | Habitation Name                                                | TEXT         |                     | True                         |
| road_name                            | Road Name                                                      | TEXT         |                     | True                         |
| packages                             | Packages from which the funds were sanctioned                  | TEXT         |                     | True                         |
| upgrade_or_new                       | Whether the project is an upgrade of an existing road or a new road? | TEXT         |                     | True                         |
| surface_type                         | Type of surface                                                | TEXT         |                     | True                         |
| physical_status                      | Status as per physical progress report                        | TEXT         |                     | True                         |
| financial_status                     | Status as per financial progress report                       | TEXT         |                     | True                         |
| contractor_name                      | Contractor Name                                                | TEXT         |                     | True                         |
| company_name                         | Company Name                                                   | TEXT         |                     | True                         |
| sanctioned_year                      | Sanctioned Year                                               | TEXT         |                     | True                         |
| work_award_date                      | Work Award Date                                               | DATE         |                     | True                         |
| completion_date                      | Work Completion Date                                          | DATE         |                     | True                         |
| length                               | Length of the Road                                            | NUMERIC      | Kilometers          | True                         |
| pavement_cost                        | Pavement Cost                                                 | NUMERIC      | Lakhs              | True                         |
| no_of_cross_drainage_works           | Number of Cross Drainage Works                               | NUMERIC      |                     | True                         |
| cross_drainage_work_cost             | Cross Drainage Work Cost                                     | NUMERIC      | Lakhs              | True                         |
| long_span_bridge_cost                | Long Span Bridge Cost                                        | NUMERIC      | Lakhs              | True                         |
| long_span_bridge_state_cost          | Long Span Bridge State Cost                                  | NUMERIC      | Lakhs              | True                         |
| protection_work                      | Protection Work                                              | NUMERIC      | Lakhs              | True                         |
| other_works                          | Other Works                                                  | NUMERIC      | Lakhs              | True                         |
| completed_length                     | Completed Length                                             | NUMERIC      | Kilometers          | True                         |
| expenditure_till_date                | Expenditure Till Date                                        | NUMERIC      | Lakhs              | True                         |
| total_cost                           | Total Cost                                                  | NUMERIC      | Lakhs              | True                         |
| population                           | Population                                                  | NUMERIC      |                     | True                         |
| sc_st_population                     | SC / ST Population                                           | NUMERIC      |                     | True                         |



---

## Daily Fertilizer Sales

Source: Ministry of Chemicals and Fertilizers

Sector: ['Food and Agriculture']

### Daily Fertilizer Sales

Granularity: District

Frequency: Daily

The dataset provides information on the daily sales of different types of fertilizers by retail outlets in India. This dataset is valuable for farmers, policymakers, researchers, and other stakeholders in the agriculture sector. Farmers can use the information to plan their fertilizer purchases and ensure that they have access to the fertilizers they need. Policymakers can use the data to monitor the supply and demand of fertilizers in different regions of the country and make informed decisions on fertilizer subsidy policies. Researchers can use the data to study the fertilizer market and identify trends and patterns in fertilizer sales. 
| Variable Name                  | Variable Description                                      | Variable Type | Unit of Measurement |
|--------------------------------|----------------------------------------------------------|--------------|---------------------|
| date                           | Date                                                    | Date         |                     |
| state_name                     | Name of State                                          | TEXT         |                     |
| state_code                     | State Code                                            | TEXT         |                     |
| district_name                  | Name of District                                      | TEXT         |                     |
| district_code                  | District Code                                         | TEXT         |                     |
| retailer_name                  | Name of Retailer                                      | TEXT         |                     |
| retailer_id                    | Retailer ID                                          | TEXT         |                     |
| attached_devices               | No of Attached PoS Devices                           | NUMERIC      |                     |
| active                         | Active                                               | BOOLEAN      |                     |
| opening_stock_reported         | Opening Stock Reported                               | BOOLEAN      |                     |
| opening_stock                  | Opening Stock (as on dry run or go live date)       | NUMERIC      | Metric Tonnes       |
| no_of_invoices_generated       | No of Invoices Generated                            | NUMERIC      |                     |
| no_of_sale_transaction         | No of Sales Transactions                            | NUMERIC      |                     |
| quantity_sold                  | Quantity Sold                                       | NUMERIC      |                     |
| n_quantity                     | Quantity of Nitrogen Sold                           | NUMERIC      |                     |
| p_quantity                     | Quantity of Phosphorus Sold                         | NUMERIC      |                     |
| k_quantity                     | Quantity of Potassium Sold                          | NUMERIC      |                     |
| s_quantity                     | Quantity of Sulfur Sold                             | NUMERIC      |                     |


---

## Port Level Import Export

Source: Directorate General of Commercial Intelligence and Statistics

Sector: ['Commerce']

### Port Level Import Export

Granularity: State

Frequency: Monthly

The Port Level Import-Export Dataset provides comprehensive monthly data on imports and exports at the principal commodity level, recorded across various ports in India. It includes detailed information on volume, value (in USD and INR), and commodity types, categorized at the 2-digit HS code level. This dataset is a crucial resource for analyzing trade patterns, regional trade performance, and economic activity. It is particularly valuable for economists, policymakers, trade analysts, and researchers studying international trade, economic development, and market trends.  
| Variable Name    | Variable Description                        | Variable Type | SubDataSet       |
|-----------------|--------------------------------------------|--------------|-----------------|
| month          | Month                                      | Date         |                 |
| trade_type     | Trade Type                                 | TEXT         | Import, Export |
| state_name     | State Name                                 | TEXT         |                 |
| state_code     | State Code                                 | TEXT         |                 |
| port           | Port for Import                           | TEXT         |                 |
| country        | Import Country                            | TEXT         |                 |
| pc_code        | Principle Commodity Code                  | TEXT         |                 |
| commodity      | Commodity Name                            | TEXT         |                 |
| units         | Quantity Unit Measurement                 | TEXT         |                 |
| quantity       | Value of commodity quantity              | NUMERIC      |                 |
| dollars_value  | Value of commodity quantity in USD       | NUMERIC      |                 |
| inr_value      | Value of commodity quantity in INR       | NUMERIC      |                 |


---

Please reach out to gursharan_sigh@isb.edu if you need any of the dataset