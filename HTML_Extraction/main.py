from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import docx2txt
# from bs4 import BeautifulSoup
# import requests
 
def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your Documents")
    st.header("Ask your Documents")
 
    # upload files
    uploaded_files = st.file_uploader("Upload your files", type=["pdf", "txt", "docx"], accept_multiple_files=True)
   
    # title = st.text_input("URL title")
    # st.write(title)
    # page = requests.get(title)
    # soup = BeautifulSoup(page.text, 'html')
    # st.write(soup)
 
    if uploaded_files:
        # extract text from uploaded files
        all_text = ""
        for uploaded_file in uploaded_files:
            if uploaded_file.type == "application/pdf":
                pdf_reader = PdfReader(uploaded_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
            elif uploaded_file.type == "text/plain":
                text = uploaded_file.read().decode("utf-8")
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = docx2txt.process(uploaded_file)
            else:
                st.write(f"Unsupported file type: {uploaded_file.name}")
                continue
            all_text += text
       
        if all_text.strip():  # Check if any text was extracted
            # split into chunks
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(all_text)
       
            if chunks:  # Ensure there are chunks to process
                # create embeddings
                embeddings = OpenAIEmbeddings()
                knowledge_base = FAISS.from_texts(texts=chunks, embedding=embeddings)
       
                # show user input
                user_question = st.text_input("Ask a question about the uploaded documents:")
                if user_question:
                    docs = knowledge_base.similarity_search(user_question)
                    if docs:  # Ensure similarity search returned results
                        llm = OpenAI()
                        chain = load_qa_chain(llm, chain_type="stuff")
                        with get_openai_callback() as cb:
                            response = chain.run(input_documents=docs, question=user_question)
                            print(response)
                   
                        st.write(response)
                    else:
                        st.write("No relevant information found in the documents.")
            else:
                st.write("No text chunks could be created from the uploaded documents.")
        else:
            st.write("No text could be extracted from the uploaded documents.")
    else:
        st.write("Please upload at least one document.")
 
if __name__ == '__main__':
    main()