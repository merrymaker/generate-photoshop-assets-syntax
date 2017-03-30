import struct
import imghdr

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return {'width': width, 'height': height}

# @note breakpoints are shifted to take on the next breakpoint value
breakpoints = {
    # @1x
    'sm': 768,
    'md': 992,
    'lg': 1200,
    'xl': 1800,
    # @2x
    'sm@2x': 768 * 2,
    'md@2x': 992 * 2,
    'lg@2x': 1200 * 2,
    'xl@2x': 1800 * 2,
}

print("==== Drag and drop image here and hit ENTER to continue ====")
filePath = input().strip()
fileNameAndExtension = filePath.rsplit('/', 1)[-1]
fileInfo = fileNameAndExtension.split('.')
fileName = fileInfo[0]
fileExtension = '.' + fileInfo[-1]

imgData = get_image_size(fileName + fileExtension)
imgData['aspectRatio'] = imgData['width'] / imgData['height']

def processPhotoshopAssetGeneratorSyntax():
    resultList = [];
    for breakpoint, width in breakpoints.items():
        width = float(width)
        height = width/imgData['aspectRatio']
        aspectRatioFriendlyDimensions = '{width}x{height}'.format(width=int(width), height=int(height))
        breakpoints[breakpoint] = aspectRatioFriendlyDimensions
        resultList.append(aspectRatioFriendlyDimensions + ' ' + fileName + '_' + breakpoint + fileExtension)
    return ', '.join(resultList)

result = processPhotoshopAssetGeneratorSyntax()

# Faqs
print("\n")
print('## FAQs')
print("\n")
print('Q: Why can\'t i paste the output into the photoshop layer?')
print('There is a 255 character limit in the layer name. To fix this, use a shorter file name and try again.')
print("\n")
print('Q: TypeError: \'NoneType\' object is not subscriptable')
print('This image cannot be used. Render it again. Use \'Save As\' on Photoshop instead of \'Export/Save as Web\' as certain metadata could have been lost during the export phase.')
print("\n")
print('Q: I pasted the output into the layer name but nothing is happening')
print('Check your desktop for the generated folder. Also ensure that the \'Photoshop > File > Generate > Image Assets\' option is checked.')
print("\n")
print('Q: FileNotFoundError: [Errno 2] No such file or directory: \'foo.jpg\' ')
print('Please ensure that the image is in the same directory as this script.')

# Result
print("\n")
print('======== Copy and paste the following text into your photoshop asset\'s layer ========')
print("\n")
print(result)
print("\n")
print('======== Copy and paste the above text into your photoshop asset\'s layer ========')
print("\n")
