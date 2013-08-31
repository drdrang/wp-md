#!/usr/bin/python

import sys
import re

'''Read a Markdown file via standard input and tidy its
reference links. The reference links will be numbered in
the order they appear in the text and placed at the bottom
of the file.'''

# The regex for finding reference links in the text. Don't find
# footnotes by mistake.
link = re.compile(r'\[([^\]]+)\]\[([^^\]]+)\]')

# The regex for finding the label. Again, don't find footnotes
# by mistake.
label = re.compile(r'^\[([^^\]]+)\]:\s+(.+)$', re.MULTILINE)

def refrepl(m):
  'Rewrite reference links with the reordered link numbers.'
  return '[%s][%d]' % (m.group(1), order.index(m.group(2)) + 1)

# Read in the file and find all the links and references.
text = sys.stdin.read()
links = link.findall(text)
labels = dict(label.findall(text))

# Determine the order of the links in the text. If a link is used
# more than once, its order is its first position.
order = []
for i in links:
  if order.count(i[1]) == 0:
    order.append(i[1])

# Make a list of the references in order of appearance.
newlabels = [ '[%d]: %s' % (i + 1, labels[j]) for (i, j) in enumerate(order) ]

# Remove the old references and put the new ones at the end of the text.
text = label.sub('', text).rstrip() + '\n'*3 + '\n'.join(newlabels)

# Rewrite the links with the new reference numbers.
text = link.sub(refrepl, text)

print text
