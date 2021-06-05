# protocol is a common polymorphism tool in Python
# it signals to user which functionality is expected
from typing import Protocol

class SoundMaker(Protocol):
    def info(self) -> str: ...

    def make_sound(self) -> str: ...

# here we don't create concrete SoundMakers but we signal to users of function 
# which object structure is expected
def make_sound_polymorphically(maker: SoundMaker): 
    return maker.make_sound()

# ABC module has several tools to work with abstract functionality
# It enforces abstract constraints at a runtime
from abc import ABC, abstractmethod

class BaseSoundMaker(ABC, SoundMaker):
    def info(self) -> str: 
        return 'Default info'

    # method marked as abstract doesn't have implementation 
    # but requires to be overridden by child classes
    @abstractmethod
    def make_sound(self) -> str: ...


class Duck(BaseSoundMaker):
    # method override, without it TypeError is thrown
    def make_sound(self) -> str:
        return 'Quack!!'

    # we have 'magical' methods that are used by interpreter 
    # to execute operators against objects
    # For example with this add we can sum two Ducks
    def __add__(self, other: 'Duck') -> str:
        return 'DoubleDuck!!!'

my_duck = Duck()
second_duck = Duck()

my_duck + second_duck