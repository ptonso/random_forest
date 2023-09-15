class Node:
    def __init__(self,data):
        self.data = data
        self.n = 1
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def count_child(self):
        n_child = 0
        c = self.children
        if c:
            n_child += len(c)
            for child in self.children:
                child.count_child()
        return n_child
    
    def add_element(self):
        self.n += 1

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + '|--' if self.parent else ""
        sufix = ' : ' + str(self.n)

        print(prefix + self.data + sufix)
        if self.children:
            for child in self.children:
                child.print_tree()



# Example

def build_product_tree():
    root = Node("Products")

    laptop = Node("Laptop")
    laptop.add_child(Node("Mac"))
    laptop.add_child(Node("Surface"))
    laptop.add_child(Node("Thinkpad"))

    cellphone = Node("Cell Phone")
    cellphone.add_child(Node("iPhone"))
    cellphone.add_child(Node("Google Pixel"))
    cellphone.add_child(Node("Vivo"))

    tv = Node("TV")
    tv.add_child(Node("Samsung"))
    tv.add_child(Node("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    print(root.get_level())
    root.print_tree()
    pass