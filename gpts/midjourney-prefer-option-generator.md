
[![Midjourney /prefer option generator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_2.png)]()
# Midjourney /prefer option generator 
This will generate 5 prefer options in a code box based on the style or description that you enter. for example "watercolor landscape --styleset" will list a prefer option of the top 5 artist of that genre and create a prefer option for each one containing their unique style.



It will also give you a short description of each of the 5 artists it suggested.



This really only works well on gpt4, gpt3.5 forgets how to format the prompt most of the time.

# Prompt

```
    When a user requests a --styleset, identify the key terms or theme within the user's input.
    Research and select five artists whose styles align with the specified theme.
    For each artist, create a /prefer option set with a weighted value system. Assign positive values to style aspects relevant to the artist, and a negative value to the contrasting aspects. Make sure the sum of all values is positive.
    In the /prefer option set, format it as follows: /prefer option set option:artist_last_name value: - aspect_1::value_1 aspect_2::value_2 ... aspect_n::value_n
    Use '::' between the aspect and its weight to signify the importance of that aspect. The higher the weight, the more important the aspect is.
    Format the /prefer option set in a code box for easy copying.
    Provide a table listing the artist names and short descriptions of their styles.

Make sure to pay attention to the user's specific requests and adjust the --styleset process accordingly.

{{ art description }}
```

## Conversation

**ASSISTANT**: Sure, I can help you with that!



To identify key terms or themes within the user's input, you can use natural language processing techniques to extract relevant keywords and phrases. Once you have identified the theme or style the user is looking for, you can select five artists whose styles align with that theme.



Here are five artists and their preferred style aspects:



1. Vincent van Gogh

/prefer option set option:van_Gogh value:  nature::4 color::5 expressionism::5 texture::4 



2. Pablo Picasso

/prefer option set option:Picasso value: cubism::5 abstract::4 color::3 shape::3



3. Salvador Dali 

/prefer option set option:Dali value: surrealism::5 realism::2 color::3 texture::2



4. Claude Monet

/prefer option set option:Monet value: impressionism::5 nature::4 color::5 light::4



5. Gustav Klimt

/prefer option set option:Klimt value: art_nouveau::5 gold::4 symbolism::3 color::4



And here's a table listing the artist names and short descriptions of their styles:



| Artist Name   | Style Description |

|---------------|-------------------|

| Vincent van Gogh | Post-Impressionist painter known for his bright colors, bold brushstrokes, and dramatic landscapes. |

| Pablo Picasso   | Cubist painter and sculptor known for his abstract, fragmented style and distorted figures. |

| Salvador Dali   | Surrealist painter known for his dreamlike, imaginative works featuring melting clocks and other bizarre imagery. |

| Claude Monet    | Impressionist painter known for his colorful, light-filled landscapes and emphasis on capturing the fleeting moments of nature. |

| Gustav Klimt   | Art Nouveau painter known for his ornate, decorative style featuring gold leaf, intricate patterns, and symbolic motifs. |


