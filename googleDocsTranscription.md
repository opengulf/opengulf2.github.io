---
layout: page
title: Transcribing images by Google Docs
description:

nav-menu: false
---

<head>
	<style>
		p{
			text-indent: 5%;
		}
	</style>
</head>
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>Blogs</h1>
		</header>
<h2 id="content">Exploring the Power of Google Vision API: Building Handwritten Ground Truth with Google Docs via Google Drive</h2>

    	<b>Fady John</b>
    	<br>
    	<b>12-12-2023</b>

<p>In today's digital era, leveraging advanced technologies to streamline and enhance our workflow is crucial. One such technology that has been making waves is the Vision API, a powerful tool provided by Google Cloud. This blog will provide a tutorial on how can harness the capabilities of the Vision API to transcribe images using Google Docs through Google Drive. Working with the HTR group, I used this method to create handwritten ground truth for an Arabic transcription model.</p>
<p>The following steps show how you can use google docs to generate transcribed text from images</p>
<ol>
	<li>Start by scanning or taking high-quality images of your handwritten documents. Upload these images to your Google Drive. Organize them into a dedicated folder for better management.</li>
	<img src="../assets/images/fadyblogstep1.png" style="width:820px;height:200px;"><br>
	<li>Simply right-click on the image and choose "Open with Google Docs." This straightforward action instantly opens the selected image directly in the Google Docs application</li>
	<img src="../assets/images/fadyblogstep2.png" style="width:750px;height:250px;"><br>
	<li>The generated document displays both the image and its transcribed text, as shown in the image below</li>
	<img src="../assets/images/fadyblogstep3.png" style="width:600px;height:250px;">
</ol>
<p>The result of that method is actually impressive, as it has the ability to transcribe complicated Arabic hostorical handwriting that many people cannot actually read. Implementing the previous method contributed to doubling the size of the Arabic transcription model's ground truth, soaring from 60 to approximately 120 pages. This substantial expansion played a pivotal role in enhancing the model's transcription accuracy. The positive impact on accuracy underscores the effectiveness of leveraging the Vision API and Google Docs integration for extending ground truth datasets.

    <br>Yet, the versatility of this method extends beyond its role in crafting training page sets. Beyond its utility for training purposes, this innovative technique opens doors to a spectrum of applications. It can be harnessed for diverse projects, ranging from data enrichment and analysis to creating comprehensive datasets for machine learning models in various domains. The seamless synergy between the Vision API and Google Docs presents a valuable tool that transcends its initial application, offering a flexible solution for data-related tasks across different fields.</p>
