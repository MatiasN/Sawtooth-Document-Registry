import cbor

from sawtooth_processor_test.message_factory import MessageFactory
from sawtooth_registry.processor.handler import REGISTRY_ADDRESS_PREFIX
from sawtooth_registry.processor.handler import make_registry_address


class IntkeyMessageFactory:
    def __init__(self, signer=None):
        self._factory = MessageFactory(
            family_name='registry',
            family_version='0.1',
            namespace=INTKEY_ADDRESS_PREFIX,
            signer=signer)

    def _dumps(self, obj):
        return cbor.dumps(obj, sort_keys=True)

    def _loads(self, data):
        return cbor.loads(data)

    def create_tp_register(self):
        return self._factory.create_tp_register()

    def create_tp_response(self, status):
        return self._factory.create_tp_response(status)

    def _create_txn(self, txn_function, name, author, docHash, url):
        payload = self._dumps({'Name': name, 'Author': author, 'DocHash': docHash, 'Url': url})

        addresses = [make_registry_address(name)]

        return txn_function(payload, addresses, addresses, [])

    def create_tp_process_request(self, verb, name, value,):
        txn_function = self._factory.create_tp_process_request
        return self._create_txn(txn_function, verb, name, value)

    def create_transaction(self, name, author, docHash, url,):
        txn_function = self._factory.create_transaction
        return self._create_txn(txn_function, name, author, docHash, url)

    def create_batch(self, triples):
        txns = [
            self.create_transaction(name, author, docHash, url)
            for name, author, docHash, url in triples
        ]

        return self._factory.create_batch(txns)

    def create_get_request(self, name):
        addresses = [make_regestry_address(name)]
        return self._factory.create_get_request(addresses)

    def create_get_response(self, name, author, docHash, url):
        address = make_registry_address(name)

        if value is not None:
            data = self._dumps({name: value})
        else:
            data = None

        return self._factory.create_get_response({address: data})

    def create_set_request(self, name, value):
        address = make_intkey_address(name)

        if value is not None:
            data = self._dumps({name: value})
        else:
            data = None

        return self._factory.create_set_request({address: data})

    def create_set_response(self, name):
        addresses = [make_intkey_address(name)]
        return self._factory.create_set_response(addresses)