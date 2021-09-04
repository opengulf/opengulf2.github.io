---
layout: page
title: Custom Named Entity Recognition in Lorimer's Gazetteer with Spacy
description: NER Information

nav-menu: false
---

<head>
<style>
img, figure {
  display: block;
  margin-left: auto; 
  margin-right: auto; 
  text-align: center;  
}
</style>
</head>
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>Blogs</h1>
		</header>
<h2 id="content">Custom Named Entity Recognition in Lorimer's Gazetteer with Spacy</h2>
    <b>Alma Kapan</b>
    <br>
    <b>8-9-2021</b>

<h3 style="text-align: center">I. Project Motivation</h3>
<p> 
I. Project motivation.
This article is second in the series exploring automated Named Entity Recognition (NER) systems for the historical texts from the <a class="link" href="https://opengulf.github.io/lorimer/">Lorimer’s Gazetteer</a>. Although NLTK, as mentioned in the <a class="link" href="https://opengulf.github.io/Aug2021ner_spacy/">first blogpost</a>, provides one of the most well-recognized and used NER systems, there are several important reasons to explore other approaches due to NLTK’s limitations when applied to the Lorimer’s Gazetteer dataset.</p> 
<p> 
Firstly, most state-of-the-art systems such as NLTK were trained on English language texts : although such systems can accurately identify English Named Entities (NEs), they perform worse when applied to non-English, transliterated words. The Lorimer’s Gazetteer primarily contains geographical names that were transliterated from Arabic to English and NLTK tends to either incorrectly tag these words (a city tagged as a person) or not recognize them. Moreover, many NEs from the Lorimer’s Gazetteer mostly appear in the historical context and do not have a large web footprint, which might make these words (i) to be underrepresented in the training data for most modern systems and, consequently, (ii) not properly recognized by these systems. </p> 
<p> 
Moreover, in NLTK, types of recognizable NEs (e.g. location, organization) are predetermined and NLTK does not officially support custom training of the NER classifier to solve the above mentioned issues. In other words, it is not possible to train the system to recognize unfamiliar words or correct the NE labels (e.g. train to tag Oman not as a person, but a location). Also, even more importantly, it is not possible to introduce new Named Entity types such as tribe names or some environmental/cultural features such as religion. In order to address these limitations and create a more robust classifier, we introduced a custom-trained Spacy NER model for transliterated entities in the Lorimer’s Gazetteer.</p> 
<p> 
This project would be valuable to a larger research community in two ways. Firstly, recognition of transliterated entities, which describe foreign people, places etc., is useful for many applications such as cross language text retrieval and translation. This pipeline can be applied to other transliterated texts with changes to the training data. </p> 
<p> 
Secondly, the Lorimer’s Gazetteer is one of the most influential and well-documented sources on the Gulf States, Saudi Arabia and Persia: each text file in the Gazetteer corresponds to a certain location. Given this, extracting custom-trained entities (tribes, languages, environment features) for each of the locations from the Gazetteer would contribute to establishing a structure and connection across locations in the Middle East based on various environment, political, cultural, geographic features, which previously would be challenging due to time, labor constraints.
</p>
<h3 style="text-align: center">
	II. Current NER solutions for Non-English texts and our approach.

</h3>
<h5 style="text-align: center"> 
Theoretical background: other approaches towards NER of transliterations.
</h5>
<p>
Before exploring the technical implementation of the Spacy based system, it would be valuable to provide theoretical background into existing NER approaches for transliterated texts. We also provide an introduction to the Spacy library and compare features of NLTK and Spacy.
</p>
<p>
Notably, the NER models for Arabic and transliterated texts (from Arabic to English and vice versa) are still underdeveloped. As most scientific studies are conducted in English in almost all Arabic-speaking countries, there is no urgency to investigate NER for Arabic and transliterated texts for many areas such as bioinformatics, drug or chemicals <a class="link" href="https://aclanthology.org/J14-2008.pdf">(Shaalan, 2013)</a>. Numerous state sponsored <a class="link" href="https://www.topcoder.com/challenges/30087004">initiatives</a> have been created to encourage greater participation from NLP researchers. </p>
<p>
Currently, the task of recognizing transliterated entities (including English transliterations of Arabic words) has been dominated by NER models that devise an algorithm to tag foreign language entities (in this case, Arabic) using either (i) metadata from Wikipedia such as inter-wiki links, article categories, and cross language links or (ii) other parallel English-foreign language data. In the first approach, the model is trained on Wikipedia texts that are available in several languages and the NER of non-English and/or transliterated words are predicted based on the trained model. This approach has several limitations as Wikipedia information can be distributed unequally as few Wikipedia contributors tend to work on the same language. Moreover, articles can have different content depending on the language: some countries do not allow articles on certain topics or an article on a divisive topic such as Crimea contains different content depending on the language (e.g. Russian or English). Given these disparities, using Wikipedia articles available in several languages for training might not yield accurate results. Automatic translation seems as a possible solution for this approach, but also might yield <a class="link" href="https://www.theverge.com/2019/1/30/18195909/google-translate-ai-machine-learning-bias-religion-macduff-hughes-interview">inaccuracies</a>. </p>
<p>
The second approach that involves training NER models on annotated data seems to be more reliable, however, there is a noticeable unavailability of tagged corpora for transliterated entities from Arabic to English. Moreover, the majority of the tagged corpora for Arabic, in general, features <a class="link" href="https://direct.mit.edu/coli/article/40/2/469/1475/A-Survey-of-Arabic-Named-Entity-Recognition-and">modern web content</a>, where historical names of locations, cities (that frequently appear in the Lorimer’s Gazetteer) might be underrepresented. To address these limitations, in this project, we annotate the Lorimer’s Gazetteer and produce rich training data that tags historical, transliterated NEs from the Lorimer’s Gazetteer. This annotated dataset can further benefit other projects working on the historical or nonhistorical texts containing transliterated words. 
</p>

<h5 style="text-align: center"> 
What is Spacy? 
</h5>
<p>
To implement the second approach (discussed above), particularly, to build a custom NER system trained on the annotated data, we decided to use Spacy, an open-source library for advanced Natural Language Processing in Python designed for production use. Spacy, similarly to NLTK, provides a default model which can recognize named or numerical entities. However, in contrast to NLTK, spaCy also allows addition of arbitrary Named Entity categories to the NER model (can be same as default or new)and training and updating the model. Spacy’s named entity recognition has been trained on the <a class="link" href="https://catalog.ldc.upenn.edu/LDC2013T19">OntoNotes 5</a> corpus and it supports the following entity types:
</p>
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy1.png" style="width:350px;
height:450px;">
  <figcaption>
  Figure 1.  This table shows examples of named entities and their types supported by Spacy. 
</figcaption>
</figure>

<br/>

<h5 style="text-align: center;"><i>Differences between NLTK and Spacy
</i></h5>
<p>The table below illustrates main differences between two libraries. 
</p> 
<table style="width:100%">
  <tr>
    <th>NLTK</th>
    <th>Spacy</th>
  </tr>
  <tr>
    <td> - NLTK is a string processing library. It takes strings as input and returns strings or lists of strings as output. 
</td>
    <td> - Spacy uses an object-oriented approach. When we parse a text, spaCy returns a document object whose words and sentences are objects themselves.
</td>
    
  </tr>
  <tr>
    <td> - NLTK doesn’t have support for word vector
</td>
    <td> - Spacy has support for word vector</td>
   
  </tr>
  <tr>
  <td> - NLTK attempts to split the text into sentences.
  <br/><br/>
 - In sentence tokenization, NLTK outperforms Spacy.
</td>
  <td> - As spaCy uses the latest and best algorithms, its performance is usually good as compared to NLTK.<br/> <br/>
 - Spacy constructs a syntactic tree for each sentence, a more robust method that yields much more information about the text. <br/><br/>
 - In word tokenization and POS-tagging Spacy performs better.

</td>
  </tr>
</table>
<figcaption>Table 1. Comparison of NLTK and Spacy libraries</figcaption>
<br/><br/>
<h3 style="text-align: center">
	III. System Description
  </h3>
<p>Compared to the NLTK model, since we manually train our classifier, we firstly create training data based on the Lorimer’s Gazetteer using the NER Annotator and labelling the Named Entities and their tags. Then, we train the Spacy model on the created training data. Finally, we evaluate our model using a sample test file.
</p>
<h4 style="text-align: center">
	Creating training data. 
  </h4>
<p>
Creation of the training data has two stages: ii) create or 
select an input file that contains desired Named Entities 
that we want our model to recognize and ii) annotate the 
input file by tagging the target entities and converting it 
into a suitable training format.
</p>
<h5 style="text-align: center;"><i> A. Create a training input file (txt) that contains target Named Entities.
</i></h5>
<p>
For this project, we annotate not all of the dataset (800+ text file) but a sample (4940 words) that contains all target NEs that we want our model to recognize.
This sample was created by merging paragraphs from some of the text files in the Lorimer’s dataset. In figure 2, you can view a screenshot of the input file.
</p>
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy2.
png" style="width:470px;
height:420px;">
  <figcaption>
  Figure 2.  A screenshot from the txt input file used for training the Spacy model.
</figcaption>
</figure>
<br/><br/>
<p>
It can be noticed that paragraphs from both Abadilah.txt and Abbadan.txt files were included in the training input file as these paragraphs contain target geographic Named Entities such as Najd, Persian Gulf, which were not tagged correctly by NLTK and that we aim Spacy model to correctly recognize.  The list of target NEs was provided by other student researchers and can be viewed here -it includes the names of main geographical locations - cities, countries and regions. 
</p><p>
Returning to the input file and figure 2, note that these paragraphs also contain information about tribes - an additional Named Entity type that we would like our model to recognize.
The final version of the input file prepared for annotation can be viewed here.

</p>
<h5 style="text-align: center;"><i>   
B. Annotate the training input file and convert it to a json 
format.
</i></h5>
<p>
Note that our input file for training is in a txt format - we have to annotate this input file and transform it into a suitable json format for Spacy to process.
</p><p>
Spacy requires a training file to be a list of tuples or lists. Each tuple should contain the text and a dictionary; a dictionary has start, end indices of the Named Entity and the category or label of the Named Entity. In the figure 3, Elon Musk is a Person entity and London, Berlin are Loc entities.
</p>
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy3.
png" style="width:370px;
height:140px;">
  <figcaption>
  Figure 3. An example of training data in the json format 
required by Spacy.
</figcaption>
</figure>
<br/><br/>
<p>
As we work with a large amount of data, manual annotation is not an efficient solution. We use the NER Annotator, an open source platform to annotate and save results to a Spacy’s json format. NER Annotator requires the following steps:</p>
<p>
1. Upload the input file - in our case we upload the input txt file from the earlier section.<br/>
2. Create Named Entity tags. As mentioned earlier, for the Spacy model, compared to the NLTK default tag list, we can create our own Named Entity tags such as Tribe or Religion. We can annotate a subset of the data to tag these custom entities, train our model based on the annotations and retrieve these custom entities across the whole dataset.<br/>
3. Annotate the text - we can annotate by line (can skip text) or the whole text as a string.<br/>
4. Export annotations as a json file.<br/>
See figure 4 to view a screenshot of the NER annotator interface.
</p>
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy4.
png" style="width:900px;
height:300px;">
  <figcaption>
Figure 4.  The NER Annotator interface. A user can tag the Named Entities with custom tags.
</figcaption>
</figure>
<br/><br/>
<p>
At this stage in the project, we introduce GPE_CUSTOM, LOC_CUSTOM, TRIBE Named Entities. ‘GPE_CUSTOM’ Named Entity tag refers to geo-political entities (e.g. cities, towns, countries) and is defined in the same way as the default GPE tag in Spacy; we add ‘custom’ suffix to differentiate two tags for potential finetuning possibilities in the future. Similarly, LOC_CUSTOM, refers to non-geo-political locations (e.g. plains, mountains, etc.). We also introduce the custom TRIBE tag, which is not defined in Spacy or NLTK. In the future, we can also introduce other tags referring to religion, environment variables, animal types, etc.
</p>
<p>
As we finish annotation of the input file, we export our results in a json format and the resulting training file can be viewed in figure 6. You can view the full file here.
</p>
<h4 style="text-align: center">
	Import libraries.
  </h4>
<p>  
After creating the training data,  we can work on creating the Spacy NER model. Firstly, we import required libraries: we import the ‘spacy’ library for the NER recognition, ‘json’ library to handle reading and writing, ‘random’ library for randomizing the training data classes. We also load the ‘en_core_web_sm’ Spacy pipeline, which has a pre-trained NER model; the pipeline also has tagger, tokenizer, lemmatizer and other components. Finally, we import the ‘displacy’ library to visualize the Named Entity Recognition results.
</p> 
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy5.
png" style="width:340px;
height:170px;">
  <figcaption>
  Figure 5. Import libraries
</figcaption>
</figure>
<br/><br/>
<h4 style="text-align: center">
	Load training data.
  </h4>
<p>
As mentioned in the earlier section ‘Creating training data’,  we have created a json training file that follows the Spacy format for training. The resulting file is a dictionary of lists with each list corresponding to a text segment (in our example, text is divided into segments by lines); each text segment has a dictionary of entities and their locations (start, end index) in the text. 
</p>
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy6.
png" style="width:650px; height:450px;">
  <figcaption>
  Figure 6.  Output from the NER Annotator: training data in a json format specified by Spacy.
</figcaption>
</figure>
<br/><br/>
<h4 style="text-align: center">
	Using Spacy’s default Named Entity Recognition.
  </h4>
<p>
In the next blogpost, we outline in detail the steps for setting up blank and pretrained Custom NER models with Spacy - full pipeline can be viewed <a class="link" 
href="https://github.com/opengulf/opengulf.github.io/tree/master/pipelines/ner_nltk">here</a>. To view a glimpse into the system, in this article, we show how Spacy’s default NER pipeline, ‘en_core’ recognizes Named Entities. You can view the code in figure 7. We use the default model to recognize Named Entities from a file called ‘abbas_bandar.txt’ from the Lorimer’s Gazetteer dataset. A detailed overview of the functions and steps will be provided in the next blogpost. We also print the list of default Named Entities recognized by the model. 
</p>
<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy7.png" style="width:430px;
height:170px;">
  <figcaption>
  Figure 7.  Load the pretrained core pipeline and detect the Named Entities.
</figcaption>
</figure>
<br/><br/>
<p>
Then, we use the ‘displacy’ library to visualize the NER outputs - view the results in figure 8. 
</p>

<figure>
  <img src="../assets/images/alma_spacy_blog/almablogSpacy8.
png" style="width:750px;
height:350px;">
  <figcaption>
  Figure 8.  Named Entity Recognition by default en-core pipeline and visualization of the results.
</figcaption>
</figure>
<br/><br/>
<p>
Notably, the default, non-customized pipeline for Spacy is 
also trained on English corpus, thus, similarly to NLTK, 
some transliterated Named Entities such as Bandar Abbas are 
mislabelled (labelled as a person instead of location). 
Fortunately, compared to NLTK, Spacy allows custom training 
of the model, therefore, we are able to improve the results. 
As mentioned earlier, custom NER model setup will be 
explained in the next article.
</p>
<p>
  View the code for NER with Spacy pipeline in <a 
class="link" 
href="https://github.com/opengulf/opengulf.github.io/tree/master/pipelines/ner_spacy">this</a> github repository.
</p>
