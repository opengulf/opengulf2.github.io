---
layout: page
title: Custom Named Entity Recognition in Lorimer's Gazetteer with Spacy
description: NER Information

nav-menu: false
---

<head>
</head>
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>Blogs</h1>
		</header>
<h2 id="content">Custom Named Entity Recognition in Lorimer's Gazetteer with Spacy</h2>
    <b>Alma Kapan</b>
    <br>
    <b>8-8-2021</b>

<h3 style="font-size: 18px; text-align: center">I. Project Motivation</h3>
<p> 
This article is second in the series exploring automated Named Entity Recognition (NER) models for the historical texts from the Lorimer’s Gazetteer. Although NLTK, as mentioned in the first blogpost, provides one of the most well-recognized and used NER systems, there are several important reasons to explore other approaches due to NLTK’s limitations when applied to the Lorimer’s Gazetteer dataset.</p> 
<p> 
Firstly, most state-of-the-art systems such as NLTK were trained on English language texts : although such systems can accurately identify Named Entities (NEs) for English texts, they perform worse when applied to non-English, transliterated words. The Lorimer’s Gazetteer has many geographical names that were transliterated from Arabic to English and NLTK tends to either incorrectly tag these words (a city tagged as a person) or not recognize them. Moreover, many NEs from the Lorimer’s Gazetteer mostly appear in the historical context and do not have a large web footprint, which might make these words (i) to be underrepresented in the training data for NLTK and other modern systems and, consequently, (ii) not properly recognized by these systems. </p>
<p> 
Moreover, in NLTK, types of recognizable Named Entities (e.g. location, organization) are predetermined and NLTK does not support custom training of the NER classifier to solve the above mentioned issues. In other words, it is not possible to train unrecognized words to be tagged with a correct label (for example, train to tag Oman not as a person, but a location and train to tag some unrecognized non-English words). Also, even more importantly, it is not possible to introduce new Named Entity types (for example, recognize Tribe names or Environmental variables). To address these limitations and to create a more robust classifier, we introduced a custom-trained Spacy NER model for transliterated entities in the Lorimer’s Gazetteer.</p>
<p> 
This project would be valuable to a larger research community in two ways. Firstly, recognition of transliterated entities, which describe foreign people, places etc., is useful for many applications such as cross language text retrieval and translation. This pipeline can be applied to other transliterated texts with changes to the provided training data. 
Secondly, the Lorimer’s Gazetteer is one of the most influential and well-documented sources on the Gulf States Saudi Arabia, Persia with each text file in the Gazetteer pertaining to a certain location. </p>
<p>
Thus,extracting custom-trained entities (tribes, languages, environment features) for each of the locations from the Gazetteer would contribute to establishing a structure and connection across locations in the Middle East based on various environment, political, cultural, geographic features, which previously would be challenging due to time, labor constraints (dependence,subjectivity).
</p>

<p>
	NER has valuable applications for many important NLP tasks with the most impactful being Information Retrieval, a task of identifying and retrieving documents based on a query (e.g. Google search). IR can benefit from NER in two ways: recognizing named entities (NEs) within the searched documents, and then extracting the relevant documents considering their classified NEs and how they are related to the query (Rosso 2009a).</p>
<p>

<h3 style="font-size: 18px; text-align: center">
	II. Current NER solutions for Non-English texts and our approach.

</h3>
<h4 style="font-size: 17px; text-align: center">
II A. Theoretical background: other approaches towards NER of transliterations.
</h4>

<p>
Before exploring the technical implementation of the Spacy based 
system, it would be valuable to provide theoretical background 
into existing NER approaches for transliterated texts. 
We provide an introduction to the Spacy library and compare 
features of NLTK and Spacy.
</p>
<p>
Notably, the NER models for Arabic and transliterated texts (from 
Arabic to English and vice versa) are still underdeveloped. As 
most scientific studies are conducted in English in almost all 
Arabic-speaking countries, there is no urgency to investigate NER 
for Arabic and transliterated texts for many areas such as 
bioinformatics, drug or chemicals (Shaalan,2013). Numerous state 
sponsored initiatives have been created to encourage greater 
participation from NLP researchers. </p>
<p>
Currently, the task of recognizing transliterated entities 
(including English transliterations of Arabic words) has been 
dominated by NER models that devise an algorithm to tag foreign 
language entities (in this case, Arabic) using either (i) metadata 
from Wikipedia such as inter-wiki links, article categories, and 
cross language links or (ii) other parallel English-foreign 
language data. In the first approach, the model is trained on 
Wikipedia texts that are available in several languages and the 
NER of non-English and/or transliterated words are predicted based 
on the trained model. This approach has several limitations as 
Wikipedia information can be distributed unequally. Few Wikipedia 
contributors tend to work on the same language. Moreover, articles 
can have different content depending on the language: some 
countries do not allow articles on a certain topic or an article 
on divisive topics such as Crimea will contain different text 
depending on the language (e.g. Russian or English). Given these 
disparities, using Wikipedia articles available in several 
languages for training might not yield accurate results. Automatic 
translation seems as a possible solution for this approach, but 
also might yield inaccuracies. </p>
<p>
The second approach that involves training NER models on annotated 
data seems to be more reliable, however, there is a noticeable 
unavailability of tagged corpora for transliterated entities from 
Arabic to English. Moreover, the majority of the tagged corpora 
for Arabic, in general, features modern web content, where 
historical names of locations, cities (that frequently appear in 
the Lorimer’s Gazetteer) might be underrepresented. To address 
these limitations, in this project, we annotate the Lorimer’s 
Gazetteer and produce rich training data that tags most common 
historical transliterated Named Entities from the Lorimer’s 
Gazetteer. This NER training data and model can be of potential 
benefit to other projects working with historical or nonhistorical 
texts containing transliterated words.

</p>
<h4 style="font-size: 17px; text-align: center">II B. Technical implementation: Custom NER with Spacy.
</h4>
<p>
<h5 style="font-size: 16px; text-align: center"> 
What is Spacy? 
</h5>
To implement the second approach, particularly, to train a custom NER system, we decided to use the Spacy, an open-source library for advanced Natural Language Processing in Python designed for production use. Spacy, similarly to NLTK, provides a default model which can recognize named or numerical entities (e.g. person, organization, language, event etc). However, differently from NLTK, spaCy also allows adding arbitrary classes to the NER model, by training the model to update it with newer trained examples.

SpaCy’s named entity recognition has been trained on the OntoNotes 5 corpus and it supports the following entity types:

<figure>
  <img src="../assets/images/almablogSpacy1.png" style="width:420px;
height:200px;">
  <figcaption>Figure 2. A sample Information Extraction Architecture pipeline. Source: <a class="link" href="https://www.nltk.org/
book">NLTK textbook</a>.
</figcaption>
</figure>
</p>
<br/>

<h5 style="font-size: 16px"><i>Differences between NLTK and Spacy
</i></h5>
<p>TBD
</p> 
<h5 style="font-size: 16px"><i>Reading the files</i></h5>

<h3 style="font-size: 18px; text-align: center">
	III. System Description
  </h3>

<h4 style="font-size: 17px; text-align: center">
	Creating training data. 
  </h4>

<h5 style="font-size: 16px"><i> A. Create a training input file (txt) that contains target Named Entities.
</i></h5>
<p>
For this project, we annotate not all of the dataset (800+ text file) but a sample (4940 words) that contains all target NEs that we want our model to recognize.
This sample was created by merging paragraphs from some of the text files in the Lorimer’s dataset. In figure 2, you can view a screenshot of the input file.

</p><p>
It can be noticed that paragraphs from both Abadilah.txt and Abbadan.txt files were included in the training input file as these paragraphs contain target geographic Named Entities such as Najd, Persian Gulf, which were not tagged correctly by NLTK and that we aim Spacy model to correctly recognize.  The list of target NEs was provided by other student researchers and can be viewed here -it includes the names of main geographical locations - cities, countries and regions. </br>

Returning to the input file and figure 2, note that these paragraphs also contain information about tribes - an additional Named Entity type that we would like our model to recognize.
The final version of the input file prepared for annotation can be viewed here.

</p>
<h5 style="font-size: 16px"><i>   
B. Annotate the training input file and convert it to a json 
format.
</i></h5>
<p>
Note that our input file for training is in a txt format - we have to annotate this input file and transform it into a suitable json format for Spacy to process.<br/>

Spacy requires a training file to be a list of tuples or lists. Each tuple should contain the text and a dictionary; a dictionary has start, end indices of the Named Entity and the category or label of the Named Entity. In the figure 3, Elon Musk is a Person entity and London, Berlin are Loc entities.
<br/>
Figure 3. An example of training data in the json format required by Spacy.

</p>
<p>
As we work with a large amount of data, manual annotation is not an efficient solution. We use the NER Annotator, an open source platform to annotate and save results to a Spacy’s json format. NER Annotator requires the following steps:</p>
<p>
- Upload the input file - in our case we upload the input txt file from the earlier section.<br/>
- Create Named Entity tags. As mentioned earlier, for the Spacy model, compared to the NLTK default tag list, we can create our own Named Entity tags such as Tribe or Religion. We can annotate a subset of the data to tag these custom entities, train our model based on the annotations and retrieve these custom entities across the whole dataset.<br/>
- Annotate the text - we can annotate by line (can skip text) or the whole text as a string.<br/>
- Export annotations as a json file.<br/>
See figure 4 to view a screenshot of the NER annotator interface.
</p>
<p>
At this stage in the project, we introduce GPE_CUSTOM, LOC_CUSTOM, TRIBE Named Entities. ‘GPE_CUSTOM’ Named Entity tag refers to geo-political entities (e.g. cities, towns, countries) and is defined in the same way as the default GPE tag in Spacy; we add ‘custom’ suffix to differentiate two tags for potential finetuning possibilities in the future. Similarly, LOC_CUSTOM, refers to non-geo-political locations (e.g. plains, mountains, etc.). We also introduce the custom TRIBE tag, which is not defined in Spacy or NLTK. In the future, we can also introduce other tags referring to religion, environment variables, animal types, etc.
</p>
<p>
As we finish annotation of the input file, we export our results in a json format and the resulting training file can be viewed in figure 6. You can view the full file here.
</p>
