import json
import os
import re

def is_english(text):
    """
    A simple check to see if the text is likely in English.
    This can be improved with more sophisticated language detection libraries if needed.
    """
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def has_clear_objective(text):
    """
    Checks for keywords that indicate a clear objective.
    """
    keywords = ['act as', 'your goal is to', 'i want you to', 'become my', 'your task is to']
    return any(keyword in text.lower() for keyword in keywords)

def is_long_enough(text):
    """
    Checks if the prompt is at least 50 words long.
    """
    return len(text.split()) >= 50

def is_well_structured(text):
    """
    Checks for some basic structural elements.
    """
    return '##' in text or '###' in text or '*' in text or '1.' in text

def classify_prompt(text):
    """
    Classifies the prompt into a domain based on keywords.
    """
    text = text.lower()
    if any(keyword in text for keyword in ['code', 'python', 'javascript', 'java', 'c++', 'html', 'css', 'debug', 'developer', 'software', 'script', 'bash']):
        return "Programming"
    if any(keyword in text for keyword in ['marketing', 'ad', 'seo', 'campaign', 'brand', 'social media', 'copywriting', 'sales']):
        return "Marketing"
    if any(keyword in text for keyword in ['academic', 'essay', 'research', 'paper', 'thesis', 'study', 'citation', 'university', 'college']):
        return "Academic"
    if any(keyword in text for keyword in ['job', 'resume', 'cv', 'interview', 'career', 'linkedin', 'cover letter']):
        return "Job-Hunting"
    if any(keyword in text for keyword in ['game', 'rpg', 'dungeon', 'adventure', 'character', 'quest']):
        return "Game"
    if any(keyword in text for keyword in ['creative', 'story', 'poem', 'novel', 'script', 'art', 'music', 'design']):
        return "Creative"
    if any(keyword in text for keyword in ['prompt', 'chatgpt', 'gpt-4', 'gpt-3', 'language model', 'ai']):
        return "Prompt-Engineering"
    if any(keyword in text for keyword in ['business', 'startup', 'entrepreneur', 'finance', 'investment', 'strategy', 'management']):
        return "Business"
    if any(keyword in text for keyword in ['productivity', 'lifestyle', 'health', 'fitness', 'diet', 'meditation', 'habit']):
        return "Productivity-Lifestyle"
    if any(keyword in text for keyword in ['jailbreak', 'unfiltered', 'unrestricted', 'dan', 'nsfw']):
        return "Jailbreaks"
    return "Creative" # Default to creative if no other domain is found

def analyze_prompts():
    """
    Analyzes all prompts in the gpts/ directory and updates the analysis_results.json file.
    """
    with open('analysis_results.json', 'r') as f:
        analysis = json.load(f)

    prompt_files = os.listdir('gpts')
    # Filter out files that have already been analyzed
    analyzed_files = [p['filepath'].split('/')[-1] for p in analysis['prompts']]
    prompt_files = [f for f in prompt_files if f not in analyzed_files and f.endswith('.md')]


    for filename in prompt_files:
        filepath = os.path.join('gpts', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                content = f.read()
            except Exception as e:
                print(f"Could not read file {filepath}: {e}")
                continue

        analysis['total_analyzed'] += 1

        # Apply quality criteria
        if (is_english(content) and
            has_clear_objective(content) and
            is_long_enough(content) and
            is_well_structured(content)):

            analysis['total_accepted'] += 1
            domain = classify_prompt(content)
            analysis['stats'][domain] += 1
            new_filename = f"{analysis['total_accepted']:03d}_{filename.replace('.md', '').replace(' ', '_')}.md"

            analysis['prompts'].append({
                "filepath": filepath,
                "domain": domain,
                "new_filename": new_filename
            })

    with open('analysis_results.json', 'w') as f:
        json.dump(analysis, f, indent=2)

if __name__ == '__main__':
    analyze_prompts()
