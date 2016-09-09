from xml.etree.cElementTree import parse


def parse_nmap_xml(file):
    """

    :param file:
    :return:
    """
    with open(file, 'r') as file_input:
        return parse(file_input)
