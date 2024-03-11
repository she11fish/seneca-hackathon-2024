import { Chat, MessageType, darkTheme } from '@flyerhq/react-native-chat-ui';
import { useState } from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { Button, Text, XStack } from 'tamagui';

const uuidv4 = () => {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = Math.floor(Math.random() * 16);
    const v = c === 'x' ? r : (r % 4) + 8;
    return v.toString(16);
  });
};
export default function TabTwoScreen() {
  const [messages, setMessages] = useState<MessageType.Any[]>([
    {
      author: { id: '06c33e8b-e835-4736-80f4-63f44b666662' },
      createdAt: Date.now(),
      id: uuidv4(),
      text: 'Greetings User!',
      type: 'text',
    },
  ]);
  const user = { id: '06c33e8b-e835-4736-80f4-63f44b66666c' };

  const addMessage = (message: MessageType.Any) => {
    setMessages([message, ...messages]);
  };

  const handleSendPress = (message: MessageType.PartialText) => {
    const textMessage: MessageType.Text = {
      author: user,
      createdAt: Date.now(),
      id: uuidv4(),
      text: message.text,
      type: 'text',
    };
    addMessage(textMessage);
  };
  return (
    <SafeAreaProvider>
      <XStack backgroundColor="#1f1c38" pt={30} justifyContent="space-evenly">
        <Button backgroundColor="$blue10">
          <Text color="white">Recommendation</Text>
        </Button>
        <Button backgroundColor="$blue10">
          <Text color="white">Tutorial</Text>
        </Button>
      </XStack>
      <Chat
        messages={messages}
        renderCustomMessage={() => null}
        onSendPress={handleSendPress}
        user={user}
        theme={{
          ...darkTheme,
        }}
      />
    </SafeAreaProvider>
  );
}
