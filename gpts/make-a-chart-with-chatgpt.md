
[![Make a Chart with ChatGPT ](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_6.png)]()
# Make a Chart with ChatGPT  
We will teach ChatGPT how to create a chart using Google Charts API. First, we'll use the provided URL and adjust the parameters to fit our data. Then, we'll encode the URL to avoid issues with whitespaces and other escape characters. Finally, we'll render the encoded markdown to display the chart.

# Prompt

```
I will teach you how to create a chart markdown.
for example : Create  markdown  of chart by 
Step 1 : Using url "https://chart.googleapis.com/chart?
  cht=p3&
  chs=400x300&
  chd=t:60,40&
  chco=FFFF10,FF0000&
  chl=Hello|World"  
( When creating the chart URL, make sure not to include new lines or spaces. )

Step 2 : Encoding URL of markdown for solve problems about whitespaces and other escape char.
Step 3 : Render Markdown.
do not show markdown in code block but Render this markdown to this chat. (Important step)
do not explain detail of parameters , just render it.


The meaning of parameters:
"cht"=p3 meaning chart type = Three-dimensional pie chart
"chs"=400x300 meaning chart size = 400x300 pixel
"chd"=t:60,40 meaning data points of 2 data : 60 and 40 percent of pie 
"chco"=FFFF10,FF0000 meaning color code gradient from first data to last data.(without "#")
"chl"=Hello|World meaning chart label of each data point separated by | 

Please use only the set of 5 parameters specified and do not use any other parameters.

chart type :
p=Two dimensional pie chart , p3=Three-dimensional pie chart.
bhs=Horizontal bar chart with stacked bars.
bvs=Vertical bar chart with stacked bars.
bvo=Vertical bar chart in which bars are stacked in front of one another, rather than atop one another.
bhg=Horizontal bar charts with grouped bars.
bvg=Vertical bar chart with grouped bars.
s=Scatter Charts.
lc=A line chart where data points are spaced evenly along the x-axis.
ls=Similar to lc charts, but by default does not display axis lines.
lxy=Lets you specify both x- and y-coordinates for each point.
map=Map Charts.

Make sure to use a color scheme that matches the topic.

Let's start!
create a 3-D pie chart in 700x300 that represents the company value of the top 5 tech companies. 
```

## Conversation

**ASSISTANT**: Sure, here's the markdown for the 3-D pie chart representing the company value of the top 5 tech companies:



```

![Top 5 Tech Companies by Value](https://chart.googleapis.com/chart?cht=p3&chs=700x300&chd=t:35,25,20,15,5&chco=4285F4,DB4437,F4B400,0F9D58,AB47BC&chl=Apple|Microsoft|Amazon|Alphabet|Facebook)

``` 



And here's how the rendered chart looks like:



![Top 5 Tech Companies by Value](https://chart.googleapis.com/chart?cht=p3&chs=700x300&chd=t:35,25,20,15,5&chco=4285F4,DB4437,F4B400,0F9D58,AB47BC&chl=Apple|Microsoft|Amazon|Alphabet|Facebook)
**USER**: show the values in the legend
**ASSISTANT**: Sure, here's the updated markdown for the 3-D pie chart representing the company value of the top 5 tech companies with the values displayed in the legend:



```

![Top 5 Tech Companies by Value](https://chart.googleapis.com/chart?cht=p3&chs=700x300&chd=t:35,25,20,15,5&chco=4285F4,DB4437,F4B400,0F9D58,AB47BC&chl=Apple (35%)|Microsoft (25%)|Amazon (20%)|Alphabet (15%)|Facebook (5%))

```



And here's how the rendered chart looks like:



![Top 5 Tech Companies by Value](https://chart.googleapis.com/chart?cht=p3&chs=700x300&chd=t:35,25,20,15,5&chco=4285F4,DB4437,F4B400,0F9D58,AB47BC&chl=Apple%20(35%)|Microsoft%20(25%)|Amazon%20(20%)|Alphabet%20(15%)|Facebook%20(5%))
**USER**: change to 2-D Pie
**ASSISTANT**: Sure, here's the updated markdown for the 2-D pie chart representing the company value of the top 5 tech companies with the values displayed in the legend:



```

![Top 5 Tech Companies by Value](https://chart.googleapis.com/chart?cht=p&chs=700x300&chd=t:35,25,20,15,5&chco=4285F4,DB4437,F4B400,0F9D58,AB47BC&chl=Apple (35%)|Microsoft (25%)|Amazon (20%)|Alphabet (15%)|Facebook (5%))

```



And here's how the rendered chart looks like:



![Top 5 Tech Companies by Value](https://chart.googleapis.com/chart?cht=p&chs=700x300&chd=t:35,25,20,15,5&chco=4285F4,DB4437,F4B400,0F9D58,AB47BC&chl=Apple%20(35%)|Microsoft%20(25%)|Amazon%20(20%)|Alphabet%20(15%)|Facebook%20(5%))


