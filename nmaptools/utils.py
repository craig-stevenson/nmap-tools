from xml.etree.ElementTree import parse


def get_ipv4_addresses(file):
    """Parses the xml output of nmap and returns a list of the ipv4 addresses which are up

    :param file: A string pointing to an xml output file from nmap
    :return: A list of strings
    """
    tree = parse(file)
    return tree.findall('*/[@attrib=ipv4]')



def get_ipv6_addresses(file):
    """Parses the xml output of nmap and returns a list of the ipv6 addresses which are up

    :param file:
    :return:
    """
    tree = parse(file)
    return tree.findall('*/[@attrib=ipv6]')


def get_services(file):
    """Parses the xml output of nmap and returns a list of the services which are running

    :param file:
    :return:
    """
    pass