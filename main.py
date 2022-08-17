from xml.dom.minidom import parse
from os import listdir
import utm.conversion

INPUT_DIR = "input/"
OUTPUT_CSV = "output.csv"

def get_point_name(point):
    """
    Gets name of a point as a string.
    :param point: Proper DOM object waypoint (wpt) from a .gpx (1.1) file
    :return: String, with name
    """
    name = point.getElementsByTagName("name")[0].firstChild.nodeValue
    return name

def get_point_UTM(point):
    """
    Gets UTM coordinates from point as a set. Converts from lat/lon to UTM.
    :param point: Proper DOM object waypoint (wpt) from a .gpx (1.1) file
    :return: UTM coordinates
    """
    lat = float(point.getAttribute("lat"))
    lon = float(point.getAttribute("lon"))
    UTM = utm.conversion.from_latlon(lat, lon)
    return UTM

def get_point_ele(point):
    """
    Gets elevation of a point as a string.
    :param point: Proper DOM object waypoint (wpt) from a .gpx (1.1) file
    :return: String, with elevation
    """
    name = point.getElementsByTagName("ele")[0].firstChild.nodeValue
    return name

def returnPointInfo(point):
    """
    Gets details of a point as a string. Only includes easting and northing.
    :param point: Proper DOM object waypoint (wpt) from a .gpx (1.1) file
    :return: String, with name, lat, long, and elevation (comma seperated)
    """
    easting, northing, e, e = get_point_UTM(point)
    text = "%s,%s,%s,%s"%(get_point_name(point), round(easting), round(northing),round(float(get_point_ele(point))))
    return text

def main():
    """
    Main program function. Finds and processes all waypoints and parses them.
    :return: none
    """
    f = open(OUTPUT_CSV, "w")
    f.write("name,easting,northing,elevation\n")
    for gpx in listdir(INPUT_DIR):
        print("Reading %s..."%INPUT_DIR+gpx)
        try:
            doc = parse(INPUT_DIR+gpx)
            points = doc.getElementsByTagName("wpt")
            for i in points:
                print(returnPointInfo(i))
                f.write(returnPointInfo(i)+"\n")
        except:
            print("Error reading %s!"%INPUT_DIR+gpx)

    f.close()
main()
