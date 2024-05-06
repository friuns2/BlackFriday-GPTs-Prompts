

# Writting VBA code to successfully create a powerpoint presentation | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22Vqs4zC1NXE-QwEKUMPsvH%22%2C%22flow%22%3Atrue%7D%7D)
With this prompt, VBA code will be generated to create a PowerPoint presentation on the topic of 'artificial intelligence in education'.



To execute this code, you must enter PowerPoint, enter the Developer tab, press Visual Basic, Insert/Module. Paste the code and run it.

# Prompt

```
You are a programmer and you need to make a PowerPoint presentation. You must do it using the VBA programming language. Write a simple, but functional VBA code for Microsoft Visual Basic version 7.1, to successfully create a 6 slide powerpoint presentation.  Use your own knowledge on the topic "artificial intelligence in education", to broadly develop the content in paragraphs, and add it to each slide. You have to use Conditional structure "case". Each slide must have a title and the paragraph of content. You have to use the Shapes.AddTextbox method to create a new text box on each slide, then add the content to this newly created text box using Slide.Shapes(2).TextFrame.TextRange.Text. Do not include images. Do not use placeholders. Do not use bullet points. Do not use Shapes.Title.TextFrame.TextRange.Text. Do not save the presentation. Don't close PowerPoint. At the end, add the following comment at the code "To execute this code you must enter PowerPoint, enter the Developer tab, press Visual Basic, Insert / Module. Paste the code and run it".
```

## Welcome Message
Here's a simple VBA code that creates a 6-slide PowerPoint presentation on the topic of "Artificial Intelligence in Education" using the Shapes.AddTextbox method to add content to each slide.



```

Sub AIinEducationPresentation()



Dim ppt As Object

Set ppt = CreateObject("PowerPoint.Application")

ppt.Visible = True



Dim pres As Object

Set pres = ppt.Presentations.Add(msoTrue)



Dim slide As Object

Dim shp As Object



For i = 1 To 6

    Set slide = pres.Slides.Add(i, ppLayoutBlank)

    

    Select Case i

        Case 1

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "Introduction"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "Artificial Intelligence is transforming education by providing personalized learning experiences to students."

        Case 2

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI in Curriculum Development"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI can assist in designing curriculums and assessments that align with each student’s individual needs, interests, and abilities."

        Case 3

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI in Teaching"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI can help teachers by automating administrative tasks, grading papers and providing personalized feedback to students."

        Case 4

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI in Student Engagement"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI offers interactive tools and games that can make learning fun and engaging for students."

        Case 5

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI Challenges"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI still faces significant challenges such as data bias, lack of transparency and ethical issues."

        Case 6

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "Conclusion"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "The use of AI in education is still in its early stages, but it has the potential to revolutionize teaching and learning by providing personalized experiences to every student."

    End Select

    

Next i



End Sub



' To execute this code you must enter PowerPoint, enter the Developer tab, press Visual Basic, Insert / Module. Paste the code and run it.

## Conversation

**ASSISTANT**: Here's a simple VBA code that creates a 6-slide PowerPoint presentation on the topic of "Artificial Intelligence in Education" using the Shapes.AddTextbox method to add content to each slide.



```

Sub AIinEducationPresentation()



Dim ppt As Object

Set ppt = CreateObject("PowerPoint.Application")

ppt.Visible = True



Dim pres As Object

Set pres = ppt.Presentations.Add(msoTrue)



Dim slide As Object

Dim shp As Object



For i = 1 To 6

    Set slide = pres.Slides.Add(i, ppLayoutBlank)

    

    Select Case i

        Case 1

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "Introduction"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "Artificial Intelligence is transforming education by providing personalized learning experiences to students."

        Case 2

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI in Curriculum Development"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI can assist in designing curriculums and assessments that align with each student’s individual needs, interests, and abilities."

        Case 3

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI in Teaching"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI can help teachers by automating administrative tasks, grading papers and providing personalized feedback to students."

        Case 4

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI in Student Engagement"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI offers interactive tools and games that can make learning fun and engaging for students."

        Case 5

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "AI Challenges"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "AI still faces significant challenges such as data bias, lack of transparency and ethical issues."

        Case 6

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 50, 500, 50).TextFrame.TextRange.Text = "Conclusion"

            slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 100, 500, 300).TextFrame.TextRange.Text = "The use of AI in education is still in its early stages, but it has the potential to revolutionize teaching and learning by providing personalized experiences to every student."

    End Select

    

Next i



End Sub



' To execute this code you must enter PowerPoint, enter the Developer tab, press Visual Basic, Insert / Module. Paste the code and run it.
**USER**: Excellent answer. The code is functional and makes all taht i nedd it.
**ASSISTANT**: I'm glad to hear that! Feel free to let me know if you have any other questions or need further assistance.

