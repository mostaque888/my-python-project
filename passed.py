import sys

import csv
import argparse
import sys

# Function to calculate total marks
def calculate_total(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to assign grade based on average
def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Main function to process student data
def process_students(input_file, output_file):
    processed_data = []

    try:
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    marks = [
                        int(row['Math']),
                        int(row['Physics']),
                        int(row['Chemistry']),
                        int(row['Biology']),
                        int(row['Computing science'])
                    ]
                except ValueError:
                    print(f"❌ Invalid marks found for student ID {row['ID']}. Skipping.")
                    continue

                total = calculate_total(marks)
                average = calculate_average(marks)
                grade = assign_grade(average)

                row['Total'] = total
                row['Average'] = round(average, 2)
                row['Grade'] = grade
                processed_data.append(row)

    except FileNotFoundError:
        print(f"❌ Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error processing file: {e}")
        sys.exit(1)

    if processed_data:
        fieldnames = list(processed_data[0].keys())
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed_data)

        print(f" Processed data saved to '{output_file}'")
        print(f" Total students processed: {len(processed_data)}")
    else:
        print(" No valid data found to process.")

# Entry point
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process student marks and generate grade report.')
    parser.add_argument('input_file', help='Path to the input CSV file containing student data.')
    parser.add_argument('output_file', help='Path to the output CSV file for results.')

    args = parser.parse_args()
    process_students(args.input_file, args.output_file)
