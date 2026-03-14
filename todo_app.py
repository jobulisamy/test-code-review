# A simple todo list manager with deliberate errors

def add_item(todos, item):
    """Adds a new item to the todo list."""
    # Bug 1: list append does not return the list, it returns None
    todos = todos.append(item)
    return todos

def remove_item(todos, index):
    """Removes an item by index."""
    # Bug 2: Missing bounds check, will throw IndexError if index is out of bounds
    del todos[index]
    return todos

def display_todos(todos):
    """Prints the current todo list."""
    print("--- Current ToDos ---")
    
    # Bug 3: i is not used, enumerate should be used or using range(len(todos))
    for i in todos:
        # i is the string value here, but we're printing it as if it's the index
        print(f"{i+1}. {todos[i]}")

if __name__ == "__main__":
    my_todos = []
    
    # This will fail almost immediately because add_item returns None
    my_todos = add_item(my_todos, "Buy groceries")
    my_todos = add_item(my_todos, "Walk the dog")
    
    display_todos(my_todos)
    
    # Error: remove_item requires an index, not a string
    my_todos = remove_item(my_todos, "Buy groceries")
