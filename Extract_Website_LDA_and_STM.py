{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNLTFxzRNco7hiGacHqvgbW",
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
      "cell_type": "markdown",
      "source": [
        "Step 1: Install Required Libraries\n",
        "Install the necessary Python libraries:"
      ],
      "metadata": {
        "id": "tkxy2tLjI13g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from bs4 import BeautifulSoup\n",
        "import requests\n",
        "\n",
        "# Replace with your website link\n",
        "url = \"https://pragmind.org\"\n",
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
        "    file.write(text_data_combined)"
      ],
      "metadata": {
        "id": "I5BTVTzJPlAC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f97bb61f-9060-4676-f6bd-3e1e71705837"
      },
      "execution_count": 53,
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
      "cell_type": "code",
      "source": [
        "! pip install selenium"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fhs-36XtPqiJ",
        "outputId": "2804e579-850d-483b-c3e6-cd6fe55fbe6d"
      },
      "execution_count": 54,
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
            "Requirement already satisfied: selenium in /usr/local/lib/python3.10/dist-packages (4.27.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.26 in /usr/local/lib/python3.10/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (2.3.0)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.10/dist-packages (from selenium) (0.28.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.10/dist-packages (from selenium) (0.11.1)\n",
            "Requirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.10/dist-packages (from selenium) (2024.12.14)\n",
            "Requirement already satisfied: typing_extensions~=4.9 in /usr/local/lib/python3.10/dist-packages (from selenium) (4.12.2)\n",
            "Requirement already satisfied: websocket-client~=1.8 in /usr/local/lib/python3.10/dist-packages (from selenium) (1.8.0)\n",
            "Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (24.3.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (3.10)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
            "Requirement already satisfied: sniffio>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.3.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from trio~=0.17->selenium) (1.2.2)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.10/dist-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
            "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! pip install gensim nltk sklearn pyldavis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hi-KlOA1PqlM",
        "outputId": "fb7c4316-ed5e-410c-b438-beed970faa45"
      },
      "execution_count": 55,
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
      "cell_type": "markdown",
      "source": [
        "Step 2: Preprocess Text Data\n",
        "Preprocessing is crucial for topic modeling."
      ],
      "metadata": {
        "id": "lfl93sdIJDDA"
      }
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
        "id": "Ie01i3aYP50M",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2220ee97-6440-4d36-b7e8-a46acd3f1bf9"
      },
      "execution_count": 56,
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
      "cell_type": "markdown",
      "source": [
        "Step 3: Train an LDA Model with Metadata\n",
        "Add metadata by associating each document with covariates (e.g., category, sentiment)."
      ],
      "metadata": {
        "id": "DtsmIsRbJJ4v"
      }
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
        "outputId": "3d900d89-92e9-4fc1-e0ce-546edf0744fb"
      },
      "execution_count": 57,
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
            "Topic 0: 0.067*\"ai\" + 0.054*\"business\" + 0.027*\"new\" + 0.027*\"research\" + 0.014*\"unprecedent\" + 0.014*\"thrive\" + 0.014*\"skills\" + 0.014*\"unlock\" + 0.014*\"advance\" + 0.014*\"innovations\"\n",
            "Topic 1: 0.097*\"ai\" + 0.097*\"pdf\" + 0.050*\"management\" + 0.050*\"lifeblood\" + 0.050*\"generation\" + 0.050*\"data\" + 0.050*\"rag\" + 0.050*\"pragmatics\" + 0.003*\"including\" + 0.003*\"greater\"\n",
            "Topic 2: 0.066*\"pragmind\" + 0.066*\"copilot\" + 0.066*\"ai\" + 0.066*\"account\" + 0.066*\"info\" + 0.004*\"contextual\" + 0.004*\"adaptive\" + 0.004*\"change\" + 0.004*\"track\" + 0.004*\"unprecedent\"\n",
            "Topic 3: 0.108*\"filler\" + 0.056*\"get\" + 0.056*\"solutions\" + 0.056*\"deliver\" + 0.056*\"innovative\" + 0.056*\"business\" + 0.056*\"ai\" + 0.003*\"customer\" + 0.003*\"contextual\" + 0.003*\"unprecedent\"\n",
            "Topic 4: 0.006*\"designing\" + 0.006*\"greater\" + 0.006*\"specific\" + 0.006*\"track\" + 0.006*\"unprecedent\" + 0.006*\"adaptive\" + 0.006*\"change\" + 0.006*\"contextual\" + 0.006*\"customer\" + 0.006*\"pragmatically\"\n",
            "Topic 5: 0.045*\"ai\" + 0.045*\"creative\" + 0.045*\"ideas\" + 0.045*\"businesses\" + 0.045*\"give\" + 0.023*\"create\" + 0.023*\"practices\" + 0.023*\"business\" + 0.023*\"act\" + 0.023*\"developing\"\n",
            "Topic 6: 0.056*\"digital\" + 0.056*\"automating\" + 0.056*\"intelligence\" + 0.056*\"innovation\" + 0.056*\"operations\" + 0.056*\"driving\" + 0.056*\"artificial\" + 0.056*\"business\" + 0.004*\"filler\" + 0.004*\"signed\"\n",
            "Topic 7: 0.079*\"cookies\" + 0.079*\"website\" + 0.079*\"use\" + 0.079*\"data\" + 0.041*\"experience\" + 0.041*\"traffic\" + 0.041*\"accepting\" + 0.041*\"user\" + 0.041*\"optimize\" + 0.041*\"analyze\"\n",
            "Topic 8: 0.156*\"sign\" + 0.005*\"give\" + 0.005*\"businesses\" + 0.005*\"ideas\" + 0.005*\"creative\" + 0.005*\"ai\" + 0.005*\"steps\" + 0.005*\"critical\" + 0.005*\"significance\" + 0.005*\"ways\"\n",
            "Topic 9: 0.110*\"business\" + 0.066*\"ai\" + 0.023*\"holds\" + 0.023*\"integration\" + 0.023*\"change\" + 0.023*\"contextual\" + 0.023*\"customer\" + 0.023*\"designing\" + 0.023*\"developments\" + 0.023*\"greater\"\n",
            "Topic 10: 0.156*\"signed\" + 0.005*\"sign\" + 0.005*\"ai\" + 0.005*\"artificial\" + 0.005*\"innovation\" + 0.005*\"potential\" + 0.005*\"drives\" + 0.005*\"transformative\" + 0.005*\"executives\" + 0.005*\"collaboration\"\n",
            "Topic 11: 0.066*\"ai\" + 0.045*\"transform\" + 0.045*\"business\" + 0.045*\"competitive\" + 0.023*\"come\" + 0.023*\"advantages\" + 0.023*\"us\" + 0.023*\"gain\" + 0.023*\"ignite\" + 0.023*\"new\"\n",
            "Topic 12: 0.053*\"pragmind\" + 0.053*\"copilot\" + 0.053*\"growth\" + 0.053*\"sharpen\" + 0.053*\"sustainable\" + 0.053*\"solutions\" + 0.053*\"explores\" + 0.053*\"ai\" + 0.053*\"business\" + 0.003*\"data\"\n",
            "Topic 13: 0.050*\"term\" + 0.050*\"profits\" + 0.050*\"short\" + 0.050*\"enables\" + 0.050*\"transcend\" + 0.050*\"confines\" + 0.050*\"branding\" + 0.050*\"legacy\" + 0.050*\"businesses\" + 0.050*\"ai\"\n",
            "Topic 14: 0.059*\"city\" + 0.059*\"st\" + 0.059*\"internet\" + 0.059*\"falak\" + 0.059*\"dubai\" + 0.059*\"uae\" + 0.059*\"al\" + 0.004*\"pragmatically\" + 0.004*\"research\" + 0.004*\"unprecedent\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Step 4: Visualize Topics\n",
        "You can use pyLDAvis to visualize the topics."
      ],
      "metadata": {
        "id": "XA2YdeC2JVM3"
      }
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
        "outputId": "b8ccbbcd-dab2-4b91-a76f-9620189e735b"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/ipykernel/ipkernel.py:283: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.\n",
            "  and should_run_async(code)\n",
            "[nltk_data] Downloading package punkt_tab to /root/nltk_data...\n",
            "[nltk_data]   Package punkt_tab is already up-to-date!\n"
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
          "execution_count": 58
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
        "url = \"https://pragmind.org/\"\n",
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
        "outputId": "89d7f644-f3e4-4ba8-80ac-401fc9912463"
      },
      "execution_count": 63,
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
            "Topic 0: 0.006*\"give\" + 0.006*\"businesses\" + 0.006*\"creative\" + 0.006*\"ai\" + 0.006*\"ideas\" + 0.006*\"information\" + 0.006*\"organizations\" + 0.006*\"springboards\" + 0.006*\"right\" + 0.006*\"steps\"\n",
            "Topic 1: 0.070*\"ai\" + 0.070*\"rights\" + 0.070*\"reserved\" + 0.070*\"pragmind\" + 0.004*\"website\" + 0.004*\"use\" + 0.004*\"cookies\" + 0.004*\"data\" + 0.004*\"optimize\" + 0.004*\"traffic\"\n",
            "Topic 2: 0.087*\"account\" + 0.005*\"designing\" + 0.005*\"greater\" + 0.005*\"specific\" + 0.005*\"track\" + 0.005*\"unprecedent\" + 0.005*\"adaptive\" + 0.005*\"change\" + 0.005*\"contextual\" + 0.005*\"customer\"\n",
            "Topic 3: 0.059*\"transform\" + 0.059*\"late\" + 0.059*\"ignite\" + 0.059*\"thinking\" + 0.059*\"ways\" + 0.059*\"new\" + 0.059*\"business\" + 0.004*\"track\" + 0.004*\"satisfaction\" + 0.004*\"unprecedent\"\n",
            "Topic 4: 0.156*\"filler\" + 0.005*\"customer\" + 0.005*\"research\" + 0.005*\"specific\" + 0.005*\"track\" + 0.005*\"unprecedent\" + 0.005*\"adaptive\" + 0.005*\"change\" + 0.005*\"contextual\" + 0.005*\"developments\"\n",
            "Topic 5: 0.056*\"ai\" + 0.056*\"business\" + 0.056*\"signed\" + 0.029*\"immense\" + 0.029*\"future\" + 0.029*\"potential\" + 0.029*\"skills\" + 0.029*\"sustaining\" + 0.029*\"businesses\" + 0.029*\"unlock\"\n",
            "Topic 6: 0.070*\"ai\" + 0.036*\"competitive\" + 0.035*\"data\" + 0.035*\"cookies\" + 0.035*\"use\" + 0.035*\"website\" + 0.018*\"business\" + 0.018*\"potential\" + 0.018*\"gain\" + 0.018*\"advantages\"\n",
            "Topic 7: 0.116*\"business\" + 0.078*\"ai\" + 0.040*\"solutions\" + 0.020*\"get\" + 0.020*\"innovative\" + 0.020*\"deliver\" + 0.020*\"significant\" + 0.020*\"sophisticated\" + 0.020*\"promise\" + 0.020*\"advantages\"\n",
            "Topic 8: 0.059*\"ai\" + 0.059*\"pdf\" + 0.059*\"generation\" + 0.059*\"management\" + 0.059*\"lifeblood\" + 0.059*\"rag\" + 0.059*\"data\" + 0.004*\"business\" + 0.004*\"demand\" + 0.004*\"new\"\n",
            "Topic 9: 0.006*\"business\" + 0.006*\"ai\" + 0.006*\"designing\" + 0.006*\"solutions\" + 0.006*\"including\" + 0.006*\"competitive\" + 0.006*\"landscape\" + 0.006*\"ultimately\" + 0.006*\"greater\" + 0.006*\"satisfaction\"\n",
            "Topic 10: 0.052*\"ai\" + 0.035*\"creativity\" + 0.035*\"critical\" + 0.035*\"thinking\" + 0.035*\"creative\" + 0.035*\"ideas\" + 0.035*\"give\" + 0.035*\"businesses\" + 0.018*\"st\" + 0.018*\"uae\"\n",
            "Topic 11: 0.006*\"designing\" + 0.006*\"greater\" + 0.006*\"specific\" + 0.006*\"track\" + 0.006*\"unprecedent\" + 0.006*\"adaptive\" + 0.006*\"change\" + 0.006*\"contextual\" + 0.006*\"customer\" + 0.006*\"pragmatically\"\n",
            "Topic 12: 0.092*\"ai\" + 0.062*\"copilot\" + 0.062*\"pragmind\" + 0.032*\"businesses\" + 0.032*\"business\" + 0.032*\"legacy\" + 0.032*\"branding\" + 0.032*\"confines\" + 0.032*\"enables\" + 0.032*\"profits\"\n",
            "Topic 13: 0.056*\"business\" + 0.056*\"automating\" + 0.056*\"innovation\" + 0.056*\"digital\" + 0.056*\"operations\" + 0.056*\"driving\" + 0.056*\"intelligence\" + 0.056*\"artificial\" + 0.003*\"developments\" + 0.003*\"designing\"\n",
            "Topic 14: 0.048*\"business\" + 0.048*\"research\" + 0.048*\"sign\" + 0.025*\"piece\" + 0.025*\"methods\" + 0.025*\"ones\" + 0.025*\"order\" + 0.025*\"keep\" + 0.025*\"track\" + 0.025*\"specific\"\n"
          ]
        }
      ]
    },
    {
      "source": [
        "import pyLDAvis.gensim_models as gensimvis\n",
        "import pyLDAvis\n",
        "import numpy as np\n",
        "\n",
        "# Prepare visualization\n",
        "vis_data = gensimvis.prepare(lda_model, corpus, dictionary, mds='mmds')\n",
        "# The 'mds' parameter specifies the multidimensional scaling algorithm to use.\n",
        "# 'mmds' is a good alternative that often avoids complex numbers.\n",
        "\n",
        "\n",
        "# If the above doesn't solve the issue, you might need to manually convert\n",
        "# complex numbers to real numbers within the vis_data object before displaying:\n",
        "\n",
        "# This is a simplified example, you might need to adjust based on the structure of vis_data\n",
        "for key in vis_data.topic_coordinates.keys():\n",
        "    if isinstance(vis_data.topic_coordinates[key], np.complex128):\n",
        "        vis_data.topic_coordinates[key] = np.real(vis_data.topic_coordinates[key])\n",
        "\n",
        "pyLDAvis.display(vis_data)\n",
        "pyLDAvis.save_html(vis_data, \"lda_visualization.html\")"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "izzFzSDJKZMR",
        "outputId": "57c1fc5e-a20c-4fca-c948-80fb3d9475eb"
      },
      "execution_count": 49,
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
      "cell_type": "markdown",
      "source": [
        "Step 5: Analysis\n",
        "You can analyze topic prevalence using the metadata:"
      ],
      "metadata": {
        "id": "wwTHl8oIJfs0"
      }
    },
    {
      "source": [
        "# Associate topics with metadata categories\n",
        "document_topics = [max(lda_model[doc], key=lambda x: x[1]) for doc in corpus]\n",
        "\n",
        "# Create a placeholder for metadata or load your actual metadata here\n",
        "# Example: Ensure metadata length matches document_topics length\n",
        "# Adjust the categories and repetition as needed to match your actual metadata\n",
        "metadata = pd.DataFrame({'category': ['AI', 'Business', 'Digital', 'Technology'] * (len(document_topics) // 4)})\n",
        "\n",
        "# If len(document_topics) is not divisible by 4, adjust to match lengths\n",
        "remainder = len(document_topics) % 4\n",
        "if remainder != 0:\n",
        "    metadata = pd.DataFrame({'category': (['AI', 'Business', 'Digital', 'Technology'] * (len(document_topics) // 4)) + ['AI', 'Business', 'Digital', 'Technology'][:remainder]})\n",
        "\n",
        "topic_metadata = pd.DataFrame({\n",
        "    \"document_topic\": [topic[0] for topic in document_topics],\n",
        "    \"metadata\": metadata[\"category\"]  # metadata now has the correct length\n",
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
        "id": "EFINcd2aOIed",
        "outputId": "5b78bfd4-fcdf-4fad-8fa6-07eaf7eb5ad7"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "metadata    document_topic\n",
            "AI          6                 2\n",
            "            4                 1\n",
            "            5                 1\n",
            "            10                1\n",
            "            12                1\n",
            "            14                1\n",
            "Business    7                 2\n",
            "            0                 1\n",
            "            2                 1\n",
            "            4                 1\n",
            "            6                 1\n",
            "            10                1\n",
            "Digital     14                2\n",
            "            1                 1\n",
            "            3                 1\n",
            "            6                 1\n",
            "            10                1\n",
            "            12                1\n",
            "Technology  5                 2\n",
            "            0                 1\n",
            "            6                 1\n",
            "            8                 1\n",
            "            12                1\n",
            "            13                1\n",
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
    },
    {
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# ... (Your existing code to create 'topic_metadata' DataFrame) ...\n",
        "\n",
        "# Display topic prevalence in a table\n",
        "topic_prevalence_table = topic_metadata.groupby(\"metadata\")[\"document_topic\"].value_counts().unstack(fill_value=0)\n",
        "print(\"Topic Prevalence Table:\")\n",
        "display(topic_prevalence_table)  # Use display for better formatting in Jupyter\n",
        "\n",
        "# Plot topic prevalence using a heatmap\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.heatmap(topic_prevalence_table, annot=True, cmap=\"YlGnBu\", fmt=\"d\")\n",
        "plt.title(\"Topic Prevalence by Metadata Category\")\n",
        "plt.xlabel(\"Topic\")\n",
        "plt.ylabel(\"Metadata Category\")\n",
        "plt.show()\n",
        "\n",
        "# Plot topic prevalence using a bar plot\n",
        "topic_prevalence_table.plot(kind=\"bar\", stacked=True, figsize=(10, 6))\n",
        "plt.title(\"Topic Prevalence by Metadata Category\")\n",
        "plt.xlabel(\"Metadata Category\")\n",
        "plt.ylabel(\"Number of Documents\")\n",
        "plt.legend(title=\"Topic\")\n",
        "plt.show()"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1457
        },
        "id": "OjaLIGj0OWNK",
        "outputId": "6bd5ffd7-9e8f-4331-ca82-a5e7abd6cceb"
      },
      "execution_count": 78,
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
            "Topic Prevalence Table:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "document_topic  0   1   2   3   4   5   6   7   8   10  12  13  14\n",
              "metadata                                                          \n",
              "AI               0   0   0   0   1   1   2   0   0   1   1   0   1\n",
              "Business         1   0   1   0   1   0   1   2   0   1   0   0   0\n",
              "Digital          0   1   0   1   0   0   1   0   0   1   1   0   2\n",
              "Technology       1   0   0   0   0   2   1   0   1   0   1   1   0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2da67384-6605-425f-a6ff-59f67ddde6b7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th>document_topic</th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "      <th>3</th>\n",
              "      <th>4</th>\n",
              "      <th>5</th>\n",
              "      <th>6</th>\n",
              "      <th>7</th>\n",
              "      <th>8</th>\n",
              "      <th>10</th>\n",
              "      <th>12</th>\n",
              "      <th>13</th>\n",
              "      <th>14</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>metadata</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>AI</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Business</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Digital</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Technology</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2da67384-6605-425f-a6ff-59f67ddde6b7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-2da67384-6605-425f-a6ff-59f67ddde6b7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-2da67384-6605-425f-a6ff-59f67ddde6b7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-771aaced-e36b-411e-a608-5f3b7d2b18bb\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-771aaced-e36b-411e-a608-5f3b7d2b18bb')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-771aaced-e36b-411e-a608-5f3b7d2b18bb button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_c60354c7-f7e6-4be2-b4e9-86581e25622e\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('topic_prevalence_table')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_c60354c7-f7e6-4be2-b4e9-86581e25622e button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('topic_prevalence_table');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "topic_prevalence_table",
              "summary": "{\n  \"name\": \"topic_prevalence_table\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": \"metadata\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Business\",\n          \"Technology\",\n          \"AI\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 0,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 1,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 2,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 3,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 4,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 5,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 2,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 6,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 2,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 7,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 0,\n        \"max\": 2,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          2,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 8,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 10,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 12,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 13,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 14,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 2,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAxEAAAIjCAYAAAB8opZ0AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAfVVJREFUeJzt3Xl8TGf///H3JGRBErEmsca+RpRSUUWLWGppe1t7SyxVLaqVotWW0C2oElqlVCm1d6GLUrXeSmmR2qp2WntVEoJEk/P7w898M02YmUicTLyefZxHM9ecOfOeyxH55DrXdSyGYRgCAAAAAAe5mR0AAAAAgGuhiAAAAADgFIoIAAAAAE6hiAAAAADgFIoIAAAAAE6hiAAAAADgFIoIAAAAAE6hiAAAAADgFIoIAAAAAE6hiABykTlz5shisejYsWNmRzFVs2bN1KxZM7Nj3LHy5cvr0UcfNTtGrmaxWDR69GizYwAAnEQRAdyCxWJxaFu/fr3ZUTN1syC5uXl5ealKlSoaNGiQzp49a3Y8ZJNjx45Z/4zffPPNTPd58sknZbFYVKhQoSy9x4oVK3LdD/r79u3T6NGjc6zgPnz4sPr3768KFSrIy8tLvr6+aty4sSZPnqyrV686fbwPPvhAc+bMyf6gAGCSfGYHAHKrefPm2TyeO3euVq9enaG9evXq2faePXv2VLdu3eTp6Zltx3z99dcVHBysa9euadOmTZo2bZpWrFihPXv2qECBAtn2PjCXl5eXFi5cqNdee82mPSkpScuXL5eXl1eWj71ixQpNnTo1VxUS+/bt05gxY9SsWTOVL18+W4/97bffqnPnzvL09FRERIRq1aqllJQUbdq0ScOGDdPevXs1Y8YMp475wQcfqFixYurVq1e2ZgUAs1BEALfw3//+1+bxTz/9pNWrV2doz07u7u5yd3fP1mO2adNG9evXlyQ99dRTKlq0qCZOnKjly5ere/fumb4mKSlJBQsWzNYcyFlt27bVF198oV9//VV16tSxti9fvlwpKSlq3bq11q5da2JC13D06FF169ZN5cqV09q1axUYGGh9buDAgTp06JC+/fZbExPmLP7uA3AUlzMBdyApKUkvvviiypQpI09PT1WtWlUTJkyQYRg2+1ksFg0aNEjz589X1apV5eXlpXr16mnjxo02+91qTsR3332npk2bysfHR76+vrr//vu1YMGCLGV++OGHJd34YUmSevXqpUKFCunw4cNq27atfHx89OSTT0qS0tLSFBsbq5o1a8rLy0slS5ZU//79dfHiRevxHn30UVWoUCHT92rUqJG1gJGk2bNn6+GHH1aJEiXk6empGjVqaNq0aQ7lTk5OVnR0tCpVqiRPT0+VKVNGw4cPV3Jyss1+N/t62bJlqlWrljw9PVWzZk2tXLkywzFPnjypvn37KigoSJ6engoODtazzz6rlJQU6z7x8fF64YUXrH/GlSpV0rhx45SWluZQbkn6/vvvFRoaKi8vL9WoUUNffPGF9bkjR47IYrFo0qRJGV63efNmWSwWLVy40O57NGrUSMHBwRnOi/nz56t169YqUqRIpq/77rvv1KRJExUsWFA+Pj5q166d9u7da32+V69emjp1qiTbS/xumjBhgsLCwlS0aFF5e3urXr16+uyzzzK8T3JysoYMGaLixYvLx8dHHTp00J9//plhv+PHj2vAgAGqWrWqvL29VbRoUXXu3Nnm78ScOXPUuXNnSVLz5s0zXFq4fPlytWvXzvrnWrFiRb3xxhtKTU2124/jx4/X5cuXNWvWLJsC4qZKlSrp+eeftz525JwuX7689u7dqw0bNlizpp/z4+g5duHCBfXs2VO+vr4qXLiwIiMj9euvv8pisWS4VGrt2rXWP9fChQurY8eO+u2332z2GT16tCwWi/bt26cePXrI399fDz74oGbPni2LxaKdO3dm+Pxvv/223N3ddfLkSbt9CSBvYyQCyCLDMNShQwetW7dOffv2VWhoqFatWqVhw4bp5MmTGX4o3LBhgxYvXqzBgwfL09NTH3zwgVq3bq1t27apVq1at3yfOXPmqE+fPqpZs6ZGjBihwoULa+fOnVq5cqV69OjhdO7Dhw9LkooWLWpt++effxQeHq4HH3xQEyZMsF7m1L9/f82ZM0e9e/fW4MGDdfToUb3//vvauXOnfvzxR+XPn19du3ZVRESEfv75Z91///3WYx4/flw//fST3nnnHWvbtGnTVLNmTXXo0EH58uXT119/rQEDBigtLU0DBw68Zea0tDR16NBBmzZt0tNPP63q1atr9+7dmjRpkg4cOKBly5bZ7L9p0yZ98cUXGjBggHx8fDRlyhQ98cQTOnHihPVznzp1Sg0aNFB8fLyefvppVatWTSdPntRnn32mK1euyMPDQ1euXFHTpk118uRJ9e/fX2XLltXmzZs1YsQInT59WrGxsXb7++DBg+rataueeeYZRUZGavbs2ercubNWrlypli1bqkKFCmrcuLHmz5+vIUOG2Lx2/vz58vHxUceOHe2+jyR1795dn376qcaOHSuLxaK//vpL33//vebNm5dpETVv3jxFRkYqPDxc48aN05UrVzRt2jQ9+OCD2rlzp8qXL6/+/fvr1KlTmV7KJ0mTJ09Whw4d9OSTTyolJUWLFi1S586d9c0336hdu3bW/Z566il9+umn6tGjh8LCwrR27Vqb52/6+eeftXnzZnXr1k2lS5fWsWPHNG3aNDVr1kz79u1TgQIF9NBDD2nw4MGaMmWKXnnlFeslhTf/P2fOHBUqVEhRUVEqVKiQ1q5dq1GjRikxMdHmfMzM119/rQoVKigsLMyhPnfknI6NjdVzzz2nQoUK6dVXX5UklSxZUpIcPsfS0tLUvn17bdu2Tc8++6yqVaum5cuXKzIyMkOmH374QW3atFGFChU0evRoXb16Ve+9954aN26sHTt2ZLj8q3PnzqpcubLefvttGYah//znPxo4cKDmz5+vunXr2uw7f/58NWvWTKVKlXKofwDkYQYAhwwcONBI/1dm2bJlhiTjzTfftNnvP//5j2GxWIxDhw5Z2yQZkoxffvnF2nb8+HHDy8vLeOyxx6xts2fPNiQZR48eNQzDMOLj4w0fHx+jYcOGxtWrV23eJy0t7bZ5bx7rhx9+MM6fP2/88ccfxqJFi4yiRYsa3t7exp9//mkYhmFERkYakoyXX37Z5vX/+9//DEnG/PnzbdpXrlxp056QkGB4enoaL774os1+48ePNywWi3H8+HFr25UrVzLkDA8PNypUqGDT1rRpU6Np06bWx/PmzTPc3NyM//3vfzb7TZ8+3ZBk/Pjjj9Y2SYaHh4dN///666+GJOO9996ztkVERBhubm7Gzz//nCHTzb594403jIIFCxoHDhywef7ll1823N3djRMnTmR4bXrlypUzJBmff/65tS0hIcEIDAw06tata2378MMPDUnGb7/9Zm1LSUkxihUrZkRGRt72PY4ePWpIMt555x1jz549hiRrP02dOtUoVKiQkZSUZERGRhoFCxa0vu7SpUtG4cKFjX79+tkc78yZM4afn59N+7/P/fT+/WeakpJi1KpVy3j44YetbXFxcYYkY8CAATb79ujRw5BkREdH3/J4hmEYW7ZsMSQZc+fOtbYtXbrUkGSsW7fObibDMIz+/fsbBQoUMK5du5bp5zCMG382koyOHTvech9H3iuzc7pmzZo25/RNjp5jn3/+uSHJiI2Nte6TmppqPPzww4YkY/bs2db20NBQo0SJEsaFCxesbb/++qvh5uZmREREWNuio6MNSUb37t0z5OrevbsRFBRkpKamWtt27NiR4b0A3Lu4nAnIohUrVsjd3V2DBw+2aX/xxRdlGIa+++47m/ZGjRqpXr161sdly5ZVx44dtWrVqlteZrF69WpdunRJL7/8coaJsekvKbmdFi1aqHjx4ipTpoy6deumQoUK6csvv8zwm8Rnn33W5vHSpUvl5+enli1b6q+//rJu9erVU6FChbRu3TpJkq+vr9q0aaMlS5bYXMa1ePFiPfDAAypbtqy1zdvb2/p1QkKC/vrrLzVt2lRHjhxRQkLCLT/D0qVLVb16dVWrVs0my81Ls25mSf+ZK1asaH0cEhIiX19fHTlyRNKN3+ouW7ZM7du3t7nc6qabfbt06VI1adJE/v7+Nu/bokULpaamZrgcLTNBQUF67LHHrI99fX0VERGhnTt36syZM5KkLl26yMvLS/Pnz7fut2rVKv31119OzcGpWbOmQkJCrJc/LViwQB07dsx0Av3q1asVHx+v7t2723w2d3d3NWzYMEOf3kr6P9OLFy8qISFBTZo00Y4dO6ztK1askKQMf1deeOGF2x7v+vXrunDhgipVqqTChQvbHNPRTJcuXdJff/2lJk2a6MqVK9q/f/8tX5eYmChJ8vHxceh9/v1ezpzTNzl6jq1cuVL58+dXv379rK91c3PLMIJ3+vRpxcXFqVevXjaXsIWEhKhly5bWP4v0nnnmmQxtEREROnXqlM15MH/+fHl7e+uJJ56w+7kA5H1czgRk0fHjxxUUFJThB46bl1QcP37cpr1y5coZjlGlShVduXJF58+fV0BAQIbnb156dLvLneyZOnWqqlSponz58qlkyZKqWrWq3Nxsf3+QL18+lS5d2qbt4MGDSkhIUIkSJTI97rlz56xfd+3aVcuWLdOWLVsUFhamw4cPa/v27Rku9/nxxx8VHR2tLVu26MqVKzbPJSQkyM/PL9P3OnjwoH777TcVL17cbhZJNoXLTf7+/ta5HOfPn1diYqLdfj148KB27drl8PtmplKlShkKvipVqki6sTxrQECAChcurPbt22vBggV64403JN34ga1UqVLWQslRPXr00LvvvqshQ4Zo8+bNeuWVVzLd7+DBg5J0y+P7+vo69H7ffPON3nzzTcXFxdnMT0n/mY8fPy43Nzebwk6SqlatmuF4V69eVUxMjGbPnq2TJ0/aFKaO/FAuSXv37tVrr72mtWvXWgsDR45x8zNfunTJofeRsn5O3+ToOXb8+HEFBgZmKAgrVapk8/jm953M+rZ69epatWpVhsnTwcHBGfZt2bKlAgMDNX/+fD3yyCNKS0vTwoUL1bFjR6eKLAB5F0UEkMc1aNAg09+2p+fp6ZmhsEhLS1OJEiVsfjueXvofetq3b68CBQpoyZIlCgsL05IlS+Tm5mad/CrdKIgeeeQRVatWTRMnTlSZMmXk4eGhFStWaNKkSbedqJyWlqbatWtr4sSJmT5fpkwZm8e3WuHK+NeEd3vS0tLUsmVLDR8+PNPnbxYD2SEiIkJLly7V5s2bVbt2bX311VcaMGBAhj8Xe7p3764RI0aoX79+Klq0qFq1apXpfjf7e968eZkWsPny2f/n4X//+586dOighx56SB988IECAwOVP39+zZ49O8sT/5977jnNnj1bL7zwgho1aiQ/Pz9ZLBZ169bNocns8fHxatq0qXx9ffX666+rYsWK8vLy0o4dO/TSSy/d9hi+vr4KCgrSnj17HMp6J+f0TXfzHLuV9KMpN7m7u6tHjx6aOXOmPvjgA/344486depUjq5OB8C1UEQAWVSuXDn98MMPunTpks1v5m5eLlGuXDmb/W/+5je9AwcOqECBArf8LeTN39zu2bMnw28cc1rFihX1ww8/qHHjxpn+kJFewYIF9eijj2rp0qWaOHGiFi9erCZNmigoKMi6z9dff63k5GR99dVXNiMFjlw2U7FiRf3666965JFHHL6M63aKFy8uX19fuz8sVqxYUZcvX1aLFi2y/F6HDh2SYRg2uQ8cOCBJNhNcW7dureLFi2v+/Plq2LChrly5op49ezr9fmXLllXjxo21fv16Pfvss7csBm6eWyVKlLD7+W7V559//rm8vLy0atUqm3ubzJ4922a/cuXKKS0tTYcPH7b5Dfnvv/+e4ZifffaZIiMj9e6771rbrl27pvj4eIcyrV+/XhcuXNAXX3yh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fupdXU66qpLF/SRJCYlXdC35usnp7OPcMZcr978rZ5dcP/+9buHCherTp48WLVqkdu3a2d3/8uXLOnz4sHr2dO5KHqeLiIiICF25ckV16tSRh4eHvL29bZ7/+2/nh6ojIyOdfs3dVtWvkGIfqG19PLDGjSUKV/55VuN2OVe5maFt2yb6++8ETZkyX+fPX1T16hX00UdjXGZokv43D31vHlfv+/4RLSVJq5eOsmnvFzVNn3620YxITuHcMZcr978rZ5dcP392yC0LhV6+fNlmhODo0aOKi4tTkSJFVLZsWY0YMUInT57U3LlzJd24hCkyMlKTJ09Ww4YNdebMGUmSt7e3/Pxu/CJn6NChat++vcqVK6dTp04pOjpa7u7u6t69u1PZLIaTM5o/+eST2z7vaEGQmJgoX19f69e3c3M/RzVf8aNT++c269pmPmHdVTRf4TqXLPwbfW8uV+5/V+/7n5553+wId+TqiTFmR7gjrnz+uPLfW5ititkBbqnCBxty7NhHBjR1eN/169erefPmGdojIyM1Z84c9erVS8eOHdP69eslSc2aNdOGDRmz39xfkrp166aNGzfqwoULKl68uB588EG99dZbqlixolOfw+mRiOwaNfD399fp06dVokQJFS5cONN7QxiGIYvFotTU1Gx5TwAAAMBVNGvW7LYrmN4sDG66WUzczqJFi+4w1Q1OFxGSlJqaqmXLlum3336TdOOudx06dHDq7tJr1661Tpp2ZjlYAAAAICdx42P7nC4iDh06pLZt2+rkyZOqWvXGLP2YmBiVKVNG3377rcNDIU2bNs30awAAAAC5m1NLvErS4MGDVbFiRf3xxx/asWOHduzYoRMnTig4OFiDBw/OUoiVK1dq06ZN1sdTp05VaGioevTooYsXL97mlQAAAED2slhybssrnC4iNmzYoPHjx9vcv6Fo0aIaO3ZsphM5HDFs2DDr5Ordu3crKipKbdu21dGjRxUVFZWlYwIAAADIGU5fzuTp6ZnpbbEvX74sD4+s3eTt6NGjqlGjhiTp888/V/v27fX2229rx44datu2bZaOCQAAAGRFXhoxyClOj0Q8+uijevrpp7V161YZhiHDMPTTTz/pmWeeUYcOHbIUwsPDQ1euXJEk/fDDD2rVqpUkqUiRInaXfwUAAABwdzk9EjFlyhRFRkaqUaNGyp8/vyTpn3/+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RISGhspiscgwDFkst7+YKzU1NVuCAQAAAGbIS3MXcopDozVHjx7VkSNHdPToUX3++ecKDg7WBx98oJ07d2rnzp364IMPVLFiRX3++ec5nRcAAACAyRwaiShXrpz1686dO2vKlClq27attS0kJERlypTRyJEj1alTp2wPCQAAANwteel+DjnF6YnVu3fvVnBwcIb24OBg7du3L1tCAQAAAGbhcib7nJ58Xr16dcXExCglJcXalpKSopiYGFWvXj1bwwEAAADIfZweiZg+fbrat2+v0qVLW1di2rVrlywWi77++utsDwgAAADcTSzxap/TRUSDBg105MgRzZ8/X/v375ckde3aVT169FDBggWzPSAAAACA3MXpIkKSChYsqKeffjq7swAAAACmY2K1fVkqIiRp3759OnHihM3cCEnq0KHDHYcCAAAAkHs5XUQcOXJEjz32mHbv3m29AZ0k603ouNkcAAAAXBmrM9nn9LyR559/XsHBwTp37pwKFCigvXv3auPGjapfv77Wr1+fAxEBAAAA5CZOj0Rs2bJFa9euVbFixeTm5iY3Nzc9+OCDiomJ0eDBg7Vz586cyAkAAADcFYxE2Od0EZGamiofHx9JUrFixXTq1ClVrVpV5cqV0++//+7wcRITEx3e19fX19mYAAAAQJawxKt9ThcRtWrV0q+//qrg4GA1bNhQ48ePl4eHh2bMmKEKFSo4fJzChQtb51HcimEYslgszLMAAAAAchGni4jXXntNSUlJkqTXX39djz76qJo0aaKiRYtq0aJFDh9n3bp1zr41AAAAkONY4tU+p4uI8PBw69eVKlXS/v379ffff8vf39/uyEJ6TZs2dfatAQAAAOQCTl/y1adPH126dMmmrUiRIrpy5Yr69OlzR2GuXLmi/fv3a9euXTYbAAAAcLe4WXJuyyucLiI++eQTXb16NUP71atXNXfu3CyFOH/+vB599FH5+PioZs2aqlu3rs0GAAAAIPdwuIhITExUQkKCDMPQpUuXlJiYaN0uXryoFStWqESJElkK8cILLyg+Pl5bt26Vt7e3Vq5cqU8++USVK1fWV199laVjAgAAAFnhloNbXuHwnIibqylZLBZVqVIlw/MWi0VjxozJUoi1a9dq+fLlql+/vtzc3FSuXDm1bNlSvr6+iomJUbt27bJ0XAAAAADZz+EiYt26dTIMQw8/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uHLfS66dn3PHXK6c39XPHVfP78rnTuybfdS1Y5g6P/WuLiddVcniNxa9SUi8omvJ101Od+8pVqyY3N3ddfbsWZv2s2fP2p3PkJSUpEWLFjl04+YKFSqoWLFiOnToUPYXEVOnTtXEiRP1xRdf6OOPP9aIESPUrl079e3bV61atcr0ciRH7dq1K9N2i8UiLy8vlS1b9q5VbLfTtm0T/f13gqZMma/z5y+qevUK+uijMS4xPFnVr5BiH6htfTywxo2l2lb+eVbjdmW870duQ9+bx5X7XnLt/Jw75nLl/K5+7rh6flc+d/pHtJQkrV46yqa9X9Q0ffrZRjMimSKrS7FmNw8PD9WrV09r1qxRp06dJN0Y2VqzZo0GDRp029cuXbpUycnJ+u9//2v3ff78809duHBBgYGO31jQYmTx2qTjx49rzpw5mjt3rv755x/t3bs3SxOspRsTRG5XhOTPn19du3bVhx9+KC8vLweO6Bp3hbyV5itce+hwXdviZkfIMvoeWcW5gzvh6uePK3P1c9+7bLTZEbLs6omFZke4pbfjcu6eHq+EtnRq/8WLFysyMlIffvihGjRooNjYWC1ZskT79+9XyZIlFRERoVKlSmWYnN2kSROVKlVKixYtsmm/fPmyxowZoyeeeEIBAQE6fPiwhg8frkuXLmn37t0O/+I+y6sz3fzB3zCM2058dsSXX36pypUra8aMGYqLi1NcXJxmzJihqlWrasGCBZo1a5bWrl2r11577Y7eBwAAALAnJ1dnclbXrl01YcIEjRo1SqGhoYqLi9PKlSutk61PnDih06dP27zm999/16ZNm9S3b98Mx3N3d9euXbvUoUMHValSRX379lW9evX0v//9z6krf5y6T0RycrL1cqZNmzbp0Ucf1fvvv6/WrVvLzS3L9YjeeustTZ48WeHh4da22rVrq3Tp0ho5cqS2bdumggUL6sUXX9SECROy/D4AAACAqxk0aNAtL19av359hraqVaveciEkb29vrVq16o4zOVxEDBgwQIsWLVKZMmXUp08fLVy4UMWKFbvjAJK0e/dulStXLkN7uXLltHv3bklSaGhohioLAAAAyG45ebO5vMLhImL69OkqW7asKlSooA0bNmjDhg2Z7vfFF184HaJatWoaO3asZsyYIQ+PG8uzXr9+XWPHjlW1atUkSSdPnsywRi4AAACQ3dwp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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0EAAAJjCAYAAADK7hpQAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAbg5JREFUeJzt3XlYVHXj/vF7AAFRNg0Xct9wRU3T1Moll8hcenrcU1DbKTXN0qdya1EzFTNTMwMztyy3rDR3c8sV09x3U9wFBBQUzu+Pfs63CReGmDnKvF/XNVfO55w552YcwptzzudYDMMwBAAAAAAuws3sAAAAAADgTJQgAAAAAC6FEgQAAADApVCCAAAAALgUShAAAAAAl0IJAgAAAOBSKEEAAAAAXAolCAAAAIBLoQQBAAAAcCmUIAD3jZiYGFksFh07dszsKKZq1KiRGjVqZHaMf61UqVJ6+umnzY5xT7NYLBoyZIjZMQAg16EEAcgWi8WSpcfq1avNjnpLNwvVzYe3t7cqVKig1157TWfPnjU7HnLIsWPHrH/HH3zwwS3X6dKliywWi/Lnz5+tffz000/3XFHZs2ePhgwZ4rBfGBw+fFgvvfSSypQpI29vb/n5+alBgwYaN26crl69avf2Pv/8c8XExOR8UAC4DQ+zAwC4P02fPt3m+ddff61ly5ZlGq9UqVKO7bNr167q2LGjvLy8cmybw4YNU+nSpXXt2jWtW7dOEydO1E8//aTdu3fLx8cnx/YDc3l7e2vWrFl69913bcaTk5O1cOFCeXt7Z3vbP/30kyZMmHBPFaE9e/Zo6NChatSokUqVKpWj2/7xxx/Vrl07eXl5qVu3bqpatarS0tK0bt069e/fX3/88Ye++OILu7b5+eef64EHHlBERESOZgWA26EEAciW5557zub5pk2btGzZskzjOcnd3V3u7u45us2wsDDVrl1bkvT888+rYMGCGjNmjBYuXKhOnTrd8jXJycnKly9fjuaAYz311FOaN2+edu7cqerVq1vHFy5cqLS0ND355JNauXKliQnvD0ePHlXHjh1VsmRJrVy5UkWLFrUui4yM1KFDh/Tjjz+amNCx+N4Hcg9OhwPgMMnJyerXr5+KFy8uLy8vhYSE6JNPPpFhGDbrWSwWvfbaa5oxY4ZCQkLk7e2tWrVqae3atTbr3e6aoJ9//lkNGzaUr6+v/Pz89PDDD2vmzJnZytykSRNJf/1jT5IiIiKUP39+HT58WE899ZR8fX3VpUsXSVJGRoaioqJUpUoVeXt7q3DhwnrppZd0+fJl6/aefvpplSlT5pb7qlevnrWASVJ0dLSaNGmiQoUKycvLS5UrV9bEiROzlDs1NVWDBw9WuXLl5OXlpeLFi+utt95SamqqzXo33+sFCxaoatWq8vLyUpUqVbRkyZJM2zx16pR69uyp4OBgeXl5qXTp0nrllVeUlpZmXSc+Pl59+vSx/h2XK1dOI0eOVEZGRpZyS9Ivv/yiGjVqyNvbW5UrV9a8efOsy44cOSKLxaKxY8dmet2GDRtksVg0a9asu+6jXr16Kl26dKbPxYwZM/Tkk0+qQIECt3zdzz//rMcee0z58uWTr6+vWrZsqT/++MO6PCIiQhMmTJBke4roTZ988onq16+vggULKm/evKpVq5a+++67TPtJTU3VG2+8oaCgIPn6+qp169b6888/M613/PhxvfrqqwoJCVHevHlVsGBBtWvXzuZ7IiYmRu3atZMkNW7cONOpqQsXLlTLli2tf69ly5bV+++/r/T09Lu+jx9//LGSkpI0depUmwJ0U7ly5dS7d2/r86x8pkuVKqU//vhDa9assWb9+zVvWf2MXbx4UV27dpWfn58CAgIUHh6unTt3ymKxZDrVbuXKlda/14CAALVp00Z79+61WWfIkCGyWCzas2ePOnfurMDAQD366KOKjo6WxWLRjh07Mn39H330kdzd3XXq1Km7vpcAzMWRIAAOYRiGWrdurVWrVqlnz56qUaOGli5dqv79++vUqVOZ/lG7Zs0azZkzR7169ZKXl5c+//xzPfnkk9q8ebOqVq162/3ExMSoR48eqlKligYOHKiAgADt2LFDS5YsUefOne3OffjwYUlSwYIFrWM3btxQixYt9Oijj+qTTz6xnib30ksvKSYmRt27d1evXr109OhRffbZZ9qxY4fWr1+vPHnyqEOHDurWrZu2bNmihx9+2LrN48ePa9OmTRo1apR1bOLEiapSpYpat24tDw8P/fDDD3r11VeVkZGhyMjI22bOyMhQ69attW7dOr344ouqVKmSdu3apbFjx+rAgQNasGCBzfrr1q3TvHnz9Oqrr8rX11effvqpnn32WZ04ccL6dZ8+fVp16tRRfHy8XnzxRVWsWFGnTp3Sd999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58+fV2Ji4l3f14MHD+r333/P8n5vpVy5cpkKa4UKFST9Nb11kSJFFBAQoFatWmnmzJl6//33Jf31D84HH3zQWvSyqnPnzho9erTeeOMNbdiwQf/73/9uud7Bgwcl6bbb9/Pzy9L+Fi9erA8++ECxsbE212f9/Ws+fvy43NzcbIqpJIWEhGTa3tWrVzV8+HBFR0fr1KlTNsU6K6VCkv744w+9++67WrlypbXYZGUbN7/mK1euZGk/UvY/0zdl9TN2/PhxFS1aNFOhLVeunM3zm//fudV7W6lSJS1dujTT5AelS5fOtG6zZs1UtGhRzZgxQ0888YQyMjI0a9YstWnTxq6SCMA8lCAALq1OnTq3PNrxd15eXpmKUUZGhgoVKmRzdOLv/v6PtlatWsnHx0fffvut6tevr2+//VZubm7Wi9elvwrdE088oYoVK2rMmDEqXry4PD099dNPP2ns2LF3nGggIyND1apV05gxY265vHjx4jbPbzfDnvGPCSvuJiMjQ82aNdNbb711y+U3y0xO6Natm+bOnasNGzaoWrVqWrRokV599dVMfy9306lTJw0cOFAvvPCCChYsqObNm99yvZvv9/Tp029ZwD087v7j89dff1Xr1q31+OOP6/PPP1fRokWVJ08eRUdHZ3vijtdff13R0dHq06eP6tWrJ39/f1ksFnXs2DFLk1HEx8erYcOG8vPz07Bhw1S2bFl5e3tr+/btevvtt++4DT8/PwUHB2v37t1ZyvpvPtM3OfMzdjt/P5p1k7u7uzp37qwpU6bo888/1/r163X69GmHzo4JIGdRggA4RMmSJbV8+XJduXLF5jejN0+3KVmypM36N3/z/ncHDhyQj4/PbX8LfPM357t37870G19HK1u2rJYvX64GDRrc8h9Jf5cvXz49/fTTmjt3rsaMGaM5c+boscceU3BwsHWdH374QampqVq0aJHNkZqsnHZVtmxZ7dy5U0888USWTwO8k6CgIPn5+d31H7tly5ZVUlKSmjZtmu19HTp0SIZh2OQ+cOCAJNlcoP7kk08qKChIM2bMUN26dZWSkqKuXbvavb8SJUqoQYMGWr16tV555ZXblpmbn61ChQrd9eu73Xv+/fffy9vbW0uXLrW5t1V0dLTNeiVLllRGRoYOHz5sc4Ri//79mbb53XffKTw8XKNHj7aOXbt2TfHx8VnKtHr1al28eFHz5s3T448/bh2/ORvi3Tz99NP64osvtHHjRtWrV++O69rzmb5d3qx+xkqWLKlVq1YpJSXF5mjQoUOHMq0n3fq93bdvnx544IEsT4HdrVs3jR49Wj/88IN+/vlnBQUFqUWLFll6LQDzcU0QAId46qmnlJ6ers8++8xmfOzYsbJYLAoLC7MZ37hxo801DSdPntTChQvVvHnz2x65aN68uXx9fTV8+HBdu3bNZpm9RzXs1b59e6Wnp1tPz/q7GzduZPpHaYcOHXT69Gl9+eWX2rlzpzp06GCz/ObX+M/Tm/75D+bbZTl16pSmTJmSadnVq1eVnJyclS/Jys3NTW3bttUPP/ygrVu3Zlp+M2P79u21ceNGLV26NNM68fHxunHjxl33dfr0ac2fP9/6PDExUV9//bVq1KhhcwTGw8NDnTp10rfffquYmBhVq1ZNoaGhdn1dN33wwQcaPHiwXn/99duu06JFC/n5+emjjz7S9evXMy0/f/689c83/9H8z79zd3d3WSwWm2vajh07lmm2vpvfC59++qnN+K1m13N3d8/02R4/fnym6+bulEmy/ZylpaXp888/z7SvW3nrrbeUL18+Pf/88zp79mym5YcPH9a4ceNuu6/bfabz5cuXKauU9c9YixYtdP36dZvvgYyMDOv05TcVLVpUNWrU0LRp02z2t3v3bv3yyy966qmn7vDV2woNDVVoaKi+/PJLff/99+rYsWOWjhACuDfw3QrAIVq1aqXGjRvrnXfe0bFjx1S9enX98ssvWrhwofr06ZPp+oeqVauqRYsWNlNkS9LQoUNvuw8/Pz+NHTtWzz//vB5++GHrvTx27typlJQUTZs2zWFfX8OGDfXSSy9p+PDhio2NVfPmzZUnTx4dPHhQc+fO1bhx4/Tf//7Xuv7Newy9+eabcnd3z3TxdPPmzeXp6alWrVrppZdeUlJSkqZMmaJChQopLi7ujlm6du2qb7/9Vi+//LJWrVqlBg0aKD09Xfv27dO3336rpUuX3vWUv3/66KOP9Msvv6hhw4bWabfj4uI0d+5crVu3TgEBAerfv78WLVqkp59+WhEREapVq5aSk5O1a9cufffddzp27JgeeOCBO+6nQoUK6tmzp7Zs2aLChQvrq6++0tmzZ2/5D+Vu3brp008/1apVqzRy5Ei7vp6/a9iwoRo2bHjHdfz8/DRx4kR17dpVDz30kDp27KigoCCdOHFCP/74oxo0aGAt+Dcn9OjVq5datGghd3d3dezYUS1bttSYMWP05JNPqnPnzjp37pwmTJigcuXK6ffff7fuq0aNGurUqZM+//xzJSQkqH79+lqxYkWmoxjSX0dipk+fLn9/f1WuXFkbN27U8uXLbaZ0v7lNd3d3jRw5UgkJCfLy8lKTJk1Uv359BQYGKjw8XL169ZLFYtH06dOz/EuDsmXLaubMmerQoYMqVaqkbt26qWrVqkpLS9OGDRs0d+5cRURESLLvM12rVi1NnDhRH3zwgcqVK6dChQqpSZMmWf6MtW3bVnXq1FG/fv106NAhVaxYUYsWLdKlS5ck2R5pGjVqlMLCwlSvXj317NnTOkW2v7+/hgwZkqX34aZu3brpzTfflJT5BtIA7nHmTEoHILe51TTBV65cMd544w0jODjYyJMnj1G+fHlj1KhRmaavlmRERkYa33zzjVG+fHnDy8vLqFmzZqbpff85RfZNixYtMurXr2/kzZvX8PPzM+rUqWPMmjXrjnlvbutWU0D/3T+nTv6nL774wqhVq5aRN29ew9fX16hWrZrx1ltvGadPn860bpcuXQxJRtOmTW+5rUWLFhmhoaGGt7e3UapUKWPkyJHGV199lelr/ucU2Ybx19TLI0eONKpUqWJ4eXkZgYGBRq1atYyhQ4caCQkJ1vVuvtf/VLJkyUzTTR8/ftzo1q2bERQUZHh5eRllypQxIiMjjdTUVOs6V65cMQYOHGiUK1fO8PT0NB544AGjfv36xieffGKkpaXd9n27uc+WLVsaS5cuNUJDQw0vLy+jYsWKxty5c2/7mipVqhhubm7WKczv5u9TZN/J7f6eV61aZbRo0cLw9/c3vL29jbJlyxoRERE207nfuHHDeP31142goCDDYrHYfB9MnTrV+pmuWLGiER0dbZ16+e+uXr1q9OrVyyhYsKCRL18+o1WrVsbJkyczTZF9+fJlo3v37sYDDzxg5M+f32jRooWxb9++W/79TZkyxShTpozh7u5uM132+vXrjUceecTImzevERwcbLz11lvG0qVLbzul9q0cOHDAeOGFF4xSpUoZnp6ehq+vr9GgQQNj/PjxNtNsZ/UzfebMGaNly5aGr6+vIcnm853Vz9j58+eNzp07G76+voa/v78RERFhrF+/3pBkzJ492yb/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\n"
          },
          "metadata": {}
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