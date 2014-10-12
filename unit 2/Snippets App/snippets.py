import csv
import logging
import argparse
import parser
import sys

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
    
def get(name, filename):
    """Retrieve a snippet with an associated name in the CSV file"""
    logging.info("Reading {!r} from {!r}".format(name, filename))
    logging.debug("Opening file")
    with open(filename, "rb") as f:
        reader = csv.reader(f,delimiter=',') 
        logging.debug("Reading snippet to file") 
        for item in reader:
            if item[0] == name:
                logging.debug("Read sucessful") 
                return item[1]
        else:
            return "Snippet not found"
    
def make_parser():
    """ Construct the command line parser """ 
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text" 
    parser = argparse.ArgumentParser(description=description)
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet") 
    put_parser.add_argument("name", help="The name of the snippet") 
    put_parser.add_argument("snippet", help="The snippet text") 
    put_parser.add_argument("filename", default="snippets.csv", nargs="?",
help="The snippet filename")

    # Subparser for the put command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet") 
    get_parser.add_argument("name", help="The name of the snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?",
help="The snippet filename")
    
    return parser
    
def main():
    """ Main function """ 
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    
    # Convert parsed arguments from Namespace to dictionary arguments = vars(arguments)
    arguments = vars(arguments)
    command = arguments.pop("command")
   
    if command == "put":
        name, snippet = put(**arguments)
        print "Stored {!r} as {!r}".format(snippet, name)
    elif command == "get":
        name = get(**arguments)
        if name == "Snippet not found":
            print "Snippet not found"
        else:
            print "Retrieved Snippet {!r}".format(name)

if __name__ == "__main__": main()