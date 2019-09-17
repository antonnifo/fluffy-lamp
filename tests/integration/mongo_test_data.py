insert_one_data = {"name" : "anton" , "company" : "icodea"}

insert_many_data      = [

    {"name" : "antonnifo", "company" : "Icodeai"           },
    {"name" : "chris"    , "company" : "Techbiz"           },
    {"name" : "ashley"   , "company" : "Yusudi"            },
    {"name" : "mwas"     , "company" : "pangani smokers"   },
    {"name" : "kamau"    , "company" : "kamau traders"     },
    {"name" : "otieno"   , "company" : "otis sugar"        },
    {"name" : "antonnif" , "company" : "icodea"            }
]

print_many_query_data   = {'name': {'$regex': '^a'}}
print_many_query_2_data = {'company': 'Icodeai'}

update_one_query = {"name": "antonnif"}
set_values = {"$set": {"name": "alaska"}}

update_many_query = {"name" : {"$regex" : "^a"}}
set_values_2 = {"$set": {"name": "pynifo"}}
