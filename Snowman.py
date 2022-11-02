import maya.cmds as cmds
#create body
cmds.polySphere(radius= 3, subdivisionsX =  20, subdivisionsY = 20, axis = (0, 1, 0), createUVs = 2, constructionHistory = 1)
cmds.move(0, 3, 0, os = 1, wd = 1, r = 1)

#create middle

cmds.polySphere(radius= 2, subdivisionsX =  20, subdivisionsY = 20, axis = (0, 1, 0), createUVs = 2, constructionHistory = 1)
cmds.move(0, 7, 0, os = 1, wd = 1, r = 1)


#create head
cmds.polySphere(radius= 1.5, subdivisionsX =  20, subdivisionsY = 20, axis = (0, 1, 0), createUVs = 2, constructionHistory = 1)
cmds.move(0, 10, 0, os = 1, wd = 1, r = 1)

cmds.select('pSphere2')
cmds.duplicate()
cmds.scale(0.15, 0.15, 0.05 )
cmds.move(0, 0, 1.986703, os = 1, wd = 1, r = 1)

cmds.duplicate()
cmds.move(0, 0.968112, -0.190773, os = 1, wd = 1, r = 1)
cmds.rotate(-25.253729, 0, 0, ws=1,fo = 1, r = 1)

cmds.select('pSphere4')
cmds.duplicate()
cmds.move(0, -0.968112, -0.190773, os = 1, wd = 1, r = 1)
cmds.rotate(25.253729, 0, 0, ws=1,fo = 1, r = 1)


cmds.polyCone(r = .5, h = 2, sx = 20, sy = 1, sz = 0, ax = (0, 1, 0), rcp = 0,  cuv = 3, ch = 1)
cmds.move(0, 10.078562, 1.485208, r = 1)
cmds.rotate(90, 0, 0, ws=1,fo = 1, r = 1)

cmds.polySphere(r = 1, sx = 20, sy = 20, ax = (0, 1, 0), cuv = 2, ch = 1)
cmds.move(0, 10.400869, 1.443712, r = 1)
cmds.scale(0.276272, 0.276272, 0.276272, r = 1)
cmds.scale(1, 1, 0.571302, r = 1)
cmds.scale(1, 1, 0.779429, r = 1)
cmds.move(-0.663711, 0, -0.199922, r = 1)
cmds.rotate(0, -14.4, 0, ws=1,fo = 1, r = 1)
cmds.rotate(-11.70408, 0, 0, ws=1,fo = 1, r = 1)

cmds.select('pSphere7')
cmds.duplicate()
cmds.move(1.38934, 0, 0, r = 1)
cmds.rotate(0, 44.42328, -26.165099, ws=1,fo = 1, r = 1)

cmds.polyCylinder(r = 0.2, h= 4, sx= 20, sy= 6, sz= 1, ax= (0, 1, 0), rcp= 0, cuv= 3, ch= 1)
cmds.move(2.490934, 7.276071, 0, r = 1)
cmds.rotate(0, 0, 55.983054, ws=1,fo = 1, r = 1)
cmds.move(0, -0.509873, 0, r = 1)


cmds.duplicate()
cmds.move(-5.327878, 1.743385, 0.878103, r=1)
cmds.rotate( 0, 19.553475, 21.997601, ws=1,fo = 1, r = 1)

cmds.polyCylinder(r = 1, h= 2, sx= 20, sy= 1, sz= 1, ax= (0, 1, 0), rcp= 0, cuv= 3, ch= 1)
cmds.move(-0.789613, 12.622588, 0, r = 1)
cmds.rotate(0, 0, 16.788201, ws=1,fo = 1, r = 1)

cmds.duplicate()
cmds.scale(1, 0.1507, 1, r = 1)
cmds.scale(1.47328, 1, 1.47328, r = 1)
cmds.move(0, -1.061886, 0, os = 1, wd = 1, r = 1)







