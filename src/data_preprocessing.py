import os
import xml.etree.ElementTree as ET
dataset_dir = "datasets/SceneTraialTrain"
word_xml_path= os.path.join(dataset_dir, "word.xml")
# print(word_xml_path)
tree = ET.parse(word_xml_path)
root = tree.getroot()
print(root)

def extract_data_from_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    return 