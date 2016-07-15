# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.types import Enum

from schematizer.models.base_model import BaseModel
from schematizer.models.database import Base
from schematizer.models.types.time import build_time_column


class EntityType(object):

    NAMESPACE = 'namespace'
    SOURCE = 'source'
    SCHEMA = 'schema'


class MetaAttributeMappingStore(Base, BaseModel):

    __tablename__ = 'meta_attribute_mapping_store'

    # The name of the entity type. It can be either namespace, source or schema.
    entity_type = Column(
        Enum(
            EntityType.NAMESPACE,
            EntityType.SOURCE,
            EntityType.SCHEMA,
            name='entity_type'
        ),
        nullable=False
    )

    # Id of the entity specified in the entity_type attribute.
    entity_id = Column(Integer, nullable=False)

    # The schema_id of the meta attribute to be mapped.
    meta_attr_schema_id = Column(Integer, ForeignKey('avro_schema.id'))

    # Timestamp when the entry is created
    created_at = build_time_column(
        default_now=True,
        nullable=False
    )

    # Timestamp when the entry is last updated
    updated_at = build_time_column(
        default_now=True,
        onupdate_now=True,
        nullable=False
    )
