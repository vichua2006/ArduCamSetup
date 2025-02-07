import ArducamEvkSDK

param = ArducamEvkSDK.Param()
param.config_file_name = "Mira220_MIPI_2Lane_640x480_12b_80fps.cfg"

cam = ArducamEvkSDK.Camera()
cam.open(param)

cam.capture()