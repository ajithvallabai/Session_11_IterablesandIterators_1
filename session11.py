import math 

class Polygon:
    """
    A polygon class is formed with a input of edges and circum radius. 
    """
    def __init__(self,num_edges, circum_radius):
        """
        function does necessary calculations and sets interior angle, edge length, apothem, area and perimeter
        :param num_edges: edges of a polygon
        :type num_edges: int
        :param circum_radius: circum radi of polygon
        :type circum_radius: int
        :return func: 
        """
        if not (isinstance(num_edges, int) and isinstance(circum_radius, int)):
            raise TypeError ("Please provde valid input")

        if num_edges < 3:
            raise ValueError("Polygons wont have edges less than 3")

        self.edges = num_edges
        self.circumradius = circum_radius
        
        self.interior_angle = (self.edges - 2)* (180/self.edges)
        self.side_length = 2 * (self.circumradius) * (math.sin(math.pi/self.edges))
        self.apothem = (self.circumradius) * (math.cos(math.pi/self.edges))
        self.area = (0.5 * self.edges * self.side_length * self.apothem)
        self.perimeter = (self.edges * self.side_length)
    @property
    def count_vertices(self):
        return self.edges

    @property
    def count_edges(self):
        return self.edges
        
    def __repr__(self):
        return "Polygon(n=%s, R=%s)" % (self.edges, self.circumradius)
    def __eq__(self, other) -> 'bool':
        """ 
        :param other: A polygon object
        :type other: class
        :return bool: equality 
        """
        if not isinstance(other,Polygon):
            raise TypeError("Object is not Comparable") 
        else:
            return ((self.edges == other.edges) and (self.circumradius == other.circumradius))
    def __gt__(self, other) -> 'bool':
        """ 
        :param other: A polygon object
        :type other: class
        :return bool: equality 
        """
        if not isinstance(other,Polygon):
            raise TypeError("Object is not Comparable") 
        else:
            return (self.edges > other.edges) 

class Polygons:
    """
    Custom polygon class we are taking maximum vertices that a 
    sequence of polygons can have and a common circum radius for it
    """
    def __init__(self,vertices, circum_radius):
        """
        We are setting edges, circum radius and maximum efficeint 
        polygon property
        """
        if not (isinstance(vertices, int) and isinstance(circum_radius, int)):
            raise TypeError ("Please provde valid input")

        self.edges = vertices
        self.circum_radius = circum_radius
        self.vertices = vertices
        self._polygons = [Polygon(i,self.circum_radius) for i in range(3, self.edges+1)]        
        self.max_efficient_polygon = self.get_efficient_polygon()

    def get_efficient_polygon(self) -> 'int':
        """
        Provides number of vertices of efficient polygon. We are 
        iterating from 3 to 10 and we are checking area/perimeter ration 
        for each polygon formed from Polygon() class.
        :return int:
        """
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]

    def __getitem__(self, num) -> 'list':  
        """ 
        :param num: edges of a polygon
        :type num: int        
        :return class: 
        """       
        return self._polygons[num]
    
    def __len__(self) -> 'int':
        """         
        :return length: int 
        """
        return self.vertices
    
    def __repr__(self) -> 'str':
        """         
        :return repr: string 
        """
        return "Polygon Sequence from 3 to max {%s} edges each with {%s} circum radius" % (self.edges, self.circum_radius)
    
    class PolygonIterator:
        def __init__(self, poly_obj) -> None:
            print("Calling PolygonIterator __init__")
            self._poly_obj = poly_obj
            self.index = 0
        
        def __iter__(self):
            print("Calling PolygonIterator instance __iter__")
            return self 
        
        def __next__(self):
            print("Calling PolygonIterator __next__")
            if self._index >= len(self._poly_obj):
                raise StopIteration
            else:
                item = self._poly_obj._polygons[self._index]
                self._index += 1
                return item