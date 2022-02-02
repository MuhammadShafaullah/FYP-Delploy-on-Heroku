import streamlit as st
from PIL import Image
from PyPDF2 import PdfFileReader
import pdfplumber
import PyMuPDF
import docx2txt
import fitz
import re
import nltk.corpus
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from spacy.lang.en import English
import numpy as np
stop = stopwords.words('english')
img = Image.open("web_lo.png")
st.image(img, width=730)
html_temp = """
    <div style ="background-color:LightBlue;padding:0px">
    <h2 style ="color:green;text-align:center;">Privacy Policy Summary Generator Using ML</h2>
    </div>
    """
# this line allows us to display the front end aspects we have
# defined in the above code
st.markdown(html_temp, unsafe_allow_html=True)

def summarizer(text):
    data = text.replace("Chapter", "")
    data= ''.join([i for i in data if not i.isdigit()])

    nlp = English()
    nlp.add_pipe('sentencizer')
    doc = nlp(data.replace("\n", ""))
    sentences = [sent.text.strip() for sent in doc.sents]
    # Let's create an organizer which will store the sentence ordering to later reorganize the
    # scored sentences in their correct order

    sentence_organizer = {k: v for v, k in enumerate(sentences)}
    # Let's now create a tf-idf (Term frequnecy Inverse Document Frequency) model
    tf_idf_vectorizer = TfidfVectorizer(min_df=2, max_features=None,
                                        strip_accents='unicode',
                                        analyzer='word',
                                        token_pattern=r'\w{1,}',
                                        ngram_range=(1, 3),
                                        use_idf=1, smooth_idf=1,
                                        sublinear_tf=1,
                                        stop_words='english')
    # Passing our sentences treating each as one document to TF-IDF vectorizer
    tf_idf_vectorizer.fit(sentences)
    # Transforming our sentences to TF-IDF vectors
    sentence_vectors = tf_idf_vectorizer.transform(sentences)
    # Getting sentence scores for each sentences
    sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
    # Sanity checkup
    print(len(sentences) == len(sentence_scores))
    # Getting top-n sentences
    N = 2
    top_n_sentences = [sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
    # Let's now do the sentence ordering using our prebaked sentence_organizer
    # Let's map the scored sentences with their indexes
    mapped_top_n_sentences = [(sentence, sentence_organizer[sentence]) for sentence in top_n_sentences]
    # print("Our top_n_sentence with their index: \n")
    for element in mapped_top_n_sentences:
        print("Element len", len(element))
    # Ordering our top-n sentences in their original ordering
    mapped_top_n_sentences = sorted(mapped_top_n_sentences, key=lambda x: x[1])
    ordered_scored_sentences = [element[0] for element in mapped_top_n_sentences]
    # Our final summary
    summary = " ".join(ordered_scored_sentences)
    summary=" ".join(summary.split())
    st.text(summary)

st.subheader("DocumentFiles")
docx_file = st.file_uploader("Upload File", type=['txt', 'docx', 'pdf'])
if st.button("Process"):
    if docx_file is not None:
        file_details = {"Filename": docx_file.name, "FileType": docx_file.type, "FileSize": docx_file.size}
        st.write(file_details)
        # Check File Type
        if docx_file.type == "text/plain":

            raw_text = str(docx_file.read(), "utf-8")  # works with st.text and st.write,used for futher processing
            summarizer(raw_text)


        elif docx_file.type == "application/pdf":
            if docx_file is not None:
                doc = fitz.open(stream=docx_file.read(), filetype="pdf")
                text = ""
                for page in doc:
                    text += page.getText()
                summarizer(text)
                doc.close()

        elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            # Use the right file processor ( Docx,Docx2Text,etc)
            raw_text = docx2txt.process(docx_file)  # Parse in the uploadFile Class directory
            st.write(raw_text)

else:
    st.subheader("About")
    st.info("Supervised By: Mam Rabia Iftikhar")
    st.success("Muhammd Azeem (18SW62)")
    st.success("Abdul Qudoos (18SW145)")
