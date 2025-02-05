from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    pdf_loader = PyPDFLoader(q1_pdf)
    pdf_documents = pdf_loader.load()
    pdf_text_list = [doc.page_content for doc in pdf_documents]
    text_splitter = CharacterTextSplitter(
        separator="\n\n",  # 以換行符拆分
        chunk_size=1000,   # 設定每個文本塊的最大長度
        chunk_overlap=0, # 塊之間的重疊字數
        length_function=len, # 用於計算長度的函數
        is_separator_regex=False # 不使用正則表達式作為分隔符
    )
    pdf_texts = text_splitter.create_documents(pdf_text_list)
    return pdf_texts[len(pdf_texts)-1]

def hw02_2(q2_pdf):
    pdf_loader = PyPDFLoader(q2_pdf)
    pdf_documents = pdf_loader.load()
    pdf_text_list = [doc.page_content for doc in pdf_documents]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=20,   # 每個塊的最大字符數
        chunk_overlap=5, # 塊之間的重疊字符數
        separators=["\n\n", "第"], # 分隔符列表，按優先級排列
    )
    pdf_texts = text_splitter.create_documents(pdf_text_list)
    return len(pdf_texts)