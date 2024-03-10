import { Link } from 'expo-router';
import { Pressable } from 'react-native';
import { YStack, H2, Separator, Image } from 'tamagui';

import { Container } from '~/tamagui.config';

export default function TabOneScreen() {
  const size = 200;
  return (
    <Container>
      <YStack flex={1} alignItems="center" justifyContent="center">
        <Image
          maxWidth={size}
          maxHeight={size}
          position="absolute"
          bottom={-60}
          left={-120}
          source={require('../../assets/purple.png')}
          width="100%"
          backgroundColor="#0f172a"
          transform={[{ rotate: '0deg' }]}
        />
        <Image
          maxWidth={size}
          maxHeight={size}
          position="absolute"
          bottom={-60}
          right={-100}
          source={require('../../assets/purple-blue.png')}
          width="100%"
          backgroundColor="#0f172a"
          transform={[{ rotate: '0deg' }]}
        />
        <Image
          maxWidth={size}
          maxHeight={size}
          position="absolute"
          top={-40}
          left={-120}
          source={require('../../assets/green-left.png')}
          width="100%"
          backgroundColor="#0f172a"
          transform={[{ rotate: '90deg' }]}
        />
        <Image
          maxWidth={size}
          maxHeight={size}
          position="absolute"
          top={-30}
          right={-100}
          source={require('../../assets/darker-green-left.png')}
          width="100%"
          backgroundColor="#0f172a"
          transform={[{ scaleX: -1 }, { rotate: '180deg' }]}
        />
        <Link href={'/chat'}>
          <H2>Welcome to LeaseEase</H2>
        </Link>
        <Separator />
      </YStack>
    </Container>
  );
}
