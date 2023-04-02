import json
import argparse

#Get the path for inputjson argparse
parser = argparse.ArgumentParser(description='Idealize labelmap')
parser.add_argument('input',
                    help='The path that contains .meta files',
                    type=str)

args = parser.parse_args()

inputjson = args.input

def add_attribute_ids_to_json(input_path, output_path):
    with open(input_path, 'r', encoding="utf8") as f:
        data = json.load(f)
        attributesSection = data['attributes']
        
        for i, class_id in enumerate(attributesSection.keys()):
            attributes = attributesSection[class_id]['attributes']
            
            for j, attribute in enumerate(attributes):
                attribute['id'] = j
                
        with open(output_path, 'w', encoding="utf8") as f:
            data['attributes'] = attributesSection
            json.dump(data, f, ensure_ascii=False)

def main():
    add_attribute_ids_to_json(inputjson, 'output.json')
    print('Done')

if __name__ == '__main__':
    main()


