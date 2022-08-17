from xml.dom.minidom import parse
doc = parse('/Users/minif/Desktop/test.GPX')#DEBUG/WIP!

def returnPointInfo(point):
    """
    Gets details of a point as a string. This is useful for debugging.
    :param point: Proper DOM object waypoint (wpt) from a .gpx (1.1) file
    :return: String, with name, lat, long, and elevation (comma seperated)
    """
    text = "%s,%s,%s,%s"%(point.getElementsByTagName("name")[0].firstChild.nodeValue,point.getAttribute("lat"),point.getAttribute("lon"),point.getElementsByTagName("ele")[0].firstChild.nodeValue)
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
