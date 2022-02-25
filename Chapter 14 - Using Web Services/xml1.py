import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Gabigolmes</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="Sim"/>
</person>'''

tree = ET.fromstring(data)
print('Nome:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

