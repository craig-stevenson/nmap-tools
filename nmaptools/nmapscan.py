from xml.etree.ElementTree import parse



class NmapScan(object):
    """ """
    def __init__(self, file_xml):
        """ """
        tree = parse(file_xml)
        self.__addresses_ipv4 = set()
        self.__addresses_ipv6 = set()
        self.__services = set()
        self.__versions = set()

        for ip in tree.getiterator('address'):
            if ip.attrib['addrtype'] == 'ipv4':
                self.addresses_ipv4.add(ip.attrib['addr'])
            elif ip.attrib['addrtype'] == 'ipv6':
                self.addresses_ipv6.add(ip.attrib['addr'])

        for service in tree.getiterator('service'):
            self.services.add(service.attrib['name'])
            self.versions.add('{} {}'.format(service.attrib['product'], service.attrib['version']))


    @property
    def addresses_ipv4(self):
        return self.__addresses_ipv4

    @property
    def addresses_ipv6(self):
        return self.__addresses_ipv6

    @property
    def services(self):
        return self.__services

    @property
    def versions(self):
        return self.__versions