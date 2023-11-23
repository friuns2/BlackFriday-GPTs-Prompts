
[![Conversion of Google Sheets Formulas Using MAP, LAMBDA, and IF Functions"](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_2.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22ySqrlJnw6bIE-9KD0pFXo%22%2C%22flow%22%3Atrue%7D%7D)
# Conversion of Google Sheets Formulas Using MAP, LAMBDA, and IF Functions" | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22ySqrlJnw6bIE-9KD0pFXo%22%2C%22flow%22%3Atrue%7D%7D)
Converting Google Sheets formulas to a specific standard using MAP, LAMBDA, and IF functions. Involves identifying columns, testing for empty strings, and adapting original formula logic within a LAMBDA function.

# Prompt

```
Hello, I would like help to convert some Google Sheets formulas to my specific standard, using the MAP, LAMBDA and IF functions. Please follow these steps when adapting the formulas:

Identify the columns that you need to use in your formula and include them in the MAP function as ranges separated by semicolon.
Write a LAMBDA function that accepts as variable arguments for each column included in the previous step.
Inside the LAMBDA function, use the IF function to test if the value in a specific column is an empty string (""), and return an empty string if it is true.
Adapt the logic of the original formula within the LAMBDA function, keeping its structure and purpose, syntax with ";" and backslash "" when present, but using the column variables provided as arguments.
Note that the standard =MAP(A2:A;B2:B;LAMBDA(ColA;ColB;IF(ColA=""; ""; always precedes.
Here are four examples of formulas that I would like you to adapt to my standard, along with the solutions already converted:
Example 1: Original formula: =IF(A2="";"";D2&" "&A2) Converted formula: =MAP(A2:A; D2:D; LAMBDA(ColA; ColD; IF(ColA=""; ""; ColD&" "&ColA)))
Example 2: Original formula: =IF(L2="";"";IF(REGEXMATCH(M2;"-DP")=TRUE;FILTER({'offer of the period pm'!E:F'offer of the period pm'!J:J'offer of the period pm'!H:I}; 'offer of the period pm'!C:C=SUBSTITUTE(M2;"-DP";"")); FILTER('offer of the period pm'!E:I; 'offer of the period pm'!C:C=SUBSTITUTE(M2;"-DP";"")))) Converted formula: =MAP(L2:L; M2:M; LAMBDA(ColL; ColM; IF(ColL=""; ""; IF(REGEXMATCH(ColM; "-DP")=TRUE; FILTER({'offer of the period pm'!E:F'offer of the period pm'!J:J'offer of the period pm'!H:I}; 'offer of the period pm'!C:C=SUBSTITUTE(ColM; "-DP"; "")); FILTER('offer of the period pm'!E:I; 'offer of the period pm'!C:C=SUBSTITUTE(ColM; "-DP"; ""))))))
Example 3: Original formula: =if(A2="";"";AND(F2=N2;G2=O2;H2=P2;I2=Q2;J2=R2)) Converted formula: =MAP(A2:A; F2:F; G2:G; H2:H; I2:I; J2:J; N2:N; O2:O; P2:P; Q2:Q; R2:R; LAMBDA(ColA; ColF; ColG; ColH; ColI; ColJ; ColN; ColO; ColP; ColQ; ColR; IF(ColA=" "; ""; AND(ColF=ColN; ColG=ColO; ColH=ColP; ColI=ColQ; ColJ=ColR)))))
Example 4: Original formula: =UNIQUE(FILTER('current ava subjects'!C:C;REGEXMATCH('current ava subjects'!C:C;B2))) Converted formula: =MAP(B2:B; LAMBDA(ColB; IF(ColB=""; ""; UNIQUE(FILTER('current ava subjects'!C:C; REGEXMATCH('current ava subjects'!C:C; ColB))))))
Now that you understand the pattern, I'm going to send you some formulas to convert, your response should contain only the final formula.
```

## Conversation

**ASSISTANT**: Sure, I can help you with that. Please provide the formulas to be converted and any necessary context or information about the columns used in the formula.


