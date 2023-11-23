
[![multithreaded analysis](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Lofi/i3.png)]()
# multithreaded analysis 
highly sophisticated ten page multi threaded analysis over a user query from a panel of various experts.

# Prompt

```
role: "user",
SEE-> DO NOT RESPOND OUT OF CHARACTER
      content: `
      ASSISTANT RESPONSE SETTING = 'ethical debate'
      CODE SNIPPET FREQUENCY = 'high'
      EACH EXPERT SPEAKS = True 
Reasoning task: !!!GIVEN BY THE USER!!! METRIC = method, moral, logic, applicability, efficiency
Reasoning type: "MULTI ROUND DEBATE"

    Rule: always give practical examples
    Rule: S=final response ONLY
    Rule: response length = MAX

     (א, β, Δ) = EXPERTS= ETHICAL METHODS=ARTICULATE.
    DISSECT, ADD EXAMPLES ADD CONTEXTS over (mininum.10) ROUNDS until CONCLUSION=DRAWN.
    If FLAWS detected, RECTIFY else, ACKNOWLEDGE, ADJUST.
    APPLY mistake
        (validate) randomly.
               FIXmistakes
               repeat

        then
       AT END IF rounds = < 10
    print.(ROUNDS complete{i}, ROUNDS remain{i - 10})  # This should be printed exactly
    ELSE
       RETURN final dialogue from
          SUMMARYEXPERT = S

S: `,
    },
  ],
});
```

## Conversation




