import csv

class csv_c:
    @staticmethod
    def csv_export(sorted_scores, filename):
        """Export the sorted scores to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Team', 'Score'])  # Header
            for team, score in sorted_scores:
                writer.writerow([team, score])
        print(f"Scores exported to {filename}")