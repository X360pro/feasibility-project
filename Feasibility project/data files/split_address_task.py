import pandas as pd
from itertools import chain

address_data = pd.read_excel("201909 12 WIPO compare list.xlsx",engine='openpyxl',)


address_data['WIPO_STREET_SEPERATE'] = "placeholder"


for id,row in address_data.iterrows():
    address = row.WIPO_STREET
    len_of_address = len(address)
    flag = True
    i=0
    street_name = []
    pincode = []
    city_name = []
    while flag and i<len_of_address :
        if str(address[i]).isdigit():
            spcl_str = []
            while address[i]!= " ":
                if not(str(address[i]).isdigit()):
                    break
                spcl_str.append(address[i])
                i+=1
            if len(spcl_str)==5:
                pincode = spcl_str
                break
            else:
                street_name += spcl_str
        else:
            street_name.append(address[i])
            i+=1
    while i<len_of_address:
        city_name.append(address[i])
        i+=1
    res = [''.join(str(ele)) for ele in street_name]
    address_data.loc[id,"WIPO_STREET_SEPERATE"] = "".join(res)
    res = [''.join(str(ele)) for ele in pincode]
    address_data.loc[id,"WIPO_COUNTRY_CODE"] = "".join(res)
    res = [''.join(str(ele)) for ele in city_name]
    address_data.loc[id,"WIPO_CITY"] = "".join(res)

header = ["WIPO_ORGANIZATION_NAME","WIPO_STREET","WIPO_CITY","WIPO_COUNTRY_CODE","WIPO_STREET_SEPERATE"]

address_data.to_excel('split_address_task.xlsx')

