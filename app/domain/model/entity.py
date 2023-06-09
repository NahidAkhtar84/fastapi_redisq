import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Entity:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # Unique identifier of the entity that will be used for internal linkage
    id = Column(BigInteger, primary_key=True, index=True)

    # Unique identifier of the entity that will be used for external purpose
    uuid = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)

    # when the entity was created
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    # who created the entity
    created_by = Column(UUID(as_uuid=True))

    # when the entity was last updated
    updated_at = Column(DateTime(timezone=True))

    # who updated the entity last time
    updated_by = Column(UUID(as_uuid=True))

    # any specific notes to keep track?
    notes = Column(String)

    # version of the entity
    version = Column(Integer, default=1)

    # status of the entity(L - Live, D - Deleted, A - Archived)
    status = Column(String, default="L")
