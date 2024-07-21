import file_reading as fr
import gui_comp
import scoring
import export_csv

points_reference = {
    "1":8,
    "2":7,
    "3":6,
    "4":5,
    "5":4,
    "6":3,
    "7":2,
    "8":1,
    ">":1,
}

# to get years
ask_parent_path = input("Type your parent folder >> ")
parent_path = ask_parent_path
print(fr.file_reading_component.return_years(parent_path))

# to get all the files
ask_year = int(input("Type your year >> "))
target_year_path = fr.file_reading_component.find_year_path(parent_path, ask_year,"WakaNats")
file_list = fr.file_reading_component.return_files(target_year_path)

# to find specific keyword only

ask_keyword = input("filter keyword >> ")
filtered_file_list = []
for file in file_list:
    if ask_keyword in file.lower():
        filtered_file_list.append(file)
    else:
        continue
print(len(filtered_file_list), ask_keyword, "found")

# get contents

file_regional_association_score_list = []
for filename in filtered_file_list:
    try:
        filepath = f"{target_year_path}/{filename}"
        file_contents = fr.file_reading_component.return_content(filepath)
        
        # get formatted version
        
        formatted_file_contents = fr.file_reading_component.format_content(file_contents, filename)
        
        # to check if there are any errors
        if type(formatted_file_contents) is tuple:
            print(formatted_file_contents)
            continue
        
        # get the regional association of the file
        file_regional_association_scores = scoring.scoring_c.return_scores(formatted_file_contents, points_reference)
        file_regional_association_score_list.append(file_regional_association_scores)
        
    except Exception as e:
        print(f"ERROR on file | {filename} | {e}")
        continue
    
# get sum of all the regional association scores
year_regional_association_scores = scoring.scoring_c.return_scores(file_regional_association_score_list)

# sort the file (descending)
year_regional_association_scores = scoring.scoring_c.score_sort(year_regional_association_scores)

# get the csv export option
ask_csv_export = input("Do you wish to save as CSV? (Y/N) >> ")
if ask_csv_export == "Y":
    ask_csv_filename = input("Type filename >> ")
    export_csv.csv_c.csv_export(year_regional_association_scores, ask_csv_filename)
        