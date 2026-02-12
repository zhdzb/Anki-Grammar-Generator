import csv
import sys

def validate_csv(file_path):
    print(f"Validating {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            expected_fields = len(header)
            print(f"Header fields ({expected_fields}): {header}")
            
            error_count = 0
            row_num = 1
            for row in reader:
                row_num += 1
                if len(row) != expected_fields:
                    print(f"Error at line {row_num}: Expected {expected_fields} fields, got {len(row)}")
                    error_count += 1
            
            if error_count == 0:
                print("Validation SUCCESS: All rows have consistent field counts.")
                print("Encoding is valid UTF-8.")
                return True
            else:
                print(f"Validation FAILED: Found {error_count} errors.")
                return False
                
    except UnicodeDecodeError:
        print("Validation FAILED: File is not valid UTF-8.")
        return False
    except Exception as e:
        print(f"Validation FAILED: {str(e)}")
        return False

if __name__ == "__main__":
    validate_csv(r"c:\Users\MB\Desktop\anki\japanese_grammar.csv")
