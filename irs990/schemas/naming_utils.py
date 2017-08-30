import re

LINE_REGEX = re.compile(r'(line.+)')
COLUMN_REGEX = re.compile(r'(column.+)')

""" Form part text massage """

def fix_name(raw_name):
    # given a variable name, shorten it to no longer than 62 characters. 
    original = raw_name
    raw_name = raw_name.replace("IRS990", "")
    raw_name = raw_name.replace("Schedule", "Sked")
    raw_name = raw_name.replace("Type", "")
    raw_name = raw_name.replace("Grp", "")
    raw_name = raw_name.replace("Miscellaneous", "Misc")
    raw_name = raw_name.lstrip('_')
    raw_name =  re.sub("[aeiou]+", "", raw_name)
    raw_name = raw_name[:62]
    print("fix name '%s'=>'%s'" % (original, raw_name))
    return raw_name

def munge_line_number(line_number):
    line_number = line_number.replace(',', '')
    line_number = line_number.replace('-', '')
    line_number = line_number.replace(' ', '_')
    line_number = line_number.strip('_')
    line_number = line_number.replace("__", "_")
    line_number = line_number.replace(")", "")
    line_number = line_number.replace("(", "")
    return line_number

def fix_line_number(raw_line_number):
    raw_line_number = raw_line_number.lower()
    line_found = re.search(LINE_REGEX, raw_line_number)

    if line_found:
        line_number  = munge_line_number(line_found.group(1))
        return line_number

    line_found = re.search(COLUMN_REGEX, raw_line_number)
    if line_found:
        line_number  = munge_line_number(line_found.group(1))
        return line_number

    line_number  = munge_line_number(raw_line_number)
    return "line_" + line_number



def fix_part_name(raw_name):
    # given a part name, shorten it to no longer than 30 characters. 
    raw_name = raw_name.lower()

    raw_name = raw_name.replace(",","")
    raw_name = raw_name.replace("/","")
    raw_name = raw_name.replace("-","")

    raw_name = raw_name.replace(" of "," ")
    raw_name = raw_name.replace(" and "," ")
    raw_name = raw_name.replace(" or "," ")

    raw_name = raw_name.replace("irs990", "")
    raw_name = raw_name.replace("schedule", "sked")
    raw_name = raw_name.replace(" ", "_")
    raw_name = raw_name.replace("__", "_")
    raw_name = raw_name.lstrip('_')

    # remove lower case vowels
    # hard truncate
    raw_name = raw_name[:30]
    #print "%s => %s" % (original, raw_name)
    return raw_name

# Work around, easier than making sense of roman numerals
# Needs custom letters for sections (i.e. V-A) 
# for part 5 section A
ordinal_hash = {
    '0':0,
    'I':10,
    'II':20,
    'II-A':21,
    'II-B':21,
    'III':30,
    'III-A':31,
    'III-B':32,
    'IV':40,
    'V':50,
    'V-A':51,
    'V-B':52,
    'V-C':53,
    'V-D':54,
    'VI':60,
    'VII':70,
    'VII-A':71,
    'VII-B':72,
    'VIII':80, 
    'IX':90, 
    'IX-A':91, 
    'IX-B':92, 
    'X':100,
    'XI':110, 
    'XII':120,
    'XIII':130,
    'XIV':140,
    'XV':150,
    'XVI':160,
    'XVI-A':162,
    'XVI-B':162,
    'XVII':170
}
