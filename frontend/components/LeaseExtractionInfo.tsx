import React, { useState } from 'react';
import { StyleSheet } from 'react-native';
import { H2, H3, H4, H5, ScrollView, View } from 'tamagui';

import { Container } from '~/tamagui.config';
import { LeaseExtraction } from '~/types/type';

const lease = {
  landlord_name: 'Mark Mark',
  landlord_company: '1950979 Ontario Inc.',
  'Tenant 1 Name': 'Doe Jane',
  'rental address': '888 Whitefield Drive, Peterborough, K9J 7P6',
  landlord_email: 'pauldietrich@parkviewhomes.ca',
  tenant_email: 'janedoe@gmail.com',
  'Phone number for emergencies or day to day': '705-755-6108',
  date_tenancy_begins: '2023/02/22',
  date_tenancy_ends: '2024/02/22',
  how_to_pay_rent: 'Rent is to be paid on the first day of each month',
  'parking rent': 0,
  'base rent': 500,
  'deposit amount': 1000,
  total_paid_each_cycle: 0,
  services_and_utilities_provided: ['Gas', 'Pay Per use Laundry'],
  tenant_and_landlord_responsibility: [
    'The tenant may assign or sublet the rental unit to another person only with the consent of the landlord. The landlord cannot arbitrarily or unreasonably withhold consent to a potential assignee or sublet of the rental unit.',
    'The landlord cannot change the locks of the rental unit unless the landlord gives the new keys to the tenant. The tenant cannot change the locks of the rental unit without the consent of the landlord.',
    'The tenant is entitled to reasonable enjoyment of the rental unit (e.g. quiet enjoyment, reasonable privacy, freedom from unreasonable disturbance and exclusive use of the rental unit)',
    'If the landlord (or anyone acting for the landlord) discriminates against the tenant based on prohibited grounds of discrimination under the Ontario Human Rights Code (the Code ), they may be violating the tenant\u2019s rights under the Code.',
    '\u201cVital services\u201d are hot or cold water, fuel, electricity, gas and heat.',
    'The landlord must keep the rental unit and property in good repair and comply with all health, safety and maintenance standards.',
    "Normally, the landlord can increase the rent only once every 12 months. The landlord must use the proper Landlord and Tenant Board form and give the tenant at least 90 days' notice before the rent increase is to take effect.",
    'The landlord can only collect a deposit for the last month\u2019s rent and a refundable key deposit. The tenant does not have to provide any other form of deposit, such as pet or damage deposits.',
    'The landlord can offer the tenant a discount for paying rent on or before the date it is due. This discount can be up to two per cent of the lawful rent.',
    'The landlord and tenant have to deliver some official notices and other documents in writing.',
    'The landlord or tenant must follow the rules of the Act when ending a tenancy.',
    'If the landlord and tenant agree that the tenancy will last for a specific period of time, this is called a fixed term tenancy. This is because both the start and end date are set out in the tenancy agreement.',
    'A new landlord has the same rights and duties as the previous landlord. A new landlord must follow all the terms of this agreement unless the tenant and new landlord agree to other terms.',
  ],
} as LeaseExtraction;

export default function LeaseExtractionInfo() {
  const [showKeyNames, setShowKeyNames] = useState(true);

  return (
    <Container>
      <ScrollView>
        <View m={0} p={0}>
          <View mt={10}>
            {Object.entries(lease).map(([key, value]) => (
              <View key={key} m={0} p={0}>
                {showKeyNames && (
                  <H4 mt={2} color="white" style={styles.key}>
                    {getKeyName(key)}
                  </H4>
                )}
                <H5 mb={2}>{Array.isArray(value) ? value.join(', ') : value}</H5>
              </View>
            ))}
          </View>
        </View>
      </ScrollView>
    </Container>
  );
}

function getKeyName(key: string): string {
  switch (key) {
    case 'landlord_name':
      return 'Landlord Name';
    case 'landlord_company':
      return 'Landlord Company';
    case 'tenant_name':
      return 'Tenant Name';
    case 'rental_address':
      return 'Rental Address';
    case 'landlord_email':
      return 'Landlord Email';
    case 'tenant_email':
      return 'Tenant Email';
    case 'Phone number for emergencies or day to day':
      return 'Emergency Phone Number';
    case 'date_tenancy_begins':
      return 'Tenancy Begins';
    case 'date_tenancy_ends':
      return 'Tenancy Ends';
    case 'how_to_pay_rent':
      return 'How to Pay Rent';
    case 'parking rent':
      return 'Parking Rent';
    case 'base rent':
      return 'Base Rent';
    case 'deposit amount':
      return 'Deposit Amount';
    case 'total_paid_each_cycle':
      return 'Total Paid Each Cycle';
    case 'services_and_utilities_provided':
      return 'Services and Utilities Provided';
    case 'tenant_and_landlord_responsibility':
      return 'Tenant and Landlord Responsibilities';
    case 'Tenant 1 Name':
      return 'Tenant Name';
    case 'rental address':
      return 'Rental Address';

    // Add more cases as needed
    default:
      return key;
  }
}

const styles = StyleSheet.create({
  key: {
    fontWeight: 'bold',
  },
});
