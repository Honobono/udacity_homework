# write a profanity check program
# compile a list of profanity words
# check every word in the target text against the profanity list

import urllib

def read_text():
    text = open("/Users/ruiyingliu/Downloads/google-python-exercises/basic/small.txt")
    contents_of_file = text.read()
    #print (contents_of_file)
    text.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if 'true' in output:
        print('Profanity Alert!')
    elif 'false' in output:
        print('No curse words found!')
    else:
        print('Could not scan the doc properly')


read_text()
