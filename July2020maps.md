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
<h2 id="content"> From Digital Historical Source to Leaflet Maps </h2> 
	<b>Liyan Ibrahim</b> 
	<br>
	<b>23-7-2020</b>
<p> 
	Visualizing historical data is a great method of portraying important historical information  to the general public. It not only allows us to create a visual narrative of the data we have but also helps historians and researchers understand the data they produce by seeing it.  Visualization, although it introduces new interpretative challenges, is quite powerful for generating new hypotheses and important research questions within that field. In our case, the historical data came from the annotation of the Geographical and Statistical section of Lorimer's <a href="https://archive.org/details/in.ernet.dli.2015.206963" class="link">Gazetteer of the Persian Gulf, Oman and Central Arabia</a>. Therefore, developing a workflow for  navigating between the platforms used for annotation and  mapping  was an important part of this project. <br>
	Recogito was a platform that was used to perform the semantic annotation of people and places, and it has the option of downloading the relevant annotations of the text file dump in the form of a CSV file. This CSV file was enriched with coordinates by means of a lookup with the relevant national data dumps coming from GeoNames. Once we had a list of places with their corresponding geocoordinates. The map-making process could begin. <br>
	Thinking about the historical relevance of the maps we were making required the team to study the content produced and evaluate the historical importance of some attributes mentioned in Lorimer's articles as well as how this could be reflected in a Leaflet map hostable in GitHub pages with open source basemaps. Once the important attributes were identified for the  geocoded places in question we used  Antconc to find the quantity of each attribute in each place name (see the short tutorial on this process in this <a href="../July2020formattingdata" class="link">blog</a>). 
</p>
<p>
	Once we had the basis of the maps, further customization was needed in order to best portray the historical context of each map. Customizing the symbology of the maps depended on analyzing the most important attributes in the datasets. For example, some required the manipulation of the symbol used in terms of colors, size or type of symbol. Others required the use of the “Rule-based” or “Classification” symbology which allowed us to change the style of the points based on a certain rule or classification of a certain column.<br>   
	Once the visuals of the maps were finalized, we used the qgis2web plugin for QGIS to design and create the Leaflet maps following the <a href="https://github.com/taylorhixson/WF" class="link">tutorial by Taylor Hixson</a>. Exporting gave us the option to further adjust other functionalities of the map such as the zoom extent and the pop-up box. The pop-up box could also be edited after exporting, by modifications directly in  the index.html file. 
</p>
<p>
	One major issue we faced was that some functionalities that QGIS facilitates in its standalone version could not be completely transferred over to a web map. An example would be the style aspect in which the size of the point on the map would be determined by a certain attribute. This was challenging since we had to rethink and evaluate the visual representation of some maps in the sense of getting the same point across through a different style supported by qgis2web. For one <a href="../wells" class="link" >map</a>, we opted for completely removing that aspect of the visual representation and presenting this numerical attribute in the pop-up box. For another <a href="../dates" class="link" >map</a>, a solution was to use the “Graduated” symbology to represent grouped sizes as different shades of the same color.
</p>
<p>
	That being said, it was important for us to accompany the maps we publish with detailed notes about each map. The notes would give a general overview of the maps, how we believe they should be explored, how they have been put together as well as any relevant information about the underlying data.. This then left us with a historical map of places mentioned in the work of Lorimer along with notes about each map for publication. 
</p>
Check out these maps <a href="../map" class="link">here!</a> 









 

 









