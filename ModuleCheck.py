#Check python module installed in local machine
#Necessary module: Numpy, Scipy, Matplotlib, Pandas, Pandas_datareader, scikit_learn
from pip._internal.utils.misc import get_installed_distributions
import matplotlib

installed_packages = get_installed_distributions()
installed_packages_list = sorted(["Module:%s, version:%s" % (i.key, i.version) for i in installed_packages])
for item in installed_packages_list:
    print(item)