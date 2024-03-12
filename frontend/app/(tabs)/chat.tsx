import { Chat, MessageType, darkTheme } from '@flyerhq/react-native-chat-ui';
import { router, useFocusEffect } from 'expo-router';
import { useCallback, useEffect, useState } from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { Text } from 'tamagui';

import { MainData } from '~/types/type';

const uuidv4 = () => {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = Math.floor(Math.random() * 16);
    const v = c === 'x' ? r : (r % 4) + 8;
    return v.toString(16);
  });
};

const mockData = {
  recommend: false,
  message: '',
  recommendation: {},
} as MainData;

export default function ChatRoute() {
  const [messages, setMessages] = useState<MessageType.Text[]>([
    {
      author: { id: '06c33e8b-e835-4736-80f4-63f44b66666a' },
      createdAt: Date.now(),
      id: uuidv4(),
      text: 'Hello there!',
      type: 'text',
    },
  ]);
  const [data, setData] = useState<MainData>();
  // const [requestPending, setRequestPending] = useState<boolean>(true);

  const user = { id: '06c33e8b-e835-4736-80f4-63f44b66666c' };
  function chatQuery(chat: string) {
    console.log(chat);
    const url = `http://192.168.2.45:5000/get_response`;
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify({
        chat,
      }),
    })
      .then((res) =>
        res
          .json()
          .then((currData: MainData) => {
            setData(currData);
            console.log(currData);
            // setRequestPending(false);
            addMessage({
              author: { id: '06c33e8b-e835-4736-80f4-63f44b66666a' },
              createdAt: Date.now(),
              id: uuidv4(),
              text: currData.message,
              type: 'text',
            });
          })
          .catch((e) => console.error(e))
      )
      .catch((e) => console.error(e));
  }
  console.log(data);

  useFocusEffect(
    useCallback(() => {
      console.log('focus mounted');
      // chatQuery('');
      // setRequestPending(true);
      return () => {
        setMessages([]), console.log('focus unmounted');
      };
    }, [])
  );

  function changeResponseText(message: string) {
    if (!messages.length) {
      setMessages([
        ...messages,
        {
          author: { id: '06c33e8b-e835-4736-80f4-63f44b66666a' },
          createdAt: Date.now(),
          id: uuidv4(),
          text: message,
          type: 'text',
        },
      ]);
    } else {
      (messages[messages.length - 1] as MessageType.Text).text = message;
      setMessages(messages);
    }
  }

  const addMessage = (message: MessageType.Text) => {
    setMessages([message, ...messages]);
  };
  const handleSendPress = (message: MessageType.PartialText) => {
    // if (requestPending) return;
    const textMessage: MessageType.Text = {
      author: user,
      createdAt: Date.now(),
      id: uuidv4(),
      text: message.text,
      type: 'text',
    };
    addMessage(textMessage);
    // chatQuery(message.text);
  };
  // if (data?.recommend) {
  //   changeResponseText('You will be redirected to the recommendations page!');
  //   setTimeout(() => {
  //     router.push('/recommendation');
  //   }, 1000);
  // }

  // if (requestPending) {
  //   changeResponseText('Loading...');
  // }
  return (
    <SafeAreaProvider>
      <Chat
        messages={messages}
        renderCustomMessage={() => null}
        onSendPress={handleSendPress}
        user={user}
        theme={darkTheme}
      />
    </SafeAreaProvider>
  );
}
