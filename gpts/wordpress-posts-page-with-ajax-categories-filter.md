
[![Wordpress posts page with ajax categories filter](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_7.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22mxN8mpiFmkHZ7Coan7jd3%22%2C%22flow%22%3Atrue%7D%7D)
# Wordpress posts page with ajax categories filter | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22mxN8mpiFmkHZ7Coan7jd3%22%2C%22flow%22%3Atrue%7D%7D)
Create a wordpress posts loop with sidebar having filter with categories that filter those posts using ajax





# Prompt

```
Create a wordpress posts loop with sidebar having filter with categories that filter those posts


```

## Conversation

**ASSISTANT**: Here's an example of how you can create a WordPress post loop with a sidebar filter that allows users to filter posts by categories:



1. First, create a new page template in your WordPress theme. You can do this by creating a new file in your theme's directory called "page-filtered-posts.php" and adding the following code at the top:



```

<?php

/*

Template Name: Filtered Posts

*/

?>

```



2. In the same file, add the following code to display the filtered posts loop:



```

<div class="row">

  <div class="col-md-8">

    <?php

      $args = array(

        'post_type' => 'post',

        'posts_per_page' => -1,

      );

      $query = new WP_Query($args);

      if ($query->have_posts()) :

        while ($query->have_posts()) :

          $query->the_post();

          ?>

            <div class="post">

              <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>

              <?php the_excerpt(); ?>

            </div>

          <?php

        endwhile;

        wp_reset_postdata();

      else :

        echo '<p>No posts found</p>';

      endif;

    ?>

  </div>



  <div class="col-md-4">

    <h3>Filter by Category</h3>

    <?php

      $categories = get_categories();

      echo '<ul>';

      foreach ($categories as $category) {

        echo '<li><a href="' . get_category_link($category->term_id) . '">' . $category->name . '</a></li>';

      }

      echo '</ul>';

    ?>

  </div>

</div>

```



This code creates a basic two-column layout using Bootstrap classes. The left column contains the post loop, which fetches all posts and displays their title and excerpt. The right column contains a list of categories that users can click to filter the posts.



3. Save the file and create a new page in WordPress using the "Filtered Posts" template you just created.



That's it! You should now have a working filtered posts loop with a sidebar filter that allows users to filter posts by categories.
**USER**: can you use ajax filter to filter these posts
**ASSISTANT**: Yes, you can use AJAX to filter these posts without reloading the entire page. Here's an example of how you can do it:



1. Enqueue jQuery and a custom JavaScript file in your WordPress theme's functions.php file:



```

function my_theme_scripts() {

  wp_enqueue_script('jquery');

  wp_enqueue_script('custom-script', get_template_directory_uri() . '/js/custom.js', array('jquery'));

}

add_action('wp_enqueue_scripts', 'my_theme_scripts');

```



2. Create a new file called "custom.js" in your theme's js directory and add the following code:



```

jQuery(document).ready(function($) {

  $('body').on('click', '#category-filter a', function(e) {

    e.preventDefault();

    var category = $(this).data('category');

    $('.post').fadeOut();



    $.ajax({

      type: 'POST',

      url: ajaxurl,

      data: {

        action: 'filter_posts',

        category: category

      },

      success: function(response) {

        $('.post-wrapper').html(response).find('.post').hide().fadeIn();

      }

    });

  });

});

```



This code listens for clicks on links within the #category-filter element (which should contain the list of category filters), gets the category from the clicked link's data attribute, hides all posts, sends an AJAX request to the server with the selected category, and updates the post wrapper element with the filtered posts.



3. Add a new function in your theme's functions.php file to handle the AJAX request:



```

function filter_posts() {

  $args = array(

    'post_type' => 'post',

    'posts_per_page' => -1

  );



  if (isset($_POST['category'])) {

    $args['tax_query'] = array(

      array(

        'taxonomy' => 'category',

        'field'    => 'slug',

        'terms'    => $_POST['category'],

      ),

    );

  }



  $query = new WP_Query($args);



  if ($query->have_posts()) :

    while ($query->have_posts()) :

      $query->the_post();

      ?>

      <div class="post">

        <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>

        <?php the_excerpt(); ?>

      </div>

      <?php

    endwhile;

    wp_reset_postdata();

  else :

    echo '<p>No posts found</p>';

  endif;



  die();

}

add_action('wp_ajax_filter_posts', 'filter_posts');

add_action('wp_ajax_nopriv_filter_posts', 'filter_posts');

```



This code checks if a category was passed in the AJAX request and adds a tax_query to the WP_Query object to filter the posts by the selected category. If no category was selected, it will return all posts. It then loops through the posts and outputs the same markup used in the initial post loop.



That's it! You can now use AJAX to filter the posts without reloading the entire page.


