---
layout: default
---

## Home, index.md (Tianbin style)
This page uses an autoplay video loop as its backround.  This code is illustrated below.


* HTML Code
```html
<!-- added to end of index.md -->
<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
```

<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>

* CSS Code
```html
<!-- added to custom _includes/head-custom2.html -->

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

## Ripping a Theme
Using GitHub pages with Jekyll requires us to establish style.  This page is built on midnight theme.  However to customize it, this required ripping authors work and doing some customization.  According to the 'Creative Commons' license provided by the author, ripping this theme is completely valid.





