def zip2(keys,values):
    res = {}
    it = iter(values)
    nullValue = False
    for key in keys:
        try:          
            if not nullValue:
                res[key] = it.next() 
            else:
                res[key] = None
        except StopIteration:
            nullValue = True
            res[key] = None
    return res

print( zip2([],[]) == {})
print( zip2([1,2,3],[4,5,6]) == {1:4,2:5,3:6} )
print( zip2([1,2],[4,5,6]) == {1:4,2:5} )
print( zip2([1,2,3],[4,5]) == {1:4,2:5,3:None} )