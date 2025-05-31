import sys
from stats import get_num_words, get_char_dict, get_sorted_dict


def get_book_text(filepath: str) -> str:
    try:
        with open(filepath) as f:
            return f.read()
    except Exception:
        return ""


def gen_report(filepath):
    # strings to print
    title_str = "=" * 12 + " BOOKBOT " + "=" * 12
    wc_str = "-" * 11 + " Word Count " + "-" * 11
    cc_str = "-" * 9 + " Character Count " + "-" * 9
    end_str = "=" * 13 + " END " + "=" * 13
    # calc vals
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    char_dict = get_char_dict(contents)
    sorted_dict = get_sorted_dict(char_dict)
    out_str = ""
    # report time
    out_str += title_str
    out_str += f"\nAnalyzing book found at {filepath}...\n"
    out_str += wc_str
    out_str += f"\nFound {num_words} total words\n"
    out_str += cc_str
    out_str += "\n"
    # loop through dict list
    for cur_dict in sorted_dict:
        key, value = cur_dict.values()
        out_str += f"{key}: {value}\n"
    out_str += end_str
    return out_str


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(gen_report(sys.argv[1]))


main()
