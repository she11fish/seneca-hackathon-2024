from pypdf import PdfReader 
from PIL import Image
import pytesseract
import cohere
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)
reader = PdfReader('sampleDocument/standardleaseontario.pdf')
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


for key, value in cleaned.items():
    if value = ""
    print(f"{key}: {value} ")
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
    
# co.chat(
#   model="command",
#   message="What is the landlord name",
#   documents=[{"title": f"User's lease Agreement page {i}", "snippet": reader.pages[i].extract_text()} for i in range(n)])
# response = co.chat(
#   model="command",
#   message="What is the tenan name",
#   prompt_truncation="AUTO",
#   documents=[{"title":key,"snippet": str(value)} for key, value in reader.get_fields().items()])

# print(response.text)