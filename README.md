# Summarization-Gradio-HuggingFace

Summarizer...A Text/Article Summarizer Web App.
Using This Web App You can Summarize the infomation of any news article/blog or any long paragraphs seamlessly.
You can Also decide what should be minimum and maximum length of summarized text should be. I Created this projects using Hugging Face Inference api. 

Many Times when we have to read a log article or paragraph we maybe don't have enough time to read it. In those cases this will make it easier for you. 
You can generate the summary easily with the help of Summarizer.

Hugging Face Transforemers is based on Transformer model. It is a Library which provides us various AL Models which can be used in our project. 

For creating web app I Used Gradio. Gradio is an open-source Python package that allows you to quickly create easy-to-use, customizable UI components for your ML model, any API, or even an arbitrary Python function using a few lines of code.

I Use newspaper3k for scraping News Article and Blog.

Features:
* Easy To use. You just have to provide an url and minimum and maximum words. And Click Submit.
* It will provide you with the ouput of your desired text. If there is any error it will handle errors. 
* For this I Have Used Facebook/bart-large-cnn models. BART is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder.
*  BART is pre-trained by corrupting text with an arbitrary noising function, and learning a model to reconstruct the original text.
* I deployed using Hugging Face spaces. [Demo](https://lnkd.in/gdnbRhdP)




