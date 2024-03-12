import React from 'react';
import { View, Text, Image, H2, H5 } from 'tamagui';
import { Container } from '~/tamagui.config';
import { Recommendation } from '~/types/type';

interface Props {
  recommendation: Recommendation;
}

export default function RecommendationComponent({ recommendation }: Props) {
  const {
    price,
    house_type,
    landlord_name,
    furnished,
    num_of_room_availables,
    description,
    location,
    image,
    label,
  } = recommendation;

  return (
    <View flex={1} mt={20} justifyContent="center">
      <View>
        <View flexDirection="row">
          <Image
            source={{ uri: 'data:image/png;base64,' + image.data }}
            width="100%"
            height={200}
          />
        </View>
      </View>
      <Text color="white" fontWeight="bold">
        Property Details
      </Text>
      <Text color="white" fontWeight="bold">
        Price: ${price}
      </Text>
      <Text color="white" fontWeight="bold">
        House Type: {house_type}
      </Text>
      <Text color="white" fontWeight="bold">
        Landlord Name: {landlord_name}
      </Text>
      <Text color="white" fontWeight="bold">
        Furnished: {furnished ? 'Yes' : 'No'}
      </Text>
      <Text color="white" fontWeight="bold">
        Number of Rooms Available: {num_of_room_availables}
      </Text>
      <Text color="white" fontWeight="bold">
        Description: {description}
      </Text>
      <Text color="white" fontWeight="bold">
        Location: {location}
      </Text>
      {/* <Text color="white" fontWeight="bold">
        Label: {label}
      </Text> */}
    </View>
  );
}
