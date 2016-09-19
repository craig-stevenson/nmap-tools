from nmaptools.utils import get_ipv4_addresses
from nmaptools.utils import get_ipv6_addresses


test_file = 'C:\\Users\\craig\\PycharmProjects\\nmaptools\\tests\\nmap_sample.xml'
print(get_ipv4_addresses(test_file))
print(get_ipv6_addresses(test_file))
