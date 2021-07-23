import math 
from session11 import Polygon,Polygons
import pytest
import os

README_CONTENT_CHECK_FOR = [
    "iterable",
    "iterator",
    "polygons",
    "StopIteration",
    "for",
    "list"    
]

# Test case (given)

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.side_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.side_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

## 5 test cases for iterator and iterable functionality

def test_iterator():
    polygons = Polygons(6, 10)
    iter_poly = iter(polygons)
    assert str(next(iter_poly)) == "Polygon(n=3, R=10)", "Please check yout implementation"
    assert str(next(iter_poly)) == "Polygon(n=4, R=10)", "Please check yout implementation"
    assert str(next(iter_poly)) == "Polygon(n=5, R=10)", "Please check yout implementation"
    assert str(next(iter_poly)) == "Polygon(n=6, R=10)", "Please check yout implementation"
    with pytest.raises(StopIteration):
        next(iter_poly)
    print("Polygons Class has implemented iterator functionality")

def test_iteratorfunc():
    polygons = Polygons(6, 10)    
    assert hasattr(polygons.PolygonIterator, '__iter__'), "Please check yout implementation"
    assert hasattr(polygons.PolygonIterator, '__next__'), "Please check yout implementation"
    assert callable(polygons.PolygonIterator.__iter__), "Please check yout implementation"    
    assert hasattr(polygons,'__getitem__'), "Please check yout implementation"
    assert callable(polygons.__getitem__), "Please check yout implementation"
    print("polygon object has all required attributes and functionality")


def test_iterables_exhaust():
    polygons = Polygons(4, 10)
    polygons_list = []
    for poly in polygons:
        polygons_list.append(poly)
        print(poly)
    for poly in polygons:
        polygons_list.append(poly)
        print(poly)
    assert len(polygons_list) > len(list(polygons)), "Please check yout implementation"
    assert len(polygons_list) == 4, "Please check yout implementation"
    print("For loop was done over polygon twice and it didnt get exhaust")
    

def test_listable():
    polygons = Polygons(10, 10)
    assert len(list(polygons)) == 8, "Please check yout implementation"
    assert str(polygons[1]) == "Polygon(n=4, R=10)", "Please check yout implementation"
    assert str(polygons[2]) == "Polygon(n=5, R=10)", "Please check yout implementation"
    print("Giving apt output when called as list(polygons)")    

def test_iterable():
    polygons = Polygons(5, 10)
    iter_poly = iter(polygons)
    assert "iterator" in str(iter_poly), "Please check yout implementation"
    assert iter_poly.__next__(), "Please check yout implementation"
    print("Iterable functionality is working fine, next() is implemented")

## Readme file - 2 test case

def test_readmeexists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    print("Readme file exists")

def test_readmeproperdescription():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
    print("Readme file contains proper description")
