{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO7RtV4SobEWeZ+HQbM3m24",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gwegayhu/dashboards-app/blob/master/Extract_Website_LDA_and_STM.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "\n",
        "# Replace with your website link\n",
        "url = \"https://www.ireadecdl.org/\"\n",
        "response = requests.get(url)\n",
        "\n",
        "# Parse the HTML content\n",
        "soup = BeautifulSoup(response.text, \"html.parser\")\n",
        "\n",
        "# Extract text data (e.g., paragraphs)\n",
        "text_data = [p.get_text() for p in soup.find_all(\"p\")]\n",
        "\n",
        "# Combine text data\n",
        "text_data_combined = \" \".join(text_data)\n",
        "\n",
        "# Save to a file for further analysis\n",
        "with open(\"website_data.txt\", \"w\", encoding=\"utf-8\") as file:\n",
        "    file.write(text_data_combined)\n"
      ],
      "metadata": {
        "id": "I5BTVTzJPlAC"
      },
      "execution_count": 64,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pip install selenium"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fhs-36XtPqiJ",
        "outputId": "4ea49fb5-5146-49ac-fb79-66b083930665"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting selenium\n",
            "  Downloading selenium-4.27.1-py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.10/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Collecting trio~=0.17 (from selenium)\n",
            "  Downloading trio-0.28.0-py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting trio-websocket~=0.9 (from selenium)\n",
            "  Downloading trio_websocket-0.11.1-py3-none-any.whl.metadata (4.7 kB)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.10/dist-packages (from selenium) (2024.12.14)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.10/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.10/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (24.3.0)\n",
            "Collecting sortedcontainers (from trio~=0.17->selenium)\n",
            "  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Collecting outcome (from trio~=0.17->selenium)\n",
            "  Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.2.2)\n",
            "Collecting wsproto>=0.14 (from trio-websocket~=0.9->selenium)\n",
            "  Downloading wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
            "Downloading selenium-4.27.1-py3-none-any.whl (9.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.7/9.7 MB\u001b[0m \u001b[31m58.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trio-0.28.0-py3-none-any.whl (486 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m486.3/486.3 kB\u001b[0m \u001b[31m29.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trio_websocket-0.11.1-py3-none-any.whl (17 kB)\n",
            "Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)\n",
            "Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)\n",
            "Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)\n",
            "Installing collected packages: sortedcontainers, wsproto, outcome, trio, trio-websocket, selenium\n",
            "Successfully installed outcome-1.3.0.post0 selenium-4.27.1 sortedcontainers-2.4.0 trio-0.28.0 trio-websocket-0.11.1 wsproto-1.2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install gensim nltk sklearn pyldavis\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hi-KlOA1PqlM",
        "outputId": "bd630917-cec2-47ef-a4c6-b8334bc15cf9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: gensim in /usr/local/lib/python3.10/dist-packages (4.3.3)\n",
            "Requirement already satisfied: nltk in /usr/local/lib/python3.10/dist-packages (3.9.1)\n",
            "Collecting sklearn\n",
            "  Using cached sklearn-0.0.post12.tar.gz (2.6 kB)\n",
            "  \u001b[1;31merror\u001b[0m: \u001b[1msubprocess-exited-with-error\u001b[0m\n",
            "  \n",
            "  \u001b[31m×\u001b[0m \u001b[32mpython setup.py egg_info\u001b[0m did not run successfully.\n",
            "  \u001b[31m│\u001b[0m exit code: \u001b[1;36m1\u001b[0m\n",
            "  \u001b[31m╰─>\u001b[0m See above for output.\n",
            "  \n",
            "  \u001b[1;35mnote\u001b[0m: This error originates from a subprocess, and is likely not a problem with pip.\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25herror\n",
            "\u001b[1;31merror\u001b[0m: \u001b[1mmetadata-generation-failed\u001b[0m\n",
            "\n",
            "\u001b[31m×\u001b[0m Encountered error while generating package metadata.\n",
            "\u001b[31m╰─>\u001b[0m See above for output.\n",
            "\n",
            "\u001b[1;35mnote\u001b[0m: This is an issue with the package mentioned above, not pip.\n",
            "\u001b[1;36mhint\u001b[0m: See above for details.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.corpus import stopwords\n",
        "from nltk.tokenize import word_tokenize\n",
        "from gensim.corpora import Dictionary\n",
        "from gensim.models.ldamodel import LdaModel\n",
        "\n",
        "# Preprocessing\n",
        "stop_words = set(stopwords.words(\"english\"))\n",
        "tokens = [word_tokenize(text.lower()) for text in text_data]\n",
        "tokens = [[word for word in token if word.isalpha() and word not in stop_words] for token in tokens]\n",
        "\n",
        "# Create dictionary and corpus for LDA\n",
        "dictionary = Dictionary(tokens)\n",
        "corpus = [dictionary.doc2bow(token) for token in tokens]\n"
      ],
      "metadata": {
        "id": "Ie01i3aYP50M"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Train an LDA model\n",
        "lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=15, passes=15)\n",
        "\n",
        "# Print topics\n",
        "for idx, topic in lda_model.print_topics(-1):\n",
        "    print(f\"Topic {idx}: {topic}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sJ9dcyD5P7UA",
        "outputId": "5acd612c-9ced-471c-a3bd-4c9823dfae02"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Topic 0: 0.006*\"designing\" + 0.006*\"greater\" + 0.006*\"specific\" + 0.006*\"track\" + 0.006*\"unprecedent\" + 0.006*\"adaptive\" + 0.006*\"change\" + 0.006*\"contextual\" + 0.006*\"customer\" + 0.006*\"pragmatically\"\n",
            "Topic 1: 0.085*\"ai\" + 0.044*\"pdf\" + 0.044*\"management\" + 0.044*\"rag\" + 0.044*\"generation\" + 0.044*\"lifeblood\" + 0.044*\"creativity\" + 0.044*\"thinking\" + 0.044*\"sparking\" + 0.044*\"data\"\n",
            "Topic 2: 0.038*\"enables\" + 0.038*\"term\" + 0.038*\"transcend\" + 0.038*\"short\" + 0.038*\"legacy\" + 0.038*\"confines\" + 0.038*\"businesses\" + 0.038*\"profits\" + 0.038*\"branding\" + 0.038*\"ai\"\n",
            "Topic 3: 0.097*\"signed\" + 0.050*\"transform\" + 0.050*\"gain\" + 0.050*\"come\" + 0.050*\"advantages\" + 0.050*\"us\" + 0.050*\"competitive\" + 0.050*\"ai\" + 0.050*\"business\" + 0.003*\"filler\"\n",
            "Topic 4: 0.106*\"ai\" + 0.071*\"business\" + 0.054*\"pragmind\" + 0.036*\"solutions\" + 0.036*\"copilot\" + 0.019*\"unlock\" + 0.019*\"high\" + 0.019*\"systems\" + 0.019*\"going\" + 0.019*\"years\"\n",
            "Topic 5: 0.145*\"filler\" + 0.075*\"info\" + 0.005*\"businesses\" + 0.005*\"ai\" + 0.005*\"give\" + 0.005*\"ideas\" + 0.005*\"creative\" + 0.005*\"creativity\" + 0.005*\"explore\" + 0.005*\"practices\"\n",
            "Topic 6: 0.056*\"driving\" + 0.056*\"automating\" + 0.056*\"innovation\" + 0.056*\"digital\" + 0.056*\"operations\" + 0.056*\"intelligence\" + 0.056*\"artificial\" + 0.056*\"business\" + 0.003*\"customer\" + 0.003*\"developments\"\n",
            "Topic 7: 0.073*\"cookies\" + 0.073*\"website\" + 0.073*\"use\" + 0.073*\"data\" + 0.073*\"sign\" + 0.038*\"accepting\" + 0.038*\"aggregated\" + 0.038*\"optimize\" + 0.038*\"user\" + 0.038*\"traffic\"\n",
            "Topic 8: 0.006*\"business\" + 0.006*\"research\" + 0.006*\"new\" + 0.006*\"enhance\" + 0.006*\"advance\" + 0.006*\"combines\" + 0.006*\"market\" + 0.006*\"field\" + 0.006*\"age\" + 0.006*\"approaches\"\n",
            "Topic 9: 0.006*\"designing\" + 0.006*\"greater\" + 0.006*\"specific\" + 0.006*\"track\" + 0.006*\"unprecedent\" + 0.006*\"adaptive\" + 0.006*\"change\" + 0.006*\"contextual\" + 0.006*\"customer\" + 0.006*\"pragmatically\"\n",
            "Topic 10: 0.110*\"business\" + 0.066*\"ai\" + 0.023*\"holds\" + 0.023*\"integration\" + 0.023*\"change\" + 0.023*\"contextual\" + 0.023*\"customer\" + 0.023*\"designing\" + 0.023*\"developments\" + 0.023*\"greater\"\n",
            "Topic 11: 0.047*\"ai\" + 0.047*\"research\" + 0.047*\"business\" + 0.024*\"pragmatics\" + 0.024*\"pdf\" + 0.024*\"specific\" + 0.024*\"diversify\" + 0.024*\"piece\" + 0.024*\"track\" + 0.024*\"ones\"\n",
            "Topic 12: 0.006*\"designing\" + 0.006*\"greater\" + 0.006*\"specific\" + 0.006*\"track\" + 0.006*\"unprecedent\" + 0.006*\"adaptive\" + 0.006*\"change\" + 0.006*\"contextual\" + 0.006*\"customer\" + 0.006*\"pragmatically\"\n",
            "Topic 13: 0.045*\"creative\" + 0.045*\"ideas\" + 0.045*\"give\" + 0.045*\"ai\" + 0.045*\"businesses\" + 0.023*\"right\" + 0.023*\"ton\" + 0.023*\"ways\" + 0.023*\"powerful\" + 0.023*\"business\"\n",
            "Topic 14: 0.053*\"ai\" + 0.027*\"explores\" + 0.027*\"importance\" + 0.027*\"focusing\" + 0.027*\"executives\" + 0.027*\"presentation\" + 0.027*\"strategic\" + 0.027*\"senior\" + 0.027*\"competitive\" + 0.027*\"potential\"\n"
          ]
        }
      ]
    },
    {
      "source": [
        "import nltk\n",
        "\n",
        "# Download the 'punkt_tab' data package\n",
        "nltk.download('punkt_tab')\n",
        "\n",
        "# ... (Rest of your existing code) ..."
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qb-cFyt5D5oZ",
        "outputId": "e34c4cba-50bb-4fb3-d6f8-3c92c36c810a"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n",
            "[nltk_data] Downloading package punkt_tab to /root/nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers/punkt_tab.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "source": [
        "# Install pyLDAvis if it's not already installed\n",
        "!pip install pyLDAvis\n",
        "\n",
        "# Import necessary packages\n",
        "from IPython import get_ipython\n",
        "from IPython.display import display\n",
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "from nltk.corpus import stopwords\n",
        "from nltk.tokenize import word_tokenize\n",
        "from gensim.corpora import Dictionary\n",
        "from gensim.models.ldamodel import LdaModel\n",
        "import pyLDAvis.gensim_models as gensimvis  # Use gensim_models for compatibility\n",
        "import pyLDAvis\n",
        "import pandas as pd\n",
        "\n",
        "# --- Web Scraping Code (Include this part from your previous cell) ---\n",
        "url = \"https://www.ireadecdl.org/\"\n",
        "response = requests.get(url)\n",
        "soup = BeautifulSoup(response.text, \"html.parser\")\n",
        "text_data = [p.get_text() for p in soup.find_all(\"p\")]  # Define text_data here\n",
        "\n",
        "# --- END OF WEB SCRAPING ---\n",
        "\n",
        "# Ensure your LDA model training code is included in this cell\n",
        "# --- START OF LDA MODEL TRAINING ---\n",
        "\n",
        "# Initialize stop words\n",
        "stop_words = set(stopwords.words(\"english\")) # Added this line to define stop_words\n",
        "\n",
        "tokens = [word_tokenize(text.lower()) for text in text_data]\n",
        "tokens = [[word for word in token if word.isalpha() and word not in stop_words] for token in tokens]\n",
        "\n",
        "# Create dictionary and corpus for LDA\n",
        "dictionary = Dictionary(tokens)\n",
        "corpus = [dictionary.doc2bow(token) for token in tokens]\n",
        "\n",
        "# Train an LDA model\n",
        "lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=15, passes=15)\n",
        "\n",
        "# Print topics (optional)\n",
        "for idx, topic in lda_model.print_topics(-1):\n",
        "    print(f\"Topic {idx}: {topic}\")"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XgfD-OdMEI3y",
        "outputId": "9feaa96c-8efa-419a-aeac-4d5ca65227b6"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pyLDAvis in /usr/local/lib/python3.10/dist-packages (3.4.1)\n",
            "Requirement already satisfied: numpy>=1.24.2 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.26.4)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.13.1)\n",
            "Requirement already satisfied: pandas>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (2.2.2)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (3.1.5)\n",
            "Requirement already satisfied: numexpr in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (2.10.2)\n",
            "Requirement already satisfied: funcy in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (2.0)\n",
            "Requirement already satisfied: scikit-learn>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.6.0)\n",
            "Requirement already satisfied: gensim in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (4.3.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (75.1.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyLDAvis) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyLDAvis) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyLDAvis) (2024.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn>=1.0.0->pyLDAvis) (3.5.0)\n",
            "Requirement already satisfied: smart-open>=1.8.1 in /usr/local/lib/python3.10/dist-packages (from gensim->pyLDAvis) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->pyLDAvis) (3.0.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=2.0.0->pyLDAvis) (1.17.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.10/dist-packages (from smart-open>=1.8.1->gensim->pyLDAvis) (1.17.0)\n",
            "Topic 0: 0.086*\"vision\" + 0.005*\"ict\" + 0.005*\"innovation\" + 0.005*\"driven\" + 0.005*\"embedding\" + 0.005*\"emerged\" + 0.005*\"enable\" + 0.005*\"future\" + 0.005*\"government\" + 0.005*\"contemporary\"\n",
            "Topic 1: 0.006*\"ict\" + 0.006*\"innovation\" + 0.006*\"designs\" + 0.006*\"driven\" + 0.006*\"embedding\" + 0.006*\"emerged\" + 0.006*\"enable\" + 0.006*\"future\" + 0.006*\"government\" + 0.006*\"conceptual\"\n",
            "Topic 2: 0.006*\"ict\" + 0.006*\"innovation\" + 0.006*\"designs\" + 0.006*\"driven\" + 0.006*\"embedding\" + 0.006*\"emerged\" + 0.006*\"enable\" + 0.006*\"future\" + 0.006*\"government\" + 0.006*\"conceptual\"\n",
            "Topic 3: 0.073*\"ict\" + 0.073*\"teachers\" + 0.038*\"development\" + 0.038*\"ecd\" + 0.038*\"education\" + 0.038*\"college\" + 0.038*\"also\" + 0.038*\"provide\" + 0.038*\"opportunities\" + 0.038*\"extensive\"\n",
            "Topic 4: 0.038*\"ecdl\" + 0.038*\"iread\" + 0.038*\"development\" + 0.038*\"uganda\" + 0.038*\"education\" + 0.020*\"empowering\" + 0.020*\"early\" + 0.020*\"childhood\" + 0.020*\"rural\" + 0.020*\"schools\"\n",
            "Topic 5: 0.065*\"approach\" + 0.065*\"triple\" + 0.065*\"tta\" + 0.065*\"innovative\" + 0.065*\"approaches\" + 0.004*\"ict\" + 0.004*\"government\" + 0.004*\"information\" + 0.004*\"emerged\" + 0.004*\"level\"\n",
            "Topic 6: 0.070*\"children\" + 0.070*\"class\" + 0.070*\"engaged\" + 0.070*\"ict\" + 0.004*\"driven\" + 0.004*\"embedding\" + 0.004*\"emerged\" + 0.004*\"enable\" + 0.004*\"future\" + 0.004*\"government\"\n",
            "Topic 7: 0.082*\"development\" + 0.055*\"early\" + 0.055*\"iread\" + 0.055*\"childhood\" + 0.029*\"design\" + 0.029*\"technologies\" + 0.029*\"available\" + 0.029*\"capability\" + 0.029*\"change\" + 0.029*\"curriculum\"\n",
            "Topic 8: 0.056*\"learning\" + 0.056*\"development\" + 0.056*\"ict\" + 0.038*\"early\" + 0.038*\"childhood\" + 0.020*\"enrich\" + 0.020*\"schools\" + 0.020*\"districts\" + 0.020*\"assisted\" + 0.020*\"support\"\n",
            "Topic 9: 0.039*\"early\" + 0.039*\"ecd\" + 0.039*\"learning\" + 0.039*\"every\" + 0.039*\"educators\" + 0.039*\"promote\" + 0.039*\"knowledge\" + 0.039*\"skills\" + 0.039*\"birth\" + 0.039*\"care\"\n",
            "Topic 10: 0.006*\"ltd\" + 0.006*\"childhood\" + 0.006*\"development\" + 0.006*\"iread\" + 0.006*\"early\" + 0.006*\"enable\" + 0.006*\"government\" + 0.006*\"future\" + 0.006*\"information\" + 0.006*\"embedding\"\n",
            "Topic 11: 0.038*\"early\" + 0.038*\"childhood\" + 0.038*\"ict\" + 0.026*\"development\" + 0.026*\"ecd\" + 0.026*\"approaches\" + 0.026*\"curriculum\" + 0.026*\"innovative\" + 0.013*\"principle\" + 0.013*\"one\"\n",
            "Topic 12: 0.031*\"children\" + 0.031*\"get\" + 0.031*\"airways\" + 0.031*\"opportunity\" + 0.031*\"learning\" + 0.031*\"colville\" + 0.031*\"ensure\" + 0.031*\"uganda\" + 0.031*\"access\" + 0.031*\"floor\"\n",
            "Topic 13: 0.006*\"ict\" + 0.006*\"innovation\" + 0.006*\"designs\" + 0.006*\"driven\" + 0.006*\"embedding\" + 0.006*\"emerged\" + 0.006*\"enable\" + 0.006*\"future\" + 0.006*\"government\" + 0.006*\"conceptual\"\n",
            "Topic 14: 0.064*\"learning\" + 0.033*\"materials\" + 0.033*\"locally\" + 0.033*\"vibrant\" + 0.033*\"sports\" + 0.033*\"practices\" + 0.033*\"moes\" + 0.033*\"ministry\" + 0.033*\"methodologies\" + 0.033*\"utilising\"\n"
          ]
        }
      ]
    },
    {
      "source": [
        "import nltk\n",
        "\n",
        "# Download the 'stopwords' dataset\n",
        "nltk.download('stopwords')\n",
        "\n",
        "# Install pyLDAvis if it's not already installed\n",
        "!pip install pyLDAvis\n",
        "\n",
        "# Import necessary packages\n",
        "from IPython import get_ipython\n",
        "from IPython.display import display\n",
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "from nltk.corpus import stopwords\n",
        "from nltk.tokenize import word_tokenize\n",
        "from gensim.corpora import Dictionary\n",
        "from gensim.models.ldamodel import LdaModel\n",
        "import pyLDAvis.gensim_models as gensimvis  # Use gensim_models for compatibility\n",
        "import pyLDAvis\n",
        "import pandas as pd\n",
        "\n",
        "# --- Web Scraping Code (Include this part from your previous cell) ---\n",
        "url = \"https://www.ireadecdl.org/\"\n",
        "response = requests.get(url)\n",
        "soup = BeautifulSoup(response.text, \"html.parser\")\n",
        "text_data = [p.get_text() for p in soup.find_all(\"p\")]  # Define text_data here\n",
        "\n",
        "# --- END OF WEB SCRAPING ---\n",
        "\n",
        "# Ensure your LDA model training code is included in this cell\n",
        "# --- START OF LDA MODEL TRAINING ---\n",
        "\n",
        "# Initialize stop words\n",
        "stop_words = set(stopwords.words(\"english\")) # Added this line to define stop_words\n",
        "\n",
        "tokens = [word_tokenize(text.lower()) for text in text_data]\n",
        "tokens = [[word for word in token if word.isalpha() and word not in stop_words] for token in tokens]\n",
        "\n",
        "# Create dictionary and corpus for LDA\n",
        "dictionary = Dictionary(tokens)\n",
        "corpus = [dictionary.doc2bow(token) for token in tokens]\n",
        "\n",
        "# Train an LDA model\n",
        "lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=15, passes=15)\n",
        "\n",
        "# Print topics (optional)\n",
        "for idx, topic in lda_model.print_topics(-1):\n",
        "    print(f\"Topic {idx}: {topic}\")\n",
        "\n",
        "# --- END OF LDA MODEL TRAINING ---\n",
        "\n",
        "\n"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eTrApv8iEcg_",
        "outputId": "70c424cc-a2fd-470f-de78-81db2273eca6"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n",
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Package stopwords is already up-to-date!\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pyLDAvis in /usr/local/lib/python3.10/dist-packages (3.4.1)\n",
            "Requirement already satisfied: numpy>=1.24.2 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.26.4)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.13.1)\n",
            "Requirement already satisfied: pandas>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (2.2.2)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (3.1.5)\n",
            "Requirement already satisfied: numexpr in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (2.10.2)\n",
            "Requirement already satisfied: funcy in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (2.0)\n",
            "Requirement already satisfied: scikit-learn>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (1.6.0)\n",
            "Requirement already satisfied: gensim in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (4.3.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from pyLDAvis) (75.1.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyLDAvis) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyLDAvis) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyLDAvis) (2024.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn>=1.0.0->pyLDAvis) (3.5.0)\n",
            "Requirement already satisfied: smart-open>=1.8.1 in /usr/local/lib/python3.10/dist-packages (from gensim->pyLDAvis) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->pyLDAvis) (3.0.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=2.0.0->pyLDAvis) (1.17.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.10/dist-packages (from smart-open>=1.8.1->gensim->pyLDAvis) (1.17.0)\n",
            "Topic 0: 0.086*\"ict\" + 0.065*\"development\" + 0.065*\"learning\" + 0.044*\"teachers\" + 0.044*\"assisted\" + 0.023*\"extensive\" + 0.023*\"utilising\" + 0.023*\"reversed\" + 0.023*\"provide\" + 0.023*\"opportunities\"\n",
            "Topic 1: 0.032*\"live\" + 0.032*\"quality\" + 0.032*\"development\" + 0.032*\"day\" + 0.032*\"habit\" + 0.032*\"made\" + 0.032*\"faculty\" + 0.032*\"ecd\" + 0.032*\"one\" + 0.032*\"early\"\n",
            "Topic 2: 0.055*\"development\" + 0.055*\"early\" + 0.037*\"childhood\" + 0.037*\"ecd\" + 0.037*\"iread\" + 0.019*\"learning\" + 0.019*\"curriculum\" + 0.019*\"design\" + 0.019*\"harness\" + 0.019*\"empowering\"\n",
            "Topic 3: 0.074*\"triple\" + 0.074*\"tta\" + 0.074*\"approach\" + 0.005*\"future\" + 0.005*\"enable\" + 0.005*\"ict\" + 0.005*\"government\" + 0.005*\"innovation\" + 0.005*\"emerged\" + 0.005*\"level\"\n",
            "Topic 4: 0.034*\"development\" + 0.034*\"iread\" + 0.034*\"childhood\" + 0.034*\"early\" + 0.034*\"airways\" + 0.034*\"colville\" + 0.034*\"box\" + 0.034*\"kampala\" + 0.034*\"house\" + 0.034*\"floor\"\n",
            "Topic 5: 0.046*\"education\" + 0.046*\"get\" + 0.046*\"opportunity\" + 0.046*\"learning\" + 0.046*\"childhood\" + 0.046*\"uganda\" + 0.046*\"access\" + 0.046*\"early\" + 0.046*\"assisted\" + 0.046*\"ensure\"\n",
            "Topic 6: 0.048*\"international\" + 0.048*\"looking\" + 0.048*\"advancing\" + 0.048*\"ahead\" + 0.048*\"continually\" + 0.048*\"country\" + 0.048*\"highest\" + 0.048*\"standards\" + 0.048*\"available\" + 0.048*\"resources\"\n",
            "Topic 7: 0.048*\"ict\" + 0.048*\"innovative\" + 0.048*\"approaches\" + 0.033*\"technology\" + 0.033*\"education\" + 0.033*\"early\" + 0.033*\"curriculum\" + 0.033*\"childhood\" + 0.017*\"societies\" + 0.017*\"empowering\"\n",
            "Topic 8: 0.064*\"learning\" + 0.033*\"materials\" + 0.033*\"locally\" + 0.033*\"vibrant\" + 0.033*\"sports\" + 0.033*\"practices\" + 0.033*\"moes\" + 0.033*\"ministry\" + 0.033*\"methodologies\" + 0.033*\"ict\"\n",
            "Topic 9: 0.006*\"ict\" + 0.006*\"innovation\" + 0.006*\"designs\" + 0.006*\"driven\" + 0.006*\"embedding\" + 0.006*\"emerged\" + 0.006*\"enable\" + 0.006*\"future\" + 0.006*\"government\" + 0.006*\"conceptual\"\n",
            "Topic 10: 0.119*\"children\" + 0.119*\"class\" + 0.062*\"engaged\" + 0.062*\"ict\" + 0.004*\"retention\" + 0.004*\"rate\" + 0.004*\"driven\" + 0.004*\"emerged\" + 0.004*\"teachers\" + 0.004*\"embedding\"\n",
            "Topic 11: 0.054*\"ecdl\" + 0.054*\"uganda\" + 0.054*\"iread\" + 0.054*\"development\" + 0.028*\"social\" + 0.028*\"significant\" + 0.028*\"contributed\" + 0.028*\"establishment\" + 0.028*\"education\" + 0.028*\"early\"\n",
            "Topic 12: 0.085*\"vision\" + 0.044*\"retention\" + 0.044*\"rates\" + 0.044*\"shown\" + 0.044*\"scored\" + 0.044*\"results\" + 0.044*\"work\" + 0.044*\"performance\" + 0.044*\"hard\" + 0.044*\"commitment\"\n",
            "Topic 13: 0.086*\"mission\" + 0.005*\"information\" + 0.005*\"level\" + 0.005*\"driven\" + 0.005*\"embedding\" + 0.005*\"emerged\" + 0.005*\"enable\" + 0.005*\"future\" + 0.005*\"government\" + 0.005*\"ict\"\n",
            "Topic 14: 0.006*\"principle\" + 0.006*\"example\" + 0.006*\"strive\" + 0.006*\"every\" + 0.006*\"ecdl\" + 0.006*\"intensively\" + 0.006*\"kyambogo\" + 0.006*\"iread\" + 0.006*\"something\" + 0.006*\"childhood\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pyldavis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i7vzXpGbFQPa",
        "outputId": "5e242e0c-ea1d-4385-d6cd-846176cecd22"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pyldavis in /usr/local/lib/python3.10/dist-packages (3.4.1)\n",
            "Requirement already satisfied: numpy>=1.24.2 in /usr/local/lib/python3.10/dist-packages (from pyldavis) (1.26.4)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.10/dist-packages (from pyldavis) (1.13.1)\n",
            "Requirement already satisfied: pandas>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from pyldavis) (2.2.2)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from pyldavis) (1.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from pyldavis) (3.1.5)\n",
            "Requirement already satisfied: numexpr in /usr/local/lib/python3.10/dist-packages (from pyldavis) (2.10.2)\n",
            "Requirement already satisfied: funcy in /usr/local/lib/python3.10/dist-packages (from pyldavis) (2.0)\n",
            "Requirement already satisfied: scikit-learn>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from pyldavis) (1.6.0)\n",
            "Requirement already satisfied: gensim in /usr/local/lib/python3.10/dist-packages (from pyldavis) (4.3.3)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.10/dist-packages (from pyldavis) (75.1.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyldavis) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyldavis) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0.0->pyldavis) (2024.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn>=1.0.0->pyldavis) (3.5.0)\n",
            "Requirement already satisfied: smart-open>=1.8.1 in /usr/local/lib/python3.10/dist-packages (from gensim->pyldavis) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->pyldavis) (3.0.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=2.0.0->pyldavis) (1.17.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.10/dist-packages (from smart-open>=1.8.1->gensim->pyldavis) (1.17.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pyLDAvis.gensim_models as gensimvis\n",
        "import pyLDAvis\n",
        "\n",
        "# Prepare visualization\n",
        "vis_data = gensimvis.prepare(lda_model, corpus, dictionary)\n",
        "pyLDAvis.display(vis_data)\n",
        "pyLDAvis.save_html(vis_data, \"lda_visualization.html\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iLGLUukUFTHi",
        "outputId": "cbe16dda-15f1-491f-ebc1-e657a6307aa7"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n"
          ]
        }
      ]
    },
    {
      "source": [
        "# Associate topics with metadata categories\n",
        "# Assuming you have a DataFrame or dictionary named 'your_metadata'\n",
        "# containing your document metadata, with a column named 'category'\n",
        "# Replace 'your_metadata' and 'category' with your actual variable and column name\n",
        "\n",
        "# IF you don't have any metadata about your documents:\n",
        "# YOU WILL NEED TO CREATE IT YOURSELF FROM YOUR WEBSCRAPING.\n",
        "# THIS DEPENDS ON THE CONTENT OF THE SCRAPED WEBSITE\n",
        "\n",
        "# Example metadata:\n",
        "# your_metadata = pd.DataFrame({'category': ['Education'] * len(text_data)}) # If you don't have any metadata, at least create some dummy data for the example to work\n",
        "\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "# Create some example metadata\n",
        "your_metadata = pd.DataFrame({'category': ['Education', 'News', 'Opinion', 'Technology', 'Business', 'Entertainment', 'Science', 'Sports', 'Health', 'Travel', 'Lifestyle', 'Food', 'Culture', 'Politics', 'Other'] * 2})\n",
        "\n",
        "your_metadata = your_metadata[:len(text_data)]  # Trim to match the number of documents\n",
        "\n",
        "document_topics = [max(lda_model[doc], key=lambda x: x[1]) for doc in corpus]\n",
        "topic_metadata = pd.DataFrame({\n",
        "    \"document_topic\": [topic[0] for topic in document_topics],\n",
        "    \"metadata\": your_metadata[\"category\"]  # Use your metadata variable here\n",
        "})\n",
        "\n",
        "# Analyze topic prevalence by metadata category\n",
        "print(topic_metadata.groupby(\"metadata\")[\"document_topic\"].value_counts())"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mVPh7R9nFllb",
        "outputId": "74b9dab2-5607-4855-89a6-dd4eeb4c0698"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "metadata       document_topic\n",
            "Business       0                 1\n",
            "               3                 1\n",
            "Culture        8                 1\n",
            "Education      7                 1\n",
            "               11                1\n",
            "Entertainment  8                 1\n",
            "               12                1\n",
            "Food           11                1\n",
            "Health         7                 1\n",
            "               14                1\n",
            "Lifestyle      8                 1\n",
            "News           4                 1\n",
            "               5                 1\n",
            "Opinion        4                 1\n",
            "               8                 1\n",
            "Other          5                 1\n",
            "Politics       4                 1\n",
            "Science        6                 1\n",
            "               11                1\n",
            "Sports         9                 1\n",
            "               12                1\n",
            "Technology     0                 1\n",
            "               14                1\n",
            "Travel         7                 1\n",
            "Name: count, dtype: int64\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n"
          ]
        }
      ]
    }
  ]
}