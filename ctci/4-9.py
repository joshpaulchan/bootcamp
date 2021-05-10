
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        if not self.left and not self.right:
            return f"{self.data}"
        return f"({self.left}) <- {self.data} -> ({self.right})"

def find_sequences_that_make_tree(tree):
    print(tree)
    pass


def main():
    tree_from_1_to_10 = Tree(5,
        Tree(3,
            Tree(2,
                Tree(1)
            ),
            Tree(4)
        ),
        Tree(8,
            Tree(7,
                Tree(6)
            ),
            Tree(10,
                Tree(9)
            )
        ),
    )

    find_sequences_that_make_tree(tree_from_1_to_10)

if __name__ == "__main__":
    main()

