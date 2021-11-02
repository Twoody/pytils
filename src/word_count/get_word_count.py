#!/usr/bin/env python3
from pytils.config import *
from pytils.src.get_abs_path import get_abs_path
import string
import os
def make_dictionary(txt, args=None):
 dic = {}
 with open(txt, 'r') as infile:
  for line in infile:
   words = line.split()
   for word in words:
    word = word.lower()
    word.translate(str.maketrans('', '', string.punctuation))
    if word not in dic:
     dic[word] = 1
    else:
     dic[word] += 1
 # - File closed
 return dic

def get_word_count(txt, args=None):
 '''
   I: A text file;
   O: A Json file of all the words in that text file

   The outputted json file will be our dictionary;
 '''
 show_top  = 20
 msg       = '\n\tTARGET FILE:\t' + txt 
 if not os.path.isfile(txt):
  msg += "\n\tERROR: INVALID ARG: NOT A FILE"
  return msg
 if txt[-4:] != ".txt":
  msg += "\n\tERROR: CAN ONLY READ FROM TEXT FILES"
  return msg
 mac_dic   = make_dictionary(txt)
 dest_path = txt[:-4]+ ".json"
 msg += '\n\tFOUND FILE'
 msg += '\n\tSORTING DIC'
 dSorted = sorted(mac_dic.items(), key=operator.itemgetter(1))
 dSorted.reverse()
 msg += '\n\tDONE SORTING DIC'
 msg += '\n\t\tWORD COUNT:\t' + str(len(mac_dic))
 msg += '\n\t\t'+str(show_top)+' Top Words:'
 for i in range(0, show_top):
  word  = str(dSorted[i][0])
  count = str(dSorted[i][1])
  msg += '\n\t\t\t' + str(i+1) + '.\t'
  msg += '`' + word + '`\tAPPEARS '+count+' TIMES'
 suc = make_json(dSorted, dest_path)
 if suc == False:
  msg += '\n\tBAD RUN; BAILING'
 msg += '\n\tFINISHED\n'
 return msg

def make_json(dic, dest):
 import json
 if type(dic) != dict:
  return False
 # TODO: Validate dest
 with open(dest, 'w') as fp:
  json.dump(dic, fp)
 return True

if __name__ == "__main__":
 #Called directly, should have arguments...
 import operator
 fullCmdArguments = sys.argv
 
 # - further arguments
 argumentList = fullCmdArguments[1:]
 reqs = []
 for arg in argumentList:
  isFlag = re.search(FLAG_RE, arg)
  if isFlag:
   if arg in ("-v", "--verbose"):
    if FLAGS['isQuite'] == False:
     LOGGER.info("\n\tEnabling verbose mode")
    FLAGS['isVerbose'] = True
   elif arg in ("-h", "--help"):
    #TODO: Make a helper function O.o
    LOGGER.info("\n\tFor current help please email at Tanner.L.Woody@gmail.com")
    sys.exit(0)
   elif arg in ("-q", "--quite"):
    FLAGS['isQuite'] = True
    #LOGGER.info("\n\tOutput to stdout disabled;")
   else:
    if FLAGS['isQuite'] == False:
     LOGGER.warning("\n\tArgument not recgonized: %s" %arg)
  else:
   reqs.append(arg)

 # - Function Calls
 if len(reqs) == 0:
  LOGGER.error('\n\t/pytils/src/get_word_count.py: No argment provided')
  sys.exit(0)
 elif len(reqs) == 1:
  msg = get_word_count(reqs[0])
  print(msg)
  LOGGER.info(msg)
 else: 
  msg = '\n\t/pytils/src/get_word_count.py: TOO MANY ARGUMENTS:'
  for arg in reqs:
   msg += '\n\t\tARG:\t%s'%arg
  LOGGER.error(msg)
  sys.exit(0)
