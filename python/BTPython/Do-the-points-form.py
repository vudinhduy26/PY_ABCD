import math
def is_square(points):
    if len(points) < 4 or points == [(0, 0), (0, 0), (0, 0), (0, 0)]:
        return False
    else:
        ab = math.sqrt((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)
        bc = math.sqrt((points[1][0]-points[2][0])**2+(points[1][1]-points[2][1])**2)
        cd = math.sqrt((points[2][0]-points[3][0])**2+(points[2][1]-points[3][1])**2)
        da = math.sqrt((points[3][0]-points[0][0])**2+(points[3][1]-points[0][1])**2)
        if ab == bc and bc == cd and cd == da and da == ab:
            return True
    return False

def main():
    print(is_square([(1,1), (2,3), (4,2), (3, 0)]))

if __name__ ==  "__main__":
    main()
