from OpenGL.GL import *
from array import *
#import Image
from PIL import Image

class Texture:
    numTextures = 1

    def __init__(self, *args):
        self.texID = Texture.numTextures
        Texture.numTextures += 1
        if (type(args[0]) is str):
           self.loadFile(args[0])
        elif (type(args[0]) is tuple) and (type(args[1]) is list):
           self.loadList(args[0], args[1])

    def loadFile(self, filename):
        im = Image.open(filename)
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
        self.filename = filename
        self.width, self.height = im.size
        self.channels = len(im.getbands())
        #self.data = im.tostring()
        self.data = im.tobytes()		
        self.initTexture()

    def loadList(self, size, data):
        self.filename = 'None'
        self.width, self.height, self.channels = size
        self.data = array('B',data).tostring()
        self.initTexture()

    def initTexture(self):
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        if (self.channels == 3):
            glTexImage2D(GL_TEXTURE_2D, 0, 3, self.width, self.height, 0, GL_RGB, GL_UNSIGNED_BYTE, self.data)
        else:
            glTexImage2D(GL_TEXTURE_2D, 0, 4, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.data)
