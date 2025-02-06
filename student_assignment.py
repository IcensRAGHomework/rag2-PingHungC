from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

# q1_pdf = "OpenSourceLicenses.pdf"
# q2_pdf = "勞動基準法.pdf"


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
    print(q2_pdf)
    pdf_loader = PyPDFLoader(q2_pdf)
    pdf_documents = pdf_loader.load()

    pdf_text_list = "\n".join(doc.page_content for doc in pdf_documents)

    text_splitter = RecursiveCharacterTextSplitter(
        separators=[r"\s+第"],
        chunk_size=5,
        chunk_overlap=0,
        is_separator_regex=True
    )
    
    pdf_texts = text_splitter.split_text(pdf_text_list)

    print(len(pdf_texts))
    for i in range(0, len(pdf_texts)):
        print("///////////////     chunk [%d]     ///////////////" % (i+1))
        print(pdf_texts[i])

    return len(pdf_texts)

# hw02_2(q2_pdf)