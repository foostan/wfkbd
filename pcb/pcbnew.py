# execfile '/tmp/pcbnew.py'
import pcbnew

OFFSET_X = float(50)
OFFSET_Y = float(50)
PITCH = float(19)

def set_position(ref, xp, yp, orientation = 0):
  module = pcb.FindModuleByReference(ref)
  module.SetPosition(pcbnew.wxPointMM(xp + OFFSET_X, yp + OFFSET_Y))
  module.SetOrientation( orientation * 10.0 )

def set_matrix_position(ref_prefix, matrix):
  i = 0
  for yi, rows in enumerate(matrix):
      for xi, p in enumerate(rows):
        i += 1
        ref = "%s%s" % (ref_prefix, i)
        xp = xi * PITCH + p[0]
        yp = yi * PITCH + p[1]
        orientation = p[2]
        set_position(ref, xp, yp, orientation)

  xp = xi * PITCH + p[0]
  yp = yi * PITCH + p[1]
  orientation = p[2]
  set_position(ref, xp, yp, orientation)


  module = pcb.FindModuleByReference(ref)
  module.SetPosition(pcbnew.wxPointMM(xp + OFFSET_X, yp + OFFSET_Y))
  module.SetOrientation( orientation * 10.0 )

#-------------

pcb = pcbnew.GetBoard()

# ProMicro
set_position('U1', 57, 3.3, -90)

# TRRS Jack
set_position('J1', 86.4, -13, 0)

# Undergrow LED
set_position('P1', 103, 24.9, 0)

# Reset Switch
set_position('RSW1', 70.5, -10.8, 0)

# R
set_position('R1', 78, -11.9, 0)
set_position('R2', 78, -9.7, 0)

# Switch
set_matrix_position('SW', [
    [[0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180]],
    [[0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180]],
    [[0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180]],
    [[0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180]],
    [[0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180], [0, 0, 180]]
])

# Diode
set_matrix_position('D', [
    [[-8, 0, -90], [8, 0, -90], [-8, 0, -90], [-19,9.5, 0], [0, 9.5, 0], [ 0, 9.5, 0], [8, 0, -90]],
    [[-8, 0, -90], [8, 0, -90], [-8, 0, -90], [-19,9.5, 0], [8, 0, -90], [-8, 0, -90], [8, 0, -90]],
    [[-8, 0, -90], [8, 0, -90], [-8, 0, -90], [-8, 0, -90], [8, 0, -90], [-8, 0, -90], [8, 0, -90]],
    [[-8, 0, -90], [8, 0, -90], [-8, 0, -90], [-8, 0, -90], [8, 0, -90], [-8, 0, -90], [8, 0, -90]],
    [[-8, 0, -90], [8, 0, -90], [-8, 0, -90], [-8, 0, -90], [8, 0, -90], [-8, 0, -90], [8, 0, -90]]
])

# Col Jack
set_matrix_position('CJ', [
    [[6, 46, 0], [6, 46, 0], [6, 46, 0], [6, 46, 0], [-6, 46, 0], [-6, 46, 0], [-6, 46, 0]],
    [[6, 30, 0], [6, 30, 0], [6, 30, 0], [6, 30, 0], [-6, 30, 0], [-6, 30, 0], [-6, 30, 0]],
    [[6, 27, 0], [6, 27, 0], [6, 27, 0], [6, 27, 0], [-6, 27, 0], [-6, 27, 0], [-6, 27, 0]],
    [[6, 11, 0], [6, 11, 0], [6, 11, 0], [6, 11, 0], [-6, 11, 0], [-6, 11, 0], [-6, 11, 0]]
])

# Row Jack
set_matrix_position('RJ', [
    [[8, -6, 0], [-8, -6, 0],                                                                                                                    [65, -6, 0], [49, -6, 0]],
    [[8, -6, 0], [-8, -6, 0],                                                                                                                    [65, -6, 0], [49, -6, 0]],
    [[8, -6, 0], [-8, -6, 0],                                                                                                                    [65, -6, 0], [49, -6, 0]],
    [[8, -6, 0], [-8, -6, 0], [-11, -6, 0], [-27, -6, 0], [-30, -6, 0], [-46, -6, 0], [-49, -6, 0], [-65, -6, 0], [-68, -6, 0], [-84, -6, 0], [-87, -6, 0], [-103, -6, 0], [-179, -11, 0]],
    [[8, -6, 0], [-8, -6, 0], [-11, -6, 0], [-27, -6, 0], [-30, -6, 0], [-46, -6, 0], [-49, -6, 0], [-65, -6, 0], [-68, -6, 0], [-84, -6, 0], [-87, -6, 0], [-103, -6, 0], [-177, -13, 0], [-196, -30, 0]]
])

#set_position('RJ25', 61, 46, 0)
#set_position('RJ38', 63, 65, 0)
#set_position('RJ39', 63, 46, 0)
