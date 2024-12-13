import pandas as pd
from sklearn.metrics import classification_report


def quality_check(input_csv_path, output_report_path):
    """
    This function takes a dataset path and an output path,
    reads the data, generates a classification report for the 'category'
    and 'predicted_category' columns, and saves it to the output file.

    :param input_csv_path: Path to the input CSV dataset
    :param output_report_path: Path to save the classification report (.txt)
    """
    data = pd.read_csv(input_csv_path)
    required_columns = {'category', 'predicted_category'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Dataset must contain the following columns: {required_columns}")

    # Computing the classification report
    report = classification_report(
        data['category'],
        data['predicted_category'],
        zero_division=0
    )

    # Saving the report to a file
    with open(output_report_path, 'w') as file:
        file.write(report)

    print(f"Classification report saved to {output_report_path}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate classification report.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input dataset (CSV file)')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output report (.txt)')
    args = parser.parse_args()

    quality_check(args.input, args.output)
