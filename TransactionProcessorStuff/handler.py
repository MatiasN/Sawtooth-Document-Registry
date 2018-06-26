import logging
import hashlib

import cbor


from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.exceptions import InternalError

LOGGER = logging.getLoggeer(__name__)

MAX_NAME_LENGTH = 64

MAX_AUTHOR_LENGTH = 32

DOC_HASH_LENGTH = 512

FAMILY_NAME = 'registry'

REGISTRY_ADDRESS_PREFIX = hashlib.sha512(
    FAMILY_NAME.encode('utf-8')).hexdigest()[0:6]

def make_registry_address(name):
    return INTKEY_ADDRESS_PREFIX + hashlib.sha512(
        name.encode('utf-8')).hexdigest()[:64]

class RegistryTransactionHandler(TransactionHandler):
	 @property
    def family_name(self):
        return FAMILY_NAME

    @property
    def family_versions(self):
        return ['0.1']

    @property
    def namespaces(self):
        return [REGISTRY_ADDRESS_PREFIX]

    def apply(self, transaction, context):
        
        header = transaction.header
        signer = header.signer_public_key

        name, author, docHash, url = _unpack_transaction(transaction)

        state = _get_state_data(name, context)

        updated_state = _do_register(name, author, docHash, url, state)

        _set_state_data(name, updated_state, context)

	def _unpack_transaction(transaction):
    	name, author, docHash = _decode_transaction(transaction)
	
    	_validate_name(name)
    	_validate_author(author)
    	_validate_docHash(docHash)
	
    	return name, value


    def _validate_name(name):
    	if not isinstance(name, str) or len(name) > MAX_NAME_LENGTH:
        	raise InvalidTransaction(
            	'Name must be a string of no more than {} characters'.format(
                	MAX_NAME_LENGTH))


    def _validate_author(author):
    	if not isinstance(author, str) or len(author) > MAX_AUTHOR_LENGTH:
        	raise InvalidTransaction(
            	'Author must be a string of no more than {} characters'.format(
                	MAX_NAME_LENGTH))    

    def _validate_docHash(docHash):
    	if not isinstance(docHash, str) or not len(docHash) == 512:
        	raise InvalidTransaction(
            	'docHash must be a sha512 hash'.format(
                	MAX_NAME_LENGTH))

    def _decode_transaction(transaction):
    	try:
        	content = cbor.loads(transaction.payload)
    	except:
        	raise InvalidTransaction('Invalid payload serialization')

    	try:
        	name = content['Name']
    	except AttributeError:
        	raise InvalidTransaction('Name is required')

    	try:
        	author = content['Author']
    	except AttributeError:
        	raise InvalidTransaction('Author is required')

        try:
        	docHash = content['DocHash']
    	except AttributeError:
        	raise InvalidTransaction('DocHash is required')

        try:
            url = content['Url']
        except AttributeError:
            raise InvalidTransaction('url is required')

    	return name, author, docHash, url


    def _get_state_data(name, context):
    	address = make_registry_address(name)

    	state_entries = context.get_state([address])

    	try:
        	return cbor.loads(state_entries[0].data)
   	 	except IndexError:
        	return {}
    	except:
        	raise InternalError('Failed to load state data')

    def _set_state_data(name, state, context):
    	address = make_intkey_address(name)

    	encoded = cbor.dumps(state)

    	addresses = context.set_state({address: encoded})

    	if not addresses:
        	raise InternalError('State error')

    def _do_register(name, author, docHash, url, state):
        msg = 'Setting "{n}" to author:{v}, hash:{t} and url:{u}'.format(
                                    n=name, v=author, t=docHash, u=url)
        LOGGER.debug(msg)

        updated = {k: v for k, v in state.items()}
        updated[name] = name, author, docHash, url

        return updated