from pandas import read_csv
import os

path_script_folder = os.path.dirname(os.path.realpath(__file__))
path_original_file = path_script_folder + "/" + "original/syukujitsu.csv"
path_processed_file = path_script_folder + "/" + "processed/odj-data-public_holidays.csv"
path_translation_file = path_script_folder + "/" + "translation.csv"

rename_header = {'国民の祝日・休日月日' : 'DATE_OF_PUBLIC_HOLIDAY'
                ,'国民の祝日・休日名称' : 'NAME_OF_PUBLIC_HOLIDAY_JP'}

# Load original data and rename headers to English
csv = read_csv(path_original_file, encoding="Shift-JIS").rename(columns=rename_header)
trans = read_csv(path_translation_file, encoding="UTF-8")

# Join translation of Japanese public holiiday names
csv = csv.merge(trans, left_on='NAME_OF_PUBLIC_HOLIDAY_JP', right_on='Japanese', how='left')
#print(csv.columns)

# Save processed data
csv.drop(labels=["Japanese"], axis=1).to_csv(path_processed_file, encoding='UTF-8')
