from pandasai.llm import GoogleGemini
# from pandasai.llm import OpenAI
import streamlit as st
import os
import pandas as pd
# from pandasai import SmartDataframe
from pandasai import Agent
from pandasai.responses.response_parser import  ResponseParser
# from pandasai.exceptions import InvalidOutputValueMismatch

from dotenv import load_dotenv

load_dotenv()

class StreamLitResponse(ResponseParser):
        def __init__(self,context) -> None:
              super().__init__(context)
        def format_dataframe(self,result):
               st.dataframe(result['value'])
               return
        def format_plot(self,result):
               st.image(result['value'])
               return
        def format_other(self, result):
               st.write(result['value'])
               return

gemini_api_key = os.environ['Gemini']
# openai_key = os.getenv("OpenAI")

def generateResponse(dataFrame,prompt):
        llm = GoogleGemini(api_key=gemini_api_key)
        # llm = OpenAI(api_token=openai_key)

        # pandas_agent = SmartDataframe(dataFrame,config={"llm":llm, "response_parser":StreamLitResponse})
        pandas_agent = Agent(dataFrame, config={"llm":llm, "response_parser":StreamLitResponse})
        answer = pandas_agent.chat(prompt)
        return answer


# Set the app tible and layout
st.set_page_config(page_title="Quantilytix Insights", page_icon="quant-logo.jpeg")

# Header section with logo and title
col1, col2 = st.columns([1, 8])
with col1:
       pass
#     st.image("quant-logo.jpeg", width=100)
with col2:
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <h1 style="margin: 0;">Quantilytix Insights</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


# st.write("# Quantilytix Insights")
st.write("##### Engage in insightful conversations with your data through powerful visualizations and analysis")
with st.sidebar:
        # st.title("Quantilytix Insights")
        st.image("quant-logo.jpeg", width=250)
        # Added a divider
        st.divider()
        # Add content to the sidebar/drawer
        # with st.expander("Data Visualization"):
        #     st.write("<div>Developed by - <span style=\"color: cyan; font-size: 24px; font-weight: 600;\">Quantilytix</span></div>",unsafe_allow_html=True)


# uploaded_file = "craig.xlsx"
uploaded_file = st.sidebar.file_uploader("Upload Your CSV File", type="csv")
if uploaded_file is not None:
        # Read the CSV file
        # df = pd.read_excel(uploaded_file)
        df = pd.read_csv(uploaded_file)

        # Display the data
        with st.expander("Preview", expanded=True):
            st.write(df.head())

        # Plot the data
        user_input = st.text_input("Type your message here",placeholder="Ask me about your data")
        with st.spinner("Generating response..."):
               if user_input:
                # try:
                        answer = generateResponse(dataFrame=df,prompt=user_input)
                        st.write(answer)
                # except InvalidOutputValueMismatch as e:
                        # st.image("./exports/charts/temp_chart.png")
                
else:
       st.write("Please upload a CSV file to begin.")

