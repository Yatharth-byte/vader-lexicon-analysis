import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

st.title("Sentimental Analysis Using Lexicon Based Approach...")
st.header("Please use proper spelling!")

iput = st.text_input("Enter Text:")
oput_dict =  analyzer.polarity_scores(iput)
col1, col2, col3 = st.beta_columns(3)

if st.button('Analyze'):
  
  with col1:
    st.header('**Negative** :angry:')
    st.header(int(oput_dict['neg']*100))
  with col2:
    st.header('**Neutral** :unamused:')
    st.header(int(oput_dict['neu']*100))
  with col3:
    st.header('**Positive** :smile:')
    st.header(int(oput_dict['pos']*100))
  if oput_dict['compound'] >= 0.05:
    st.write("Its ",int(oput_dict['pos']*100),"% Positive.")
  elif oput_dict['compound'] <= -0.05:
    st.write("Its ",int(oput_dict['neg']*100),"% Negative.")
  else:
    st.write("Its ",int(oput_dict['neu']*100),"% Neutral.") 
 
