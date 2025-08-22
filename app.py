import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


def main():
    load_dotenv()

    st.set_page_config(page_title="Ask you csv 📊")
    st.header("Interact with your data")

    user_csv = st.file_uploader("Upload your csv data", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Interact with your data")

        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"), temperature=0)
        agent = create_csv_agent(llm, user_csv, verbose=True)

        if user_question is not None and user_question != "":
            # st.write(f"Your question was{user_question}")
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
