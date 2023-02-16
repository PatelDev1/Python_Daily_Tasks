#Single Level Inheritance

class Parent:
    def display_parent(self):
        print("This is Parent Class")


class Child(Parent):
    def display_child(self):
        print("This is Child Class")



obj = Child()
obj.display_parent()
obj.display_child()
