import code49 as c49


# Decoder
def decode(code):
  # Buffer & index
  buffer, index = '', 0

  # For each line except last line (Ignore checksum)
  for i, row in enumerate(code[:-1]):
    # Extract pattern, remove head '11' and tail '4'
    ptrn = row[2:-1]

    # For each symbol
    for j in range(4):
      # Get value
      val = None
      if c49.ROW_PARITY[i][j] == '0' or len(code) == i + 1:
        val = c49.EVEN_PARITY_PATTERNS.index(ptrn[j << 3:(j + 1) << 3])
      else:
        val = c49.ODD_PARITY_PATTERNS.index(ptrn[j << 3:(j + 1) << 3])

      # Extract 2 characters from value
      c1, c2 = val // 49, val % 49

      # Append buffer
      try:
        index += 1
        buffer += c49.CHAR_MAP[c1]
      except:
        pass

      try:
        index += 1
        if index % 8 != 0 or index == 0:
          buffer += c49.CHAR_MAP[c2]
      except:
        pass

  # Return buffer
  return buffer


# Main entry
if __name__ == '__main__':
  # Test encoder
  # test.test_cases()

  # Decode
  code = [
    '11143121314115211131114321124131314',
    '11221611211411251111225122311314214',
    '11123232212411212332131231332321114',
    '11251311211242114112215212413213114',
    '11123121511212521211113243422213114',
    '11224211311211313421211153141112154'
  ]
  text = decode(code)
  print(text)
