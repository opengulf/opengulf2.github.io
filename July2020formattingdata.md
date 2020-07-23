---
layout: page
title: Creating Maps 
description: Lorimer Information  

nav-menu: false
---
<head>
	<style>
		p{
			text-indent: 10%;
		}
	</style>
</head>
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>Blogs</h1>
		</header>
<h2 id="content">Extracting Repeated Quantities from Plain Text Files Using AntConc and Formulas in Google Sheets </h2>

		<b>Liyan Ibrahim</b>
		<br>
		<b>23-7-2020</b>

<p> 
	When creating historical data for map-making, structured datasets makes the process easier and cleaner. This blog will provide a detailed tutorial on how to extract quantities of a certain attribute from a collection of text files using low-barrier digital platforms:<i> AntConc and Google Sheets</i>. In this tutorial, I will be extracting the number of donkeys mentioned in each text file. 	
	<ol>
		<li>Download all the text files into one folder. </li>
		<li>Import all the text files into AntConc File → Open Directory and navigate to the same folder with the text files and import them. <<br>
		Once these files are imported, AntConc should look like this:</li>
		<img src="../assets/images/i1.jpg" style="width:500px;height:300px;"><br>
		Note that: All the text file names are seen in the left hand window named “Corpus Files” and the total number of files is seen under “Total No.” at bottom left. Now that AntConc is setup, insert a search term to search for your desired attribute as shown <br>
		<li>Now that AntConc is setup, use the search term to search for your desired attribute as shown</li>
		<img src="../assets/images/i2.jpg" style="width:700px;height:200px;">
		<li>AntConc will generate a screen as follows with the search term and the total number of concordance hits (that is, the total occurrences  of “donkey” found) is seen in the upper left corner and the corresponding file name for each result on the right side</li>
		<figure>
			<img src="../assets/images/i3.jpg" style="width:500px;height:300px;">
			<br>
		</figure>
		<li>Since AntConc provides the data in a consistent KWIC (keyword in context) format, we can save the output for further manipulation as a text file by going to File → Save Output as shown</li>
		<img src="../assets/images/i4.jpg" style="width:300px;height:300px;">
		<li>For extracting the entities and the quantities the txt file  saved from AntConc can now be imported into GoogleSheets using File → Import → Upload</li>
		<li>Since the txt file has tabs separating what were previously Columns in AntConc, Google sheets can detect that automatically and place the same values into columns. The following settings should be chosen for the data to be imported correctly</li>
		<img src="../assets/images/i5.jpg" style="width:200px;height:300px;">
		<li>Google Sheets should now look like this </li>
		<img src="../assets/images/i6.jpg" style="width:500px;height:300px;">
		<li>Since the quantity we want to extract is in column B, insert a new empty column between B and C.</li>
		<li>It is also important to note that, since our data is consistent, the number we want in almost always present at the end of the sentence in column B.</li>
		<li>We can now use a formula to extract the last word/number from column B 
			<ul>
				<li>If you have consistent spacing, use the following formula, replacing text with the cell containing the value (in my case, B1) :<br>
				=TRIM(RIGHT(SUBSTITUTE(text," ",REPT(" ",100)),100)) </li>
				<li>If you have inconsistent spacing, use the following formula, replacing text with the cell containing the value (in my case, B1):<br>
				=TRIM(RIGHT(SUBSTITUTE(TRIM(text)," ", REPT(" ", 100)),100))</li>
			</ul></li>			
		<li>Replicate for the rest of the cells and the output should be as shown </li>
		<img src="../assets/images/i7.jpg" style="width:500px;height:300px;">
		<li>OPTIONAL: To further clean up the data, choose a format in which only the relevant content is in the sheet. For my case, we only needed the number of donkeys and the file name. The following is the data after cleaning it </li>
		<img src="../assets/images/i8.jpg" style="width:400px;height:400px;">
	</ol>






 

 









