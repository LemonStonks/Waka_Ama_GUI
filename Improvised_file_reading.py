import os

class file_reading_component:
    @staticmethod
    def return_years(parent_directory):
        return [f for f in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, f)) and f.startswith("WakaNats")]

    @staticmethod
    def find_year_path(parent_directory, year, prefix):
        year_folder = f"{prefix}{year}"
        full_path = os.path.join(parent_directory, year_folder)
        return full_path if os.path.exists(full_path) else None

    @staticmethod
    def return_files(year_path):
        return [f for f in os.listdir(year_path) if os.path.isfile(os.path.join(year_path, f))]

    @staticmethod
    def return_content(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def format_content(content, file_name):
        # Implement your content formatting logic here
        # For now, just return the content as is
        return content