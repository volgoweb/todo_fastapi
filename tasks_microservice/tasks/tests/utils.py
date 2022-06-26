class Anything:
    """An object of this class is equal any another objec.
    It's really helpful in checking of dictionaries in tests.
    Example:
        def test_something():
            # ...
            assert result == {
                'attr_with_unpredictable_value': Anything(),
                'attr1': 'txt',
            }
    """
    def __eq__(self, other):
        return True
