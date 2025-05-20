# High Granular Datasets - India Data Portal

## Port Level Import Export

Source: Directorate General of Commercial Intelligence and Statistics

Sector: Commerce

### Port Level Import Export

The Port Level Import-Export Dataset provides comprehensive monthly data on imports and exports at the principal commodity level, recorded across various ports in India. It includes detailed information on volume, value (in USD and INR), and commodity types, categorized at the 2-digit HS code level. This dataset is a crucial resource for analyzing trade patterns, regional trade performance, and economic activity. It is particularly valuable for economists, policymakers, trade analysts, and researchers studying international trade, economic development, and market trends. 
<details close>
<summary> Metadata</summary>

| Variable Name          | Variable Description                  | Variable Type | SubDataSet       |
|------------------------|---------------------------------------|---------------|------------------|
| month                  | Month                                 | DATE          |                  |
| trade_type             | Trade Type                            | TEXT          | Import, Export   |
| state_name             | State Name                            | TEXT          |                  |
| state_code             | State Code                            | TEXT          |                  |
| port                   | Port for Import                       | TEXT          |                  |
| country                | Import Country                        | TEXT          |                  |
| pc_code                | Principle Commodity Code              | TEXT          |                  |
| commodity              | Commodity Name                        | TEXT          |                  |
| units                  | Quantity Unit Measurement             | TEXT          |                  |
| quantity               | Value of commodity quantity           | NUMERIC       |                  |
| dollars_value          | Value of commodity quantity in USD    | NUMERIC       |                  |
| inr_value              | Value of commodity quantity in INR    | NUMERIC       |                  |

Granularity: State

Frequency: Monthly

Years Covered: 2018-2024

Data Retrival Date: 16-09-2024
---
</details>

## Pradhan Mantri Awaas Yojana - Gramin

Source: Ministry of Rural Development

Sector: Government Schemes

### Pradhan Mantri Awaas Yojana - Gramin

The dataset provides an in-depth view of the Pradhan Mantri Awaas Yojana - Gramin (PMAY-G), illustrating the scheme's progress and impact at the granular level of Gram Panchayats. It includes a multi-year record of houses sanctioned and completed, with detailed breakdowns by social categories to facilitate nuanced policy assessment and socio-economic analyses. The data highlights geographical variances and temporal trends, serving as an invaluable resource for policymakers, social researchers, and the general public interested in the effectiveness and inclusivity of rural housing developments under government schemes.
<details close>
<summary> Metadata</summary>

| Variable Name                                      | Variable Description                                 | Variable Type | Unit of Measurement |
|----------------------------------------------------|------------------------------------------------------|----------------|----------------------|
| state_name                                         | State Name                                           | Text           |                      |
| district_name                                      | District Name                                        | Text           |                      |
| block_name                                         | Block Name                                           | Text           |                      |
| panchayat_name                                     | Panchayat Name                                       | Text           |                      |
| target_fixed_by_panch                              | Target fixed by Panchayat                            | Numeric        | Number               |
| registered                                         | Registered                                           | Numeric        | Number               |
| breakup_of_reg_st                                  | Breakup of Registration ST                           | Numeric        | Number               |
| breakup_of_reg_sc                                  | Breakup of Registration SC                           | Numeric        | Number               |
| breakup_of_reg_minorities                          | Breakup of Registration Minorities                   | Numeric        | Number               |
| breakup_of_reg_ph                                  | Breakup of Registration PH                           | Numeric        | Number               |
| breakup_of_reg_others                              | Breakup of Registration Others                       | Numeric        | Number               |
| sanc_made                                          | Sanctions Made                                       | Numeric        | Number               |
| breakup_of_sanc_st                                 | Breakup of Sanction ST                               | Numeric        | Number               |
| breakup_of_sanc_sc                                 | Breakup of Sanction SC                               | Numeric        | Number               |
| breakup_of_sanc_minorities                         | Breakup of Sanction Minorities                       | Numeric        | Number               |
| breakup_of_sanc_ph                                 | Breakup of Sanction PH                               | Numeric        | Number               |
| breakup_of_sanc_others                             | Breakup of Sanction Others                           | Numeric        | Number               |
| completed                                          | Completed                                            | Numeric        | Number               |
| breakup_of_cmp_st                                  | Breakup of Completion ST                             | Numeric        | Number               |
| breakup_of_cmp_sc                                  | Breakup of Completion SC                             | Numeric        | Number               |
| breakup_of_cmp_minorities                          | Breakup of Completion Minorities                     | Numeric        | Number               |
| breakup_of_cmp_ph                                  | Breakup of Completion PH                             | Numeric        | Number               |
| breakup_of_cmp_others                              | Breakup of Completion Others                         | Numeric        | Number               |
| house_compl_2014_2015                              | Houses Completed in 2014-15                          | Numeric        | Number               |
| house_compl_2015_2016                              | Houses Completed in 2015-16                          | Numeric        | Number               |
| house_compl_2016_2017                              | Houses Completed in 2016-17                          | Numeric        | Number               |
| house_compl_2017_2018                              | Houses Completed in 2017-18                          | Numeric        | Number               |
| house_compl_2018_2019                              | Houses Completed in 2018-19                          | Numeric        | Number               |
| house_compl_2019_2020                              | Houses Completed in 2019-20                          | Numeric        | Number               |
| house_compl_2020_2021                              | Houses Completed in 2020-21                          | Numeric        | Number               |
| house_compl_2021_2022                              | Houses Completed in 2021-22                          | Numeric        | Number               |
| house_compl_2022_2023                              | Houses Completed in 2022-23                          | Numeric        | Number               |
| house_compl_2023_2024                              | Houses Completed in 2023-24                          | Numeric        | Number               |
| sanctions_made                                     | Sanctions Made                                       | Numeric        | Number               |
| breakup_of_sanction_women                          | Breakup of Sanction Women                            | Numeric        | Number               |
| breakup_of_sanction_men                            | Breakup of Sanction Men                              | Numeric        | Number               |
| breakup_of_sanction_joint_wife_and_husband         | Breakup of Sanction Joint Wife And Husband           | Numeric        | Number               |
| breakup_of_sanction_others                         | Breakup of Sanction Others                           | Numeric        | Number               |
| breakup_of_completion_women                        | Breakup of Completion Women                          | Numeric        | Number               |
| breakup_of_completion_men                          | Breakup of Completion Men                            | Numeric        | Number               |
| breakup_of_completion_joint_wife_and_husband       | Breakup of Completion Joint Wife And Husband         | Numeric        | Number               |
| breakup_of_completion_others                       | Breakup of Completion Others                         | Numeric        | Number               |
| completed                                          | Houses Completed                                     | Numeric        | Number               |

Granularity: Gram Panchayat

Frequency: Other

Years Covered: 2014-2024

Data Retrival Date: 20-12-2023

---
</details>

## Mahatma Gandhi National Rural Employment Guarantee Act

Source: Ministry of Rural Development

Sector: Rural Development

### MGNREGA

The Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) dataset provides detailed information on the implementation of the MGNREGA program in India. The MGNREGA program is a flagship social welfare program of the Indian government that guarantees 100 days of employment to every rural household in the country, with a special focus on the poorest and most marginalized communities. The dataset includes information on the number of households and individuals who have benefited from the program, the amount of funds disbursed, and the types of work undertaken by program beneficiaries. The dataset is organized according to various dimensions, such as state, district, and financial year, making it easy for users to filter and analyze the data according to their specific needs. The dataset is relevant to a wide range of stakeholders, including government officials, social scientists, policy think tanks, media houses, and newsrooms. The data is collected and maintained by the Ministry of Rural Development, Government of India, and is available for download on the MGNREGA website. The dataset is a valuable resource for researchers, policymakers, and journalists interested in issues related to rural employment, poverty reduction, social inclusion, and sustainable development in India.
<details close>
<summary> Metadata</summary>

| Variable Name                                   | Variable Description                                                        | Variable Type | Unit of Measurement |
|-------------------------------------------------|------------------------------------------------------------------------------|----------------|----------------------|
| year                                            | Year                                                                         | Text           |                      |
| state_name                                      | Name of the state                                                            | Text           |                      |
| district_name                                   | Name of the district                                                         | Text           |                      |
| block_name                                      | Name of the block                                                            | Text           |                      |
| gp_name                                         | Name of the Gram Panchayat                                                  | Text           |                      |
| reg_hh                                          | Number of registered households                                              | Numeric        |                      |
| reg_pers                                        | Number of registered persons                                                 | Numeric        |                      |
| del_jobcards_hh                                 | Number of deleted job cards for households                                   | Numeric        |                      |
| del_jobcards_pers                               | Number of deleted job cards for persons                                      | Numeric        |                      |
| incl_jobcards_hh                                | Number of included job cards for households                                  | Numeric        |                      |
| incl_jobcards_pers                              | Number of included job cards for persons                                     | Numeric        |                      |
| cumul_hh_jobcards_sc                            | Cumulative job cards issued for Scheduled Castes for households              | Numeric        |                      |
| cumul_hh_jobcards_sts                           | Cumulative job cards issued for Scheduled Tribes for households              | Numeric        |                      |
| cumul_hh_jobcards_others                        | Cumulative job cards issued for other categories for households              | Numeric        |                      |
| cumul_hh_jobcards_tot                           | Total cumulative job cards issued for all categories for households          | Numeric        |                      |
| emp_demand_hh                                   | Number of households demanding employment                                    | Numeric        |                      |
| emp_demand_pers                                 | Number of persons demanding employment                                       | Numeric        |                      |
| emp_offer_hh                                    | Number of households offered employment                                      | Numeric        |                      |
| emp_offer_pers                                  | Number of persons offered employment                                         | Numeric        |                      |
| emp_avail_hh                                    | Number of households availing employment                                     | Numeric        |                      |
| emp_avail_pers                                  | Number of persons availing employment                                        | Numeric        |                      |
| emp_avail_tot_persondays                        | Total person-days of employment availed                                      | Numeric        |                      |
| emp_avail_central_persondays                    | Person-days of employment availed under central liability                    | Numeric        |                      |
| emp_avail_states_persondays                     | Person-days of employment availed under state's liability                    | Numeric        |                      |
| fam_completed_100_days                          | Number of households completing 100 days of employment                       | Numeric        |                      |
| land_reform_benef_hh                            | Number of households benefiting from land reform or IAY schemes              | Numeric        |                      |
| disabled_benef_indiv                            | Number of disabled individuals benefiting from the scheme                    | Numeric        |                      |
| joint_acc_women                                 | Number of joint account of women                                             | Numeric        |                      |
| total_acc_women                                 | Number of total account of women                                             | Numeric        |                      |
| women_beneficiary_workers_with_acc              | Number of women beneficiary workers with an account                          | Numeric        |                      |
| women_beneficiary_active_workers_with_acc       | Number of women beneficiary active workers with an account                   | Numeric        |                      |
| applied_jobcards                                | Number of applied job cards                                                  | Numeric        | Lakh                 |
| issued_jobcards                                 | Number of issued job cards                                                   | Numeric        | Lakh                 |
| registered_workers_scs                          | Number of registered workers from Scheduled Castes                           | Numeric        | Lakh                 |
| registered_workers_sts                          | Number of registered workers from Scheduled Tribes                           | Numeric        | Lakh                 |
| registered_workers_others                       | Number of registered workers from other categories                           | Numeric        | Lakh                 |
| total_registered_workers                        | Total number of registered workers                                           | Numeric        | Lakh                 |
| registered_workers_women                        | Number of registered female workers                                          | Numeric        | Lakh                 |
| active_jobcards                                 | Number of active job cards                                                   | Numeric        | Lakh                 |
| active_workers_scs                              | Number of active workers from Scheduled Castes                               | Numeric        | Lakh                 |
| active_workers_sts                              | Number of active workers from Scheduled Tribes                               | Numeric        | Lakh                 |
| active_workers_others                           | Number of active workers from other categories                               | Numeric        | Lakh                 |
| total_active_workers                            | Total number of active workers                                               | Numeric        | Lakh                 |
| active_workers_women                            | Number of active female workers                                              | Numeric        | Lakh                 |

Granularity: Gram Panchayat

Frequency: Yearly

Years Covered: 2014-2024

Data Retrival Date: 31-08-2023

---
</details>

[Dataset Summary: Category Wise Workers](https://indiadataportal.com/p/mgnrega-mahatma-gandhi-national-rural-employment-guarantee-act/r/mord-mgnrega_category_wise_worker-gp-yr-aaa#dataset-summary)

[Dataset Summary: Employment Generated](https://indiadataportal.com/p/mgnrega-mahatma-gandhi-national-rural-employment-guarantee-act/r/mord-mgnrega_employment_generated-gp-yr-aaa#dataset-summary)

[Dataset Summary: Women Joint Accounts](https://indiadataportal.com/p/mgnrega-mahatma-gandhi-national-rural-employment-guarantee-act/r/mord-mgnrega_women_joint_acc-gp-yr-aaa#dataset-summary)

## UDISE

Source: Ministry of Education

Sector: Education

### UDISE

The Unified District Information System for Education (UDISE) is a comprehensive database of schools in India, encompassing over 1.5 million schools, 9.6 million teachers, and 264 million children. Developed by the Government of India under the Ministry of Education, UDISE serves as a vital management information system that systematically collects, collates, and disseminates data on various aspects of school education. It captures detailed information on school infrastructure, teacher qualifications, student enrollment, and other key educational parameters. Data is collected bi-annually from pre-primary to higher secondary levels across all states and union territories, ensuring a robust and up-to-date overview of the education sector.
<details close>
<summary> Metadata</summary>

| Variable Name                            | Variable Description                                    | Variable Type |
|------------------------------------------|--------------------------------------------------------|--------------|
| state_name                               | State                                                 | TEXT         |
| state_code                               | State Code                                           | TEXT         |
| district_name                            | District                                             | TEXT         |
| district_code                            | District Code                                        | TEXT         |
| sub_district_name                        | Sub-District                                         | TEXT         |
| sub_district_code                        | Sub-District Code                                    | TEXT         |
| cluster_name                             | Cluster                                             | TEXT         |
| village_name                             | Village                                             | TEXT         |
| udise_village_code                       | UDISE Village Code                                  | TEXT         |
| pincode                                  | Pincode                                             | TEXT         |
| ward                                     | Ward                                                | TEXT         |
| school_name                              | School Name                                         | TEXT         |
| udise_school_code                        | School Code                                         | TEXT         |
| school_category                          | School Category                                     | TEXT         |
| school_type                              | School Type                                         | TEXT         |
| management                               | Management                                          | TEXT         |
| year_of_establishment                    | Year of Establishment                               | TEXT         |
| longitude                                | Longitude                                           | NUMERIC      |
| latitude                                 | Latitude                                            | NUMERIC      |
| status                                   | Status                                             | TEXT         |
| location_type                            | Location Type                                      | TEXT         |
| class_from                               | Class From                                         | NUMERIC      |
| class_to                                 | Class To                                           | NUMERIC      |
| aff_board_sec                            | Affiliation Board for Secondary Education         | TEXT         |
| aff_board_h_sec                          | Affiliation Board for Higher Secondary Education  | TEXT         |
| pre_primary                              | Pre Primary Rooms                                  | NUMERIC      |
| class_rooms                              | Class Rooms                                        | NUMERIC      |
| other_rooms                              | Other Rooms                                        | NUMERIC      |
| total_teachers                           | Teachers                                           | NUMERIC      |
| pre_primary_students                     | Pre Primary Students                               | NUMERIC      |
| i_students                               | Students in Class I                                | NUMERIC      |
| ii_students                              | Students in Class II                               | NUMERIC      |
| iii_students                             | Students in Class III                              | NUMERIC      |
| iv_students                              | Students in Class IV                               | NUMERIC      |
| v_students                               | Students in Class V                                | NUMERIC      |
| vi_students                              | Students in Class VI                               | NUMERIC      |
| vii_students                             | Students in Class VII                              | NUMERIC      |
| viii_students                            | Students in Class VIII                             | NUMERIC      |
| ix_students                              | Students in Class IX                               | NUMERIC      |
| x_students                               | Students in Class X                                | NUMERIC      |
| xi_students                              | Students in Class XI                               | NUMERIC      |
| xii_students                             | Students in Class XII                              | NUMERIC      |
| class_students                           | Non Primary Students                               | NUMERIC      |
| class_with_pre_primary_students          | Total Students                                    | NUMERIC      |

Granularity: Point

Frequency: Biannually

Years Covered: 1701-2021

Data Retrival Date: 12-01-2022

---
</details>

[Dataset Summary: Basic School Details](https://indiadataportal.com/p/udise/r/moe-udise_basic_details-pl-ot-sib)

## Daily Coal Stocks

Source: Ministry of Power

Sector: Energy

### Daily Coal Stocks

Coal Stocks data is taken from thermal power stations across India. The data is collected daily. It contains coal stock data by state, sector, and individual power station. The data field includes mode of transport,  capacity, normative stocks, actual stocks, receipt, consumption, plant load factor, the criticalness of the plant, reason for critical etc., for each power station.
<details close>
<summary> Metadata</summary>

| Variable Name                            | Variable Description                                     | Variable Type | Unit Of Measurement      |
|------------------------------------------|----------------------------------------------------------|----------------|---------------------------|
| date                                     | Date                                                     | DATE           |                           |
| state_name                               | State Name                                               | TEXT           |                           |
| state_code                               | State Code                                               | TEXT           |                           |
| power_station_name                       | Power Station Name                                       | TEXT           |                           |
| sector                                   | Sector of Power Station                                  | TEXT           |                           |
| utility                                  | Utility of Power Station                                 | TEXT           |                           |
| mode_of_transport                        | Mode of Transport Coal                                   | TEXT           |                           |
| capacity                                 | Capacity of Power Station                                | NUMERIC        | Mega Watt                 |
| daily_requirement                        | Requirement for the day                                  | NUMERIC        | Thousand Tonnes           |
| daily_receipt                            | Receipt For Day                                          | NUMERIC        | Thousand Tonnes           |
| daily_consumption                        | Consumption For Day                                      | NUMERIC        | Thousand Tonnes           |
| req_normative_stock                      | Required Normative Stock                                 | NUMERIC        | Thousand Tonnes           |
| normative_stock_days                     | Required Normative Stock in Days                         | NUMERIC        | Number of Days            |
| indigenous_stock                         | Actual Indigenous Stock                                  | NUMERIC        | Thousand Tonnes           |
| import_stock                             | Actual Imported Stock                                    | NUMERIC        | Thousand Tonnes           |
| total_stock                              | Actual Total Stock                                       | NUMERIC        | Thousand Tonnes           |
| stock_days                               | Actual Stock in Days                                     | NUMERIC        | Number of Days            |
| plf_prcnt                                | Plant Load Factor Percentage                             | NUMERIC        | Percentage                |
| actual_vs_normative_stock_prcnt          | Percentage of Actual Stock vs Normative Stock            | NUMERIC        | Percentage                |
| is_critical                              | Critical or Super Critical Status                        | TEXT           |                           |
| remarks                                  | Reasons for Critical in Remarks                          | TEXT           |                           |

Granularity: Power Station

Frequency: Daily

Years Covered: 2018-2025

Data Retrival Date: 03-04-2025

---
</details>

[Dataset Summary: Daily Coal Stocks](https://indiadataportal.com/p/power/r/mop-coal_stock-pl-dl-aaa)

## Exports and Imports of India

Source: Directorate General of Commercial Intelligence and Statistics

Sector: Commerce

### Exports and Imports of India

The "Exports and Imports of India" dataset provides a comprehensive view of trade exports and imports of India across the globe. This dataset covers the periodical monthly data of exports in terms of value in both USD and INR and also in terms of quantity. Each record provides the date, target country, type of product (both in terms of HS code and the commodity name), the value of the commodity, and the quantity of the commodity being exported. 
<details close>
<summary> Metadata</summary>

| Variable Name     | Variable Description                        | Variable Type | Unit Of Measurement     |
|-------------------|---------------------------------------------|----------------|--------------------------|
| date              | Date                                        | DATE           |                          |
| country_name      | Country Name                                | TEXT           |                          |
| alpha_3_code      | ISO Alpha 3 Code                            | TEXT           |                          |
| country_code      | Country Code                                | TEXT           |                          |
| region            | Region Name                                 | TEXT           |                          |
| region_code       | Region Code                                 | TEXT           |                          |
| sub_region        | Sub-Region Name                             | TEXT           |                          |
| sub_region_code   | Sub-Region Code                             | TEXT           |                          |
| hs_code           | Harmonized System Code                      | TEXT           |                          |
| commodity         | Commodity Name                              | TEXT           |                          |
| unit              | Unit of Quantity                            | TEXT           |                          |
| value_qt          | Quantity of commodity                       | NUMERIC        | Thousands Units          |
| value_rs          | Value of commodity quantity in INR          | NUMERIC        | Lacs                     |
| value_dl          | Value of commodity quantity in US Dollars   | NUMERIC        | Million                  |

Granularity: Country

Frequency: Monthly

Years Covered: 2007-2025

Data Retrival Date: 05-09-2025

---
</details>

[Dataset Collection](https://indiadataportal.com/p/export-trade-statistics)

## Road Connectivity-PMGSY

Source: Ministry of Rural Development

Sector: Rural Development, Socio Economic

### Road Connectivity-PMGSY

: The dataset provides comprehensive financial and physical progress information for all road projects that are being implemented under the Pradhan Mantri Gram Sadak Yojana (PMSGY) in India. PMSGY is a government-led initiative aimed at connecting all unconnected habitations in rural areas with all-weather roads, which is critical to the socio-economic development of rural India. The dataset includes information such as the total cost of the project, the amount of funds allocated, the expenditure incurred so far, the length of the road constructed, the percentage of the road completed, and the quality of the construction work. This information can be used to monitor the progress of each project and to identify any areas where improvements are needed. 
<details close>
<summary> Metadata</summary>

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

Granularity: Road

Frequency: Yearly

Years Covered: 1960-2021

Data Retrival Date: 01-04-2021

---
</details>

## SHG Financial and Member Profile Details

Source: Ministry of Rural Development

Sector: Financial Inclusion, Rural Development

### SHG Financial and Member Profile Details

This dataset provides an extensive and nuanced profile of Self-Help Groups (SHGs) across diverse geographic and socio-economic contexts. It includes detailed information on the SHG's location, specifying the state, district, block, Gram Panchayat, and village, alongside a unique SHG identifier and its name. Key administrative details such as the date of formation, type of SHG, promoting entity, and banking information—including the bank name, branch, and account opening date—are also recorded. The dataset meticulously documents membership demographics, including total membership counts, gender distribution, and classifications by social categories such as Scheduled Caste, Scheduled Tribe, Other Backward Classes, and Other Social Categories. Additionally, it captures data on members with disabilities, both self-disabled and those with disabled family members, and provides insights into religious affiliations (Hindu, Christian, Muslim, Sikh, Buddhist, Jain, Parsi) and economic status, distinguishing between Above Poverty Line (APL), Below Poverty Line (BPL), and Poorest of the Poor under the PIP category.
<details close>
<summary> Metadata</summary>


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

Granularity: SHG

Frequency: Other

Years Covered: 

Data Retrival Date: 18-08-2024

---
</details>

[Dataset Collection](https://indiadataportal.com/p/nrlm-national-rural-livelihoods-mission)

## Bank Outlets and ATM's

Source: Reserve Bank of India

Sector: Banking, Economy, Financial Inclusion

### Bank Outlets and ATM's

The Banking Outlet section of the Reserve Bank of India's Database on Indian Economy (DBIE) provides comprehensive data on the distribution and reach of banking services across India. It includes the location (latitude and longitude) of banking outlets, along with associated information such as bank name, bank type (Branch, CSP, Office, Business Correspondent, Digital Banking Unit [DBU], NAIO), bank group (e.g., foreign, public, private, payment banks, regional, local), their IFSC codes, date of opening, population group (metropolitan, urban, rural, semi-urban) associated with the outlet, and whether the outlet is a domestic or overseas branch. This dataset supports analyses of financial inclusion, accessibility, and the expansion of banking infrastructure.  
<details close>
<summary> Metadata</summary>

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

Granularity: Point

Frequency: Other

Years Covered: 1900-2023

Data Retrival Date: 12-01-2023

---
</details>

[Dataset Summary: Bank Outlets and ATM's](https://indiadataportal.com/p/reserve-bank-of-india/r/rbi-bank_outlets_and_atms-pl-ot-aaa)

## CGWB - Changes in Depth to Water Level

Source: India Water Resources Information System

Sector: Climate and Weather

### CGWB - Changes in Depth to Water Level

Central Ground Water Board monitors groundwater levels throughout the country on a regional scale, four times in a year during the months of March/April/May, August, November and January.This data is collected under the mode of acquisition �Manual�.  For monitoring of ground water level, CGWB has a dedicated network of about 25000 monitoring stations called �National Hydrograph Network Stations (NHNS)�, which comprises open dug wells and purpose-built bore/tube wells for water level monitoring called piezometers.  Similarly, CGWB has initiated automatic high frequency monitoring by installing Digital Water Level Recorders (DWLR) with telemetry systems under the National Hydrology Project (NHP).   This data is collected under the mode of acquisition �Telemetry�.
<details close>
<summary> Metadata</summary>

| Variable Name   | Variable Description       | Variable Type | Unit of Measurement |
|-----------------|----------------------------|---------------|---------------------|
| date            | Date                       | DATE          |                     |
| state_name      | State Name                 | TEXT          |                     |
| state_code      | State Code                 | TEXT          |                     |
| district_name   | District Name              | TEXT          |                     |
| district_code   | District Code              | TEXT          |                     |
| station_name    | Station Name               | TEXT          |                     |
| latitude        | Latitude                   | NUMERIC       |                     |
| longitude       | Longitude                  | NUMERIC       |                     |
| basin           | Basin                      | TEXT          |                     |
| sub_basin       | Sub Basin                  | TEXT          |                     |
| source          | Source                     | TEXT          |                     |
| currentlevel    | Depth to Water Level       | NUMERIC       | Meters              |
| level_diff      | Level Difference           | NUMERIC       |                     |

Granularity: Station

Frequency: 

Years Covered: 1965-2025

Data Retrival Date: 02-04-2025

---
</details>

[Dataset Summary: CGWB - Changes in Depth to Water Level](https://indiadataportal.com/p/groundwater/r/mojs-wris_cgwb_wells_level_changes-pl-ot-aaa)

## Daily Non-Renewable Power Generation

Source: Ministry of Power

Sector: Energy

### Daily Non-Renewable Power Generation

Power Generation data is taken from nuclear, thermal and hydro power stations across india. The data is collected on daily basis. It contains generation data by state, sector, power station type, individual power station and unit level. The data field includes installed capacity, day's power generaiton target, actual generation etc. for each power station.
<details close>
<summary> Metadata</summary>

| Variable Name                              | Variable Description                        | Variable Type | Unit Of Measurement |
|--------------------------------------------|---------------------------------------------|---------------|---------------------|
| date                                       | Date                                        | DATE          |                     |
| state_name                                 | State Name                                  | TEXT          |                     |
| state_code                                 | State Code                                  | TEXT          |                     |
| sector                                     | Sector of Power Station                     | TEXT          |                     |
| power_station_type                         | Type of Power Station                       | TEXT          |                     |
| power_station                              | Name of Power Station                       | TEXT          |                     |
| power_station_unit                         | Power Station Unit                          | TEXT          |                     |
| monitored_cap_in_mw                        | Total Monitored Capacity                    | NUMERIC       | Mega Watt           |
| todays_power_generation_programe_in_mu     | Program of Today's Power Generation         | NUMERIC       | Mega Unit           |
| todays_actual_power_generation_in_mu       | Today's Actual Power Generation             | NUMERIC       | Mega Unit           |


Granularity: Power Station

Frequency: Daily

Years Covered: 2017-2025

Data Retrival Date: 30-04-2025

---
</details>

[Dataset Summary: Power Generation](https://dev.indiadataportal.com/p/power/r/mop-power_generation-pl-dl-abc#dataset-summary)

## APMC arrivals and prices

Source: Ministry of Agriculture & Farmers Welfare

Sector: Food and Agriculture

### Agriculture Marketing

The Agricultural Marketing Information Network (AGMARKNET) dataset provides daily price and arrival information for more than 300 different commodities and over 1500 varieties of agricultural produce from wholesale markets across India. This comprehensive dataset is collected from Agricultural Produce Market Committees (APMCs) and covers 4549 markets as of January 16, 2025.

The data is uploaded to the AGMARKNET portal, which provides easy access to commodity-wise, variety-wise daily prices and arrivals information. This information can be used to analyze the dynamics of agricultural markets, identify patterns and trends, and inform policymaking decisions. The dataset is a valuable resource for researchers, policymakers, and market participants who need to understand the challenges facing India's agricultural sector, which plays a vital role in the country's economy and food security.

<details close>
<summary> Metadata</summary>

| Variable Name     | Variable Description   | Variable Type | Unit Of Measurement     |
|-------------------|------------------------|----------------|--------------------------|
| report_date       | Date                   | DATE           |                          |
| state_name        | State                  | TEXT           |                          |
| state_code        | State Code             | TEXT           |                          |
| district_name     | District               | TEXT           |                          |
| district_code     | District Code          | TEXT           |                          |
| market_center     | Market Center          | TEXT           |                          |
| market_code       | Market Center Code     | TEXT           |                          |
| latitude          | Latitude               | NUMERIC        |                          |
| longitude         | Longitude              | NUMERIC        |                          |
| commodity_type    | Commodity Type         | TEXT           |                          |
| commodity         | Commodity              | TEXT           |                          |
| variety           | Variety                | TEXT           |                          |
| origin            | Origin                 | TEXT           |                          |
| arrivals_tonnes   | Arrivals               | NUMERIC        | Tonnes                   |
| arrivals_unit     | Arrivals Unit          | TEXT           |                          |
| min_price         | Minimum Price          | NUMERIC        | INR / quintalls         |
| max_price         | Maximum Price          | NUMERIC        | INR / quintalls         |
| modal_price       | Modal Price            | NUMERIC        | INR / quintalls         |
| price_unit        | Price Unit             | TEXT           |                          |


Granularity: Market Center

Frequency: Daily

Years Covered: 2019-2025

Data Retrival Date: 30-04-2025

---
</details>

[Dataset Summary: Agriculture Marketing](https://indiadataportal.com/p/agriculture-marketing/r/moafw-agmarknet_commodities-ol-dl-l5y)

## Daily Fertilizer Sales

Source: Ministry of Chemicals and Fertilizers

Sector: Food and Agriculture

### Daily Fertilizer Sales

The dataset provides information on the daily sales of different types of fertilizers by retail outlets in India. This dataset is valuable for farmers, policymakers, researchers, and other stakeholders in the agriculture sector. Farmers can use the information to plan their fertilizer purchases and ensure that they have access to the fertilizers they need. Policymakers can use the data to monitor the supply and demand of fertilizers in different regions of the country and make informed decisions on fertilizer subsidy policies. Researchers can use the data to study the fertilizer market and identify trends and patterns in fertilizer sales. 
<details close>
<summary> Metadata</summary>

| Variable Name              | Variable Description              | Variable Type | Unit of Measurement |
|----------------------------|-----------------------------------|---------------|---------------------|
| date                       | Date                              | DATE          |                     |
| state_name                 | Name of State                     | TEXT          |                     |
| state_code                 | State Code                        | TEXT          |                     |
| district_name              | Name of District                  | TEXT          |                     |
| district_code              | District Code                     | TEXT          |                     |
| retailer_name              | Name of Retailer                  | TEXT          |                     |
| retailer_id                | Retailer ID                        | TEXT          |                     |
| attached_devices           | No of Attached PoS Devices        | NUMERIC       |                     |
| active                     | Active                            | BOOLEAN       |                     |
| opening_stock_reported     | Opening Stock Reported            | BOOLEAN       |                     |
| opening_stock              | Opening Stock (as on dry run or go live date) | NUMERIC       | Metric Tonnes       |
| no_of_invoices_generated   | No of Invoices Generated          | NUMERIC       |                     |
| no_of_sale_transaction     | No of Sales Transactions          | NUMERIC       |                     |
| quantity_sold              | Quantity Sold                     | NUMERIC       |                     |
| n_quantity                 | Quantity of Nitrogen Sold         | NUMERIC       |                     |
| p_quantity                 | Quantity of Phosphorus Sold       | NUMERIC       |                     |
| k_quantity                 | Quantity of Potassium Sold        | NUMERIC       |                     |
| s_quantity                 | Quantity of Sulfur Sold           | NUMERIC       |                     |

Granularity: District

Frequency: Daily

Years Covered: 2015-2021

Data Retrival Date: 01-01-2022

---
</details>

## VAHAN Vehicle Registrations

Source: Ministry of Road Transport and Highways

Sector: Economy, Transportation

### VAHAN Vehicle Registrations

The "VAHAN Vehicle Registrations" dataset provides comprehensive data on vehicle registrations across India, offering insights into various aspects such as vehicle norms, manufacturers, fuel types, categories, and classes. This dataset includes key variables like the date of registration, state names and codes, Regional Transport Office (RTO) names and codes, vehicle manufacturers, fuel types (e.g., petrol, diesel, electric), vehicle categories (e.g., two-wheeler, four-wheeler), and vehicle classes. Additionally, it categorizes data by specific norms, vehicle types, and other criteria, detailing the number of registrations for each category. This resource is invaluable for policymakers, transportation authorities, analysts, and the automotive industry, enabling them to monitor and understand trends in vehicle registrations, compliance with regulations, and the environmental impact of fuel usage across different regions and RTOs in India.
<details close>
<summary> Metadata</summary>

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

Granularity: Regional Transport Office

Frequency: Monthly

Years Covered: 2019-2024

Data Retrival Date: 27-06-2024

---
</details>

[Dataset Collection](https://indiadataportal.com/p/vehicle-registrations)

## Mission Antyodaya 2020

Source: Ministry of Rural Development

Sector: Socio Economic

### Mission Antyodaya 2020

The Mission Antyodaya dataset offers an extensive overview of village-level infrastructure, socio-economic indicators, and resource availability across India. This comprehensive dataset, collected under the Mission Antyodaya initiative, aims to uplift the most underprivileged rural communities by providing detailed insights into various aspects of rural life. This dataset serves as a crucial tool for policymakers, researchers, and development practitioners, providing a holistic view of rural development needs and achievements. By capturing diverse aspects of village life, the dataset facilitates comprehensive monitoring, planning, and implementation of initiatives aimed at improving rural infrastructure and services, thereby contributing to poverty alleviation and sustainable development in India's rural areas.
<details close>
<summary> Metadata</summary>

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

Granularity: Village

Frequency: Yearly

Years Covered: 2020

Data Retrival Date: 28-05-2024

---
</details>

[Dataset Collection](https://indiadataportal.com/p/mission-antyodaya)

Please reach out to gursharan_sigh@isb.edu if you need any of the dataset