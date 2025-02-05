# High Granular Datasets - India Data Portal

## Daily Coal Stocks

Source: Ministry of Power

Sector: ['Energy']

### Daily Coal Stocks

Granularity: Point

Frequency: Daily 

Coal Stocks data is taken from thermal power stations across India. The data is collected daily. It contains coal stock data by state, sector, and individual power station. The data field includes mode of transport,  capacity, normative stocks, actual stocks, receipt, consumption, the criticalness of the plant, etc., for each power station.

| Variable Name                                  | Variable Description                              | Variable Type | Unit Of Measurement  |
|-----------------------------------------------|------------------------------------------------|--------------|----------------------|
| date                                          | Date                                          | DATE         |                      |
| state_name                                    | State Name                                    | TEXT         |                      |
| state_code                                    | State Code                                    | TEXT         |                      |
| mode_of_transport                             | Mode of Transport Coal                        | TEXT         |                      |
| power_station_name                            | Power Station Name                            | TEXT         |                      |
| sector                                        | Sector of Power Station                       | TEXT         |                      |
| utility                                       | Utility of Power Station                      | TEXT         |                      |
| capacity_in_mw                                | Capacity of Power Station                     | NUMERIC      | Mega Watt            |
| req_for_day_in_th_tonnes                      | Requirement for the day in Thousand Tonnes    | NUMERIC      | Thousand Tonnes      |
| normative_stock_req_days                      | Required Normative Stock in Days             | NUMERIC      |                      |
| normative_stock_req_in_th_tonnes              | Required Normative Stock in Thousand Tonnes  | NUMERIC      | Thousand Tonnes      |
| actual_stock_indigenous_in_th_tonnes          | Actual Indigenous Stock in Thousand Tonnes   | NUMERIC      | Thousand Tonnes      |
| actual_stock_import_in_th_tonnes              | Actual Imported Stock in Thousand Tonnes     | NUMERIC      | Thousand Tonnes      |
| actual_stock_total_in_th_tonnes               | Actual Total Stock in Thousand Tonnes        | NUMERIC      | Thousand Tonnes      |
| actual_stock_days                             | Actual Stock in Days                         | NUMERIC      |                      |
| percentage_of_actual_stock_vs_normative_stock | Percentage of Actual Stock Vs Normative Stock | NUMERIC      | Percentage           |
| receipt_for_day_in_th_tonnes                  | Receipt for the Day in Thousand Tonnes       | NUMERIC      | Thousand Tonnes      |
| consumption_for_day_in_th_tonnes              | Consumption for the Day in Thousand Tonnes   | NUMERIC      | Thousand Tonnes      |
| critical_or_sup_critical                      | Critical or Super Critical                   | TEXT         |                      |
| reasons_for_critical_remarks                  | Reasons for Critical Remarks                 | TEXT         |                      |


[Data Summary](https://indiadataportal.com/p/power/r/mop-coal_stock-pl-dl-aaa#dataset-summary)

---

## UDISE 2023

Source: Ministry of Education

Sector: ['Education']

### UDISE 2023

Granularity: Point

Frequency: Biannually



---

## VAHAN Vehicle Registrations

Source: Ministry of Road Transport and Highways

Sector: ['Economy', 'Transportation']

### VAHAN Vehicle Registrations

Granularity: Regional Transport Office

Frequency: Monthly

The "VAHAN Vehicle Registrations" dataset provides comprehensive data on vehicle registrations across India, offering insights into various aspects such as vehicle norms, manufacturers, fuel types, categories, and classes. This dataset includes key variables like the date of registration, state names and codes, Regional Transport Office (RTO) names and codes, vehicle manufacturers, fuel types (e.g., petrol, diesel, electric), vehicle categories (e.g., two-wheeler, four-wheeler), and vehicle classes. Additionally, it categorizes data by specific norms, vehicle types, and other criteria, detailing the number of registrations for each category. This resource is invaluable for policymakers, transportation authorities, analysts, and the automotive industry, enabling them to monitor and understand trends in vehicle registrations, compliance with regulations, and the environmental impact of fuel usage across different regions and RTOs in India.

---

## Port Level Import Export

Source: Directorate General of Commercial Intelligence and Statistics

Sector: ['Commerce']

### Port Level Import Export

Granularity: State

Frequency: Monthly



---

## APMC arrivals and prices

Source: Ministry of Agriculture & Farmers Welfare

Sector: ['Food and Agriculture']

### Agriculture Marketing

Granularity: Market Center

Frequency: Daily



---

## Daily Fertilizer Sales

Source: Ministry of Chemicals and Fertilizers

Sector: ['Food and Agriculture']

### Daily Fertilizer Sales

Granularity: District

Frequency: Daily



---

## Road Connectivity-PMGSY

Source: Ministry of Rural Development

Sector: ['Rural Development', 'Socio Economic']

### Road Connectivity-PMGSY

Granularity: Road

Frequency: Yearly



---

## SHG Financial and Member Profile Details

Source: Ministry of Rural Development

Sector: ['Financial Inclusion', 'Rural Development']

### SHG Financial and Member Profile Details

Granularity: SHG

Frequency: Other

This dataset provides an extensive and nuanced profile of Self-Help Groups (SHGs) across diverse geographic and socio-economic contexts. It includes detailed information on the SHG's location, specifying the state, district, block, Gram Panchayat, and village, alongside a unique SHG identifier and its name. Key administrative details such as the date of formation, type of SHG, promoting entity, and banking information—including the bank name, branch, and account opening date—are also recorded. The dataset meticulously documents membership demographics, including total membership counts, gender distribution, and classifications by social categories such as Scheduled Caste, Scheduled Tribe, Other Backward Classes, and Other Social Categories. Additionally, it captures data on members with disabilities, both self-disabled and those with disabled family members, and provides insights into religious affiliations (Hindu, Christian, Muslim, Sikh, Buddhist, Jain, Parsi) and economic status, distinguishing between Above Poverty Line (APL), Below Poverty Line (BPL), and Poorest of the Poor under the PIP category.

Metadata -
 
| Variable Name          | Variable Description                                     | Variable Type | Unit Of Measurement |
|------------------------|-----------------------------------------------------------|---------------|---------------------|
| state_name             | State Name                                                | TEXT          |                     |
| district_name          | District Name                                             | TEXT          |                     |
| block_name             | Block Name                                                | TEXT          |                     |
| gp_name                | Gram Panchayat Name                                       | TEXT          |                     |
| village_name           | Village Name                                              | TEXT          |                     |
| shg_name               | Self Help Group Name                                      | TEXT          |                     |
| shg_id                 | Self Help Group ID                                        | TEXT          |                     |
| formation_date         | Date of Formation of SHG                                  | DATE          |                     |
| shg_type               | Type of SHG                                               | TEXT          |                     |
| promoted_by            | SHG Promoted By                                           | TEXT          |                     |
| bank_name              | Name of the bank where SHG is registered                  | TEXT          |                     |
| bank_branch            | Name of the bank branch where SHG is registered           | TEXT          |                     |
| acc_opening_date       | Date of opening of Bank Account                           | TEXT          |                     |
| total_members          | Number of members in SHG                                  | NUMERIC       | Numerical           |
| female                 | Number of female members in SHG                           | NUMERIC       | Numerical           |
| male                   | Number of male members in SHG                             | NUMERIC       | Numerical           |
| sc                     | Number of Scheduled Caste members in SHG                  | NUMERIC       | Numerical           |
| st                     | Number of Scheduled Tribe members in SHG                  | NUMERIC       | Numerical           |
| obc                    | Number of members belonging to Other Backward Classes     | NUMERIC       | Numerical           |
| other_category         | Number of members belonging to Other Social Categories    | NUMERIC       | Numerical           |
| disabled               | Number of members with disabilities                       | NUMERIC       | Numerical           |
| family_mem_disabled    | Number of members with a disabled family member           | NUMERIC       | Numerical           |
| hindu                  | Number of Hindu members                                   | NUMERIC       | Numerical           |
| christian              | Number of Christian members                               | NUMERIC       | Numerical           |
| muslim                 | Number of Muslim members                                  | NUMERIC       | Numerical           |
| sikh                   | Number of Sikh members                                    | NUMERIC       | Numerical           |
| buddhist               | Number of Buddhist members                                | NUMERIC       | Numerical           |
| jain                   | Number of Jain members                                    | NUMERIC       | Numerical           |
| parsi                  | Number of Parsi members                                   | NUMERIC       | Numerical           |
| apl                    | Number of members categorized as Above Poverty Line (APL) | NUMERIC       | Numerical           |
| bpl                    | Number of members categorized as Below Poverty Line (BPL) | NUMERIC       | Numerical           |
| pop                    | Number of members categorized as Poorest of the Poor under PIP category | NUMERIC       | Numerical           |
| poor                   | Number of members categorized as Poor under PIP category  | NUMERIC       | Numerical           |


---

## Mission Antyodaya 2020

Source: Ministry of Rural Development

Sector: ['Socio Economic']

### Mission Antyodaya 2020

Granularity: Village

Frequency: Yearly

The Mission Antyodaya dataset offers an extensive overview of village-level infrastructure, socio-economic indicators, and resource availability across India. This comprehensive dataset, collected under the Mission Antyodaya initiative, aims to uplift the most underprivileged rural communities by providing detailed insights into various aspects of rural life. This dataset serves as a crucial tool for policymakers, researchers, and development practitioners, providing a holistic view of rural development needs and achievements. By capturing diverse aspects of village life, the dataset facilitates comprehensive monitoring, planning, and implementation of initiatives aimed at improving rural infrastructure and services, thereby contributing to poverty alleviation and sustainable development in India's rural areas.

---

## CGWB - Changes in Depth to Water Level

Source: Ministry of Jal Shakti

Sector: ['Climate and Weather']

### CGWB - Changes in Depth to Water Level

Granularity: Station

Frequency: Quarterly



---

Please reach out to gursharan_sigh@isb.edu if you need any of the dataset