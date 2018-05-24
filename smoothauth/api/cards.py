def binToInt(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal


# Convert output into integers
def decodeCard(raw_card_read):
    proxHex = '0x'
    for h in (reversed(raw_card_read)):
        # JRK - added if statement to handle 1-digit numbers without leading 0
        if (h < 16 and h > 0):
            proxHex += '0' + hex(h)[2:]
        else:
            proxHex += hex(h)[2:]
    # Get 24-digit binary (slice the first 2 and last 1 digit from the binary)
    return proxHex


def processBadgeHex(proxHex):
    b = (bin(int(proxHex, 16))[4:-1])
    '''
    Get Facility Access Code by slicing the first 8 binary digits and
    converting to integer. Then get the Card ID Number by converting the
    last 16 digits to integer
    '''
    fac = binToInt(b[:7])
    idNum = binToInt(b[-16:])
    return(fac, idNum)
