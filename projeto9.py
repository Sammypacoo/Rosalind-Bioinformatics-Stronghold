{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Rosalind_Projeto9.ipynb",
      "provenance": [],
      "mount_file_id": "1xbf7FwbDuXLsnuy-zZ4PMAaEbZTYQRQO",
      "authorship_tag": "ABX9TyMU5oCzt3xXm9O/fFv+LezK",
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
        "<a href=\"https://colab.research.google.com/github/Sammypacoo/Rosalind-Bioinformatics-Stronghold/blob/main/projeto9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"/content/drive/MyDrive/Rosalind/Projeto9/rosalind_subs.txt\") as f:\n",
        "        contents = f.read()"
      ],
      "metadata": {
        "id": "go_Idds7ClEE"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lista=contents.split(\"\\n\")"
      ],
      "metadata": {
        "id": "TnXbVgK1CzRY"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "string=lista[0]\n",
        "string"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 157
        },
        "id": "3HT3oro6DAyd",
        "outputId": "20e8a621-0b43-4cdf-a2bd-51660821a728"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'GGCGTCAGGGCGTCAAGGGGCGTCAGGCGTCAAATATTGGCGTCATTGAGGCGTCAGTCCATTGGCGTCAGAGAAAAGTCCGGCGTCACAGGCGTCATTGGTGGCGTCAGACGGGCGTCAGGCGTCACGGGGCGTCAGGCGTCAATGCTCTAGAGGCGTCAGGGCGTCAACGGGGCGTCAGGCGTCAGTTGGCGTCAGGGCGTCATGGCGTCAGGCGTCAGGCGTCAGTCAGGCGTCAGGCGTCAGGCGTCACCTGGCGTCAGGCGTCATCTTGAAGGCGTCAAGGCGTCATGATGGCGTCAGGCGTCAGAGGCGTCATGAAGTAGTTACGGCGTCAGGTGTGGGCGTCAGGCGTCAGGCGTCAGGCGTCAGGCGTCAGGCGTCACGAGGCGTCAGGCGTCAAAACGGGCGTCAGGCGTCAGGCGTCAACGTGGCGTCAGCGGCGTCAAGGGCGTCAGGGCGTCACGGCGTCACCAAGCAATTGCAGGCGTCATGGCGTCAGGGCGTCACGGCGTCACGGCGTCATACGGCGTCAACGGCGTCATAGGCGTCAGGCGTCAAGGGCAGGGCGTCAGGCGTCAGGCGTCATGGCGTCAGGCGTCATCCGTACTGGCGTCAAGGGCGTCATTTCGCTAAGGCGTCAGGCGTCAGGCGTCAGGGCGTCAGGCGTCACAGGCGTCAAGGCGTCAGGCGTCACGGTCGGCGTCAAGGGCGTCAGGCGTCAGAGCGGGCGTCAAGGGCGTCACGGGCGTCATTCCGTTGGGGCGTCACGGCGTCAGAGGCGTCAGTAGGCGTCATGGCGTCAGGCGTCAGGCGTCAACCAGGTGAGGCGTCAGGGCGTCACGGCGTCAGGCGTCACAGGCGTCACGGCGTCATTATAGGCGTCAGGCGTCAGGCGTCACCCAAGTTTCGGGCGTCAGGCGTCAGGCGTCACATCGATGGCGTCA'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t=lista[1]\n",
        "t"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "PXx6z20sDKKZ",
        "outputId": "008de928-6922-4518-fbc7-53e0c803ddf4"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'GGCGTCAGG'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tam=len(t)\n",
        "tam"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KQpnqxzjDOCc",
        "outputId": "f72723e5-56a8-464f-bb68-65db7b2fde32"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pos=[]\n",
        "# Para conjunto contendo a palavra \"ATAT\"\n",
        "for i in range (len(string)):\n",
        "  # dividi a string em grupos do tamanho da string que quer achar\n",
        "    item=string[i:tam+i]\n",
        "    #print(item)\n",
        "    #print(i)\n",
        "    if item==t:\n",
        "      pos+=[i+1]\n",
        "pos\n",
        "print(*pos)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hBJ5nDOE6Pr3",
        "outputId": "8df33609-4f50-4f08-bf93-7df19db7baea"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 19 114 131 155 174 191 207 214 232 239 256 296 331 344 351 358 365 372 389 408 415 451 495 547 568 575 590 637 644 651 659 683 711 799 806 829 845 881 888 913 920\n"
          ]
        }
      ]
    }
  ]
}