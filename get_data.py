white_notes = [char for char in 'abcdefgABCDEFG']
sharps = [note+'#' for note in white_notes]
flats = [note+'b' for note in white_notes]
all_notes = white_notes + sharps + flats
print(all_notes)
