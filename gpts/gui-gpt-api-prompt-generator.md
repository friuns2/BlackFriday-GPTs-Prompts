

# GUI GPT API prompt generator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22fp7U3k9Z3BnbzvqLt1tBC%22%2C%22flow%22%3Atrue%7D%7D)
A GUI GPT-3/4 API prompt generator written in Python. Can be used to create for prompt engineering to create more advanced prompts in a visual way and fetch results directly in the interface.

# Prompt

```
You are an experienced python developer. Your task is to develop a visual (GUI) desktop prompt editor with the following features:

Selection of a role for ChatGPT to use from a list of most popular roles (e.g. Lawyer, Software Developer, Marketing Specialist, etc.).

A slider to regulate Top P of the model

A slider to regulate Temperature of the model

A checkbox to include markdown (results in prompt addendum that requests to include headings, formatting, etc.)

A checkbox to include questions from the model (results in prompt addendum that requests to include the text "If you have any clarifying questions about the task, ask now before answering")

A text field to input the base prompt

A button to generate the resulting prompt

A text field that is editable and displays the resulting prompt (separate from the chat)

A widget to select a GPT model from a list of all available models

A button to call the selected GPT API to fetch the answer to the prompt from field 8.

A chat log to display the result of queries, with new queries getting added to the bottom like in ChatGPT.


The Right panel containing the chat should take 80% width and the left panel with the prompts and buttons should be 20% width.

The chat should support text with markup.

Develop python code for the requested program.
```

## Welcome Message
Sure, here is an example Python code to develop a visual desktop prompt editor with the requested features using the PyQt5 GUI framework:



```python

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QCheckBox, QSlider

from PyQt5.QtCore import Qt



class PromptEditor(QMainWindow):



    def __init__(self):

        super().__init__()

        self.setWindowTitle("ChatGPT Prompt Editor")

        self.setFixedSize(800, 600)



        # Create the left panel widget for prompts and buttons

        left_panel = QWidget(self)

        left_panel.setMinimumWidth(160)



        vbox = QVBoxLayout()



        # Create a dropdown list for role selection

        role_label = QLabel("Select a role:")

        self.role_combo = QComboBox()

        self.role_combo.addItems(["Lawyer", "Software Developer", "Marketing Specialist"])

        vbox.addWidget(role_label)

        vbox.addWidget(self.role_combo)



        # Create a slider for Top P regulation

        top_p_label = QLabel("Top P:")

        self.top_p_slider = QSlider(Qt.Horizontal)

        self.top_p_slider.setMinimum(0)

        self.top_p_slider.setMaximum(100)

        self.top_p_slider.setValue(50)

        vbox.addWidget(top_p_label)

        vbox.addWidget(self.top_p_slider)



        # Create a slider for Temperature regulation

        temp_label = QLabel("Temperature:")

        self.temp_slider = QSlider(Qt.Horizontal)

        self.temp_slider.setMinimum(1)

        self.temp_slider.setMaximum(100)

        self.temp_slider.setValue(50)

        vbox.addWidget(temp_label)

        vbox.addWidget(self.temp_slider)



        # Create a checkbox for markdown

        self.markdown_checkbox = QCheckBox("Include Markdown")

        vbox.addWidget(self.markdown_checkbox)



        # Create a checkbox for questions

        self.questions_checkbox = QCheckBox("Include Questions")

        vbox.addWidget(self.questions_checkbox)



        # Create a text field for inputting the base prompt

        prompt_label = QLabel("Enter your base prompt:")

        self.prompt_textedit = QTextEdit()

        vbox.addWidget(prompt_label)

        vbox.addWidget(self.prompt_textedit)



        # Create a button for generating the resulting prompt

        self.generate_button = QPushButton("Generate Prompt")

        vbox.addWidget(self.generate_button)



        # Create an editable text field to display the resulting prompt

        result_label = QLabel("Resulting Prompt:")

        self.result_textedit = QTextEdit()

        self.result_textedit.setReadOnly(False)

        vbox.addWidget(result_label)

        vbox.addWidget(self.result_textedit)



        # Create a dropdown list to select GPT model

        model_label = QLabel("Select GPT Model:")

        self.model_combo = QComboBox()

        self.model_combo.addItems(["GPT-3", "GPT-Neo"])

        vbox.addWidget(model_label)

        vbox.addWidget(self.model_combo)



        # Create a button for fetching answer from selected GPT API

        self.api_button = QPushButton("Get Answer")

        vbox.addWidget(self.api_button)



        left_panel.setLayout(vbox)



        # Create the right panel widget for chat logs

        right_panel = QWidget(self)

        right_panel.setMinimumWidth(640)



        self.chat_textedit = QTextEdit()

        self.chat_textedit.setReadOnly(True)



        vbox = QVBoxLayout()

        vbox.addWidget(self.chat_textedit)



        right_panel.setLayout(vbox)



        # Set the widths of the panels using a grid layout manager

        grid = QGridLayout()

        grid.setColumnStretch(0, 20)

        grid.setColumnStretch(1, 80)

        grid.addWidget(left_panel, 0, 0)

        grid.addWidget(right_panel, 0, 1)



        main_widget = QWidget()

        main_widget.setLayout(grid)

        self.setCentralWidget(main_widget)



        # Connect the generate button to create resulting prompt

        self.generate_button.clicked.connect(self.create_prompt)



        # Connect the API button to fetch answer from selected GPT API

        self.api_button.clicked.connect(self.fetch_answer)



    # Function to create the resulting prompt based on user inputs

    def create_prompt(self):

        role = self.role_combo.currentText()

        top_p = float(self.top_p_slider.value()) / 100

        temperature = float(self.temp_slider.value()) / 100

        markdown = self.markdown_checkbox.isChecked()

        questions = self.questions_checkbox.isChecked()

        base_prompt = self.prompt_textedit.toPlainText()



        # Add markdown and questions if checkboxes are checked

        prompt = base_prompt

        if markdown:

            prompt += "\n\nPlease include headings, formatting, etc. in your answer."

        if questions:

            prompt += "\n\nIf you have any clarifying questions about the task, ask now before answering."



        # Set the resulting prompt in the editable text field

        self.result_textedit.setPlainText(prompt)



    # Function to fetch answer from selected GPT API

    def fetch

## Conversation

**ASSISTANT**: Sure, here is an example Python code to develop a visual desktop prompt editor with the requested features using the PyQt5 GUI framework:



```python

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QCheckBox, QSlider

from PyQt5.QtCore import Qt



class PromptEditor(QMainWindow):



    def __init__(self):

        super().__init__()

        self.setWindowTitle("ChatGPT Prompt Editor")

        self.setFixedSize(800, 600)



        # Create the left panel widget for prompts and buttons

        left_panel = QWidget(self)

        left_panel.setMinimumWidth(160)



        vbox = QVBoxLayout()



        # Create a dropdown list for role selection

        role_label = QLabel("Select a role:")

        self.role_combo = QComboBox()

        self.role_combo.addItems(["Lawyer", "Software Developer", "Marketing Specialist"])

        vbox.addWidget(role_label)

        vbox.addWidget(self.role_combo)



        # Create a slider for Top P regulation

        top_p_label = QLabel("Top P:")

        self.top_p_slider = QSlider(Qt.Horizontal)

        self.top_p_slider.setMinimum(0)

        self.top_p_slider.setMaximum(100)

        self.top_p_slider.setValue(50)

        vbox.addWidget(top_p_label)

        vbox.addWidget(self.top_p_slider)



        # Create a slider for Temperature regulation

        temp_label = QLabel("Temperature:")

        self.temp_slider = QSlider(Qt.Horizontal)

        self.temp_slider.setMinimum(1)

        self.temp_slider.setMaximum(100)

        self.temp_slider.setValue(50)

        vbox.addWidget(temp_label)

        vbox.addWidget(self.temp_slider)



        # Create a checkbox for markdown

        self.markdown_checkbox = QCheckBox("Include Markdown")

        vbox.addWidget(self.markdown_checkbox)



        # Create a checkbox for questions

        self.questions_checkbox = QCheckBox("Include Questions")

        vbox.addWidget(self.questions_checkbox)



        # Create a text field for inputting the base prompt

        prompt_label = QLabel("Enter your base prompt:")

        self.prompt_textedit = QTextEdit()

        vbox.addWidget(prompt_label)

        vbox.addWidget(self.prompt_textedit)



        # Create a button for generating the resulting prompt

        self.generate_button = QPushButton("Generate Prompt")

        vbox.addWidget(self.generate_button)



        # Create an editable text field to display the resulting prompt

        result_label = QLabel("Resulting Prompt:")

        self.result_textedit = QTextEdit()

        self.result_textedit.setReadOnly(False)

        vbox.addWidget(result_label)

        vbox.addWidget(self.result_textedit)



        # Create a dropdown list to select GPT model

        model_label = QLabel("Select GPT Model:")

        self.model_combo = QComboBox()

        self.model_combo.addItems(["GPT-3", "GPT-Neo"])

        vbox.addWidget(model_label)

        vbox.addWidget(self.model_combo)



        # Create a button for fetching answer from selected GPT API

        self.api_button = QPushButton("Get Answer")

        vbox.addWidget(self.api_button)



        left_panel.setLayout(vbox)



        # Create the right panel widget for chat logs

        right_panel = QWidget(self)

        right_panel.setMinimumWidth(640)



        self.chat_textedit = QTextEdit()

        self.chat_textedit.setReadOnly(True)



        vbox = QVBoxLayout()

        vbox.addWidget(self.chat_textedit)



        right_panel.setLayout(vbox)



        # Set the widths of the panels using a grid layout manager

        grid = QGridLayout()

        grid.setColumnStretch(0, 20)

        grid.setColumnStretch(1, 80)

        grid.addWidget(left_panel, 0, 0)

        grid.addWidget(right_panel, 0, 1)



        main_widget = QWidget()

        main_widget.setLayout(grid)

        self.setCentralWidget(main_widget)



        # Connect the generate button to create resulting prompt

        self.generate_button.clicked.connect(self.create_prompt)



        # Connect the API button to fetch answer from selected GPT API

        self.api_button.clicked.connect(self.fetch_answer)



    # Function to create the resulting prompt based on user inputs

    def create_prompt(self):

        role = self.role_combo.currentText()

        top_p = float(self.top_p_slider.value()) / 100

        temperature = float(self.temp_slider.value()) / 100

        markdown = self.markdown_checkbox.isChecked()

        questions = self.questions_checkbox.isChecked()

        base_prompt = self.prompt_textedit.toPlainText()



        # Add markdown and questions if checkboxes are checked

        prompt = base_prompt

        if markdown:

            prompt += "\n\nPlease include headings, formatting, etc. in your answer."

        if questions:

            prompt += "\n\nIf you have any clarifying questions about the task, ask now before answering."



        # Set the resulting prompt in the editable text field

        self.result_textedit.setPlainText(prompt)



    # Function to fetch answer from selected GPT API

    def fetch
**USER**: continue
**ASSISTANT**:     _answer(self):

        model = self.model_combo.currentText()

        prompt = self.result_textedit.toPlainText()



        # Call the selected GPT API to fetch the answer

        # Here, we would use the appropriate library or package to interact with the API

        # We will just print a dummy message for demonstration purposes

        answer = f"Fetching answer from {model} API for prompt: '{prompt}'..."

        self.chat_textedit.append(answer)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    editor = PromptEditor()

    editor.show()

    sys.exit(app.exec_())

```



This code creates a `QMainWindow` with two panels - the left panel for prompts and buttons and the right panel for chat logs. The left panel contains various widgets such as dropdown lists, sliders, text fields, and buttons that allow users to select various options and input their base prompt. The `create_prompt()` function generates the resulting prompt based on user inputs, which is displayed in the editable text field. The `fetch_answer()` function fetches the answer from the selected GPT API and displays it in the chat log.



Note that the implementation of the `fetch_answer()` function depends on the specific GPT API being used, and here we have used a dummy message for demonstration purposes.

