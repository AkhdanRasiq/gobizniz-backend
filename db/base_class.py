from sqlalchemy.ext.declarative import declarative_base

Base            = declarative_base()


# Use below code if we need a custome declarative_base and remove above code

# from typing import Any
# from sqlalchemy.ext.declarative import as_declarative, declared_attr


# @as_declarative()
# class Base:
#     id: Any
#     __name__: str

#     #to generate tablename from classname
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
