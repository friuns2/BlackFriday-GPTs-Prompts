
[![Super Website Code Generator Prompt](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_8.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22yA3h3HveN0z6F4w-eM34e%22%2C%22flow%22%3Atrue%7D%7D)
# Super Website Code Generator Prompt | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22yA3h3HveN0z6F4w-eM34e%22%2C%22flow%22%3Atrue%7D%7D)
a skilled HTML/CSS/JavaScript developer, that will create the code for a website.

# Prompt

```
As a skilled HTML/CSS/JavaScript developer, create the html code with file name index.html, the CSS code with file name styles.css, and JavaScript code for smooth scroll to anchor with file name script.js for website with the following features:

- Website name: {{ website name }}
- An 'About' section that includes: {{ about }}
- A 'Services' section listing the following services: {{ services }}
- A 'Contact' section with the following information: 
  - Business Address: {{ address }}
  - Phone Number: {{ phone number }}
  - Email Address: {{ email }}
- Links to the following social media profiles: 
  - Facebook: {{ facebook link }}
  - Twitter: {{ twitter link }}
  - Instagram: {{ instagram link }}
  - LinkedIn: {{ linkedin link }}
  - YouTube: {{ youtube link }}
- Additional features as specified by the user: {{ additional information }}

```

## Conversation

**ASSISTANT**: Here's the HTML, CSS, and JavaScript code for a website with smooth scroll to anchor feature:



HTML - index.html:

```

<!DOCTYPE html>

<html>

  <head>

    <title>flow.incomegpt</title>

    <link rel="stylesheet" href="styles.css">

  </head>

  <body>



    <!-- Navbar -->

    <nav>

      <ul>

        <li><a href="#about">About</a></li>

        <li><a href="#services">Services</a></li>

        <li><a href="#contact">Contact</a></li>

        <li><a href="#social-media">Social Media</a></li>

        <li><a href="#additional-features">Additional Features</a></li>

      </ul>

    </nav>



    <!-- About Section -->

    <section id="about">

      <h2>About</h2>

      <p>Flow IncomeGPT is a website created using our Super Website Code Generator Prompt available on FlowGPT.</p>

    </section>



    <!-- Services Section -->

    <section id="services">

      <h2>Services</h2>

      <ul>

        <li>Generate your website no-cost!</li>

      </ul>

    </section>



    <!-- Contact Section -->

    <section id="contact">

      <h2>Contact</h2>

      <p>Business Address: iamherenow/</p>

      <p>Phone Number: call.iinc/</p>

      <p>Email Address: i@innerinetcompany.com</p>

    </section>



    <!-- Social Media Links -->

    <section id="social-media">

      <h2>Follow us on social media:</h2>

      <ul>

        <li><a href="https://www.facebook.com/innerinetcompany">Facebook</a></li>

        <li><a href="https://twitter.com/innerinetco">Twitter</a></li>

        <li><a href="https://www.instagram.com/hnsdomains/">Instagram</a></li>

        <li><a href="https://www.linkedin.com/">LinkedIn</a></li>

        <li><a href="https://www.youtube.com/innerinetwork">YouTube</a></li>

      </ul>

    </section>



    <!-- Additional Features -->

    <section id="additional-features">

      <h2>Additional Features</h2>

      <p>Upvote innerinetcompany on FlowGPT</p>

    </section>



    <script src="script.js"></script>

  </body>

</html>

```



CSS - styles.css:

```

/* General styling */

body {

  font-family: Arial, sans-serif;

  margin: 0;

  padding: 0;

}



h2 {

  font-size: 24px;

  font-weight: bold;

  margin-top: 40px;

}



p {

  font-size: 16px;

  margin-bottom: 10px;

}



ul {

  list-style: none;

  padding: 0;

}



a {

  color: #000;

  text-decoration: none;

}



nav {

  background-color: #f2f2f2;

  position: fixed;

  top: 0;

  width: 100%;

}



nav ul {

  display: flex;

  justify-content: space-around;

  align-items: center;

  margin: 0;

  padding: 10px 0;

}



nav li {

  margin-left: 20px;

}



/* Section-specific styling */

#about {

  background-color: #f2f2f2;

  padding: 40px 20px;

}



#services {

  background-color: #e6e6e6;

  padding: 40px 20px;

}



#contact {

  background-color: #d9d9d9;

  padding: 40px 20px;

}



#social-media {

  background-color: #cccccc;

  padding: 40px 20px;

}



#additional-features {

  background-color: #bfbfbf;

  padding: 40px 20px;

}

```



JavaScript - script.js:

```

// Smooth scroll to anchor

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

  anchor.addEventListener('click', function (e) {

    e.preventDefault();



    document.querySelector(this.getAttribute('href')).scrollIntoView({

      behavior: 'smooth'

    });

  });

});

```



Note that you may need to adjust the file paths for your CSS and JavaScript files based on where they are stored relative to your HTML file. This code will create a fixed navbar at the top of the page with links to each section. When clicked, these links will smoothly scroll to each corresponding section using JavaScript


