import Improvised_file_reading as fr
import Improvised_scoring
import Improvised_export_csv

# Points reference dictionary
points_reference = {
    "1": 8,
    "2": 7,
    "3": 6,
    "4": 5,
    "5": 4,
    "6": 3,
    "7": 2,
    "8": 1,
    ">": 1,
}

def get_parent_directory():
    """Prompt the user for the parent directory path."""
    return input("Enter the path to your parent directory >> ")

def get_selected_year():
    """Prompt the user to select a specific year."""
    return int(input("Enter the year you are interested in >> "))

def get_keyword_filter():
    """Prompt the user for a keyword to filter files."""
    return input("Enter a keyword to filter the files >> ").lower()

def get_save_as_csv():
    """Prompt the user to export the scores to a CSV file."""
    return input("Would you like to save the results as a CSV file? (Y/N) >> ").upper() == "Y"

def get_csv_filename():
    """Prompt the user for the CSV filename."""
    return input("Enter the filename for the CSV >> ")

def main():
    # Get user inputs
    parent_directory = get_parent_directory()
    print(fr.file_reading_component.return_years(parent_directory))
    
    selected_year = get_selected_year()
    year_path = fr.file_reading_component.find_year_path(parent_directory, selected_year, "WakaNats")
    files_in_year = fr.file_reading_component.return_files(year_path)
    
    keyword_filter = get_keyword_filter()
    filtered_files = [file for file in files_in_year if keyword_filter in file.lower()]
    print(len(filtered_files), keyword_filter, "found")
    
    # Process the contents of the filtered files
    regional_scores = []
    for file_name in filtered_files:
        try:
            file_path = f"{year_path}/{file_name}"
            content = fr.file_reading_component.return_content(file_path)
            
            # Format the content of the file
            formatted_content = fr.file_reading_component.format_content(content, file_name)
            
            # Check for errors in formatting
            if isinstance(formatted_content, tuple):
                print(formatted_content)
                continue
            
            # Calculate the scores based on the formatted content
            scores = Improvised_scoring.scoring_c.return_scores(formatted_content, points_reference)
            regional_scores.append(scores)
            
        except Exception as e:
            print(f"ERROR on file | {file_name} | {e}")
            continue
    
    # Calculate the total scores for the selected year
    total_scores = Improvised_scoring.scoring_c.return_scores(regional_scores)
    
    # Sort the scores in descending order
    sorted_scores = Improvised_scoring.scoring_c.score_sort(total_scores)
    
    # Export to CSV if the user wants to
    if get_save_as_csv():
        csv_filename = get_csv_filename()
        Improvised_export_csv.csv_c.csv_export(sorted_scores, csv_filename)

if __name__ == "__main__":
    main()