class PathNotFoundException(Exception):
    ## DO NOT MODIFY ANYTHING IN THIS CLASS
    def __init__(self):
        super().__init__("A path does not exist between the specified start and end points")