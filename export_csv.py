import csv

class csv_c():
    def init(self):
        pass

    @staticmethod
    def csv_export(files_regional_association_score_list, csv_filename):
        # return True if successful and False if not
            # CSV file name


        with open(csv_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Place", "Regional Association", "points"])
            for i, (Regional_Association, points) in enumerate(files_regional_association_score_list(), 1):
                writer.writerow([i, Regional_Association, points])
        return True