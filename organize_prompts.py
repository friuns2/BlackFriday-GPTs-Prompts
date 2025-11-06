import json
import os
import shutil

def organize_prompts():
    """
    Reads the analysis_results.json file and moves the accepted prompts
    to their new locations in batches.
    """
    with open('analysis_results.json', 'r') as f:
        analysis = json.load(f)

    batch_size = 200
    prompts = analysis['prompts']

    for i in range(0, len(prompts), batch_size):
        batch = prompts[i:i + batch_size]

        for prompt in batch:
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
    organize_prompts()
