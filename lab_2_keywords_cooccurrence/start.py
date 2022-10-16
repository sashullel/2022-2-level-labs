"""
Co-occurrence-driven keyword extraction starter
"""

from pathlib import Path
from main import (
    extract_phrases,
    extract_candidate_keyword_phrases,
    calculate_frequencies_for_content_words,
    calculate_word_degrees,
    calculate_word_scores,
    calculate_cumulative_score_for_candidates,
    get_top_n,
    extract_candidate_keyword_phrases_with_adjoining,
    calculate_cumulative_score_for_candidates_with_stop_words,
    # generate_stop_words,
    # load_stop_words
)

def read_target_text(file_path: Path) -> str:
    """
    Utility functions that reads the text content from the file
    :param file_path: the path to the file
    :return: the text content of the file
    """
    with open(file_path, 'r', encoding='utf-8') as target_text_file:
        return target_text_file.read()


if __name__ == "__main__":
    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as fd:
        stop_words = fd.read().split('\n')

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH_GENOME = ASSETS_PATH / 'genome_engineering.txt'
    TARGET_TEXT_PATH_ALBATROSS = ASSETS_PATH / 'albatross.txt'
    TARGET_TEXT_PATH_PAIN_DETECTION = ASSETS_PATH / 'pain_detection.txt'
    TARGET_TEXT_PATH_GAGARIN = ASSETS_PATH / 'gagarin.txt'

    corpus = {
        'gagarin': read_target_text(TARGET_TEXT_PATH_GAGARIN),
        'albatross': read_target_text(TARGET_TEXT_PATH_ALBATROSS),
        'genome_engineering': read_target_text(TARGET_TEXT_PATH_GENOME),
        'pain_detection': read_target_text(TARGET_TEXT_PATH_PAIN_DETECTION)
    }

    for title, text in corpus.items():
        print(f'info about the text called {title}')
        phrases = extract_phrases(text)
        print(f'phrases: {phrases}')

        candidate_keyword_phrases = extract_candidate_keyword_phrases(phrases, stop_words)
        print(f'candidate keyword phrases: {candidate_keyword_phrases}')

        word_frequency = calculate_frequencies_for_content_words(candidate_keyword_phrases)
        print(f'word freq: {word_frequency}')

        word_degrees = calculate_word_degrees(candidate_keyword_phrases, list(word_frequency.keys()))
        print(f'word degrees: {word_degrees}')

        word_scores = calculate_word_scores(word_degrees, word_frequency)
        print(f'word scores: {word_scores}')

        keyword_phrases_with_scores = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, word_scores)
        print(f'keyword phrases with scores: {keyword_phrases_with_scores}')

        top_lst = get_top_n(keyword_phrases_with_scores, 10, 3)
        print(f'top n lst {top_lst}')

        candidate_keyword_phrases_with_adj = extract_candidate_keyword_phrases_with_adjoining(
            candidate_keyword_phrases, phrases)

        keyword_phrases_with_scores_with_stops = calculate_cumulative_score_for_candidates_with_stop_words(
            candidate_keyword_phrases, word_scores, stop_words)

        top_lst_with_stops = get_top_n(keyword_phrases_with_scores_with_stops, 10, 3)
        print(f'top n lst with stop words: {top_lst_with_stops}')

        print()

    #RESULT = None

    #assert RESULT, 'Keywords are not extracted'
