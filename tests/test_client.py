import unittest
from signrequest_client import SignRequestClient


class TestClient(unittest.TestCase):
    """
    This is a quick integration test only usable for SignRequest developers
    """
    def setUp(self):
        self.client = SignRequestClient(
            username='testuser@signrequest.com', password='testuser',
            subdomain='test-subdomain',
            api_base_endpoint='http://localhost:8080/api/v1/'
        )

    def test_client(self):
        with open('SignRequestDemoDocument.pdf') as f:
            doc = self.client.create_document_from_file(file_object=f)
            uuid = doc.get('uuid')
            self.assertIsNotNone(uuid)

        signrequest = self.client.create_signrequest(
            uuid, from_email='testuser@signrequest.com', who='o',
            signers=[
                {'email': 'michael@signrequest.com'}
            ])

        signrequest_uuid = signrequest.get('uuid')
        self.assertIsNotNone(signrequest_uuid)

        doc = self.client.get_document(uuid)
        uuid = doc.get('uuid')
        self.assertIsNotNone(uuid)

        events = self.client.get_events()
        self.assertGreaterEqual(events['count'], 1)

        events_for_doc = self.client.get_events(doc_uuid=uuid)
        self.assertGreaterEqual(events_for_doc['count'], 1)

        all_docs = self.client.get_documents()
        self.assertGreaterEqual(all_docs['count'], 1)

        filtered_docs = self.client.get_documents(filter_params='signrequest__from_email=testuser@signrequest.com')
        self.assertGreaterEqual(filtered_docs['count'], 1)

if __name__ == '__main__':
    unittest.main()
