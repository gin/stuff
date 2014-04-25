#===============================================================================
# Burrows-Wheeler transform
#   by Luigi Leung
#
# Reference: http://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
#===============================================================================

import string

def generate_all_rotations(input_string):
    # Pad to match wikipedia's example. This is because Python sort '^' to
    # beginning of list instead of 2nd-to-last in wiki's example. Input using
    # "banana" instead of wiki's "^banana|"
    string_split = '^' + input_string + '|'
    rotations = [string_split]
    for i in xrange(len(string_split)-1):
        string_split = list(string_split)
        string_split = [string_split.pop()] + string_split    # Last char to front
        rotations += [''.join(string_split)]
    return rotations

def sort_rotations(list_of_rotations):
    sorted_r = sorted(list_of_rotations)
    # Adjust ^'s position (1st position to 2nd-to-last position) to
    # match wikipedia's example
    sorted_r = sorted_r[1:-1] + [sorted_r[0]] + [sorted_r[-1]]
    return sorted_r

def take_last_column(sorted_rotations):
    output_string = ''
    for row in sorted_rotations:
        output_string += row[-1]
    return output_string

def bwt_encode(input_string):
    print "Input:"
    print input_string,"\n"

    step1 = generate_all_rotations(input_string)
    print "Step 1: Generate a list of all rotations"
    for element in step1:
        print element
    print ""                            # Line break to improve cmd out visuals

    step2 = sort_rotations(step1)
    print "Step 2: Sort all rotations in alphabetical order"
    for element in step2:
        print element
    print ""                            # Line break to improve cmd out visuals

    output_tranformed_string = take_last_column(step2)
    print "Output: Burrows-Wheeler transformed string"
    print output_tranformed_string, "\n"
    return output_tranformed_string

def bwt_decode(input_string):
    add_table = []                      # Output will be 1st element in list
    add_element = [[char] for char in list(input_string)]   # Init first column
    add_table += add_element
    sort_table = []
    for count in xrange(len(input_string)-1):
        sort_table = sorted(add_table)
        # Not needed but moving ^'s position to 2nd-to-last position in order to
        # match wikipedia's example
        sort_table = sort_table[1:-1] + [sort_table[0]] + [sort_table[-1]]
        # Take last char of each row
        add_element = [ [row[-1]] for row in sort_table ]
        # Append each char to end of row
        add_table = [ add_table[i]+add_element[i] for i in xrange(len(input_string)) ]
    sort_table = sorted(add_table)
    print "Visualize final add/sort table:"
    for element in sort_table:
        print ''.join(element)
    print ""                            # Line break to improve cmd out visuals
    output = sort_table.pop(0)
    print "First element:"
    print ''.join(output), "\n"
    output = output[1:-1]               # Remove padding ('^' and '|')
    output = ''.join(output)            # Turn list of char to string
    print "Original (pre-Burrows-Wheeler transformed) string:"
    print output, "\n"
    return output


def main():
    input_string = "banana"
    #input_string = "atgagagcctag"
    #===========================================================================
    # Limitations:
    # Input has to be alphanumeric and lower-case only (no symbols)
    #===========================================================================
    # This is because the symbol ^ in ASCII is ranked between capital letters
    # and lower-case letters. The sort() function has to be adjusted in order to
    # remove this input limitations.
    #
    # Another solution is to deviate from wikipedia's intermediary examples by
    # removing the paddings (^ and |) within this code. This does not require
    # programming tricks on the sort() function. The output will be different
    # from wikipedia's example but is equally valid in reducing Kolmogorov
    # complexity to achieve a more efficient string compression.
    #===========================================================================

    # Reduce Kolmogorov complexity for more efficient compression
    print "##################################################"
    print "# Burrows-Wheeler Transform"
    print "##################################################"
    string_for_compression = bwt_encode(input_string)

    # Compress (some external process for storage, etc)
    string_compressed = string_for_compression
    # Decompress
    string_decompressed = string_compressed

    # Recover pre-Burrow-Wheeler-transformed state
    print "##################################################"
    print "# Inverse Burrows-Wheeler Transform"
    print "##################################################"
    original_string = bwt_decode(string_decompressed)


if __name__ == "__main__":
    main()
