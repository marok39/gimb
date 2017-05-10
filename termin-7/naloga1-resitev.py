
def family_tree(family):
    """ Vrni slovar v katerem je ima vsak starš seznam svojih otrok """
    tree = {}
    for parent, child in family:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    return tree

def children(tree, name):
    """ Vrni seznam imen otrok osebe z imenom 'name' """
    if name in tree:
        return tree[name]
    return []

def grandchildren(tree, name):
    """ Vrni seznam imen vnukov osebe z imenom 'name' """
    grandchildren = []
    for child in children(tree, name):
        for grandchild in children(tree, child):
            grandchildren.append(grandchild)
    return grandchildren

def main():
    family = [  ('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'),
                ('alice', 'mary'), ('alice', 'tom'), ('alice', 'judy'),
                ('renee', 'rob'), ('renee', 'bob'), ('sid', 'rob'),
                ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'),
                ('rob', 'jim')]

    tree = family_tree(family)
    print(children(tree, 'bob'))
    print(grandchildren(tree, 'renee'))

if __name__ == "__main__":
    main()
