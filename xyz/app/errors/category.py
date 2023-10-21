class CategoryNotFoundError(ValueError):
    def __init__(self, message):
        super(CategoryNotFoundError, self).__init__(message)