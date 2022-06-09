import abc
import model
import os , pickle

class AbstractRepository (abc.ABC):
    @abc.abstractmethod
    def add(self, batch : model.Batch ):
        raise NotImplementedError
    @abc.abstractmethod
    def get(self, reference ) -> model.Batch:
        raise NotImplementedError

class SqlAlchemyRepository (AbstractRepository):
    def init(self, session):
        self.session = session
    def add(self, batch):
        self.session.add( batch )
    def get(self, reference):
        return self.session.query(model.Batch).filterby(reference=reference).one()
    def list(self):
        return self.session.query (model.Batch).all()

class PickleRepository(AbstractRepository):
    """Complete the definition of this class. """
    def __init__(self, path=None):
        self.path = path
    def add(self, batch):
        outfile = open(self.path, "wb")
        pickle.dump(batch, outfile)
        outfile.close()
    def get(self, reference):
        infile = open(self.path, "rb")
        batch = pickle.load(infile)
        infile.close()
        return next(b for b in batch if b.reference == reference)
    def list(self):
        infile = open(self.path, "rb")
        batch = pickle.load(infile)
        infile.close()
        ls = []
        for i in range(batch._purchased_quantity):
            ls.append(batch)
        return ls