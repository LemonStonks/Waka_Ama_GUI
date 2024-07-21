# indicates the number of files in the folder

import os



# Creating a class
class file_reading_component():
    # Attributes or stat of this/that
    def __init__(self):
      pass
    
    @staticmethod
    def return_years(path):
      # return years in a list e.g [year1, year2]
      years_files = {}
      year_list = os.listdir(path)
      
      for year in year_list:
        years_files[year] = len(os.listdir(path + "/" + year)) # to put inside the year dictionary
        
        return year_list
      
    @staticmethod
    def find_year_path(path, year, prefix):
      # it returns the path of the argument year
      year_list = os.listdir
      year_path = None
      
      for i in year_list:
        if i == f"{prefix}{year}":
          year_path = f"{path}/{prefix}{year}"
      return year_path
    
    @staticmethod
    def return_files(year_path):
      # returns the list of files in a dir e.g [file1, file2, file3]
      
      file_list = os.listdir(year_path)
      
      return file_list 
    
    @staticmethod
    def return_content(file_path):
      # returns dictionary of the contents of the file and it includes its file name and content on a raw form
      """
      ["1, team,reg","2,team,reg"]
      
      """     
      with open(file_path) as file:
        file_contents = file.readlines()
      return file_contents
    
    @staticmethod
    def format_content(file_contents, filename):
      # return a dictionary of the formatted/categorized version of the contents of the file contents
      
      race_info = file_contents[0]
      subsequent_rows = file_contents[1:-1]
      
      # race info
      formatted_race_info = race_info.split(',')
      
      clean_formatted_race_info = []
      
      for i in formatted_race_info:
        if i != "":
          clean_formatted_race_info.append(i)
        else:
          continue
      formatted_race_info = clean_formatted_race_info
      
      
      race_number = formatted_race_info[0]
      race_type = formatted_race_info[1]
      race_heat = formatted_race_info[2]
      race_title = formatted_race_info[3]
      race_length = formatted_race_info[4]
      race_start_time = formatted_race_info[5]
    
      
      race_info_attributes = {"number":race_number,
                              "type":race_type,
                              "heat":race_heat,
                              "title":race_title,
                              "length":race_length,
                              "start_time":race_start_time}
                              
      
      # TEAMS
      team_list = []
      for string_team in subsequent_rows:
        formatted_team = string_team.split(',')
        
        clean_formatted_team = []
        
        for i in formatted_team:
          if i != "":
            clean_formatted_team.append(i)
          else:
            continue
        formatted_team = clean_formatted_team
        
        
        # I removed the uneccessary commas
        team_place = formatted_team[0]
        team_id = formatted_team[1]
        team_lane = formatted_team[2]
        team_name = formatted_team[3]
        team_regional_association = formatted_team[4]
        team_elapsed_time = formatted_team[5]
        team_difference = formatted_team[6]
        team_start = formatted_team[7]
        team_attributes = {"place": team_place,
                           "id":team_id,
                           "lane":team_lane,
                           "name":team_name,
                           "regional_association":team_regional_association,
                           "elapsed_time":team_elapsed_time,
                           "difference":team_difference,
                           "start":team_start}
        team_list.append(team_attributes)
        
        
      file_attributes = [race_info_attributes,team_list]
      
      return file_attributes
        
                                  
    




























'''Years_Files = {}

for every_item in dir_list:
  file_count = len(os.listdir(path + "/" + every_item)) # gives the numbers of files in the folder  
  Years_Files[every_item] = file_count # put inside the dictionary

print(Years_Files)'''

