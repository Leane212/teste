import pytest
from python.atividades.atividade09_collection import Item, ItemCollection

def test_add_item_valido():
    collection = ItemCollection()
    item = Item(name="papel")

    collection.add_item(item)
    assert collection.get_items()[0] == item        
    assert len(collection.get_items()) == 1    

def test_add_item_invalido():
    collection = ItemCollection()

    with pytest.raises(ValueError) as e:
        collection.add_item(None)
    assert str(e.value) == 'Item must be a valid Item instance'
    
    with pytest.raises(ValueError) as e:
        collection.add_item("not_an_item_instance")
    assert str(e.value) == 'Item must be a valid Item instance'

def test_remove_item():
    collection = ItemCollection()
    item = Item(name="item1")
    collection.add_item(item)

    collection.remove_item(item)
    assert len(collection.get_items()) == 0

def test_remove_nonexistent_item():
    collection = ItemCollection()
    item = Item(name="papel")

    with pytest.raises(ValueError) as e:
        collection.remove_item(item)
    assert str(e.value) == 'Item not found in the collection'

