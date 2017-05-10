
def family_tree(fam):
    """ Vrni slovar v katerem je ima vsak starš seznam svojih otrok """
    family = {}
    for parent, child in fam:
        if parent in family:
            family[parent].append(child)
        else:
            family[parent] = [child]
    return family


def children(tree, name):
    """ Vrni seznam imen otrok osebe z imenom 'name' """
    if name in tree:
        return tree[name]
    else:
        return None


def grandchildren(tree, name):
    """ Vrni seznam imen vnukov osebe z imenom 'name' """
    grand = []
    if name in tree:
        for child in tree[name]:
            if child in tree:
                grand.extend(tree[child])
    return grand


def main():
    family = [  ('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'),
                ('alice', 'mary'), ('alice', 'tom'), ('alice', 'judy'),
                ('renee', 'rob'), ('renee', 'bob'), ('sid', 'rob'),
                ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'),
                ('rob', 'jim')]
    tree = family_tree(family)
    print(children(tree, "bob"))
    print(children(tree, "alice"))
    print(grandchildren(tree, "sid"))
    print(grandchildren(tree, "tom"))

if __name__ == "__main__":
    main()
