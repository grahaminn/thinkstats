bag1994 = 0.5
bag1996 = 0.5

ebag1994 = 0.2 * 0.1
ebag1996 = 0.2 * 0.14

bag1994e = (bag1994 * ebag1994) / ((ebag1994 * bag1994) + (ebag1996 * bag1996))

print 'probability we have a 1994 bag when we draw a yellow and a green at random', bag1994e
