import json

def transform_people_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        people_data = json.load(file)

    transformed_data = []

    for person in people_data:
        transformed_person = {
            "model": "movies.person",
            "pk": person.get('id'),
            "fields": {
                "name": person.get('name'),
                "poster_path": person.get('poster_path'),
                "character": person.get('character', ''),
                "job": person.get('job', '')
            }
        }
        # Remove empty fields (character/job) if they are not provided
        transformed_person['fields'] = {k: v for k, v in transformed_person['fields'].items() if v}
        
        transformed_data.append(transformed_person)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(transformed_data, file, indent=2, ensure_ascii=False)

input_file = "people_data.json"
output_file = "transformed_people_data.json"

transform_people_data(input_file, output_file)
