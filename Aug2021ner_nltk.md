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
<h2 id="content">Named Entity Recognition in Lorimer's Gazetteer with NLTK</h2>

	<b>Alma Kapan</b> 
	<br>
	<b>8-8-2021</b>

<p> 
	John G. Lorimer, the British civil servant who compiled a 5,000-page, two-volume secret encyclopedia entitled <i>Gazetteer of the Persian Gulf, Oman and Central Arabia</i>, created originally in 1908 and declassified in 1955, covered extensive ground with a team of British and native agents across India and the Gulf to assemble his historical text and geographical index of the Arabian Peninsula and Gulf region. While this text, in its comprehensive nature and detailed observations, is of great significance to scholars and researchers working within this geographical scope, what was of interest to me as I spent the past several weeks annotating it was the enduring presence of the village names mentioned in the text and the potential legacy of the <i>Gazetteer</i> today.
</p>
<p>
	Taking Lorimer’s <a href="https://archive.org/details/in.ernet.dli.2015.206964/page/n1967/mode/2up" class="link">article</a> on Wādi Tāyīn (وادي طايين) for instance, in Volume II: Geographical and Statistical starting on page 1875, it becomes clear that very few of the names that he lists in this article have changed, rendering my task of annotating toponyms with geographical coordinates a great deal easier. In an annotation tool called <a href="https://recogito.pelagios.org/" class="link">Recogito</a>, after realizing that Lorimer’s list of villages follows a contemporary road called Route 25 in southeastern Oman that leads to the Wādi in question, all I had to do in order to annotate the historical text was to follow along this road and identify each village as I headed to the end of the Wādi. In his list of “principal places in or directly connected with Wādi Tāyīn,” Lorimer lists 23 villages, their locations relative to the Wādi and surrounding villages, their physical attributes, the families that live in each village, and natural resources (1908 edition, p. 1875).
</p>
<p>
	When I began noticing that each village followed the previous one on the somewhat circular Route 25—and later on a smaller road that leads to Wādi Khabbah (وادي خبّه)—I sought to visualize a path connecting the towns and to map a potential route that Lorimer or one of his informants might have taken in their trips to the region. Although the text makes no explicit mention of Route 25 or of an extant path, this coincidence struck me. Beginning with Ba’ad on the left, a village that falls about halfway across the upper semicircle of Route 25, I connected the villages listed by Lorimer in geographic order, tracing the path created by this route.<br>
	<figure>
	<img src="../assets/images/nadasblog.jpg" style="width:500px;height:300px;">
	<figcaption><i>Google Map showing Route 25 and villages leading to Wādi Tāyīn</i></figcaption>
</figure>
</p>
<p>
	 The initial, pleasant surprise of the alignment of these villages with Route 25 inspired me to look more closely into the contemporary significance of this route. Given that only one of the 23 villages is listed by Lorimer as “practically depopulated” and “[having] ceased to exist as a village,” I assumed that the rest still existed today (p. 1878). A simple Google search of “Route 25 Oman'' yielded countless travel blogs that recommended walking and trekking itineraries along Route 25 leading to Wādi Dima wa Tāyīn, a name given to the area where the two wadis meet. I was struck not only by the consistency of these particular toponyms over time, but by the continuity of the descriptions of these areas by the Gazetteer and by tourists today.
</p>
<p>
	In order to trace this line, I started by creating a simple Google Map containing each of the villages listed by Lorimer, in geographical order, using latitudinal and longitudinal coordinates sourced from GeoNames. The map above suggests a potential itinerary that Lorimer may have followed; however, given that these villages were not all listed in his text in geographical order, I traced a second itinerary that follows his listing’s order so as to adhere more closely to his observations and notes. The maps below—showing just five of the villages in Lorimer’s list—indicate what this alternative route may have looked like, with a comparison to the geographically ordered map below it. I’ve created this alternative map with just five villages because these are the only ones amongst his list which do not follow geographical order.<br>
	<figure>
		<img src="../assets/images/nadasblog2.jpg" style="width:500px;height:300px;"><br>
		<img src="../assets/images/nadasblog3.jpg" style="width:500px;height:300px;">
		<figcaption>Both maps show the following villages: Shāt (شات) in <span style="color:#FF0000;">red</span>; Hammām (حمّام) in <span style="color:#0000FF;">blue</span>; Qurr (قرّ) in <span style="color:#FFFF00;">yellow</span>; Sibal (سبل) in <span style="color:#800080;">purple</span>; and Hida (حدا) in <span style="color:#FFA500;">orange</span>, before the path continues back along Route 25 in <span style="color:#008000;">green</span>.</figcaption>
	</figure>
</p>
<p>
	Though the order of the villages as he lists them inspires questions about how he may have gathered his notes or what circumstances may have caused him to go back and forth along this route—how cool is it to try to think like Lorimer (or one of the countless agents who collected data on his behalf) and to put myself in their shoes, in this time and place?—what I found more interesting in my research is the fact that the villages, in whatever order they are connected, nonetheless adhere to the path created by Route 25, or perhaps, more interestingly, created the path that Route 25 follows.
</p>
<p>
	The historical implications of this reflection are manifold, but considering that the Gazetteer was written in the early 20th century, I find the tangibility and contemporary relevance of his writings in something such as a still-in-use road and the legacy of this particular itinerary as a popular path amongst trekking communities of all demographics simply fascinating. While geographical indexes such as Lorimer’s Gazetteer often feel distant and inaccessible to non-academics, by grounding these writings in approachable topics such as trekking and tourism, these historical texts and the spaces which they reference can be linked to contemporary communities whose priorities are just as spatially, geographically, and topographically oriented.
</p>
	See the <a href="https://www.google.com/maps/d/u/0/viewer?mid=10lDPJuu5VnFO3ofcrBUYTWh3U6Ba-xj9&ll=23.110989824741395%2C58.662744400000015&z=10" class="link">Wadi Ta'iyin Map</a> and its corresponding <a href="https://github.com/opengulf/Lorimer_data/blob/master/Wadi_Al_Tayin.csv" class="link">dataset</a>.


	





 

 









