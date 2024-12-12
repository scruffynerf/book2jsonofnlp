import sys
import argparse
# import os
# from pathlib import Path
from booknlp.english.english_booknlp import EnglishBookNLP
from transformers import logging
logging.set_verbosity_error()


class BookNLP():

    def __init__(self, language, model_params):

        if language == "en":
            self.booknlp = EnglishBookNLP(model_params)

    def process(self, inputFile, outputFolder, idd):
        self.booknlp.process(inputFile, outputFolder, idd)


def proc():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--language', help='Currently on {en}', required=True)
    parser.add_argument('-i', '--inputFile', help='Filename to run BookNLP on', required=True)
    parser.add_argument('-o', '--outputFolder', help='Folder to write results to', required=True)
    parser.add_argument('--id', help='ID of text (for creating filenames within output folder)', required=True)

    args = vars(parser.parse_args())

    language = args["language"]
    inputFile = args["inputFile"]
    outputFolder = args["outputFolder"]
    idd = args["id"]

    print(f"tagging {inputFile}")

    valid_languages = {"en"}
    if language not in valid_languages:
        print(f"{language} not recognized; supported languages: {valid_languages}")
        sys.exit(1)

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref", "model": "small",
    }

    booknlp = BookNLP(language, model_params)
    booknlp.process(inputFile, outputFolder, idd)


if __name__ == "__main__":
    proc()
