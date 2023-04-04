import numpy as np

'''
To determine if an infinite line passes through a triangular pyramid, we can check if the line intersects any of the four triangular faces of the pyramid. 

The triangular faces can be represented by the following combinations of vertices: (A, B, C), (A, B, D), (A, C, D), and (B, C, D).

For each face of the pyramid represented by the triangle (X, Y, Z):
 > We determine the intersection between the line and the plane (X, Y, Z)
        >> If the infinite line is parallel to the plane (X, Y, Z), then the infinite line does not passes 
          through a triangular pyramid
        >> But If the infinite line intersects with the plane (X, Y, Z) at point P:
            >>> We determine if the point P relies inside the triangle (X, Y, Z):
                >>>> We calculate the barycentrics coordinate (alpha, beta, gamma) of P with respect to the triangle (X, Y, Z)
                >>>> If the barycentrics coordinate (alpha, beta, gamma) are all non negative, then P relies in the triangle (X, Y, Z)
                >>>> If one of the barycentrics coordinate (alpha, beta, gamma) are negative, then P relies outside of the triangle (X, Y, Z)
         
            >>> If P relies inside the triangle (X, Y, Z), then the infinite line does passes 
          through a triangular pyramid
        
            >>> If P does not relies insiden the triangle (X, Y, Z), we try the next face of the pyramid
            
            >>> If for all faces of the pyramid, the intersection is not inside the triangle, then the infinite line does not pass
            through the pyramid
'''

def point_on_triangle(P, A, B, C):
    '''
      Determine if a 3D point P lies inside a triangle defined by points A, B, and C
      INPUTS:
          P: 3D point to analyze
          A, B, C: 3D Points defining the triangle
      
      OUTPUTS:
          TRUE: The 3D point P lies inside a triangle defined by points A, B, and C
          FALSE: No
          
      METHODOLOGY:
      1. We calculate the barycentric coordinates (alpha, beta, gamma) of point P with respect to the triangle (A, B, C)
      
      2. If all the barycentric coordinates are non-negative, then the point P lies inside the triangle
    '''
    AC = C - A
    AB = B - A
    AP = P - A

    dot00 = np.dot(AC, AC)
    dot01 = np.dot(AC, AB)
    dot02 = np.dot(AC, AP)
    dot11 = np.dot(AB, AB)
    dot12 = np.dot(AB, AP)
    
    # Barycentric coordinates 
    # nnormalize the areas of the sub-triangles by dividing each area by the area of the main triangle 

    inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
    alpha = (dot11 * dot02 - dot01 * dot12) * inv_denom
    beta = (dot00 * dot12 - dot01 * dot02) * inv_denom
    gamma = 1 - alpha - beta

    return (alpha >= 0) and (beta >= 0) and (gamma >=0)

def line_triangle_intersection(L, LDir, A, B, C):

    '''
      Determines if a line represented by (L, LDir) crosses a triangle (A, B, c)
      INPUTS:
          L: 3D point belonging to the line
          LDir: Direction of the line
          A, B, C: 3D Points defining the triangle
      
      OUTPUTS:
          TRUE: The line crosses the triangle (A, B, C)
          FALSE: Otherwise
    '''
    normal = np.cross(B - A, C - A)
    dot = np.dot(normal, LDir)
    
    # The line is parallel to the plane (A, B, C), therefore there is no intersection with the plane (A, B, C)
    if abs(dot) < 1e-8:
        return False

    t = np.dot(normal, A - L) / dot
    intersection = L + LDir * t

    return point_on_triangle(intersection, A, B, C)

def line_pyramid_intersection(L, LDir, A, B, C, D):

    '''
      We iterate over the faces of the pyramid
      For each face we determine if the line intersect inside the face, then we return True
    '''
    
    return (
        line_triangle_intersection(L, LDir, A, B, C) or
        line_triangle_intersection(L, LDir, A, B, D) or
        line_triangle_intersection(L, LDir, A, C, D) or
        line_triangle_intersection(L, LDir, B, C, D)
    )

# Example usage
L = np.array([0.5, 0.5, -1])
LDir = np.array([0, 0, 1])

A = np.array([0, 0, 0])
B = np.array([1, 0, 0])
C = np.array([0, 1, 0])
D = np.array([0, 0, 1])

print(line_pyramid_intersection(L, LDir, A, B, C, D))
