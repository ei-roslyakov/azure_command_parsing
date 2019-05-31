import codecs
import io
import sys
import textfsm
from dateutil import parser


AMOUNT_REMAINING = int(sys.argv[1]) * -1
TEMPLATE_FILE_NAME = "./templates/wide_data.template"
INPUT_DATA = sys.stdin.read()


def get_text_from_file(file_name):
    with codecs.open(file_name, "r", "utf-8") as input_file:
        return input_file.read()


def sort_pole(elem):
    return elem[2]


def main():
    data_to_be_parsed = INPUT_DATA
    template_text = get_text_from_file(TEMPLATE_FILE_NAME)
    template_io = io.StringIO(template_text)
    template_io.seek(0)
    parser_fsm = textfsm.TextFSM(template_io)
    parsing_result = parser_fsm.ParseText(data_to_be_parsed)
    new_wide_data = []
    for item in parsing_result:
        item[2] = parser.parse(item[2])
        new_wide_data.append(item)

    new_wide_data.sort(key=sort_pole)
    for item in new_wide_data[:AMOUNT_REMAINING]:
        print(item[0], item[3])


if __name__ == '__main__':
    main()
