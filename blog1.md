---
layout: page
title: Creating Maps 
description: Lorimer Information  

nav-menu: false
---
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>Blogs</h1>
		</header>
<h2 id="content">Formatting Data for Maps - Navigation between Platforms</h2>
<p> 
	<i>Liyan Ibrahim</i> 
	<br>
	<i>14-7-2020</i>
</p>
<p> 
	When making Maps for historical data such as in our case, a certain format of datasets makes the process easier and cleaner. This blog will provide a detailed tutorial on how to extract quantities of a certain attribute from a collection of text files using Google Sheets and AntConc. 
	In this tutorial, I will be extracting the number of donkeys in each text file.
	<ol>
		<li>Download all the text files into one folder </li>
		<li>Import all the text files onto AntConc by going to File → Open File(s) and navigating to the folder with the text files and select all of them to import <<br>
		Once these files are imported, AntConc should look like this:</li>
		<img src="assets/images/i1.jpg" style="width:500px;height:300px;">
		<p>Note that: All the text file names are seen on the left under “Corpus Files” and the total number of files is seen under “Total No.”  </p>
		<li>Now that AntConc is setup, use the search term to search for your desired attribute as shown</li>
		<img src="assets/images/i2.jpg" style="width:700px;height:200px;">
		<li>AntConc should generate a screen that looks like this with the attribute searched for in blue and the total number of concordance hits (the total number of “donkey” entries found) is seen in the upper left corner and the corresponding file name for each result on the right side</li>
		<img src="assets/images/i3.jpg" style="width:500px;height:300px;">
		<li>Since the format of the data is consistent, we can save the output as a text file by going to File → Save Output as shown</li>
		<img src="assets/images/i4.jpg" style="width:300px;height:300px;">
		<li>The text file that is saved from AntConc can now be imported into GoogleSheets using File → Import → Upload</li>
		<li>Since the text file has tabs separating what was previously Columns in AntConc, Google sheets can detect that automatically and place the same values into columns. The following settings should be chosen for the data to be imported correctly</li>
		<img src="assets/images/i5.jpg" style="width:200px;height:300px;">
		<li>Google Sheets should now look like this </li>
		<img src="assets/images/i6.jpg" style="width:500px;height:300px;">
		<li>Since the quantity we want to extract is in column B, insert a new empty column between B and C</li>
		<li>It is also important to note that, since our data is consistent, the number we want in almost always present at the end of the sentence in column B</li>
		<li>We can now use a formula to extract the last word/number from column B 
			<ul>
				<li>If you have consistent spacing, use the following formula, replacing text with the cell containing the value (in my case, B1) :<br>
				=TRIM(RIGHT(SUBSTITUTE(text," ",REPT(" ",100)),100)) </li>
				<li>If you have inconsistent spacing, use the following formula, replacing text with the cell containing the value (in my case, B1):<br>
				=TRIM(RIGHT(SUBSTITUTE(TRIM(text)," ", REPT(" ", 100)),100))</li>
			</ul></li>			
		<li>Replicate for the rest of the cells and the output should be as shown </li>
		<img src="assets/images/i7.jpg" style="width:500px;height:300px;">
		<li>OPTIONAL: To further clean up the data, choose a format in which only the relevant content is in the sheet. For my case, we only needed the number of donkeys and the file name. The following is the data after cleaning it </li>
		<img src="assets/images/i8.jpg" style="width:400px;height:400px;">
	</ol>






 

 









