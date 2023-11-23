
[![ChatGPT as an IT specialist](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/abstract/abs_2.png)]()
# ChatGPT as an IT specialist 
As a professional IT specialist, chatGPT will review a codebase written in your desire programming language and turn it into professional-grade code and will identify any errors, optimize the code for performance and readability, and ensure that it adheres to industry best practices. chatGPT will give you some review include a detailed report outlining the changes he made and the rationale behind them. 



⚠️ You can change the programming language to whatever you want

# Prompt

```
Hello, ChatGPT. As a professional IT specialist, I need you to review a codebase written in javascript and turn it into professional-grade code. The codebase consists of many files with many lines of code. Your task is to identify any errors, optimize the code for performance and readability, and ensure that it adheres to industry best practices.

To complete this task, you should follow the steps below:

1. Read through the entire codebase to gain a comprehensive understanding of the functionality it provides.

2. Identify any coding errors or inconsistencies, such as syntax errors, incorrect data types, or inefficient algorithms. Note these errors in a report for the developer(s) to review.

3. Optimize the codebase for performance and readability. This may include refactoring code to eliminate redundancy, improving naming conventions, or reorganizing code blocks for clarity.

4. Ensure that the codebase adheres to industry best practices, such as proper documentation, code commenting, and appropriate use of programming patterns.

5. Create a detailed report outlining the changes you made and the rationale behind them. The report should include before-and-after code snippets to illustrate the changes.

If you have any questions or concerns, please do not hesitate to ask. I will share you the code after this, execute after i send it.
```

## Conversation

**ASSISTANT**: Sure, feel free to send the codebase and I'll do my best to provide feedback and optimize it for performance and readability.
**USER**: return (

    <div>

      {!session && (

        <>

          <button onClick={() => handleSignIn('google')}>Sign in with Google</button>

        </>

      )}

      {session && (

        <>

          <p>Welcome, {session.user.name}!</p>

          <button onClick={() => signOut()}>Sign out</button>

        </>

      )}

    </div>

  )



turn this into clean code
**ASSISTANT**: Here's a cleaner version of the code you provided, while keeping its functionality intact:



```

<div>

  {!session ? (

    <button onClick={() => handleSignIn('google')}>Sign in with Google</button>

  ) : (

    <>

      <p>Welcome, {session.user.name}!</p>

      <button onClick={() => signOut()}>Sign out</button>

    </>

  )}

</div>

```



The changes I made:

- Removed unnecessary surrounding `<>` fragments when there is only one child element.

- Replaced the if-statement with a ternary operator for better readability.

- Changed the second if-statement to an equivalent else statement inside the ternary operator.


