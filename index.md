---
layout: default
---

## Home (Tianbin style)
This page uses an autoplay video loop as its backround.


* HTML Code
```html
<!-- added to end of index.md -->
<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>
```

* CSS Code
```html
<!-- added to custom _includes/ index.md -->

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

<div id="video_wrapper">
  <video autoplay loop>
    <source src="https://drive.google.com/uc?export=view&id=1Qote5m--Bme0bE4_o6wAKNRxWY8pJnuL" type="video/mp4">
  </video>
</div>

