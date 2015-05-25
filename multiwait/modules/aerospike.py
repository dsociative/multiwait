from __future__ import absolute_import

from . import register
from .base import Condition


class AerospikeWait(Condition):
    '''
    Wait until aerospike has finished loading indexes.
    '''

    defaults = {
        'host': 'localhost',
        'port': 3000
    }

    def test(self):
        import aerospike
        from aerospike.exception import ClientError
        config = {
            'hosts': [ (self.host, self.port) ]
        }
        client = aerospike.client(config)

        try:
            client.connect()
            return True
        except ClientError:
            return False




register('aerospike', AerospikeWait)