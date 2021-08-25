---
layout: page
title: Creating Maps 
description: Lorimer Information  

nav-menu: false
---
<head>
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
<h3 style="font-size: 18px; text-align: center">I. Project Motivation<h3>
<p> 
This project sits at the intersection of Data Mining, Digital Humanities and Natural Language Processing, particularly, Information Extraction. We aim at detecting the geographical Named Entities from the John G. Lorimer's Gazetteer of the Persian Gulf, Central Arabia and Oman, a canonical artifact of British imperial knowledge production about the Gulf region, including contemporary Iran, Iraq and the GCC states. The dataset includes more than 800 text files pertaining to each geographical location. View more details about the dataset <a href="https://opengulf.github.io/lorimer/" class="link">here</a>.</p> 
<p> 
Whereas a group of researchers have been annotating the Gazetteer manually and in a semi-automated way using Recogito, an NER system with higher levels of automation would enable a more in-depth and computational approach to the analysis of the data. In particular, an automated NER system enables the extraction of an unprecedented amount of information in a short span of time and helps to navigate some of the limitations common for manual and semi-automated systems (continuous inter-annotation collaboration, time and labor constraints). Moreover, the output of the automated system, the dictionary of Named Entities from all text files allows reevaluating existing assumptions about the data, finding new patterns and answering research questions that would be considerably difficult to answer before (e.g. "How often text about location A references  location B?", "what is the connection between the text files" etc.). </p> 
<p> 
Moreover, the Gazetteer has an incomparably diverse and extensive set of geographical named entities that could be of great use for future visualization and data mining projects. You can also learn more about similar Data Mining projects in Humanities in this 
<a href="https://asistdl.onlinelibrary.wiley.com/doi/full/10.1002/bult.2012.1720380406" class="link">paper</a>. 
</p>

<h3 style="font-size: 18px; text-align: center"> II. What is NER and its importance<h3>
<p>
Named Entity Recognition (NER) is the task of locating, extracting and classifying names with a specific set of named entity types (e.g. Person, Organization, Location). This task can be broken down into two sub-tasks: identifying the boundaries of the named entity and identifying its type. Below are the most common types of Named Entities that are supported by NLTK,  Stanford CoreNLP and other libraries. 

</p>
<figure>
  <img src="../assets/images/almablog1.png" style="width:500px;
height:300px;">
  <figcaption>Figure 1. This table shows common Named Entities and their types. Credits to <a href="https://www.nltk.org/book">NLTK</a>.
</figcaption>
</figure>

<p>
	NER has valuable applications for many important NLP tasks with the most impactful being Information Retrieval, a task of identifying and retrieving documents based on a query (e.g. Google search). IR can benefit from NER in two ways: recognizing named entities (NEs) within the searched documents, and then extracting the relevant documents considering their classified NEs and how they are related to the query (Rosso 2009a).</p>
<p>
	<i>For example, the word “Aljazeera” can be tagged either as an Organization (news source) or as a Location (island) - correct NE tagging will facilitate extraction of the correct documents based on a query.</i></p>
	<p>
In these series of blog posts, we explore two Named Entity Recognition models: an NER model using NLTK (Natural Language Toolkit) and an NER model custom-trained for Arabic language using Spacy. 
</p>
<h3 style="font-size: 18px; text-align: center">
	III. Named Entity Recognition with NLTK
</h3>
<h4 style="font-size: 17px; text-align: center">III. A. About NLTK and its Information Extraction architecture, as outlined by NLTK</h4>

<p>
	The Natural Language Toolkit, or more commonly NLTK, is a set of libraries written in python for Natural Language Processing for English-language texts by Steven Bird and Edward Loper at the University of Pennsylvania. NLTK is a leading platform for many NLP tasks including Named Entity Recognition, therefore, an NER model based on NLTK can serve as a good baseline. However, as authors recognize themselves (NLTK, chapter 7), it is trained primarily on English language text and, thus, does not always predict Named Entity labels and values for foreign language or transliterated texts.
</p>
	<!--figure>
		<img src="../assets/images/nadasblog2.jpg" style="width:500px;height:300px;"><br>
		<img src="../assets/images/nadasblog3.jpg" style="width:500px;height:300px;">
		<figcaption>Both maps show the following villages: Shāt (شات) in <span style="color:#FF0000;">red</span>; Hammām (حمّام) in <span style="color:#0000FF;">blue</span>; Qurr (قرّ) in <span style="color:#FFFF00;">yellow</span>; Sibal (سبل) in <span style="color:#800080;">purple</span>; and Hida (حدا) in <span style="color:#FFA500;">orange</span>, before the path continues back along Route 25 in <span style="color:#008000;">green</span>.</figcaption>
	</figure-->
<h4 style="font-size: 17px; text-align: center">III. B. System description</h4>
<p>
Naturally, our NER model based on NLTK follows the Information Extraction Architecture outlined by NLTK:
<figure>
  <img src="../assets/images/almablog2.png" style="width:500px;
height:300px;">
  <figcaption>Figure 2. A sample Information Extraction Architecture pipeline. Credits to <a href="https://www.nltk.org/
book">NLTK</a>.
</figcaption>
</figure>
</p>
<p>
To summarize the steps, the system starts with <b>splitting the raw text</b> into words using a tokenizer (sometimes pre-segmenting text into sentences first). Next, each sentence is tagged with <b>part-of-speech tags</b>, which will prove very helpful in the next steps: <b>chunking</b> and finally <b>named entity detection</b>.
</p>
<h5 style="font-size: 16px"><i>Text preprocessing</i></h5>
<p>Firstly, to facilitate work of the classifier and convert input texts to the suitable format for NLTK, we need to preprocess input texts. After experiments and literature review, we performed the following preprocessing steps:<br/>
a. Transliterate common Arabic letters to English letters based on the list provided by Professor Wrisley. This step was introduced after the initial run of the system showed that entities starting with an Arabic letter are not recognized; for example, the word Ārabistan is not recognized. This could be potentially explained by the fact that the NLTK model is not trained on non-English words (see more in the ‘Flaws’ section).
<figure>
  <img src="../assets/images/almablog3.png" style="width:500px;
height:300px;">
  <figcaption>Figure 3. Conversion of Arabic letters to their English counterparts.</figcaption>
</figure>
b. Remove stop words. Stop words are defined as words that do not have semantic importance and are commonly removed in Information Retrieval tasks. In our model, we remove stop words defined by NLTK, which usually include pronouns, articles, etc. Learn more about stop words in NLTK <a class="link" href="https://pythonprogramming.net/stop-words-nltk-tutorial/">here</a>.<br/>
Based on the initial runs of the model, we also created our own list of stop words, which currently includes month and day of the week names. These words are recognized as a named entity by NLTK, but are not of interest for our current research questions. See figure <a href="../assets/images/almablog4.png">here</a>.
</p>
<h5 style="font-size: 16px"><i>Import libraries</i></h5>
<p> 
After preprocessing,  we import required libraries: we import nltk and also use glob, os, csv to handle file reading and writing. We load the nltk 'words' corpora to use the english language training corpus. We download the punkt library for sentence tokenization, averaged_perceptron_tagger for part of speech tagging and 'maxent_ne_chunker' for chunking the tokens using part of speech tags.
<figure>
  <img src="../assets/images/almablog5.png" 
style="width:500px;
height:300px;">
  <figcaption>Figure 5. List of libraries required for our model.</figcaption>
</figure>
</p> 
<h5 style="font-size: 16px"><i>Reading the files</i></h5>
<p>
We first define the file path and then use the glob library to iterate through each text file in the folder. We have also created entities_filtered and entity_name arrays to store the needed information for each file and ner_full and all_entity_names arrays to store information across all files - we will write our output to a csv file. Then, we clean the filename and finally read each file as a large string.
<figure>
  <img src="../assets/images/almablog6.png" 
style="width:500px;
height:300px;">
  <figcaption>Figure 6. Reading the input files and converting raw text to string.</figcaption>
</figure>
</p> 
<h5 style="font-size: 16px"><i>Tokenization</i></h5>
<p>
Tokenization refers to splitting the text into tokens, which is a sequence of characters that we want to treat as a group such as hairy, his, or :). In our model, we use the built-in word_tokenize function and below is the snippet of the code and output. Notice that NLTK tokens can include words, punctuation, apostrophes etc.
<figure>
  <img src="../assets/images/almablog7.png" 
style="width:500px;
height:300px;">
  <figcaption>Figure 7. Tokenization of the text and model output.</figcaption>
</figure>
</p> 
<h5 style="font-size: 16px"><i>Part of Speech tagging</i></h5>
<p> 
A part-of-speech tagger, or POS-tagger, processes a sequence of words, and attaches a part of speech tag to each word. NLTK provides documentation for each tag, which can be queried using the tag, e.g. nltk.help.upenn_tagset('NN'). Some corpora have README files with tagset documentation, see nltk.corpus.corpora_name.readme(). A list of most common NLTK part of speech tags can be viewed here:
<figure>
  <img src="../assets/images/almablog7.png" 
style="width:500px;
height:300px;">
  <figcaption>Figure 7. Tokenization of the text and model 
output.</figcaption>
</figure>
</p> 



	See the <a href="https://www.google.com/maps/d/u/0/viewer?mid=10lDPJuu5VnFO3ofcrBUYTWh3U6Ba-xj9&ll=23.110989824741395%2C58.662744400000015&z=10" class="link">Wadi Ta'iyin Map</a> and its corresponding <a href="https://github.com/opengulf/Lorimer_data/blob/master/Wadi_Al_Tayin.csv" class="link">dataset</a>.


	




