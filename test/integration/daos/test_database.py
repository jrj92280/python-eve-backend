def test_write_to_database(mongo_database):
    item_id = mongo_database.create('items', {'name': 'cup'})
    item = mongo_database.get('items', item_id)

    assert item['name'] == 'cup'
