from xml.dom.minidom import parse
import utm
doc = parse('/Users/minif/Desktop/test.GPX')#DEBUG/WIP!

def get_point_name(point):
    name = point.getElementsByTagName("name")[0].firstChild.nodeValue
    return name

def get_point_UTM(point):
    lat = point.getAttribute("lat")
    lon = point.getAttribute("lon")
    UTM = utm.from_latlon(lat, lon)
    return UTM

def get_point_ele(point):
    name = point.getElementsByTagName("ele")[0].firstChild.nodeValue
    return name

def returnPointInfo(point):
    """
    Gets details of a point as a string. This is useful for debugging.
    :param point: Proper DOM object waypoint (wpt) from a .gpx (1.1) file
    :return: String, with name, lat, long, and elevation (comma seperated)
    """
    text = "%s,%s,%s"%(get_point_name(point),get_point_UTM(point),get_point_ele(point))
    return text

def main():
    """
    Main program function. Finds and processes all waypoints and parses them.
    :return: none
    """
    points = doc.getElementsByTagName("wpt")
    for i in points:
        print(returnPointInfo(i))
main()
