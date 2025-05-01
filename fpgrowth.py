class TreeNode:
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.link = None  # next node with same item

    def increment(self, count):
        self.count += count

def build_header_table(transactions, min_support):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    header_table = {}
    for item, count in item_counts.items():
        if count >= min_support:
            header_table[item] = [count, None]  # [count, head of node link]
    return header_table

def sort_items(transaction, header_table):
    return sorted(
        [item for item in transaction if item in header_table],
        key=lambda item: (-header_table[item][0], item)
    )

def insert_tree(transaction, node, header_table):
    if not transaction:
        return

    first_item = transaction[0]
    if first_item in node.children:
        node.children[first_item].increment(1)
    else:
        new_node = TreeNode(first_item, 1, node)
        node.children[first_item] = new_node

        # Link header table
        if header_table[first_item][1] is None:
            header_table[first_item][1] = new_node
        else:
            current = header_table[first_item][1]
            while current.link:
                current = current.link
            current.link = new_node

    insert_tree(transaction[1:], node.children[first_item], header_table)

def build_fp_tree(transactions, min_support):
    header_table = build_header_table(transactions, min_support)
    if not header_table:
        return None, None

    root = TreeNode(None, 1, None)

    for transaction in transactions:
        ordered_items = sort_items(transaction, header_table)
        insert_tree(ordered_items, root, header_table)

    return root, header_table

def find_prefix_paths(base_item, node):
    conditional_patterns = []
    while node:
        path = []
        parent = node.parent
        while parent and parent.item:
            path.append(parent.item)
            parent = parent.parent
        if path:
            conditional_patterns.append((list(reversed(path)), node.count))
        node = node.link
    return conditional_patterns

def mine_fp_tree(header_table, prefix, min_support, frequent_patterns):
    sorted_items = sorted(header_table.items(), key=lambda x: x[1][0])
    for item, (count, node) in sorted_items:
        new_pattern = prefix + [item]
        frequent_patterns.append((new_pattern, count))

        conditional_patterns = find_prefix_paths(item, node)
        conditional_transactions = []
        for pattern, count in conditional_patterns:
            conditional_transactions.extend([pattern] * count)

        subtree, sub_header = build_fp_tree(conditional_transactions, min_support)
        if sub_header:
            mine_fp_tree(sub_header, new_pattern, min_support, frequent_patterns)

def fp_growth(transactions, min_support):
    tree, header = build_fp_tree(transactions, min_support)
    frequent_patterns = []
    if header:
        mine_fp_tree(header, [], min_support, frequent_patterns)
    return frequent_patterns

transactions = [
    ['a', 'b', 'd'],
    ['b', 'c', 'e'],
    ['a', 'b', 'c', 'e'],
    ['b', 'e'],
    ['a', 'b', 'c', 'e']
]

min_support = 2
patterns = fp_growth(transactions, min_support)

print("Frequent Patterns:")
for pattern, count in patterns:
    print(f"{pattern}: {count}")
