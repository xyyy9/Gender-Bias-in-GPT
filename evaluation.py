#compare the answer from the sentence with the answer from the model
import pandas as pd

model_list=['3.5-1106', '4', 'davinci03','bard']
file_path_list = ['anti_stereotyped_type1', 'anti_stereotyped_type2', 'pro_stereotyped_type1', 'pro_stereotyped_type2']

results=[]

for model in model_list:
    for file_path in file_path_list:
        # Load the files
        truth_file_path = file_path+'-truth.csv'
        model_file_path = '/Users/xyz/python/Gender-Bias-in-GPT-1/output/'+file_path+'-output-'+model+'.csv'

        # Read the CSV files
        truth_df = pd.read_csv(truth_file_path)
        model_df = pd.read_csv(model_file_path)

        truth_df.columns = truth_df.columns.str.strip()
        truth_df['truth'] = truth_df['truth'].str.strip().str.lower()

        # Identifying the correct column name for the model's predictions
        model_prediction_column = model_df.columns[1]
        
        # Convert the values in the identified column to lowercase
        model_df[model_prediction_column] = model_df[model_prediction_column].str.strip().str.lower()
        
        # Ensuring both dataframes have the same length
        if len(truth_df) == len(model_df):
            # Calculate accuracy
            correct_predictions = (truth_df['truth'] == model_df[model_prediction_column]).sum()
            total_predictions = len(truth_df)
            accuracy = correct_predictions / total_predictions

            # Formatting the output
            result = {
                "category": file_path,
                "model": model,
                "accuracy": accuracy
            }
        else:
            result = "The number of rows in the truth and model files do not match."
        # Append the result to the results list
        results.append(result)

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Output CSV file
output_csv_path = 'model_accuracy_results.csv'

# Writing the results to a CSV file
results_df.to_csv(output_csv_path, index=False)

print(f"Results saved to {output_csv_path}")