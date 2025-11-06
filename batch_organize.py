import json
import os
import shutil
import sys

def organize_prompts(batch_num, batch_size=100):
    """
    Reads the analysis_results.json file and moves a specific batch of accepted prompts.
    """
    with open('analysis_results.json', 'r') as f:
        analysis = json.load(f)

    prompts = analysis['prompts']
    start_index = batch_num * batch_size
    end_index = start_index + batch_size

    # Slice the prompts list to process only the current batch
    prompts_to_process = prompts[start_index:end_index]

    for prompt in prompts_to_process:
        old_filename = prompt['filepath'].split('/')[-1]
        old_filepath = os.path.join('gpts', old_filename)
        domain = prompt['domain']
        new_filename = prompt['new_filename']
        new_filepath = os.path.join(domain, new_filename)

        try:
            shutil.copy(old_filepath, new_filepath)
        except FileNotFoundError:
            print(f"File not found: {old_filepath}")
        except Exception as e:
            print(f"Error moving file {old_filepath} to {new_filepath}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python batch_organize.py <batch_num>")
        sys.exit(1)

    batch = int(sys.argv[1])
    organize_prompts(batch)
