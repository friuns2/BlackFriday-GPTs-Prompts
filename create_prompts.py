import json
import os
import shutil

def create_prompt_files():
    with open('analysis_results.json', 'r') as f:
        data = json.load(f)

    for prompt in data['prompts']:
        original_filepath = prompt['filepath']
        domain = prompt['domain']
        new_filename = prompt['new_filename']

        new_directory = domain
        new_filepath = os.path.join(new_directory, new_filename)

        try:
            shutil.copyfile(original_filepath, new_filepath)
            print(f"Successfully copied {original_filepath} to {new_filepath}")
        except FileNotFoundError:
            print(f"Error: {original_filepath} not found. Skipping.")
        except Exception as e:
            print(f"An error occurred while copying {original_filepath}: {e}")

if __name__ == "__main__":
    create_prompt_files()
