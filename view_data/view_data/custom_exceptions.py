class EmptyHostnameInputError(Exception):
    """Raised when hostname is empty"""

    pass


class EmptyDatabaseInputError(Exception):
    """Raised when database name is empty"""

    pass


class EmptyPortInputError(Exception):
    """Raised when port number is empty"""

    pass


class EmptyUserInputError(Exception):
    """Raised when user is empty"""

    pass


class EmptyPasswordInputError(Exception):
    """Raised when password is empty"""

    pass
class EmptyQueryInput(Exception):
    """Raised when query is empty in read records"""

    pass