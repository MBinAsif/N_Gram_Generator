import streamlit as st
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Disable the warning for using st.pyplot() without arguments
st.set_option('deprecation.showPyplotGlobalUse', False)

nltk.download('punkt')
nltk.download('stopwords')

def generate_ngrams(text, n, method, remove_stopwords):
    if method == 'word_tokenize':
        tokens = word_tokenize(text)
    elif method == 'custom_tokenize':
        # Implement your custom tokenization logic here if needed
        pass
    else:
        tokens = word_tokenize(text)  # Default to word_tokenize

    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.lower() not in stop_words]

    result = list(ngrams(tokens, n))
    freq_dist = FreqDist(result)

    # Create a dictionary from FreqDist ensuring elements are strings
    freq_dict = {str(gram): freq for gram, freq in freq_dist.items()}

    fig, ax = plt.subplots(figsize=(10, 6))
    freq_dist.plot(20, cumulative=False)
    plt.title(f"Top 20 {n}-grams")
    plt.xlabel("N-gram")
    plt.ylabel("Frequency")
    plt.tight_layout()
    st.pyplot(fig)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(freq_dict)
    st.image(wordcloud.to_array())

    return result

def main():
    st.title('Advanced N-gram Generator')

    text = st.text_area('Enter Text:')
    n = st.number_input('N value:', min_value=1, value=2)
    method = st.selectbox('Tokenization method:', ['word_tokenize', 'custom_tokenize'])
    remove_stopwords = st.checkbox('Remove stopwords')

    if st.button('Generate'):
        ngrams_result = generate_ngrams(text, n, method, remove_stopwords)
        st.write('Generated n-grams:')
        st.write(ngrams_result)

if __name__ == '__main__':
    main()
