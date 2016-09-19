from nmaptools.nmapscan import NmapScan

FILE = 'nmap_sample.xml'


def test_addresses_ipv4():
    """ """
    scan = NmapScan(FILE)
    print('ipv4 addresses')
    print(scan.addresses_ipv4)

def test_services():
    """ """
    scan = NmapScan(FILE)
    print('services')
    print(scan.services)

def test_versions():
    """ """
    scan = NmapScan(FILE)
    print('versions')
    print(scan.versions)

if __name__ == '__main__':
    from os import listdir
    print(listdir('.'))

if __name__ == '__main__':
    test_addresses_ipv4()
    test_services()
    test_versions()