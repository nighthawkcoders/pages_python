---
layout: default
---

<!-- HTML for Video Play -->

<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>

<!-- Remainder of this file is the story of how it is made -->

## Home (Tianbin style)
This page uses an autoplay video loop as its backround.  This Code, HTML and CSS, is illustrated below.


* HTML Code [index.md](https://github.com/nighthawkcoders/pages_python/edit/gh-pages/index.md)

```html
<!-- added to index.md -->
<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
```

* CSS Code

```html
<!-- pages_python/_includes/head-custom2.html -->

<style>
#video_wrapper {
    margin:0px;
    padding:0px;
}
#video_wrapper video {
    position: fixed;
    top: 50%; left: 50%;
    z-index: -99; important!
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translate(-50%, -50%);
}
</style>
```

## Ripping a [theme: jekyll-theme-midnight](https://github.com/pages-themes/midnight/blob/master/_layouts/default.html)
Using GitHub pages with Jekyll requires us to establish style.  This page is built on midnight theme.  However to customize it, this required ripping authors work and doing some customization.  According to the [Creative Commons license](https://github.com/pages-themes/midnight/blob/master/LICENSE) provided by the author, ripping this theme is completely valid.

```html
<!-- pages_python/_layouts/default.html
     customization added to original midnight theme found through GitHub Pages -->
<html lang="{{ site.lang | default: "en-US" }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    {% seo %}
    <link rel="stylesheet" href="{{ '/assets/css/style.css?v=' | append: site.github.build_revision | relative_url }}">
    <script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
    <script src="{{ '/assets/js/respond.js' | relative_url }}"></script>
    <!--[if lt IE 9]>
      <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <!--[if lt IE 8]>
    <link rel="stylesheet" href="{{ '/assets/css/ie.css' | relative_url }}">
    <![endif]-->
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    {% include head-custom.html %}
    
    <!-- nighthawk coding society has inserted its own file for thigs like <style>-->
    {% include head-custom2.html %}

  </head>
  <body>
      <div id="header">
        <nav>
          <ul>
            <li class="fork"><a href="{{ site.github.repository_url }}">View On GitHub</a></li>
            {% if site.show_downloads %}
              <li class="downloads"><a href="{{ site.github.zip_url }}">ZIP</a></li>
              <li class="downloads"><a href="{{ site.github.tar_url }}">TAR</a></li>
              <li class="title">DOWNLOADS</li>
            {% endif %}
          </ul>
        </nav>
      </div><!-- end header -->

    <div class="wrapper">

      <section>
        <div id="title">
          <h1>{{ site.title | default: site.github.repository_name }}</h1>
          <p>{{ site.description | default: site.github.project_tagline }}</p>
          <hr>
          <span class="credits left">Project maintained by <a href="{{ site.github.owner_url }}">{{ site.github.owner_name }}</a></span>
          <!-- Credit goes to peron in next line, as nighthawkcoding society is rebranding this as their own
               <span class="credits right">Hosted on GitHub Pages &mdash; Theme by <a href="https://twitter.com/mattgraham">mattgraham</a></span> -->
          <span class="credits right">Hosted on GitHub Pages &mdash; Theme by <a href="https://twitter.com/NighthawkCoding">nighthawkcodingsociety</a></span> 
        </div>
        
        <!-- nighthawk coding society has inserted navigation that can be updated in independent file -->
        {% include navigation.html %}

        <!-- this is Jekyll magic, each md file in site will be inserted here -->
        {{ content }}

      </section>

    </div>
  </body>
</html>
```
