import copy
import csv
import json
import os
from os.path import isfile, join

csv_file = open('231018 UNSW Building List_3.csv', newline='')
reader = csv.DictReader(csv_file)

data = {}
for row in reader:
    data[row['Ref'].strip()] = row

# Create CZML
czml = [
    {
        "id":"document",
        "version":"1.0",
        "clock": {
            "interval": "2023-12-18T00:00:00Z/2023-12-21T00:00:00Z",
            "currentTime": "2023-12-20T00:00:00Z"
        }
    }
]

files = [f for f in os.listdir("./ids") if isfile(join("./ids", f)) and f.endswith('.glb')]

for f in files:
    # building_name = f.removesuffix('.glb')
    # building_name = building_name.replace('_', ' ')
    building_ref = f.removesuffix('.glb')
    building_data = data.get(building_ref)
    building_name = building_data['Building'] if building_data else building_ref
    czml_packet = {
        "id": building_ref,
        "name": building_name,
            "position": {
            "cartographicDegrees":[
                151.2377963138279, -33.92097413945967, 0
            ]
        },
        "properties": {
            "Reference": "",
            "Building": building_name,
            "TTW Job Nos": "",
            "Year": "",
            "UNSW PM": "",
            "Age Risk Rating": 1,
            "Structural Engineer": "",
            "Structural Drawings": "",
            "Structural Framing System": "",
            "Typology Risk": 1,
            # "Structural Seismic Risk Level": 0,
            "Priority Rating": 1,
            "Façade Typology": "",
            "Façade Safety Risk": "",
            "Façade Risk Identification": "",
            "Façade Observations": "",
            "Status": "",
            "Notes": ""
        },
        "model": {
            "shadowMode": "DISABLED",
            "gltf": {
                "uri": f"https://ttwgeometrystorage.blob.core.windows.net/digitaltwins/unsw/{f}"
            },
            "nodeTransformations": {
                building_name: {
                    "rotation": {
                        "unitQuaternion": [ 0, -0.009, 0, 1 ]
                    }
                }
            },
            "scale": {
                "number": 1.0
            },
            "show": {
                "boolean": True
            }
        }
    }

    building_data = data.get(building_ref)
    if building_data:
        czml_packet["properties"]['Reference'] = building_data['Ref']
        czml_packet["properties"]['TTW Job Nos'] = building_data['TTW Job Nos']
        czml_packet["properties"]['Year'] = building_data['Year']
        czml_packet["properties"]['UNSW PM'] = building_data['UNSW PM']
        czml_packet["properties"]['Age Risk Rating'] = building_data['Age Risk Rating']
        czml_packet["properties"]['Structural Engineer'] = building_data['Structural Engineer']
        czml_packet["properties"]['Structural Drawings'] = building_data['Structural Drawings']
        czml_packet["properties"]['Structural Framing System'] = building_data['Structural Framing System']
        czml_packet["properties"]['Typology Risk'] = building_data['Typology Risk']
        czml_packet["properties"]['Priority Rating'] = building_data['Priority Rating']
        czml_packet["properties"]['Asset Priority Rating'] = building_data['Asset Priority Rating']
        czml_packet["properties"]['Façade Typology'] = building_data['Facade Typology']
        czml_packet["properties"]['Façade Safety Risk'] = building_data['Facade Safety Risk']
        czml_packet["properties"]['Façade Risk Identification'] = building_data['Facade Risk Identification']
        czml_packet["properties"]['Façade Observations'] = building_data['Facade Observations']
        czml_packet["properties"]['Status'] = building_data['Status']
        czml_packet["properties"]['Notes'] = building_data['Notes']
        # czml_packet["properties"]['Structual Seismic Risk Level'] = building_data['Structual Seismic Risk Level']

    czml.append(czml_packet)

czml_json = json.dumps(czml)
f = open('./unsw.czml', 'w')
f.write(czml_json)
f.close()
csv_file.close()

# Create CZML variations for dropdown options
year_czml = copy.deepcopy(czml)
for packet in year_czml:
    if packet['id'] == 'document':
        continue

    if packet['properties']['Age Risk Rating'] == '3':
        packet['model']['color'] = { 'rgba': [182, 209, 251, 255] }
    elif packet['properties']['Age Risk Rating'] == '5':
        packet['model']['color'] = { 'rgba': [255, 128, 255, 255] }
year_czml_json = json.dumps(year_czml)

typology_czml = copy.deepcopy(czml)
for packet in typology_czml:
    if packet['id'] == 'document':
        continue

    if packet['properties']['Typology Risk'] == '2':
        packet['model']['color'] = { 'rgba': [182, 209, 251, 255] }
    elif packet['properties']['Age Risk Rating'] == '3':
        packet['model']['color'] = { 'rgba': [255, 128, 255, 255] }
typology_czml_json = json.dumps(typology_czml)

facade_safety_czml = copy.deepcopy(czml)
for packet in facade_safety_czml:
    if packet['id'] == 'document':
        continue

    if packet['properties']['Façade Safety Risk'] == 'Very High':
        packet['model']['color'] = { 'rgba': [255, 80, 80, 255] }
    if packet['properties']['Façade Safety Risk'] == 'High':
        packet['model']['color'] = { 'rgba': [247, 155, 75, 255] }
    if packet['properties']['Façade Safety Risk'] == 'Medium':
        packet['model']['color'] = { 'rgba': [131, 255, 131, 255] }
facade_safety_czml_json = json.dumps(facade_safety_czml)

priority_czml = copy.deepcopy(czml)
for packet in priority_czml:
    if packet['id'] == 'document':
        continue

    if packet['properties']['Asset Priority Rating'] == 'HIGH':
        packet['model']['color'] = { 'rgba': [255, 80, 80, 255] }
    elif packet['properties']['Asset Priority Rating'] == 'MEDIUM':
        packet['model']['color'] = { 'rgba': [247, 155, 75, 255] }
    elif packet['properties']['Asset Priority Rating'] == 'LOW':
        packet['model']['color'] = { 'rgba': [131, 255, 131, 255] }
priority_czml_json = json.dumps(priority_czml)

# Create catalog
terria_catalog = {
    "catalog": [
        {
            "name": "TTW Digital Twins",
            "isOpen": True,
            "type": "group",
            "members": [
                {
                    "id": "unsw",
                    "name": "UNSW",
                    "type": "czml",
                    "attribution": "© 2024 Taylor Thomson and Whitting",
                    "czmlString": czml_json,
                    "modelDimensions": [
                        {
                            "id": "view_options",
                            "name": "View",
                            "options": [
                                {
                                    "id": "option1",
                                    "name": "Default",
                                    "value": {
                                        "czmlString": czml_json
                                    }
                                },
                                {
                                    "id": "option2",
                                    "name": "Age Risk",
                                    "value": {
                                       'legends': [
                                            {
                                                "title": "",
                                                "items": [
                                                    {
                                                        "title": "Building constructed pre-1979",
                                                        "color": '#ff80ff'
                                                    },
                                                    {
                                                        "title": "Building constructed 1979-1999",
                                                        "color": '#b6d1fb',
                                                        "addSpacingAbove": True,
                                                    },
                                                    {
                                                        "title": "Building constructed post-2000",
                                                        "color": '#e6dac4',
                                                        "addSpacingAbove": True,
                                                    }
                                                ]
                                            }
                                        ],
                                        "czmlString": year_czml_json
                                    }
                                },
                                {
                                    "id": "option3",
                                    "name": "Typology Risk",
                                    "value": {
                                        'legends': [
                                            {
                                                "title": "",
                                                "items": [
                                                    {
                                                        "title": "Typology risk 3",
                                                        "color": '#ff80ff'
                                                    },
                                                    {
                                                        "title": "Typology risk 2",
                                                        "color": '#b6d1fb',
                                                        "addSpacingAbove": True,
                                                    },
                                                    {
                                                        "title": "Typology risk 1",
                                                        "color": '#e6dac4',
                                                        "addSpacingAbove": True,
                                                    }
                                                ]
                                            }
                                        ],
                                        "czmlString": typology_czml_json
                                    }
                                },
                                {
                                    "id": "option4",
                                    "name": "Façade Safety Risk",
                                    "value": {
                                        'legends': [
                                            {
                                                "title": "",
                                                "items": [
                                                    {
                                                        "title": "Façade Safety Risk Very High",
                                                        "color": '#ff9696'
                                                    },
                                                    {
                                                        "title": "Façade Safety Risk High",
                                                        "color": '#f79b4b',
                                                        "addSpacingAbove": True,
                                                    },
                                                    {
                                                        "title": "Façade Safety Risk Medium",
                                                        "color": '#b3ffb3',
                                                        "addSpacingAbove": True,
                                                    },
                                                    {
                                                        "title": "Façade Safety Risk Low",
                                                        "color": '#e6dac4',
                                                        "addSpacingAbove": True,
                                                    }
                                                ]
                                            }
                                        ],
                                        "czmlString": facade_safety_czml_json
                                    }
                                },
                                {
                                    "id": "option5",
                                    "name": "Priority Rating",
                                    "value": {
                                        'legends': [
                                            {
                                                "title": "",
                                                "items": [
                                                    {
                                                        "title": "Priority AP1",
                                                        "color": '#ff9696'
                                                    },
                                                    {
                                                        "title": "Priority AP2",
                                                        "color": '#f79b4b',
                                                        "addSpacingAbove": True
                                                    },
                                                    {
                                                        "title": "Priority AP3",
                                                        "color": '#b3ffb3',
                                                        "addSpacingAbove": True
                                                    },
                                                    {
                                                        "title": "Priority AP4",
                                                        "color": '#e6dac4',
                                                        "addSpacingAbove": True,
                                                    }
                                                ]
                                            }
                                        ],
                                        "czmlString": priority_czml_json
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

with open('./unsw_4.json', 'w') as f:
    f.write(json.dumps(terria_catalog))