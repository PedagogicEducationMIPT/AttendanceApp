def test_insert(database, records):
    database.record(records[0])
    assert database.list_all() == [records[0]]




