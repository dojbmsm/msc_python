import pandas as pd
import os


class TSVAnalyzer:
    def __init__(self, file_path):
        """Initializes the class and loads the TSV file."""
        self.file_path = file_path
        self.df = None
        self.load_data()

    def load_data(self):
        """Reads the TSV file into a pandas DataFrame."""
        if os.path.exists(self.file_path):
            # sep='\t' tells pandas to look for tabs
            self.df = pd.read_csv(self.file_path, sep='\t')
            print(f"--- Successfully loaded: {self.file_path} ---")
        else:
            print(f"Error: File '{self.file_path}' not found.")

    def print_stats(self):
        # To find number connections in social media between people are realistic or not by analyzing youtube and facebook connections between people.
        # Load the tsv file
        # yt = pd.read_csv('facebook.tsv', sep='\t')
        counts = self.df["FromNodeId"].value_counts().reset_index(name='con_count')
        avg_con = counts["con_count"].mean()
        min_con = counts["con_count"].min()
        max_con = counts["con_count"].max()
        sd_con = counts["con_count"].std()
        print(f"Stats for file: {self.file_path}")
        print(f"Average {avg_con}")
        print(f"Min {min_con}")
        print(f"Max {max_con}")
        print(f"Standard D {sd_con}")
# We can conclude that even though the mean number of conditions are a very acceptable 7.97 or 24 Max is 28000 odd which is a outlier. but generally 80 odd standard deviation is possible for a person to have connections
# git hub https://github.com/dojbmsm/msc_python
# --- Execution Block ---
def main():
    # Example 1: Analyzing a sales file
    youtube = TSVAnalyzer('youtube.tsv')
    youtube.print_stats()

    # Example 2: Analyzing a weather file
    facebook = TSVAnalyzer('facebook.tsv')
    facebook.print_stats()


if __name__ == "__main__":
    main()