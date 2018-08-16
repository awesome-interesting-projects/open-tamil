## -*- coding: utf-8 -*-
#(C) 2018 Muthiah Annamalai
# This file is part of Open-Tamil project
# You may use or distribute this file under terms of MIT license

import codecs
import json
import tamil
import sys
#e.g. python morse_encode.py கலைஞர்
def encode(text):
    with codecs.open("tamilmorse.json","r","utf-8") as fp:
        codebook = json.loads(fp.read())
    output = [codebook.get(l,l) for l in tamil.utf8.get_letters(text)]
    print(u" ".join(output))
    return

if __name__ == u"__main__":
    encode(u" ".join([i.decode("utf-8") for i in sys.argv[1:]]))
