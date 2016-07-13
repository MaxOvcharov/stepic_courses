import pdb


pdb.set_trace()
string = raw.input()
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)
## Tansverse the NodeTress in every possible way to get codings
def huffmanCodeTree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (r, l) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + "0"))
    d.update(huffmanCodeTree(r, False, binString + "1"))
    return d

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

#Sort the frequency table based on occurrence this will also convert the
#dict to a list of tuples
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq
while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    # Re-sort the list
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

if len(freq)== 1:
    list(freq[0])
    huffmanCode = {str(freq[0][0]): "0"}
else:
    huffmanCode = huffmanCodeTree(nodes[0][0])

a = ''
for i in list(string):
    for key, value in huffmanCode.items():
        if i == key:
            a += value

print (str(len(huffmanCode)) + " " + str(len(a)))
    
for char, s in freq:
    print (str(char) + " " + str(huffmanCode[char]))

print (a)
