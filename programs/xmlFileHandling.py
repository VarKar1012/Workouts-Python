data = '''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breafast">idily</item>
    <price>$2.5</price>
    <description>
    two idyly's with chatney
    </description>
    <calories>553</calories>
</food>
<food>
    <item name="breafast">Dosha</item>
    <price>$1.5</price>
    <description>
    Dosha with vada
    </description>
    <calories>700</calories>
</food>
</metadata>'''

import xml.etree.ElementTree as ET

# -----------------------------------------
# converting xml string data to py obj

# tree = ET.fromstring(data)
# print(tree) #<Element 'metadata' at 0x0000018485F6FB00> 
# returns obj named main root tag <metadata>

# print(type(tree)) #<class 'xml.etree.ElementTree.Element'>
# print(tree.tag) #metadata

# print(tree[0][3].tag) #calories
# -----------------------------------------
# converting an xml file to py obj

# treeObj = ET.parse('sample.xml')
# tree = treeObj.getroot()
# print(tree) #<Element 'catalog' at 0x00000246C7A1FBA0>

# for i in tree:
#     print(i) 
# returns list of book obj

# for i in tree[0]:
#     print(i.tag)
# out:
# author
# title
# genre
# price
# publish_date
# description
# -----------------------------------------
# -----------------------------------------
# to get attribute
# treeObj = ET.parse('sample.xml')
# tree = treeObj.getroot()

# for i in tree:
#     print(i.tag, i.attrib) 
    # attribute is returned as dictionary
    # for no attrib, empty dict is returned
# book {'id': 'bk101'}
# book {'id': 'bk102'}
# book {'id': 'bk103'} ...

# ----------------------
# to get content of a tag
# treeObj = ET.parse('sample.xml')
# tree = treeObj.getroot()

# for i in tree.findall('book'):
#     author = i.find('author').text
#     title = i.find('title').text
#     print(author, title)
# Gambardella, Matthew XML Developer's Guide
# Ralls, Kim Midnight Rain
# Corets, Eva Maeve Ascendant
# ...
# -----------------------------------------
# to edit a tag content and attribute

treeObj = ET.parse('sample.xml')
tree = treeObj.getroot()

# # iter - to iterate over a specified tag in file
# for i in tree.iter('description'):
#     # iterates over all description tags
#     new = str(i.text) + 'new data has been added'
#     i.text = new

# # add this updates tag including all the other tags to new file
# treeObj.write('newSample.xml')

# for i in tree.iter('description'):
#     new = str(i.text) + 'new data has been added'
#     i.text = new
#     i.set('update', 'yes') #to add attribute to <description>
# treeObj.write('newSample1.xml')
# -------------------------------------------
# -------------------------------------------
# to edit in limited number of tags

treeObj = ET.parse('sample.xml')
tree = treeObj.getroot()

# for i in tree[0].iter('description'):
#     new = str(i.text) + 'new data has been added'
#     i.text = new
#     i.set('update', 'yes') #to add attribute to <description>
# treeObj.write('newSample2.xml')

# tree[0][0].text  = 'new'
# treeObj.write('sample7.xml')
# -------------------------------------------
# to create a new tag
# treeObj = ET.parse('sample.xml')
# tree = treeObj.getroot()

# to add new tag in first book tag
# ET.SubElement(tree[0], 'speciality')
# for i in tree[0].iter('speciality'):
#     i.text = 'indian'
# treeObj.write('sample3.xml')

# for i in tree.iter('book'):
#     new = ET.SubElement(i, 'speciality')
#     new.text = 'indian'
# treeObj.write('sample4.xml')
#   ||
#   \/
# for i in tree.findall('book'):
#     new = ET.SubElement(i, 'speciality')
#     new.text = 'indian'
# treeObj.write('sample5.xml')
#   ||
#   \/
# for i in range(len(tree)):
#     ET.SubElement(tree[i], 'speciality')
#     for j in tree[i].iter('speciality'):
#         j.text = 'indian'
# treeObj.write('sample6.xml')
# ----------------------------------------------
# to remove an attrib

# treeObj = ET.parse('newSample1.xml')
# tree = treeObj.getroot()

# # tree[0][5].attrib.pop('update')
# # treeObj.write('newSample3.xml')

# for i in tree.iter('description'):
#     i.attrib.pop('update')
# treeObj.write('newSample4.xml')

# ----------------------------------------------
# to remove a tag

# treeObj = ET.parse('newSample1.xml')
# tree = treeObj.getroot()

# # ET.dump(tree) #displays in console
# # tree[0].remove(tree[0][0])
# # treeObj.write('newSample5.xml')

# tree[0].clear()
# treeObj.write('newSample6.xml')



