export interface LeaseExtraction {
  landlord_name: string;
  landlord_company: string;
  'Tenant 1 Name': string;
  'rental address': string;
  landlord_email: string;
  tenant_email: string;
  'Phone number for emergencies or day to day': string;
  date_tenancy_begins: string;
  date_tenancy_ends: string;
  how_to_pay_rent: string;
  'parking rent': number;
  'base rent': number;
  'deposit amount': number;
  total_paid_each_cycle: number;
  services_and_utilities_provided: string[];
  tenant_and_landlord_responsibility: string[];
}
