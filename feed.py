# Practical Actions Page: https://raybo.org/slides_practicalactions/site/slides/01_01/index.html 
# Apple RSS Feed Info: https://help.apple.com/itc/podcasts_connect/#/itcbaf351599

import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    # Creates an element in an xml tree and an rss tag within that element
    rss_element = xml_tree.Element('rss', {
        'version':'2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    })

# Creates a channel tag with no subdata
channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']

# Creates a title tag within the channel tag, pulling text labled by title from the feed.yaml file
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']

# Brckets are used to add elements, 'href' is used in RSS info for apple podcasts
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})

xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix

xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

# RSS info has every episode listed with the "item" tag
for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    # Grab the same author info for every episode
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']

    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })
    


# Builds a tree out of the element that we've been building to be outputted
output_tree = xml_tree.ElementTree(rss_element)

# Encoding found at the top of RSS info for apple podcasts
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True) 