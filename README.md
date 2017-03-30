# generate-photoshop-assets-syntax
Generate assets layer syntax for Photoshop CC 2014 and above to render different image dimensions while maintaining aspect ratio

#### Pre-requisites

1. Python 3+
2. Adobe Photoshop CC 2014 and above
3. Supported extensions: .jpg

#### Assumptions

- MacOS Sierra 10.x environment
- Other environments have not been tested

#### Usage

1. Place image in same directory as the main script file (`generate-psd-assets.py`).
2. Open terminal, `cd` to the aforementioned directory and run `python generate-psd-assets.py`.
3. Drag and drop the image into the terminal window and hit `enter`.
4. If successful, output will be presented in the terminal window.
5. Open Photoshop and with the image loaded.
6. Go to `Photoshop > File > Generate > Image Assets` and ensure that it is checked.
7. Copy the output from the terminal window and paste it into the layer name in Photoshop.
8. A folder with the generated assets will be created in the aforementioned directory. Done!

#### FAQs

**Q: Why can't i paste the output into the photoshop layer?**
There is a 255 character limit in the layer name. To fix this, use a shorter file name and try again.

**Q: TypeError: 'NoneType' object is not subscriptable'**
This image cannot be used. Render it again. Use 'Save As' on Photoshop instead of 'Export > Save as Web' as certain metadata could have been lost during the export phase.

**Q: I pasted the output into the layer name but nothing is happening**
Check your desktop for the generated folder. Also ensure that the 'Photoshop > File > Generate > Image Assets' option is checked.

**Q: FileNotFoundError: [Errno 2] No such file or directory: 'foo.jpg'**
Please ensure that the image is in the same directory as this script.

#### Resources
[Adobe tutorial on generating assets layers](https://helpx.adobe.com/photoshop/using/generate-assets-layers.html)
