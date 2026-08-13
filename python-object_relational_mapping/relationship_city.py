#!/usr/bin/python3
"""Module that defines the City class linked to the cities table."""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Represents a city in the cities MySQL table."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
