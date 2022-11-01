from lxml import etree

with open("santo_domingo.osm") as f:
  xml_str = f.read()

xml_str = xml_str.encode('UTF-8')


class Node():
  
  def __init__(self, id, lat, lon, tags : dict):

    self.id = id,
    self.lat = lat,
    self.lon = lon,
    self.tags = tags

  def __str__(self):
    lat = self.lat[0]
    lon = self.lon[0]
    id = self.id[0]
    return f'{(({lat},{lon}), {id})}'

  def __repr__(self):
    return str(self)

root = etree.fromstring(xml_str)
nodes = []

for element in root.getchildren():
  if element.tag != "node" : continue
  attrib = element.attrib
  tags_dict = {}
  for tag in element.getchildren():
    tags_dict[tag.attrib['k']] = tag.attrib['v']
  node = Node(
      attrib["id"],
      attrib["lat"],
      attrib["lon"],
      tags_dict
  )
  nodes.append(node)

nodes

graphs = {}
for element in root.getchildren():
  if element.tag != "way" : continue
  ref = []
  for tag in element.findall('nd'):
    ref.append(tag.attrib['ref'])
    graphs[element.attrib['id']] = ref
      
graphs