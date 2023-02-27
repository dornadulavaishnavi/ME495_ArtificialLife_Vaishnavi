from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL_SENSOR: 

    def __init__(self):

        self.depth  = 3

        self.string1 = '<material name="Green">'

        self.string2 = '    <color rgba="0.1 0.9 0.1 0.9"/>'

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )