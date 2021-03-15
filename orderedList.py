class OrderedList:

    def __init__(self, identifier: str, init_list: list):
        self.identifier = identifier
        self.list = init_list
        self.list.sort()

    def get_first_occurrence(self, element) -> int:
        return self.list.index(element)

    def include_elements(self, element_list: list):
        self.list += element_list
        self.list.sort()

    def remove_range(self, start, end):
        start_index = self.list.index(start)
        end_index = len(self.list) - 1 - self.list[::-1].index(end)
        self.list = self.list[:start_index] + self.list[end_index+1:]

    def remove_first_occurrence(self, element):
        self.list.remove(element)

    def get_initial_and_end_position(self, element) -> tuple:
        initial = self.list.index(element)
        end = (len(self.list) - 1 - self.list[::-1].index(element))
        return initial, end

    def __str__(self) -> str:
        return str(self.list)


def numbersTest():
    print("\n\nTesting for Numbers\n")

    initial_list = [44,55,12,0,12,14, 50.5, 50.5]
    identifier = "Testing List"

    print("\nList before inserting into OrderedList")
    print(initial_list)
    myList = OrderedList(identifier, initial_list)
    print("\nList after inserting into OrderedList")
    print(myList)

    element = 12
    print("\nReturning first occurrence of", element)
    print(myList.get_first_occurrence(element))

    list_to_include = [10,99,54,2.5,99]
    print(f"\nIncluding list {list_to_include} to current OrderedList")
    myList.include_elements(list_to_include)
    print("After including:", myList)

    start = 2.5
    end = 12
    print(f"\nRemoving range of elements from {start} to {end}")
    myList.remove_range(start, end)
    print("After removing: ", myList)

    element = 99
    print(f"\nRemoving first occurrence of {element}")
    myList.remove_first_occurrence(element)
    print("After removing:", myList)

    element = 50.5
    print(f"\nReturning initial and final position of {element}")
    print(myList.get_initial_and_end_position(element))

    print("\nTesting the __str__ method")
    print(str(myList))


def stringTest():
    print("\n\nTesting for Strings\n")

    initial_list = ["Python", "List", "Strings", "Lists", "Week", "Weak", "Strings"]
    identifier = "Testing List"

    print("\nList before inserting into OrderedList")
    print(initial_list)
    myList = OrderedList(identifier, initial_list)
    print("\nList after inserting into OrderedList")
    print(myList)

    element = "Strings"
    print("\nReturning first occurrence of", element)
    print(myList.get_first_occurrence(element))

    list_to_include = ["Apple", "Away", "Doctor", "Apple", "Iron"]
    print(f"\nIncluding list {list_to_include} to current OrderedList")
    myList.include_elements(list_to_include)
    print("After including:", myList)

    start = "Away"
    end = "Lists"
    print(f"\nRemoving range of elements from {start} to {end}")
    myList.remove_range(start, end)
    print("After removing: ", myList)

    element = "Python"
    print(f"\nRemoving first occurrence of {element}")
    myList.remove_first_occurrence(element)
    print("After removing:", myList)

    element = "Apple"
    print(f"\nReturning initial and final position of {element}")
    print(myList.get_initial_and_end_position(element))

    print("\nTesting the __str__ method")
    print(str(myList))


if __name__ == "__main__":
    numbersTest()
    stringTest()
    
