__all__ = ['Address']


class Address(object):
    def __init__(self, address):
        self.host = None
        self.port = None
        self.path = None
        if isinstance(address, basestring):
            self.path = address
        elif len(address) >= 2:
            self.host = address[0]
            self.port = address[1]
        else:
            raise ValueError('Unexpected params for Address: {}'.format(address))

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.__dict__ == other.__dict__
        )

    def __ne__(self, other):
        return not self.__eq__(other)


    def __repr__(self):
        return "<Address host: '{}', port: '{}', path: '{}'>".format(
            self.host,
            self.port,
            self.path,
        )
