import re
import gradio as gr
import pandas as pd

def proses_cleaning(inifilenya):
    # Import file csv ke Pandas
    df = pd.read_csv(inifilenya.name)

    # Ambil teks yang akan diproses dalam format list
    # bowo: Text_tweet
    # calier: text // text tweet
    # farid: ['Text tweet']
    
    #texts = df.Text_tweet.to_list()
    texts = df['Text_tweet'].to_list()

    # Lakukan cleansing pada teks
    cleaned_texttt = []
    for text in texts:
        cleaned_texttt.append(re.sub(r'https\S+|[^a-zA-Z0-9]', '', text))

    return cleaned_texttt

gradio_ui = gr.Interface(proses_cleaning, 
                        title="Data Processing and Modeling",
                        description="Aplikasi Web Data Processing dan Modeling",
                        inputs="file", 
                        outputs="json")

gradio_ui.launch()