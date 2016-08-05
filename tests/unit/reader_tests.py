from balance import reader
from nose.tools import assert_equal


def test_transaction_import_mapping():
    mappings = [
        ("foo", 8)
    ]
    expected = [
        { "foo": "DE24ZZZ00000561652" }
    ]
    actual = reader.read_transactions('examples/dummy.csv', mappings)
    assert_equal(actual, expected)
