import cns1, flight_data

mi_file_name = "2018-04-27 11-16-16_mission_insight.csv"
dataflash_file_name = "2018-04-27 11-16-16.log"
field_vars_file_name = "2018-04-27 11-16-16_field_variables.csv"

cns1.generate(mi_file_name, dataflash_file_name, field_vars_file_name, "CNS1.json")
flight_data.generate(mi_file_name, dataflash_file_name, "FLIGHT_DATA.json")