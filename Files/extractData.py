data1 = 'Welcome to the Python Wiki, a user-editable compendium of knowledge\n\
based around the Python programming language. Some pages are protected\n\
against casual editing - see WikiEditingGuidelines for more information\n\
about editing content.'

data2 = 'Python is a great object-oriented, interpreted, and interactive\n\
programming language. It is often compared (favorably of course :-) )\n\
to Lisp, Tcl, Perl, Ruby, C#, Visual Basic, Visual Fox Pro, Scheme or Java...\n\
and it\'s much more fun.'

f1 = open('words1.txt', 'w+')
f2 = open('words2.txt', 'w+')

f1.write(data1)
f2.write(data2)

f1.close()
f2.close()