from pypdf import PdfReader 
from PIL import Image
from dotenv import load_dotenv
import os
import string
import json


def extract(path):
    reader = PdfReader(path)
    fields = reader.get_fields()
    # print(reader.get_fields().keys())
    cleaned = {}
    cleaned["landlord_name"] = fields["Landlords Legal Name"]["/V"]
    cleaned["landlord_company"] = fields["Landlords Legal Name"]["/DV"]
    tenants_first_name = [fields[f"First Name Tenant {i}"]["/V"] for i in range(1, 5)]
    tenants_last_name = [fields[f"Last Name Tenant {i}"]["/V"] for i in range(1, 5)]
    for i in range(4):
        name = f"{tenants_first_name[i]} {tenants_last_name[i]}"
        if len(name) > 5:
            cleaned[f"Tenant {i+1} Name"] = name

    cleaned["rental address"] = f"{fields["Rental Unit Street Number"]["/DV"]} {fields["Rental Unit Street Name"]["/DV"]}, {fields["Rental Unit CityTown"]["/DV"]}, {fields["Rental Unit Postal Code"]["/DV"]}"
    cleaned["landlord_email"] = fields["Email address for Landlord"]["/DV"]
    cleaned["tenant_email"] = fields["Email address for Tenants"]["/V"]
    cleaned["Phone number for emergencies or day to day"] = fields["Phone number for emergencies or day to day"]["/DV"]
    cleaned["date_tenancy_begins"] = fields["Date Tenancy Begins"]["/V"]
    cleaned["date_tenancy_ends"] = fields["Date Tenancy Ends"]["/V"]
    cycle = "month" if fields["time rent paid"]["/V"] == "/Choice1" else fields["other eg weekly"]["/V"]
    cleaned["how_to_pay_rent"] = f"{fields["date rent due on"]["/TU"]} {fields["date rent due on"]["/DV"]} day of each {cycle}"
    cleaned["parking rent"] =  0 if fields["Parking rent"]["/V"] == '' else int(fields["Parking rent"]["/V"])
    cleaned["base rent"] = int(fields["Base rent"]["/V"][1:])
    cleaned["deposit amount"] = int(fields["rent deposit amount"]["/V"])
    cleaned["total_paid_each_cycle"] = int(cleaned["parking rent"]) + int(cleaned["parking rent"])
    cleaned["services_and_utilities_provided"] = []
    for service in ["Gas", "Air Conditioning", "Additional Storage Space", "Guest Parking"]:
        if fields[f"Services- {service}"]["/V"] == "/Choice1":
            cleaned["services_and_utilities_provided"].append(service)
    if fields["Services On Site Laundry Pay Per Use"]["/V"] == "/Yes":
        cleaned["services_and_utilities_provided"].append("Pay Per use Laundry")
    else:
        cleaned["services_and_utilities_provided"].append("Free Laundry")

    pages = []
    for x in reader.pages[7:12]:
        pages.extend(x.extract_text().split("\n"))
    result = []
    while i < len(pages):
        if pages[i][0] in string.ascii_uppercase[1:] and pages[i][1] == ".":
            print("ADDING")
            
            com = (pages[i+1] + pages[i+2]).strip()
            
            first = com.find(".")
            second = com.find(".", first + 1)
            if second == -1:
                result.append(com[:first+1])
            else: 
                if second > 100:
                    result.append(com[:second+1])
                else:
                    result.append(com[:com.find(".", second+1)])
            i+=2
        else:
            i+=1
    result.reverse()
    cleaned["tenant_and_landlord_responsibility"] = result
    json_data = json.dumps(cleaned, indent=4)
    return json_data
# Write JSON data to a file
# with open("data.json", "w") as json_file:
#     json_file.write(json_data)
        
# for y in result:
#     print(y)
# summaries = []
# response = co.summarize( 
#         text=reader.pages[11].extract_text(),
#         length='short',
#     format='paragraph',
#     model='summarize-xlarge',
#     additional_command='',
#     temperature=0.3)
# print(response.summary)
# for x in reader.pages:
    
#         ) 
# print(summaries)

# response = co.summarize(
#   model="command",
#   message="What is the tenan name",
#   prompt_truncation="AUTO")
# for i in reader.pages[te]
# print(reader.pages[10].extract_text())
# for key, value in cleaned.items():
#     # if value = ""
#     print(f"{key}: {value} ")
# for key, value in reader.get_fields().items():
#     print(key, value)

# print(fields)
# print(type(reader.get_fields()))
# printing number of pages in pdf file 
# print(reader.get_fields())
# print(type())
# getting a specific page from the pdf file 
# for page in reader.pages[:14]:
#     # extracting text from page 
#     text = page.extract_text() 
#     print(text) 

# for i in range(7, 12):
#     response = co.chat(
#     model="command",
#     message="What are the responsibility of the tenants, be specific as what listed on the document",
#     documents=[{"title": f"User's lease Agreement page {i}", "snippet": reader.pages[i].extract_text()}])
#     print(response.text)