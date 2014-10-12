import csv
import logging

logging.basicConfig(filename = "output.log", level = logging.DEBUG)

def put(name, snippet, filename):
    """Store a snippet with an associated name in the CSV file"""
    logging.info("Writing {!r}:{!r} to {!r}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f) 
        logging.debug("Writing snippet to file") 
        writer.writerow([name, snippet])
    logging.debug("Write sucessful") 
    return name, snippet