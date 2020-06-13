# Start of script
def resolutionListTextOnly():
  print("Resolution list")
  print("256x144") # (144p) Not recommended
  print("352x240") # (240p) Not recommended
  print("480x360") # (360p) Not recommended
  print("600x480") # (480p)
  print("1280x720") # (720p)
  print("1920x1080") # (1080p)
  print("2560x1440") # (1440p)
  print("3840x2160") # (2160p) [2K/4K]
  print("7680x4320") # (4320p) [4K/8K]
  print("15360x8640") # (8640p) [8K/16K]
  print("30720x17280") # (17280p) [16/17K / 30K/32K]
  # That is as far as I am currently willing to go with the resolution
# Run
print("Resolution list")
confirmResList1 = input("Press the [ENTER] key to view the list of resolution")
print(resolutionListTextOnly())
print("End of list")
noMoreExit = input("Press [ENTER] key to quit")
print("The file has been closed, if the file is not closed, please close out of it via the X button, or a taskkill")
# End of script
