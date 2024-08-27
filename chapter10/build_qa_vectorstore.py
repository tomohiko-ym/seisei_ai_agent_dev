# GitHub: https://github.com/naotaka1128/llm_app_codes/chapter_010/build_qa_vectorstore.py


import pandas as pd
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

###### dotenv を利用しない場合は消してください ######
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    import warnings
    warnings.warn("dotenv not found. Please make sure to set your environment variables manually.", ImportWarning)
################################################

def main():
    # CSVファイルから「よくある質問」を読み込む
    file_path = "./chapter10/data/bearmobile_QA.csv"
    qa_df = pd.read_csv(file_path)  # question,answer

    # ベクトルDBに書き込むデータを作る
    qa_texts = []
    for _, row in qa_df.iterrows():
        qa_texts.append(f"question: {row['question']}\nanswer: {row['answer']}")

    # 上記のデータをベクトルDBに書き込む
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(qa_texts, embeddings)
    db.save_local('./chapter10/vectorstore/qa_vectorstore')


if __name__ == '__main__':
    main()
    print('done')
