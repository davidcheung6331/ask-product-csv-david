import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import pandas as pd
import os
from PIL import Image
# import subprocess

st.set_page_config(
    page_title="Ask your CSV",
    page_icon="🗂",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Demo Page by AdCreativeDEv"
    }
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

image = Image.open("excel.png")
st.image(image, caption='created by MJ')

st.title("🗂 :blue[Ask your CSV file]")

with st.sidebar:    
    # Set API keys
    system_openai_api_key = os.environ.get('OPENAI_API_KEY')
    system_openai_api_key = st.text_input(":key: OpenAI Key :", value=system_openai_api_key)
    os.environ["OPENAI_API_KEY"] = system_openai_api_key
    st.divider()  
    st.text("Sample CSV file: ")
    image = Image.open("record.png")
    st.image(image, caption='Sample purchase-orders.csv')

    

filename = "purchase-orders.csv"
agent = create_csv_agent(OpenAI(openai_api_key=system_openai_api_key,temperature=0), 
                         filename, 
                         verbose=True)



query1 = "how many records  ?"
query2 = "how many female and male ?"
query3 = "Summarize the 3 Product Category, and display the name and its total count ?"
query4 = "how many females have stayed more than 3 years? "
query5 = "how many females from city category A purchase product_Category_1 ?"
query6 = "What is the total number of Product Category_1 purchased by female from city category B whose age is 0-17 ?"

Qstr1 = "Record Count ?"
Qstr2 = "Gender Classification ?"
Qstr3 = "Product Classification ?"
Qstr4 = "Customer Residencies classification ? "
Qstr5 = "Customer Purchase Record by Gender, City and Product ?"
Qstr6 = "Count of Product Category Purchase by Female with age between 0-17 ?"
Qstr7 = ""

# with st.expander("CSV file Content"):
#    df = pd.read_csv(filename)        
#    st.write(df.head(5))
    # st.write(df)

finalQuery = "Select Query Type"
queryselection =st.radio ("Sample Query : ",
                        (Qstr1, Qstr2, Qstr3, Qstr4, Qstr5))

# default choice
finalQuery = query1

if queryselection == Qstr1:
    finalQuery = query1

if queryselection == Qstr2:
    finalQuery = query2

if queryselection == Qstr3:
    finalQuery = query3

if queryselection == Qstr4:
    finalQuery = query4

if queryselection == Qstr5:
    finalQuery = query5


st.info(finalQuery, icon="ℹ️")

if st.button("Query"):
    finalResponse = agent.run(finalQuery)
    st.info(finalResponse, icon="ℹ️")
    # subprocess.call(["say", finalResponse])







log = """

how many females from city category A purchase product_Category_1 ?

> Entering new AgentExecutor chain...
Thought: I need to filter the dataframe to only include females from city category A
Action: python_repl_ast
Action Input: df[(df['Gender'] == 'F') & (df['City_Category'] == 'A')]['Product_Category_1'].count()
Observation: 35704

Thought: I now know the final answer

Final Answer: 35704 females from city category A purchase product_Category_1.

> Finished chain.

Q: Summarize the 3 Product Category, and display the name and its total count ?
> Entering new AgentExecutor chain...
Thought: I need to count the number of each Product Category
Action: python_repl_ast
Action Input: df['Product_Category_1'].value_counts()
Observation: 5     150933
1     140378
8     113925
11     24287
2      23864
6      20466
3      20213
4      11753
16      9828
15      6290
13      5549
10      5125
12      3947
7       3721
18      3125
20      2550
19      1603
14      1523
17       578
9        410
Name: Product_Category_1, dtype: int64
Thought: I need to count the number of each Product Category
Action: python_repl_ast
Action Input: df['Product_Category_2'].value_counts()
Observation: 8.0     64088
14.0    55108
2.0     49217
16.0    43255
15.0    37855
5.0     26235
4.0     25677
6.0     16466
11.0    14134
17.0    13320
13.0    10531
9.0      5693
12.0     5528
10.0     3043
3.0      2884
18.0     2770
7.0       626
Name: Product_Category_2, dtype: int64
Thought: I need to count the number of each Product Category
Action: python_repl_ast
Action Input: df['Product_Category_3'].value_counts()
Observation: 16.0    32636
15.0    28013
14.0    18428
17.0    16702
5.0     16658
8.0     12562
9.0     11579
12.0     9246
13.0     5459
6.0      4890
18.0     4629
4.0      1875
11.0     1805
10.0     1726
3.0       613
Name: Product_Category_3, dtype: int64
Thought: I now know the final answer


Final Answer: Product_Category_1 has 5, 1, 8, 11, 2, 6, 3, 4, 16, 15, 13, 10, 12, 7, 18, 20, 19, 14, 17, 9 as its categories with 150933, 140378, 113925, 24287, 23864, 20466, 20213, 11753, 9828, 6290, 5549, 5125, 3947, 3721, 3125, 2550, 1603, 1523, 578, and 410 counts respectively. Product_Category_2 has 8.0, 14.0, 2.0, 16.0, 15.0, 5.0, 4.0, 6.0, 11.0, 17.0, 13.0, 9.0, 12.0, 10.0, 3.0, 18.0, 7.0 as its categories with 64088, 55108, 49217, 43255, 37855, 26235, 25677, 16466, 14134, 13320, 10531, 5693, 5528, 3043, 2884, 2770, and 626 counts respectively. Product_

> Finished chain.




Q: how many females have stayed more than 3 years?

Entering new AgentExecutor chain...

Thought: I need to filter the dataframe to only include females who have stayed more than 3 years

Action: python_repl_ast

Action Input: df[(df['Gender'] == 'F') & (df['Stay_In_Current_City_Years'] == '4+')].shape[0]

Observation: 18596

Thought: I now know the final answer
Final Answer: 18596 females have stayed more than 3 years.

> Finished chain.

"""
with st.expander("explanation"):
    st.code(log)

