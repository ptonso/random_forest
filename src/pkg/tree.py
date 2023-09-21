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



# ________________



def unique_vals(rows, col):
    '''
    find the unique values for a column in a dataset.
    '''
    return set([row[col] for row in rows])

def class_counts(rows):
    '''
    counts the number of each type of example in a dataset.
    '''
    counts = {} # a dictionary of label -> count.
    for row in rows: # label inside last columns
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)

class Question:
    '''
    Dataset partitioning
    '''
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        '''
        method to print the question
        '''
        if is_numeric(self,value):
            condition = ">="
        return "Is %s %s %s ?" % (header[self.column],condition,str(self.value))

def partition(rows, question):
    '''
    partition dataset    
    '''
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def info_gain(left, right, current_uncertainty):
    p = float(len(left) / len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def find_best_split(rows):

    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0])

    for col in range(n_features):
        values = set([row[col] for row in rows])

        for val in values:
            question = Question(col, val)
            true_rows, false_rows = partition(rows, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question
    
    return best_gain, best_question

class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)

class Decision_Node:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(rows):
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)

    true_branch = build_tree(true_rows)

    false_branch = build_tree(false_rows)

    return Decision_Node(question, true_branch, false_branch)


def print_tree(node, spacing=""):

    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return
    
def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions
    
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs



if __name__ == '__main__':

    training_data = [
        ['Green', 3, 'Apple'],
        ['Yellow', 3, 'Apple'],
        ['Red', 1, 'Grape'],
        ['Red', 1, 'Grape'],
        ['Yellow', 3, 'Lemon'],
        ]

    header = ["color", "diameter", "label"]

    testing_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
    ]

    my_tree = build_tree(training_data)

    for row in testing_data:
        print("Actual: %s. Predicted: %s" % (row[-1], print_leaf(classify(row, my_tree))))