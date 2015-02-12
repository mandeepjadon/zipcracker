import zipfile
from threading import Thread
from optparse import OptionParser
def crackfile(zipfile,password):
    try:
        zipfile.extractall(pwd=password)
        print "password found !! "
        return password
    except (KeyboardInterrupt , SystemExit):
        raise
    except:
        return
def main():
    parser= OptionParser("Specify -f <zipname> -d <wordlist> or --help for help")
    parser.add_option("-f","--file",dest="zipname",help="specify the zipfile name 

with proper path")
    parser.add_option("-w","--wordlist",dest="wordlist",help="specify the wordlist 

with proper path")
    (options, args)= parser.parse_args ()
    if (options.zipname== None) | (options.wordlist== None):
        print parser.usage
    else:
        zipname= options.zipname
        wordlist= options.wordlist
        zname = zipfile.ZipFile(zipname)
        pfile= open(wordlist)
        for lines in pfile.readlines():
            password=lines.strip("\n")
            res= crackfile(zname,password)
            if res:
                print password
                return
            else:
                pass
        else:
            print "not found"
            pfile.close()
if __name__=='__main__':
    main()
    
    
    
