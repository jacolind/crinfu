'''
this file contains the plotting defaults used
'''

## styles

plt.style.available
plt.style.use('seaborn-whitegrid')
plt.style.use('seaborn-white')
plt.style.use('seaborn-darkgrid')
plt.style.use('ggplot')
plt.style.use('seaborn-pastel')
plt.style.use('seaborn-colorblind') # use this one with gray background

# as of 17 dec i like seaborn-pastel and seaborn-colorblind but the colorblind need some alpha in it i think.
# need to ensure it is ok to print it also.

## choice A

CUSTOM_A = True

if CUSTOM_A:

  # alpha
  ALPHA = 0.70

  # todo make below work
  #plt.rcParams["scatter.marker"] = 'o'

## custom choice B

CUSTOM_B = False

if CUSTOM_B:

  SMALL_SIZE =10
  MEDIUM_SIZE = 12
  BIGGER_SIZE = 14

  # http://www.scipy-lectures.org/intro/matplotlib/index.html#line-styles

  plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
  plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
  plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of x and y labels
  plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
  plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
  plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
  plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

##