#!/usr/bin/python

"""
Virtual FTP User adding/deleting script for BerkeleyDB and vsftpd
KOksay <koray.oksay@gmail.com>

HISTORY
-------
  Version 0.1: Initial Release, 20140203
"""


import bsddb
import optparse
import sys


def parse_args():
    """ Parses config parameters """
    parser = optparse.OptionParser(usage='%prog (-a <USERNAME> -p <PASSWORD> || -d <USERNAME> || -s (True|False) ) -f <VIRTUALDB_FILE>', 
                                   version='%prog version 0.1\nKoray Oksay 20140203')
    parser.add_option("-a", "--add",  dest="username", default=None, help="Username to add")
    parser.add_option("-d", "--delete",  dest="del_user", default=None, help="Username to delete")
    parser.add_option("-p", "--password", dest="password", default=None, help="User Password")
    parser.add_option("-s", "--showdb", dest="showdb", default=False, help="Show Virtual User Database Content")
    parser.add_option("-f", "--file",  dest="bsddb_file", default="/etc/vsftpd/vsftpd-virtual-user.db", 
                      help="Virtual User Database. Default is /etc/vsftpd/vsftpd-virtual-user.db")
    (options, args) = parser.parse_args(sys.argv)
    return options


def add_user(username, password, filename):
    """Add a new user or update an existing user"""
    action = "added"
    try:
        db = bsddb.hashopen(filename, 'c')
        if username in db:
            action = "updated"
        db[username] = password
        db.close()
        print username + " was " + action + " successfully..."
    except: 
        print "Cannot add or update database... " 


def delete_user(username, filename):
    """Delete existing user"""
    try:
        db = bsddb.hashopen(filename, 'c')
        if username in db:
            db.pop(username)
            db.close()
            print "Username " + username + " was deleted successfully..."
        else:
            print "No such user " + username
    except:
        print "Cannot delete from database..."


def show_database(filename):
    """ Show database contents. (Usernames and passwords) """
    try:
        db = bsddb.hashopen(filename, 'r')
    except:
        print "Cannot open database"
        return

    for k, v in db.items():
        print k + " : " + v


def main():
    """ main function """
    options = parse_args()
    filename = options.bsddb_file
    username = options.username
    del_user = options.del_user
    password = options.password
    showdb = options.showdb

    if username and del_user:
        print "You cannot add and delete user at the same time!..."
        exit(1)
    elif not username and not del_user and not showdb:
        print "You must add or delete user or show db contents"
        exit(2)
    
    if username:
        add_user(username, password, filename)
    elif del_user:
        delete_user(del_user, filename)
    elif showdb:
        show_database(filename)


if __name__ == '__main__':
    main()

