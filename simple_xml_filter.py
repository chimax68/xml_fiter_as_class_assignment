import sys

def filter_xml (infile, outfile):
    import re
    out_string = ''
    with open(infile) as instream:
        instring = instream.read()
        xml_pattern = re.compile('<[^>],</style>.*</style>,*>')
        out_string = xml_pattern.sub('',instring)
        out_string2 = out_string.replace('&amp', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&gt;', '\'')
        
    with open(outfile,'w') as outstream:
        outstream.write(out_string2)

def main(args):
    infile = args[1]
    split_point = infile.rindex('.')
    outfile = infile[:split_point]+'.txt'
    filter_xml(infile,outfile)

sys.exit(main(sys.argv))
