from nmaptools import parser


tree = parser.parse_nmap_xml('C:\\Users\\craig\\PycharmProjects\\nmaptools\\tests\\nmap_sample.xml')
for a in tree.getiterator('address'):
    print(a.get('addr'))