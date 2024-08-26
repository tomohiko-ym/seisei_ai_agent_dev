import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

# 認証情報の取得
try:
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    bq_client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    st.write("認証情報が正常にロードされました。")
except Exception as e:
    st.error(f"認証情報のロードに失敗しました: {e}")

st.write(credentials)
st.write(bq_client)

# クエリの実行
query = "Let's start analysis"
try:
    query_job = bq_client.query(query)
    results = query_job.result()
    st.write("クエリが正常に実行されました。")
except Exception as e:
    st.error(f"クエリの実行に失敗しました: {e}")

