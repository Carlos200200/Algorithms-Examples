#####################
## Strip Comments
## Codewars 4 Kyu
#####################


# Strip a text with the markers
# Space at the end of the line has to delete

def strip_comments(strng, markers):
    Lines = strng.split("\n")
    Str = ""
    for L in Lines:
        for m in markers:
            L = L.split(m)[0]
        Str += L
        while len(Str) != 0:
            if Str[-1] == " " or Str[-1] == "\t":
                Str = Str[:-1]
            else:
                break
        Str += "\n"
    return Str[:-1] if len(Str) != 0 else Str


#test.assert_equals(solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas#
#test.assert_equals(solution('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
#test.assert_equals(solution(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')
