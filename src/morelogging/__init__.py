import uuid
from functools import cached_property
import hashlib

class LogHandler:
    ...

class LogStream:
    def __init__(self, name: str) -> None:
        self.name = name
        self.uuid = uuid.uuid4().hex
        self.data = []
        self.handlers = {}

    @cached_property
    def identifier(self) -> str:
        return hashlib.sha3_512(str((self.name, self.uuid)))

    def add_handler(self, handler) -> str:
        self.handlers[handler.identifier] = handler
        return handler.identifier

    def remove_handler(self, handler_id: str) -> LogHandler:
        if self.handlers.get(handler_id):
            return self.handlers.pop(handler_id)
        else:
            raise KeyError(f"Attempted to remove handler with identifier {handler_id} form log stream {self.name} ({self.identifier}), meanwhile {handler_id} was not found.")

    def __setattr__(self, name, value):
        if name in {'name', 'uuid'}:
            raise RuntimeError(f"Attempted to modify immutable property {LogStream.name} to '{value}'.")
        self.__dict__[name] = value

    def add_item(self, item: list) -> None:
        self.data.append(item)
        for handler in self.handlers.values():
            handler.push(item)
