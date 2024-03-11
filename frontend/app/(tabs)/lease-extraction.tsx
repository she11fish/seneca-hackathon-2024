import * as DocumentPicker from 'expo-document-picker';

import { Container } from '~/tamagui.config';
import { useState } from 'react';
import { Button, H1, H3, H5, H6 } from 'tamagui';
import FontAwesome from '@expo/vector-icons/FontAwesome';
import LeaseExtractionInfo from '~/components/LeaseExtractionInfo';

export default function LeaseExtraction() {
  const [pdf, setPdf] = useState<DocumentPicker.DocumentPickerAsset>();
  const [uploadStatus, setUploadStatus] = useState<boolean>(false);

  const uploadLease = async () => {
    try {
      const result = await DocumentPicker.getDocumentAsync({ type: 'application/pdf' });
      if (!result.canceled) {
        console.log(pdf);
        setPdf(result.assets[0]);
      }
    } catch (error) {
      console.error('Error picking PDF', error);
    }
  };
  const upload = async () => {
    setUploadStatus(true);
  };

  if (!uploadStatus) {
    return (
      <Container style={{ flex: 1 }} justifyContent="center" alignItems="center">
        <Button onPress={uploadLease} w={'100%'} h={'20%'} textAlign="center">
          <H1 color="#38bdf8">Select Lease</H1>
          {/* <FontAwesome color="#38bdf8" size={80} name="cloud-upload" /> */}
        </Button>
        {pdf && (
          <H6 mt="$5" color="#38bdf8">
            {pdf.name}
          </H6>
        )}
        {pdf && (
          <Button mt={30} onPress={upload} w={'50%'} h={'10%'} textAlign="center">
            <H3 color="#38bdf8">Upload</H3>
          </Button>
        )}
      </Container>
    );
  }
  return <LeaseExtractionInfo />;
}
