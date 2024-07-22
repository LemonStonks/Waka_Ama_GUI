import os
import customtkinter as ct
from tkinter import messagebox # For displaying pop-up dialogs
from tkinter import filedialog # For accessing folders
import csv_export
import tkinter as tk

class program_functions_component():
    def __init__(self):

        self.parent_folder = ""
        self.target_year = 0
        self.target_keyword = 0
        

    def check_inputs_is_valid(self):
        # Display the parent directory
        # Display the selected year
        # Display the keyword for filtering


        if self.check_parent_folder_is_valid() == True:
            if self.check_target_year_is_valid() == False:
                return True
            else:
                return self.check_target_year_is_valid()
        else:
            return self.check_parent_folder_is_valid()
        
        
    def check_parent_folder_is_valid(self):
        try:
            parent_folder_items = os.listdir(self.parent_folder)
        except:
            return f"You must select a folder"
        # Verify if there is any content inside
        if parent_folder_items:
            for i in parent_folder_items:
                if "WakaNats" in i:
                    return True
                else:
                    continue
            # If there is no Wakanats found
            return f"There is no WakaNats found {self.parent_folder}"

        else:
            return f"There is no items inside {self.parent_folder}"


    def check_target_year_is_valid(self):
        # Verify if the value is an integer
        
        
        if self.target_year.isdigit():
            # Retrieve all available years
            all_available_years_folders = self.get_all_wakanats()
            
            all_available_years = []
            # Extract just the year from the date string
            for i in all_available_years_folders:
                all_available_years.append(i[-4:]) # the last 4 strigs


            # Determine if the input year falls within the specified range of years
            if self.target_year in all_available_years:
                return True
            else:
                return f"The year {self.target_year} is not accessible"


        else:
            return f"{self.target_year} is not a year"



    # Used exclusively within the system
    def get_all_wakanats(self):
        
        parent_folder_items = os.listdir(self.parent_folder)
        wakanats_folders = []

        # Store the Wakanats folders
        for i in parent_folder_items:
            if "WakaNats" in i:
                wakanats_folders.append(i)

        return wakanats_folders
        

    
    def get_target_year_files(self):
        year_path = self.parent_folder + "/WakaNats" + self.target_year
        year_files = os.listdir(year_path)
        
        if year_files:
            return year_files
        else:
            return f"{self.target_year} have no files inside"



    def find_lif_files(self,year_files):

        lif_files = []

        
        for i in year_files:
            if ".lif" in i:
                lif_files.append(i)
            else:
                continue
        
        # if there are lif files
        if lif_files:
            
            # if keyword specified
            if self.target_keyword:
                lif_files_with_keyword = []

                # find keyword on the lif files
                for i in lif_files:
                    if self.target_keyword in i:
                        lif_files_with_keyword.append(i)
                    else:
                        continue
                
                # if there are lif files with the keyword
                if lif_files_with_keyword:
                    return lif_files_with_keyword
                
                else:
                    return f"No LIF files match the specified keyword {self.target_keyword}"
            else:
                # if keyword is not specified then just return the lif files
                return lif_files
        else:
            # if no lif files are found
            return f"There are no lif files found in {self.target_year}"
    


    def read_n_categorize_file(self,lif_file):

        lif_teams = []


        with open(f'{self.parent_folder}/WakaNats{self.target_year}/{lif_file}', 'r') as file:
            lif_file_lines = file.readlines()

        # separate header
        header = lif_file_lines.pop(0)

        # remove the commas
        header_list_with_empty_items = header.split(",")

        # Filter out empty items using list comprehension
        cleaned_header = [item for item in header_list_with_empty_items if item]

        # check if inbalanced header
        if len(cleaned_header) != 6:
                return f"{lif_file} have an error on race information: {cleaned_header}."



        # separate body

        for line in lif_file_lines:
            
            # pass if there is DNS or DQ or Disqualified
            if "DQ" in line:
                continue
            if "DNS" in line:
                continue
            if "Disqualified" in line:
                continue

            # There are only 10 items on a body
            # remove the commas
            list_with_empty_items = line.split(",")

            # Filter out empty items using list comprehension
            cleaned_line = [item for item in list_with_empty_items if item]

            
            # check if inbalance line
            if len(cleaned_line) != 10:
                return f"{lif_file} have an issue with the team line: {line}."
            
            # categorize
            team_place = cleaned_line[0]
            team_name = cleaned_line[3]
            team_regional_association = cleaned_line[4]

            # check if valid
            if team_place.isdigit() == False:
                return f"{lif_file} have an issue with the team line: {line}."
            if team_name.isdigit() != False:
                return f"{lif_file} have an issue with the team line: {line}."
            if team_regional_association.isdigit() != False:
                return f"{lif_file} have an issue with the team line: {line}."
            
            


            lif_teams.append([team_place,team_name,team_regional_association])
        
        return lif_teams



    def get_all_scores(self,lif_files_contents_dir):
        
        regional_association_scores = {}

        for lif_file_name in lif_files_contents_dir:
            teams_list = lif_files_contents_dir[lif_file_name]

            for team in teams_list:
                team_place = team[0]
                team_name = team[1]
                team_regional_association = team[2]



                if int(team_place) == 1:
                    team_score = 8
                if int(team_place) == 2:
                    team_score = 7
                if int(team_place) == 3:
                    team_score = 6
                if int(team_place) == 4:
                    team_score = 5
                if int(team_place) == 5:
                    team_score = 4
                if int(team_place) == 6:
                    team_score = 3
                if int(team_place) == 7:
                    team_score = 2
                if int(team_place) > 7: # 8 and onwards
                    team_score = 1
                
                # print("team place", team_place, team_score, lif_file_name, team_name)

                # add to the dictionary
                if team_regional_association in regional_association_scores:
                    regional_association_scores[team_regional_association] += team_score
                else:
                    regional_association_scores[team_regional_association]  = team_score
        
        return regional_association_scores
                

    def sort_descending(self,regional_association_results):
        regional_association_results = dict(sorted(regional_association_results.items(), key=lambda item: item[1], reverse=True))
        return regional_association_results



class gui_component():
    def __init__(self):   
        self.root = ct.CTk() # opens the customtkinter library
        self.root.geometry("700x600") # widthxheight
        

        # constants
        SCALE_CONSTANT = 2 # 1.5 is a suitable # scale constant for scaling the widget and the window
        FONT_BASE_CONSTANT = 20 / SCALE_CONSTANT # also increases the fonts size relative to the scale constant
        self.POINTS_REFFERENCE = {
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


        # fonts
        self.title_font = ct.CTkFont(size=int(FONT_BASE_CONSTANT * SCALE_CONSTANT),weight="bold") # Creates a bold and big font for the title

        # window scaling
        ct.set_window_scaling(SCALE_CONSTANT * 0.4)  # Increase the widget size by scale constant
        ct.set_widget_scaling(SCALE_CONSTANT * 0.9)  # Increase window size by scale constant

        # theme
        ct.set_appearance_mode("dark") # makes the UI light mode. There is dark,system,light.
        ct.set_default_color_theme("dark-blue") # changes the theme. There is "blue" (standard), "green", "dark-blue"


        # maximize root
        self.root.rowconfigure(0,weight=1) # maximize the root window to only 1 row
        self.root.columnconfigure(0,weight=1) # maximize the root window to only 1 column
        
        # Homepage variables
        # -- data processing # Creating variables to be used in the program # do not change
        self.processed_year_files = "" # variable if for all the year files count
        self.processed_year_filtered_files = "" # variable for all the final processed year files count
        self.current_loading_file = "" # current file being processed
        self.parent_path = "" # for the folder path

        # program functions instance
        self.program_functions  = program_functions_component()

        # starts homepage
        self.home() # starts the homepage function

    
    def home(self):
        self.remove_current_screen()

        # homepage frame
        homepage_frame = ct.CTkFrame(self.root) # creates the homepage frame
        homepage_frame.grid(row=0,column=0,sticky="NSEW") # displays the homepage frame to the maximizes root window specified earlier

        # setup homepage frame 2
        homepage_frame.rowconfigure(0,weight=0) # title size == left+right panel size
        # -- title
        homepage_frame.rowconfigure(1,weight=3) # title size == left+right panel size
        # -- left and right panel
        homepage_frame.rowconfigure(2,weight=2) # title size == left+right panel size

        # -- maximizes the col 
        homepage_frame.columnconfigure(0,weight=1) # removes the homepage columns


        # title 
        title_label = ct.CTkLabel(homepage_frame,text="Waka Ama Race Ranking System",font=self.title_font) # Creates the title with its text
        title_label.grid(row=1,column=0,sticky="nsew") # maximize the display on the its row with using sticky arguement and value "north south east west" 
        
        # inner frame
        inner_frame = ct.CTkFrame(homepage_frame) # Creates the inner frame for the input boxes, etc.
        inner_frame.grid(row=2,column=0,sticky="nsew") # maximizes it again

        # configure the inner frame: 3 rows, 2 columns
        inner_frame.rowconfigure(0,weight=1) # all equal
        inner_frame.rowconfigure(1,weight=1) # all equal
        inner_frame.rowconfigure(2,weight=1) # all equal


        inner_frame.columnconfigure(0,weight=1) # column equal
        
        
        

        # To Open and Select a Folder
        self.parent_folder_button = ct.CTkButton(inner_frame,text="Pick a folder",command=self.pick_folder) # Creates a button to open folder
        self.parent_folder_button.grid(row=0,column=0) # displays the open folder
        

        # To input the file's keyword
        self.keyword_input = ct.CTkEntry(inner_frame,placeholder_text="Type keyword file") # Creates an input box for the keyword
        self.keyword_input.grid(row=1,column=0) # displays the keyword input box
        self.processed_keyword = self.keyword_input.get()

        # To input the year
        self.year_input = ct.CTkEntry(inner_frame,placeholder_text="Type the year") # Creates the year input box
        self.year_input.grid(row=2,column=0) # displays the year input box
        self.processed_year = self.year_input.get()

        # save to csv
        self.save_to_csv_var = tk.BooleanVar(value=True)
        self.save_to_csv_switch = ct.CTkSwitch(inner_frame,text="Save to CSV",variable=self.save_to_csv_var) # Creates save to CSV switch
        self.save_to_csv_switch.grid(row=3,column=0) # displays save to csv switch

        # proceed
        proceed_button = ct.CTkButton(inner_frame,text="Enter",command=self.loading_screen) # Creates the proceed button
        proceed_button.grid(row=4,column=0) #displays the proceed button


    def loading_screen(self):
        
        self.remove_current_screen()

        # create the frame
        loading_frame = ct.CTkFrame(self.root) # creates the loading frame
        loading_frame.grid() # Displays the loading frame

        # create the title
        loading_title_label = ct.CTkLabel(loading_frame, text=f"Initializing {self.year_input.get()} {self.keyword_input.get()}") # creates the loading title
        loading_title_label.grid() # displays the loading title message

        # create the current file loading
        self.loading_file_label = ct.CTkLabel(loading_frame, text=f"Analyzing {self.current_loading_file}") # creates the loading text message
        self.loading_file_label.grid() # displays the loading text message

        # add the loading 
        self.loading_progressbar = ct.CTkProgressBar(loading_frame) # sets up the loading bar
        self.loading_progressbar.grid() # shows the loading bar
        self.loading_progressbar.start() # begins the loading bar animation
        
        # loading process
        self.loading_process() # initiates the loading process

    def error(self,title,message):
        messagebox.showerror(title=title,message=message)

    def success(self,title,message):
        messagebox.showinfo(title=title,message=message)
    
    
    def loading_process(self):
        def process_file(index):
            if index < len(lif_files_from_year):
                lif_file_name = lif_files_from_year[index]
                self.current_loading_file = lif_file_name
                self.loading_file_label.configure(text=f"Processing {lif_file_name}")
                lif_file_teams = self.program_functions.read_n_categorize_file(lif_file_name)
                if isinstance(lif_file_teams, list):
                    lif_files_contents_dir[lif_file_name] = lif_file_teams
                else:
                    # print(lif_file_teams)
                    self.error("Oops, Error has been found!", lif_file_teams)
                # Schedule the next file processing after 7 seconds
                self.root.after(7, process_file, index + 1)
            else:
               # All files have been processed; move on to the next steps
                regional_associations_results = self.program_functions.get_all_scores(lif_files_contents_dir)
                regional_associations_results = self.program_functions.sort_descending(regional_associations_results)
                # print(regional_associations_results)
                self.success("Program Successfully Operated", message="All Regional Associations successfully scored")


                # processing completed
                self.loading_progressbar.stop() # halts the animation
                
                if self.save_to_csv_switch.get() == 1:
                    
                    csv_path = csv_export.export(regional_associations_results)

                    if  csv_path != False:
                        # print("Successful")
                        self.success("Saved successfully",message=f"CSV saved to {csv_path}")
                    else:
                        # print("Save to CSV error")
                        self.error("Save to CSV",message="Cannot save to CSV")
                    

                self.home()
        

        self.program_functions.target_year = self.year_input.get()
        self.program_functions.parent_folder = self.parent_path
        self.program_functions.target_keyword = self.keyword_input.get()

        if self.program_functions.check_inputs_is_valid() == True:
            target_year_files = self.program_functions.get_target_year_files()
            if isinstance(target_year_files, list):
                lif_files_from_year = self.program_functions.find_lif_files(target_year_files)
                if isinstance(lif_files_from_year, list):
                    lif_files_contents_dir = {}

                    # Begin handling the first file
                    process_file(0)


                else:
                    # print(lif_files_from_year)
                    self.error(title="lif files",message=lif_files_from_year)
                    self.home()
            else:
                # print(target_year_files)
                self.error(title="year files", message=target_year_files)
                self.home()
        else:
            # print(self.program_functions.check_inputs_is_valid())
            self.error(title="You must put a valid input", message=self.program_functions.check_inputs_is_valid())
            self.home()


    def pick_folder(self):
        folder_path = filedialog.askdirectory()  # Open a folder selection dialog
        if folder_path: # checks if folder exists
                self.parent_path = folder_path
        else: # if folder is not found
            self.error("Error", message="You must select a folder") # display an error dialog. Folder error and the message "Cannot open folder"
    
    def remove_current_screen(self): # defines a function for removing the current screen
        
        # removes the existing frame
        if self.root.winfo_children():  # checks if there are any widgets on the screen
            for widget in self.root.winfo_children(): # iterates over each widget
                if isinstance(widget, ct.CTkFrame): # targets only the frames
                    widget.grid_remove() # hides the frame

    def run(self):
        self.root.mainloop() # show the entire graphical user interface
    
# launch the application
gui = gui_component() # initializes the GUI component
gui.run() # invokes the display method