### Session 11 - Iterables and Iterators - I

Google Colab - [here](https://colab.research.google.com/drive/1hEFlhwuSk2q4kCKAXqZdj83YMD3H3aEX?usp=sharing)

#### Iterator

iterator is a object that helps to iterate over iterable objects like list, tuples. it uses __iter__ for initalization and uses next() method for iteration

```
        def __iter__(self):
            print("Calling PolygonIterator instance __iter__")
            return self 
```

it is used when below function is done 
```
polygons = Polygons(6, 10)
iter_poly = iter(polygons)
```

#### next()

```
        def __next__(self):
            print("Calling PolygonIterator __next__")
            if self._index >= len(self._poly_obj):
                raise StopIteration
            else:
                item = self._poly_obj._polygons[self._index]
                self._index += 1
                return item

```
next() is used to fetch the next item(iterable) in a iterator. When it has fetched all the objects it raises a exception StopIteration. once all the items are exhausted , exception is raised and it denotes end of iterator.

#### getitem()

```
        def __getitem__(self, num) -> 'list':  
            """ 
            :param num: edges of a polygon
            :type num: int        
            :return class: 
            """       
            return self._polygons[num]
```

getitem() is used to fetch a particular item in a list and also it helps while forming a new list

#### Iterable

Even when we iterate over a object again and again with for loop it should not get exhausted i.e there should be no need for re-initalization

```
    polygons = Polygons(4, 10)
    polygons_list = []
    for poly in polygons:
        polygons_list.append(poly)
        print(poly)
    for poly in polygons:
        polygons_list.append(poly)
        print(poly)
```

#### list()

Even when we call the object with list(obj) it should apt number of outputs

```
polygons = Polygons(10, 10)
assert len(list(polygons)) == 8
```


