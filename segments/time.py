from time import localtime, strftime

def add_time_segment(powerline):

    powerline.append(' %s ' % strftime("%H:%M:%S", localtime()), Color.TIME_FG, Color.TIME_BG)
