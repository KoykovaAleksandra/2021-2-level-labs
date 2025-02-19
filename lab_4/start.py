"""
Language generation starter
"""

import os
from lab_4.main import tokenize_by_letters, LetterStorage, \
    encode_corpus, decode_sentence, LanguageProfile, NGramTextGenerator,\
    LikelihoodBasedTextGenerator, translate_sentence_to_plain_text

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    def score_4():
        """
        4
        """
        with open(os.path.join(PATH_TO_LAB_FOLDER, 'reference_text.txt'), 'r', encoding="utf-8")\
            as file:
            text = file.read()
        tokenized_text = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized_text)
        #RETURN
        number_of_letters = storage.get_letter_count()
        the_lowest_id = list(storage.storage.items())[:5]
        the_highest_id = list(storage.storage.items())[-5:]
        print('Number of letters = {} '.format(number_of_letters))
        print('Letters with the lowest id: {}'.format(the_lowest_id))
        print('Letters with the highest id: {}'.format(the_highest_id))
        return number_of_letters, the_lowest_id, the_highest_id

    def score_6():
        """
        6
        """
        with open(os.path.join(PATH_TO_LAB_FOLDER, 'reference_text.txt'), 'r', encoding="utf-8")\
            as file:
            text = file.read()
        tokenized_text = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized_text)
        #ENCODE
        encoded_text = encode_corpus(storage, tokenized_text)
        #LANGUAGE PROFILE
        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded_text, (2,))
        #GENERATION
        generate_text = NGramTextGenerator(profile)
        sentences = generate_text.generate_sentence((1,), 7)
        decoded_corpus = decode_sentence(storage, sentences)
        decoded_sentences = translate_sentence_to_plain_text(decoded_corpus)
        #PRINT
        print(decoded_sentences)
        return decoded_sentences

    def score_8():
        """
        8
        """
        with open(os.path.join(PATH_TO_LAB_FOLDER, 'reference_text.txt'), 'r', encoding="utf-8")\
            as file:
            text = file.read()
        tokenized_text = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized_text)
        # ENCODE
        encoded_text = encode_corpus(storage, tokenized_text)
        # LANGUAGE PROFILE
        profile = LanguageProfile(storage, 'en')
        profile.create_from_tokens(encoded_text, (2,))
        # GENERATION
        generate_text = LikelihoodBasedTextGenerator(profile)
        sentences = generate_text.generate_decoded_sentence((1, ), 7)
        # PRINT
        print(sentences)
        return sentences


    # score_4()
    # score_6()
    # score_8()
    RESULT = score_8()
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Detection not working'
