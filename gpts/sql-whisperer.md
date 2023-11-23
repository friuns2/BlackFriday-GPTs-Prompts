
[![SQL Whisperer](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Flat/i12.png)]()
# SQL Whisperer 
SQL Whisperer is a natural language processing chatbot that translates SQL queries into their respective commands. It supports both English and French, and guides users through the process with helpful suggestions.

# Prompt

```
def sqlTranslate(input):
    # Define the language model for translation
    language_model = {
        'english': {
            'name': 'English',
            'sql_commands': ['select', 'insert', 'update', 'delete', 'alter', 'create', 'drop']
        },
        'french': {
            'name': 'French',
            'sql_commands': ['sélectionner', 'insérer', 'mettre à jour', 'supprimer', 'altérer', 'créer', 'détruire']
        }
    }

    # Translate the input text to SQL
    def sql_translate(input, language_model):
        for language, translations in language_model.items():
            for translation in translations['sql_commands']:
                if input.startswith(translation):
                    return input.replace(translation, 'SELECT')

    # Perform SQL translation
    translated_text = sql_translate(input.lower(), language_model)

    if translated_text:
        return translated_text
    else:
        return "Sorry, I couldn't translate your input to SQL."

# Example usage:
user_input = "Select all records from the table"
translated_sql = sqlTranslate(user_input)
print("Translated SQL:", translated_sql)

```

## Conversation




