# Streamlit N-gram Generator

This is a web-based N-gram Generator built using Streamlit, NLTK, Matplotlib, and WordCloud libraries in Python. The application allows users to input text, generate n-grams, visualize frequency distributions, and display word clouds based on the provided text.

## Features

- Input text area for users to input their desired text.
- Selection for N value to specify the size of n-grams (bi-grams, tri-grams, etc.).
- Tokenization methods available: `word_tokenize` and `custom_tokenize` (can be extended).
- Option to remove stopwords from the input text.
- Visualization of top 20 n-grams' frequency distribution using Matplotlib.
- Display of a word cloud representing the generated n-grams.

## Libraries/Frameworks Used

### Streamlit
- **Description**: Streamlit is an open-source Python library used to create web applications for machine learning and data science projects. It simplifies the process of turning data scripts into shareable web apps.

### NLTK (Natural Language Toolkit)
- **Description**: NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to linguistic resources and tools, including tokenization, stemming, tagging, parsing, and more.

### Matplotlib
- **Description**: Matplotlib is a comprehensive library for creating static, interactive, and animated visualizations in Python. It's widely used for generating plots, histograms, bar charts, and other graphical representations.

### WordCloud
- **Description**: WordCloud is a Python library used to generate word clouds from text. It allows the creation of visually appealing representations of word frequency in a given text by emphasizing frequently occurring words.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/streamlit-ngram-generator.git
    cd streamlit-ngram-generator
    ```

2. Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

After installing the dependencies, run the Streamlit application by executing the following command:
```bash
streamlit run app.py

## Contributing
Contributions are welcome! If you want to contribute to this project, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

-----------------------------------------------------------------------------------------------

Feel free to modify and expand the README file according to your specific project details, usage instructions, or any additional information you'd like to provide to potential users or contributors on GitHub.

