"""This module shows sample class declaration and it's usage."""

class Doberman():
    """This class docstring shows how to use sphinx and rst syntax

    The first line is brief explanation, which may be completed with 
    a longer one. For instance to discuss about its methods. The only
    method here is :func:`function1`'s. The main idea is to document
    the class and methods's arguments with 

    - **parameters**, **types**, **return** and **return types**::

          :param arg1: description
          :param arg2: description
          :type arg1: type description
          :type arg1: type description
          :return: return description
          :rtype: the return type description

    - and to provide sections such as **Example** using the double commas syntax::

          :Example:

          followed by a blank line !

      which appears as follow:

      :Example:

      followed by a blank line

    - Finally special sections such as **See Also**, **Warnings**, **Notes**
      use the sphinx syntax (*paragraph directives*)::

          .. seealso:: blabla
          .. warnings also:: blabla
          .. note:: blabla
          .. todo:: blabla

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: That (and when) a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.

    Here below is the results of the :func:`function1` docstring.

    """

    def __init__(self, bark_sound):
        """Create new doberman.

        :param bark_sound: bark sound of this doberman
        :type bark_sound: str

        """

        self.bark_sound = bark_sound

    def bark(self):
        """Barking sound specific to this doberman.

        :rtype: str

        :Example:

        >>> dobby = Doberman("Hello Monadic World!")
        >>> dobby.bark()
        'Hello Monadic World!'

        """

        return self.bark_sound        

    @staticmethod
    def default_bark(): 
        """Barking sound common to all dobermans.

        :rtype: str

        :Example:

        >>> Doberman.default_bark()
        'Default barking...'
        
        """
        
        return 'Default barking...'


if __name__ == '__main__':
    dog_charlie = Doberman('Loud barking...')
    dog_bravo = Doberman('Not so loud barking...')

    print(dog_charlie.bark())
    print(dog_bravo.bark())
    print(dog_charlie.default_bark())
    print(dog_bravo.default_bark())
    print(Doberman.default_bark())
    print(type(dog_bravo))