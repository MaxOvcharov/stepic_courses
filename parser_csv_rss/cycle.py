class DictAttr(dict):
     def __getattr__(self, name):
            try:
                return self[name]
            except KeyError:
                raise AttributeError
                
                
x = DictAttr([('one', 1), ('two', 2), ('three', 3)])

print x
print x['three']
print x.get('one')
print x.get('five', 'missing')
print x.one
print x.five
