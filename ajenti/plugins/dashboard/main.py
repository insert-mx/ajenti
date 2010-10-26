import platform

from ajenti.com import Interface
from ajenti.ui import *
from ajenti import version
from ajenti.utils import detect_distro, detect_platform
from ajenti.api import CategoryPlugin

from api import *


class Dashboard(CategoryPlugin):
    text = 'Dashboard'
    icon = '/dl/dashboard/icon_small.png'
    folder = 'top'

    widgets = Interface(IDashboardWidget)

    def get_ui(self):
        # Arrange widgets in two columns
        lc = UI.VContainer()
        rc = UI.VContainer()
        w = UI.HContainer(lc, rc)
        
        for i in range(0, len(self.widgets)):
            if i % 2 == 0:
                rc.append(self.widgets[i].get_ui())
            else:
                lc.append(self.widgets[i].get_ui())

        u = UI.PluginPanel(UI.Label(text=detect_distro()), w, title=platform.node(), icon='/dl/dashboard/distributor-logo-%s.png'%detect_platform(mapping=False))
        return u
