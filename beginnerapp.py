# Imports required
import json
import pandas as pd


final_data = {'label': '', 'id': '', 'link': '', 'children': []}



def csv_to_json_convertor():
    """This function is to upload the CSV file into the Program"""

    try:
        df = pd.read_csv('data.csv') #Reading Csv.

    except FileNotFoundError:
        print("File was not found!")

    df.dropna(how='all', inplace=True)  #dropping the null rows
    df.fillna(0, inplace=True)  #Placing 0 where there is empty columns


    records = df.to_dict('records')
    # print(records)


    try:
        final_data['label'] = records[0]['Level 1 - Name']
        final_data['id'] = records[0]['Level 1 - ID']
        final_data['link'] = records[0]['Level 1 - URL']
    except:
        print("Root node error.")
        return

    level2_ids = []
    level3_ids = []

    for record in records:
        if record['Level 2 - ID'] and not record['Level 2 - Name'] == 0 and record['Level 2 - ID'] not in level2_ids:
            level2_ids.append(record['Level 2 - ID'])
            final_data['children'].append(
                {'label': record['Level 2 - Name'], 'link': record['Level 2 URL'], 'id': (record['Level 2 - ID']),
                 'children': []})
        if record['Level 3 - ID'] and not record['Level 3 - Name'] == 0 and record['Level 3 - ID'] not in level3_ids:
            level3_ids.append(record['Level 3 - ID'])
            level2_child = next(target for target in final_data['children'] if target["id"] == record['Level 2 - ID'])
            level2_child['children'].append(
                {'label': record['Level 3 - Name'], 'link': record['Level 3 URL'], 'id': (record['Level 3 - ID']),
                 'children': []})

    """Dumping the data into Json text format """

    with open('struct.json', 'w') as f:
        json.dump(final_data, f, indent=4)
        print('Stuct.json file has been created.')

    print(final_data)
    print('bye bye')
    return final_data

csv_to_json_convertor()