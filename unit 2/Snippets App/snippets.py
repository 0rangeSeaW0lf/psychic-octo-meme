import csv
import logging
import argparse
import parser
import sys
from cStringIO import StringIO

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
    
def read(command, name, filename):
    """Read rows in the CSV file and execute an operation based on given command"""
    logging.info("Reading {!r} from {!r}".format(name, filename))
    logging.debug("Opening file")
    with open(filename, "rb") as f:
        reader = csv.reader(f,delimiter = ',')
        logging.debug("Reading snippet to file")
        logging.debug(reader)
        if command == "get":
            return get(reader,name)
        elif command == "search":
            return search(reader, name)
        elif command == "modify":
            return modify(name, reader, filename)

def get(reader,name):
    """Retrieve a snippet with an associated name in the CSV file"""
    for item in reader:
        if item[0] == name:
            logging.debug("Read sucessful")
            return item[1]
    else:
        logging.debug("Reading final finished")
        return "Snippet not found"
        
def search(reader, string):
    snippet = []
    for item in reader:
        if string in item[1]:
            logging.debug("Read sucessful")
            snippet.append ("\n".join([item[0],item[1]]))
    
    logging.debug("Reading final finished")        
    
    if not snippet:
        return "String not found"
    else:
        return "\n\n".join(snippet)

def modify(names, reader, filename):
    values = []
    # logging.info("Reading {!r} from {!r}".format(name, filename))
    # logging.debug("Opening file")
    # with open(filename, "rb") as f:
    #     reader = csv.reader(f,delimiter = ',')
    #     logging.debug("Reading snippet to file")
    i = 0
    for item in reader:
        if item[0] == names:
            i += 1
            continue
        else:
            values.append([item[0],item[1]])
    
    if i > 0:
        values.append([names,raw_input("Please, type new snippet: ")])
        values.sort()
        with open(filename, "wb+") as f:
            writer = csv.writer(f)
            for value in values:
               writer.writerow(value)
        return "{}".format(names)
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

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?",
help="The snippet filename")

    # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search", help="Search a word in a snippet")
    search_parser.add_argument("name", help="The snippet text")
    search_parser.add_argument("filename", default="snippets.csv", nargs="?",
help="The snippet filename")

    # Subparser for the modify command
    logging.debug("Constructing modify subparser")
    modify_parser = subparsers.add_parser("modify", help="Modify a snippet")
    modify_parser.add_argument("name", help="The name of the snippet")
    modify_parser.add_argument("filename", default="snippets.csv", nargs="?",
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
        name = read(command, **arguments)
        if name == "Snippet not found":
            print "Snippet not found"
        else:
            print "Retrieved Snippet {!r}".format(name)
    elif command == "search":
        snippet = read(command, **arguments)
        if snippet == "Snippet not found":
            print "Snippet not found"
        else:
            print "Snippet Found!\n==============\n\n{}".format(snippet)
    elif command == "modify":
        name = read(command, **arguments)
        if name == "Snippet not found":
            print "Snippet not found"
        else:
            print "Modified Snippet {!r}".format(name)

if __name__ == "__main__": main()