import code49 as c49


# Test encoder
def test_encoder(text, code):
  # Encode text
  tmp = c49.encode(text)

  # Length match
  assert len(tmp) == len(code), f'length not match: {len(tmp)} != {len(code)}'

  # Row match
  for i, row in enumerate(tmp):
    assert row == code[i], f'row {i + 1} not match: {i} != {code[i]}'

  # Matched
  print('test matched')


# Test cases
def test_cases():
  test_encoder(
    '0',
    [
      '11215211132242113122421131122125214',
      '11224211311115222224211213511311314'
    ]
  )
  test_encoder(
    'TEST',
    [
      '11213413112211411422421131111131624',
      '11224211311213224122321321142123124'
    ]
  )
  test_encoder(
    '-A.5 $/0+W%7',
    [
      '11142121413111321434113211111511424',
      '11511311311221141441211232121124324',
      '11224211311314141122241212111114164'
    ]
  )
  test_encoder(
    'THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG. 123',
    [
      '11113141321114141323122114122421224',
      '11211131431221341214222113212113244',
      '11314211312124112343311121122125124',
      '11511151111141211513222123151121324',
      '11122333112523111111314132123134114',
      '11341221215131221111212324122133224',
      '11233211311223123224212113116131124',
      '11511151111122512211141152311332124'
    ]
  )
