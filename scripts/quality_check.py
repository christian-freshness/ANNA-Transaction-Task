import argparse

import pandas as pd
from sklearn.metrics import classification_report


def extract_first_level(category):
    """Extracts the first level of a hierarchical category."""
    if pd.isna(category):
        return 'Unknown'
    return category.split('/')[0].strip()  # Extracts first level before '/'


def generate_classification_report(input_file, output_file):
    data = pd.read_csv(input_file)

    data['category_first_level'] = data['category'].apply(extract_first_level)
    data = data[(data['category_first_level'] != 'Unknown')]

    # Generating the classification report
    report = classification_report(
        data['category_first_level'],
        data['predicted_category']
    )

    with open(output_file, 'w') as f:
        f.write(report)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate classification report for first-level categories.')
    parser.add_argument('--input', required=True, help='Path to the input dataset (CSV file).')
    parser.add_argument('--output', required=True, help='Path to save the classification report (TXT file).')
    args = parser.parse_args()

    generate_classification_report(args.input, args.output)
