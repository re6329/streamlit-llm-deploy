import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# 専門家リスト
expart_types = [
    "民俗学",
    "都市伝説",
    "心霊現象",
    "世界の歴史",
    "世界の宗教"
]

# 専門家LLMの回答を生成する関数
def llm_query(query, expert_type) :

    system_message = f"""
    あなたは{expert_type}の専門家です。
    以下の制約条件と入力文をもとに、{expert_type}の専門家として、正確かつ簡潔に回答してください。
    """

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=query)
    ]

    result = llm(messages)

    return result

# 環境変数読み込み
load_dotenv()

st.title("専門家LLMに質問してみよう！")

# 専門家タイプ選択（ラジオボタンに変更）
expert_type = st.radio("専門家を選んでください", expart_types)

# ユーザー入力
user_input = st.text_input("質問を入力してください")

# ↓↓ ボタン押下時の処理 ↓↓
if st.button("質問する") :

    if user_input.strip() == "" :
        st.warning("質問を入力してください")

    else :

        with st.spinner("専門家が回答中...") :

            result = llm_query(user_input, expert_type)

            st.success("回答が届きました！")

            st.write(f"### 専門家（{expert_type}）の回答")

            st.write(result.content)
