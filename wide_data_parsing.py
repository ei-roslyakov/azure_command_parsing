import argparse
import codecs
import io
import sys
import textfsm
from dateutil import parser


TEMPLATE_FILE_NAME = "./templates/wide_data.template"
INDEX_COLUMN_TIME_CREATE = 0
INDEX_COLUMN_NAME = 3


def get_text_from_file(file_name):
    with codecs.open(file_name, "r", "utf-8") as input_file:
        return input_file.read()


def create_stream_from_text_file(file_name):
    template_text = get_text_from_file(file_name)
    template_io = io.StringIO(template_text)
    template_io.seek(0)

    return template_io


def sort_pole(elem):
    return elem[2]


def parse_command_line():
    parsers = argparse.ArgumentParser()
    parsers.add_argument('-q',
                         default=-5,
                         type=int)

    return parsers.parse_args()


def parse_data():
    data_to_be_parsed = sys.stdin.read()
    template_io = create_stream_from_text_file(TEMPLATE_FILE_NAME)

    parser_fsm = textfsm.TextFSM(template_io)
    parsing_result = parser_fsm.ParseText(data_to_be_parsed)
    new_wide_data = []

    for item in parsing_result:
        item[2] = parser.parse(item[2])
        new_wide_data.append(item)

    return new_wide_data


def main(data_to_be_sorted):
    amount_remaining = parse_command_line()
    data_to_be_sorted.sort(key=sort_pole)
    for item in data_to_be_sorted[:amount_remaining.q * -1]:
        print(item[INDEX_COLUMN_TIME_CREATE], item[INDEX_COLUMN_NAME])


if __name__ == '__main__':
    main(parse_data())
