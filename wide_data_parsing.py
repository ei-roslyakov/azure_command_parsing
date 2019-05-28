import codecs
import io
import sys
import textfsm
import terminaltables
from dateutil import parser


AMOUNT_REMAINING = int(sys.argv[1]) * -1
TEMPLATE_FILE_NAME = "./templates/wide_data.template"
DATA_FILE_NAME = "./data/wide_data.txt"
# DATA_FILE_NAME = sys.stdin.read()


def get_text_from_file(file_name):
    with codecs.open(file_name, "r", "utf-8") as input_file:
        return input_file.read()        


def sort_pole(elem):
    return elem[2]


def main():
    data_to_be_parsed = get_text_from_file(DATA_FILE_NAME)
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
    print("************************residual data************************")
    for item in new_wide_data[AMOUNT_REMAINING:]:
        print(item[0], item[3])
    print("************************data to be deleted************************")
    for item in new_wide_data[:AMOUNT_REMAINING]:
        print(item[0], item[3])
    print("\n")
    user_decision = input("Press Y to continue deleting images ")
    print("\n")
    if user_decision == "Y":
        for item in new_wide_data[:AMOUNT_REMAINING]:
            print("Image has been deleted {} {}".format(item[0], item[3]))

    # table_to_be_printed = terminaltables.AsciiTable(
    #     [parser.header] +
    #     parsing_result
    # )


main()
