import codecs
import io
import textfsm
import terminaltables


TEMPLATE_FILE_NAME = "./templates/wide_data.template"
# TEMPLATE_FILE_NAME = "./templates/extra_simple_wide_data.template"
DATA_FILE_NAME = "./data/wide_data.txt"


def get_text_from_file(file_name):
    with codecs.open(file_name, "r", "utf-8") as input_file:
        return input_file.read()        


def main():
    data_to_be_parsed = get_text_from_file(DATA_FILE_NAME)
    template_text = get_text_from_file(TEMPLATE_FILE_NAME)
    
    template_io = io.StringIO(template_text)
    template_io.seek(0)
    
    parser = textfsm.TextFSM(template_io)
    parsing_result = parser.ParseText(data_to_be_parsed)
    print("parsing_result:\n{}".format(parsing_result))
    # table_to_be_printed = terminaltables.AsciiTable(
    #     [parser.header] +
    #     parsing_result
    # )
    
    # print("Parsed Data:\n{}".format(table_to_be_printed.table))


main()




