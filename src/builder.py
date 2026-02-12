import genanki
import csv
import os
import glob
import zlib

class AnkiBuilder:
    def __init__(self, level="N5"):
        self.level = level.upper()
        self.deck_name = f"JLPT {self.level} 文法"
        # Generate a stable deck_id based on the name
        self.deck_id = zlib.adler32(self.deck_name.encode('utf-8'))
        
        self.css = self._load_file('src/templates/style.css')
        self.front_html = self._load_file('src/templates/front.html')
        self.back_html = self._load_file('src/templates/back.html')
        
        self.model = self._create_model()
        self.deck = genanki.Deck(self.deck_id, self.deck_name)

    def _load_file(self, path):
        # Handle path relative to the script execution or absolute
        if not os.path.exists(path):
            # Try finding it relative to this script if run from root
            if os.path.exists(os.path.join(os.getcwd(), path)):
                 return self._read_content(path)
            else:
                 print(f"Warning: File {path} not found.")
                 return ""
        return self._read_content(path)

    def _read_content(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def _create_model(self):
        # Use a consistent model ID for all levels so they share the same Note Type in Anki
        # This allows you to update the styling for all levels at once in Anki
        model_id = 1607392319 
        return genanki.Model(
            model_id,
            'JLPT Grammar Model',
            fields=[
                {'name': 'Grammar'},
                {'name': 'Meaning'},
                {'name': 'Connection'},
                {'name': 'Simple_Example_JP'},
                {'name': 'Simple_Example_CN'},
                {'name': 'Hard_Example_JP'},
                {'name': 'Hard_Example_CN'},
                {'name': 'Similar_Grammar'},
                {'name': 'Difference'},
            ],
            templates=[{
                'name': 'Card 1',
                'qfmt': self.front_html,
                'afmt': self.back_html,
            }],
            css=self.css
        )

    def add_notes_from_csv(self, csv_path):
        print(f"Reading data from {csv_path}...")
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None) # Skip header
                if not header:
                    return

                count = 0
                for row in reader:
                    # Pad fields if necessary
                    while len(row) < 9:
                        row.append('')
                    
                    note = genanki.Note(
                        model=self.model,
                        fields=row[0:9]
                    )
                    self.deck.add_note(note)
                    count += 1
                print(f"Loaded {count} notes for {self.level}.")
        except Exception as e:
            print(f"Error reading CSV {csv_path}: {e}")

    def export_package(self, output_path):
        try:
            genanki.Package(self.deck).write_to_file(output_path)
            print(f"Successfully exported package to {output_path}")
        except Exception as e:
            print(f"Error exporting package: {e}")

if __name__ == "__main__":
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Find all n*_grammar.csv files in data/
    # This allows automatic generation for N5, N4, N3, etc. just by adding files.
    data_files = glob.glob(os.path.join('data', 'n*_grammar.csv'))
    
    if not data_files:
        print("No grammar data files found in data/ (looking for n*_grammar.csv)")
    
    for csv_path in data_files:
        filename = os.path.basename(csv_path)
        # Extract level from filename (e.g., "n5_grammar.csv" -> "N5")
        # Assuming format is {level}_grammar.csv
        parts = filename.split('_')
        if len(parts) > 0:
            level = parts[0].upper()
        else:
            level = "UNKNOWN"
        
        print(f"Processing {level} ({csv_path})...")
        builder = AnkiBuilder(level=level)
        builder.add_notes_from_csv(csv_path)
        
        output_file = os.path.join('output', f"{level}_Grammar.apkg")
        builder.export_package(output_file)
