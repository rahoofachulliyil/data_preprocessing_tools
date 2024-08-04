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


class EmptyInputDataframeError(Exception):
    """Raised when Dataframe is empty"""

    pass


class ColumnNameNotMatchError(Exception):
    """Raised column name in input and database is different"""

    pass
