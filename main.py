import xml.etree.ElementTree as ET
import yaml

def parse_xml_to_dict(xml_file):
    """
    Parses the XML file and returns a list of dictionaries with radio station data.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    radios = []

    for bookmark in root.findall(".//bookmark"):
        name = bookmark.get('name')
        url = bookmark.get('url')
        radios.append({'name': name, 'format': 'mp3', 'source': url})

    return radios

def convert_to_yaml(radios, yaml_file):
    """
    Converts the list of radios to YAML format and writes it to a file.
    """
    yaml_data = {'radios': radios}
    with open(yaml_file, 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False)

def write_simple_config(radios, config_file):
    """
    Writes a simpler config file with station name and URL on each line.
    """
    with open(config_file, 'w') as file:
        for radio in radios:
            file.write(f"{radio['name']}, {radio['source']}\n")

def main():
    xml_file = 'bookmarks.xml'  # Input XML file
    # for https://github.com/angelodlfrtr/radiotray/blob/master/cmd/player/player.go project:
    yaml_file = '.radiotray.yaml'  # Output YAML file for RadioTray on MacOS, ~/.radiotray.yaml
    # for the https://github.com/jcheng8/goradio/blob/master/radio.go project:
    # download the file, then run it directly:
    # - GO111MODULE=off go get .
    # - GO111MODULE=off go run radio.go
    simple_config_file = 'stations'  # Output simple config file, ~/.goradio/stations

    # Parse the XML file
    radios = parse_xml_to_dict(xml_file)

    # Convert and write to YAML
    convert_to_yaml(radios, yaml_file)

    # Write to simpler config file
    write_simple_config(radios, simple_config_file)

    print("Conversion to YAML and simple config file completed!")

if __name__ == "__main__":
    main()

# This script does both conversions: XML to YAML and XML to a simple text config.
# Run this script with your XML file, and it will create both the .radiotray.yaml file and the simple stations config file.
# If you have any questions or need further assistance, feel free to type 'next' or 'continue'. 😄
