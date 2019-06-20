import argparse
import io
import sys

from dateutil import parser

import textfsm


WIDE_DATA_PARSING_TEMPLATE = \
    "Value created_time ([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]*[A-Za-z]*)\n" \
    "Value digest (\w+:\w+)\n" \
    "Value last_update_time ([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]*[A-Za-z]*)\n" \
    "Value name (.*)\n" \
    "Value signed (True|False)\n" \
    "\n" \
    "Start\n" \
    "  ^${created_time}\s+${digest}\s+${last_update_time}\s+${name}\s+${signed}.* -> Record\n"  # noqa


INDEX_COLUMN_TIME_CREATE = 0
INDEX_COLUMN_NAME = 3


def create_io_from_string(value):
    template_io = io.StringIO(value)
    template_io.seek(0)

    return template_io


def sort_pole(elem):
    return elem[2]


def parse_command_line():
    parsers = argparse.ArgumentParser()
    parsers.add_argument(
        "-q",
        default=5,
        type=int
    )

    return parsers.parse_args()


def parse_data():
    data_to_be_parsed = sys.stdin.read()
    template_io = create_io_from_string(WIDE_DATA_PARSING_TEMPLATE)

    parser_fsm = textfsm.TextFSM(template_io)
    parsing_result = parser_fsm.ParseText(data_to_be_parsed)
    new_wide_data = []

    for item in parsing_result:
        item[2] = parser.parse(item[2])
        new_wide_data.append(item)

    return new_wide_data


def main(data_to_be_sorted):
    amount_remaining = parse_command_line()
    data_to_be_sorted.sort(key=sort_pole, reverse=True)

    to_be_delete = []
    no_deleted = []

    for item in data_to_be_sorted[abs(amount_remaining.q):]:
        to_be_delete.append(item)

    for item in data_to_be_sorted[:abs(amount_remaining.q)]:
        no_deleted.append(item)

    del_image = []
    untag_image = []

    for item in to_be_delete:
        for value in no_deleted:
            if item[1] == value[1]:
                untag_image.append(item)
            else:
                del_image.append(item)
            break

    for item in del_image:
        create_time = (item[INDEX_COLUMN_TIME_CREATE])
        image_name = (item[INDEX_COLUMN_NAME])
        data_to_write = "{} {}\n".format(create_time, image_name)
        with open("del_image.txt", "a+") as file_to_write:
            file_to_write.write(data_to_write)

    for item in untag_image:
        create_time = (item[INDEX_COLUMN_TIME_CREATE])
        image_name = (item[INDEX_COLUMN_NAME])
        data_to_write = "{} {}\n".format(create_time, image_name)
        with open("untag_image.txt", "a+") as file_to_write:
            file_to_write.write(data_to_write)


if __name__ == "__main__":
    main(parse_data())
